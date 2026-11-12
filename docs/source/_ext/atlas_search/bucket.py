"""Read the public BrainGlobe atlas bucket.

The BrainGlobe Atlas API (v3) stores every atlas as a set of components on S3
(https://brainglobe.s3.us-west-2.amazonaws.com/atlas/)::

    atlases/<atlas>/<version>/manifest.json   -> points at the components
    templates/<name>/<version>/template.ome.zarr
    annotation-sets/<name>/<version>/annotations_compressed.ome.zarr
    annotation-sets/<name>/<version>/hemispheres.ome.zarr
    annotation-sets/<name>/<version>/annotations.precomputed   (meshes)
    terminologies/<name>/<version>/terminology.csv

Only the coronal previews need numpy, Pillow and zstandard.
"""

from __future__ import annotations

import configparser
import csv
import io
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

BUCKET = "https://brainglobe.s3.us-west-2.amazonaws.com"
ROOT = f"{BUCKET}/atlas"
WORKERS = 16


def fetch(url: str, retries: int = 3) -> bytes | None:
    """GET a URL, returning None on 403/404."""
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (403, 404):
                return None
            if attempt == retries - 1:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == retries - 1:
                raise
    return None


def fetch_json(url: str):
    data = fetch(url)
    return None if data is None else json.loads(data)


def list_bucket(prefix: str) -> dict[str, str]:
    """All keys under a prefix with their LastModified time (ISO 8601)."""
    out: dict[str, str] = {}
    token = None
    while True:
        q = f"list-type=2&prefix={urllib.parse.quote(prefix)}&max-keys=1000"
        if token:
            q += f"&continuation-token={urllib.parse.quote(token)}"
        xml = fetch(f"{BUCKET}/?{q}").decode()
        out.update(re.findall(r"<Key>([^<]+)</Key><LastModified>([^<]+)</LastModified>", xml))
        m = re.search(r"<NextContinuationToken>([^<]+)</NextContinuationToken>", xml)
        if not m:
            return out
        token = m.group(1)


def version_key(v: str):
    return tuple(int(x) for x in re.findall(r"\d+", v))


def parse_terminology(text: str) -> list[dict]:
    def to_int(v):
        try:
            return int(float(v))
        except (TypeError, ValueError):
            return None

    return [
        {
            "id": to_int(r.get("identifier")),
            "parent": to_int(r.get("parent_identifier")),
            "value": to_int(r.get("annotation_value")),
            "name": (r.get("name") or "").strip(),
            "acronym": (r.get("abbreviation") or "").strip(),
            "color": (r.get("color_hex_triplet") or "").strip(),
        }
        for r in csv.DictReader(io.StringIO(text))
    ]


def crawl() -> dict:
    """Every published version of the atlases in last_versions.conf.

    Returns ``{"atlases": [...], "terminologies": {location: rows},
    "meshes": {annotation set location: bool}}``; each atlas is its manifest
    plus ``key``, ``latest`` and ``uploaded`` (ISO time of the manifest upload).
    """
    conf = configparser.ConfigParser()
    conf.read_string(fetch(f"{ROOT}/atlases/last_versions.conf").decode())
    latest = dict(conf["atlases"])

    uploaded: dict[tuple[str, str], str | None] = {}
    for k, mod in list_bucket("atlas/atlases/").items():
        m = re.fullmatch(r"atlas/atlases/([^/]+)/([^/]+)/manifest\.json", k)
        if m and m.group(1) in latest:
            uploaded[(m.group(1), m.group(2).replace("_", "."))] = mod
    for key, version in latest.items():
        uploaded.setdefault((key, version), None)

    def manifest(item):
        key, version = item
        m = fetch_json(f"{ROOT}/atlases/{key}/{version.replace('.', '_')}/manifest.json")
        if m is None:
            print(f"atlas search: missing manifest for {key} {version}", file=sys.stderr)
            return None
        return {**m, "key": key, "version": m.get("version") or version,
                "latest": latest[key] == version, "uploaded": uploaded[item]}

    with ThreadPoolExecutor(WORKERS) as ex:
        atlases = [m for m in ex.map(manifest, sorted(uploaded)) if m]

    def terminology(loc):
        data = fetch(f"{ROOT}{loc}/terminology.csv")
        return loc, parse_terminology(data.decode("utf-8-sig")) if data else None

    def meshes(loc):
        info = fetch_json(f"{ROOT}{loc}/annotations.precomputed/info")
        return loc, bool(info and info.get("mesh"))

    latest_atlases = [a for a in atlases if a["latest"]]
    with ThreadPoolExecutor(WORKERS) as ex:
        terms = dict(ex.map(terminology, {a["terminology"]["location"] for a in latest_atlases}))
        mesh = dict(ex.map(meshes, {a["annotation_set"]["location"] for a in latest_atlases}))
    atlases.sort(key=lambda a: (a["key"], version_key(a["version"])))
    return {"atlases": atlases, "terminologies": terms, "meshes": mesh}


# --------------------------------------------------------------------------
# Coronal previews
# --------------------------------------------------------------------------
PREVIEW_MIN_PLANE = 200  # px: coarsest level at least this wide in the slice plane
NP_DTYPES = {
    "uint8": "u1", "uint16": "<u2", "uint32": "<u4", "uint64": "<u8", "int8": "i1",
    "int16": "<i2", "int32": "<i4", "int64": "<i8", "float32": "<f4", "float64": "<f8",
}


def omezarr_levels(url: str) -> list[dict]:
    """Multiscale levels (finest first) of an OME-Zarr v0.5 (zarr v3) image."""
    group = fetch_json(f"{url}/zarr.json")
    if group is None:
        return []
    attrs = group.get("attributes", {})
    levels = []
    for ds in attrs.get("ome", attrs)["multiscales"][0]["datasets"]:
        arr = fetch_json(f"{url}/{ds['path']}/zarr.json")
        if arr is None:
            continue
        tf = {t["type"]: t for t in ds["coordinateTransformations"]}
        cke = arr.get("chunk_key_encoding", {"name": "default"})
        levels.append({
            "path": ds["path"],
            "scale": tf["scale"]["scale"],
            "translation": tf.get("translation", {}).get("translation", [0.0, 0.0, 0.0]),
            "shape": arr["shape"],
            "chunks": arr["chunk_grid"]["configuration"]["chunk_shape"],
            "dtype": arr["data_type"],
            "zstd": any(c["name"] == "zstd" for c in arr.get("codecs", [])),
            "separator": cke.get("configuration", {}).get(
                "separator", "/" if cke.get("name") == "default" else "."),
            "fill_value": arr.get("fill_value") or 0,
        })
    return levels


def read_plane(url: str, level: dict, axis: int, index: int):
    """Read one plane (fixed ``index`` along ``axis``) of a zarr v3 array.

    Chunks are 3D, so every chunk that the plane crosses is fetched whole.
    Missing or truncated chunks are left at the fill value.
    """
    import numpy as np
    import zstandard

    shape, chunks = level["shape"], level["chunks"]
    dtype = np.dtype(NP_DTYPES[level["dtype"]])
    rem = [d for d in range(3) if d != axis]
    out = np.full([shape[d] for d in rem], level["fill_value"], dtype=dtype)
    ci, local = divmod(index, chunks[axis])
    n = [-(-shape[d] // chunks[d]) for d in range(3)]

    def block(ab):
        coord = [0, 0, 0]
        coord[axis], coord[rem[0]], coord[rem[1]] = ci, *ab
        raw = fetch(f"{url}/{level['path']}/" + level["separator"].join(["c", *map(str, coord)]))
        if raw is None:
            return ab, None
        if level["zstd"]:
            raw = zstandard.ZstdDecompressor().decompressobj().decompress(raw)
        data = np.frombuffer(raw, dtype=dtype)
        if data.size != int(np.prod(chunks)):
            return ab, None
        return ab, np.take(data.reshape(chunks), local, axis=axis)

    with ThreadPoolExecutor(8) as ex:
        for (a, b), plane in ex.map(block, [(a, b) for a in range(n[rem[0]]) for b in range(n[rem[1]])]):
            if plane is not None:
                r0, c0 = a * chunks[rem[0]], b * chunks[rem[1]]
                h, w = min(chunks[rem[0]], shape[rem[0]] - r0), min(chunks[rem[1]], shape[rem[1]] - c0)
                out[r0:r0 + h, c0:c0 + w] = plane[:h, :w]
    return out


def coronal_preview(atlas: dict, rows: list[dict] | None, path: Path) -> dict | None:
    """Write the middle coronal section of an atlas to ``path`` (PNG).

    The image shows the template beside the annotation in the atlas colours,
    viewed from the front with superior at the top. Returns a description of
    the section for the caption, or None if there is no template.
    """
    import numpy as np
    from PIL import Image

    o = (atlas.get("orientation") or "").lower()
    try:
        ap = next(i for i, c in enumerate(o) if c in "ap")
        v = next(i for i, c in enumerate(o) if c in "si")
        hz = next(i for i, c in enumerate(o) if c in "lr")
    except StopIteration:
        return None
    t_url = f"{ROOT}{atlas['template']['location']}/template.ome.zarr"
    a_url = f"{ROOT}{atlas['annotation_set']['location']}/annotations_compressed.ome.zarr"
    levels = omezarr_levels(t_url)
    if not levels:
        return None
    wide = [lv for lv in levels if max(lv["shape"][d] for d in range(3) if d != ap) >= PREVIEW_MIN_PLANE]
    tl = wide[-1] if wide else levels[0]
    index = tl["shape"][ap] // 2
    pos = tl["translation"][ap] + index * tl["scale"][ap]  # mm

    def oriented(plane):
        if [d for d in range(3) if d != ap].index(v) != 0:
            plane = plane.T  # rows = superior/inferior axis
        return plane[::-1] if o[v] == "i" else plane

    tpl = oriented(read_plane(t_url, tl, ap, index)).astype(np.float64)
    nz = tpl[tpl > 0]
    lo, hi = np.percentile(nz, [0.5, 99.5]) if nz.size else (0.0, 1.0)
    grey = np.clip((tpl - lo) / max(hi - lo, 1e-9) * 255, 0, 255)

    overlay = None
    alevels = omezarr_levels(a_url)
    if alevels:
        al = min(alevels, key=lambda lv: sum(abs(np.log(a / b)) for a, b in zip(lv["scale"], tl["scale"])))
        ai = min(max(int(round((pos - al["translation"][ap]) / al["scale"][ap])), 0), al["shape"][ap] - 1)
        lab = oriented(read_plane(a_url, al, ap, ai))
        lab = lab[(np.arange(grey.shape[0]) * lab.shape[0]) // grey.shape[0]]
        lab = lab[:, (np.arange(grey.shape[1]) * lab.shape[1]) // grey.shape[1]]
        # region colour over the template; outside the annotation, a darkened template
        overlay = np.repeat(grey[..., None] * 0.5, 3, axis=2)
        colours = {r["value"]: r["color"] for r in rows or [] if r["value"] is not None}
        for value in np.unique(lab):
            if value == 0:
                continue
            hexc = colours.get(int(value), "c8c8c8").lstrip("#")
            rgb = np.array([int(hexc[i:i + 2], 16) for i in (0, 2, 4)] if len(hexc) == 6 else [200] * 3)
            mask = lab == value
            overlay[mask] = rgb * 0.8 + grey[mask][:, None] * 0.2

    # physical aspect ratio, then template and annotation side by side
    aspect = (grey.shape[1] * tl["scale"][hz]) / (grey.shape[0] * tl["scale"][v])
    height = grey.shape[0]
    width = max(1, round(height * aspect))
    panels = [Image.fromarray(grey.astype(np.uint8)).convert("RGB")]
    if overlay is not None:
        panels.append(Image.fromarray(overlay.astype(np.uint8)))
    panels = [p.resize((width, height), Image.NEAREST) for p in panels]
    gap = max(4, width // 50)
    image = Image.new("RGBA", (len(panels) * width + (len(panels) - 1) * gap, height), (0, 0, 0, 0))
    for i, p in enumerate(panels):
        image.paste(p, (i * (width + gap), 0))
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, optimize=True)
    return {
        "index": index,
        "count": tl["shape"][ap],
        "from_anterior_mm": (index if o[ap] == "a" else tl["shape"][ap] - 1 - index) * tl["scale"][ap],
        "shown_um": round(tl["scale"][ap] * 1000, 3),
        "left": "left" if o[hz] == "l" else "right",
        "annotation": overlay is not None,
    }
