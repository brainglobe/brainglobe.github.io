#!/usr/bin/env python
"""Crawl the public BrainGlobe atlas bucket and build a static search index.

The BrainGlobe atlas API (v3) stores every atlas as a set of components on
S3 (https://brainglobe.s3.us-west-2.amazonaws.com/atlas/):

    atlases/<atlas>/<version>/manifest.json   -> points at the components
    templates/<name>/<version>/template.ome.zarr
    annotation-sets/<name>/<version>/annotations_compressed.ome.zarr
    annotation-sets/<name>/<version>/hemispheres.ome.zarr
    annotation-sets/<name>/<version>/annotations.precomputed   (meshes)
    terminologies/<name>/<version>/terminology.csv

This script reads ``last_versions.conf`` and every manifest, inspects the
OME-Zarr metadata of each component, converts each terminology to JSON, and
enriches the atlases with the hand-maintained titles, categories and
descriptions in ``collections.toml`` at the repository root. The output is
written to ``public/data`` and consumed by the static website.

Only the standard library is required. If ``numpy`` and ``zstandard`` are
installed, a display intensity range is also computed for every template,
and a small coronal-section preview (template + annotation labels) is written
for every atlas to ``public/data/previews`` so the site never has to read
the volumes just to show a slice. Previews are named after the store versions
and are reused when they already exist.

Usage::

    python scripts/build_index.py [--out public/data] [--collections collections.toml]
"""

from __future__ import annotations

import argparse
import base64
import configparser
import csv
import datetime as dt
import io
import json
import re
import sys
import tomllib
import urllib.error
import urllib.parse
import urllib.request
import zlib
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

BUCKET = "https://brainglobe.s3.us-west-2.amazonaws.com"
ROOT = f"{BUCKET}/atlas"
# Categories of collections.toml, in the order the site lists them (keep in
# sync with GROUP_ORDER in src/search.js).
GROUPS = [
    "Mouse", "Rat", "Other rodent", "Fish", "Lizard", "Amphibian",
    "Human and non-human primate", "Other mammal", "Bird", "Invertebrate",
]
USER_AGENT = "brainglobe-search-index-builder"
VOXEL_BUDGET = 8e6  # max voxels decoded per template for the display range

try:  # optional, for template intensity ranges
    import numpy as np
    import zstandard
except ImportError:  # pragma: no cover
    np = None
    zstandard = None


# --------------------------------------------------------------------------
# HTTP helpers
# --------------------------------------------------------------------------
def fetch(url: str, retries: int = 3) -> bytes | None:
    """GET a URL, returning None on 403/404."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=60) as r:
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


def loc_url(location: str) -> str:
    """Manifest locations start with '/', relative to the atlas root."""
    return ROOT + location


# --------------------------------------------------------------------------
# OME-Zarr inspection
# --------------------------------------------------------------------------
def inspect_omezarr(url: str) -> dict | None:
    """Return multiscale level info for an OME-Zarr v0.5 (zarr v3) group."""
    group = fetch_json(f"{url}/zarr.json")
    if group is None:
        return None
    attrs = group.get("attributes", {})
    ome = attrs.get("ome", attrs)
    ms = ome["multiscales"][0]
    axes = ms["axes"]
    levels = []
    for ds in ms["datasets"]:
        arr = fetch_json(f"{url}/{ds['path']}/zarr.json")
        if arr is None:
            continue
        scale = next(
            t["scale"] for t in ds["coordinateTransformations"] if t["type"] == "scale"
        )
        trans = next(
            (
                t["translation"]
                for t in ds["coordinateTransformations"]
                if t["type"] == "translation"
            ),
            [0.0] * len(scale),
        )
        codecs = [c["name"] for c in arr.get("codecs", [])]
        cke = arr.get("chunk_key_encoding", {"name": "default"})
        levels.append(
            {
                "path": ds["path"],
                "scale": scale,
                "translation": trans,
                "shape": arr["shape"],
                "chunks": arr["chunk_grid"]["configuration"]["chunk_shape"],
                "dtype": arr["data_type"],
                "codecs": codecs,
                "separator": cke.get("configuration", {}).get(
                    "separator", "/" if cke.get("name") == "default" else "."
                ),
                "fill_value": arr.get("fill_value", 0),
            }
        )
    return {
        "axes": [
            {
                "name": a["name"],
                "unit": a.get("unit"),
                "orientation": (a.get("orientation") or {}).get("value"),
            }
            for a in axes
        ],
        "levels": levels,
    }


def intensity_range(url: str, level: dict) -> list[float] | None:
    """Compute a robust display range from the coarsest pyramid level."""
    if np is None or level["codecs"] not in (["bytes", "zstd"], ["bytes"]):
        return None
    shape, chunks = level["shape"], level["chunks"]
    dtype = np.dtype(
        {
            "uint8": "u1", "uint16": "<u2", "uint32": "<u4", "int8": "i1",
            "int16": "<i2", "int32": "<i4", "float32": "<f4", "float64": "<f8",
        }[level["dtype"]]
    )
    sep = level["separator"]
    n = [-(-s // c) for s, c in zip(shape, chunks)]
    chunk_voxels = int(np.prod(chunks))
    # Sample chunks nearest the volume centre, within a voxel budget, so
    # single-level templates with huge chunks stay cheap.
    centre = [(x - 1) / 2 for x in n]
    coords = sorted(
        ((i, j, k) for i in range(n[0]) for j in range(n[1]) for k in range(n[2])),
        key=lambda c: sum((a - b) ** 2 for a, b in zip(c, centre)),
    )
    budget = max(1, int(VOXEL_BUDGET // chunk_voxels))
    values = []
    dctx = zstandard.ZstdDecompressor()
    for c in coords[:budget]:
        key = sep.join(["c", *map(str, c)])
        raw = fetch(f"{url}/{level['path']}/{key}")
        if raw is None:
            continue
        if "zstd" in level["codecs"]:
            # streaming API: also handles frames without a content size
            raw = dctx.decompressobj().decompress(raw)
        values.append(np.frombuffer(raw, dtype=dtype)[::7])
    if not values:
        return None
    v = np.concatenate(values).astype(np.float64)
    v = v[v > 0]
    if v.size == 0:
        return None
    lo, hi = np.percentile(v, [0.5, 99.8])
    return [float(round(lo, 4)), float(round(hi, 4))]


# --------------------------------------------------------------------------
# Coronal previews
# --------------------------------------------------------------------------
PREVIEW_MIN_PLANE = 200  # px: coarsest level at least this wide in the slice plane
NP_DTYPES = {
    "uint8": "u1", "uint16": "<u2", "uint32": "<u4", "uint64": "<u8", "int8": "i1",
    "int16": "<i2", "int32": "<i4", "int64": "<i8", "float32": "<f4", "float64": "<f8",
}
OPPOSITE = {"a": "p", "p": "a", "s": "i", "i": "s", "l": "r", "r": "l"}


def read_plane(url: str, level: dict, axis: int, index: int, problems: list | None = None):
    """Read one plane (fixed ``index`` along ``axis``) of a zarr v3 array.

    Zarr chunks are 3D, so every chunk the plane crosses is fetched whole; this
    is why previews are made once here rather than in the browser.
    """
    shape, chunks = level["shape"], level["chunks"]
    dtype = np.dtype(NP_DTYPES[level["dtype"]])
    rem = [d for d in range(3) if d != axis]
    out = np.full([shape[d] for d in rem], level.get("fill_value") or 0, dtype=dtype)
    ci = index // chunks[axis]
    local = index - ci * chunks[axis]
    n = [-(-shape[d] // chunks[d]) for d in range(3)]

    def get_block(ab):
        a, b = ab
        coord = [0, 0, 0]
        coord[axis], coord[rem[0]], coord[rem[1]] = ci, a, b
        key = level["separator"].join(["c", *map(str, coord)])
        raw = fetch(f"{url}/{level['path']}/{key}")
        if raw is None:
            return ab, None  # missing chunk = fill value
        if "zstd" in level["codecs"]:
            raw = zstandard.ZstdDecompressor().decompressobj().decompress(raw)
        block = np.frombuffer(raw, dtype=dtype)
        if block.size != int(np.prod(chunks)):
            # e.g. a truncated object in the bucket: leave this region blank
            print(f"  ! corrupt chunk {url}/{level['path']}/{key} "
                  f"({block.size} of {int(np.prod(chunks))} values)", file=sys.stderr)
            if problems is not None:
                problems.append(f"{level['path']}/{key}")
            return ab, None
        # keep only the plane, not the whole decompressed chunk
        return ab, np.take(block.reshape(chunks), local, axis=axis).copy()

    blocks = [(a, b) for a in range(n[rem[0]]) for b in range(n[rem[1]])]
    with ThreadPoolExecutor(8) as ex:
        for (a, b), plane in ex.map(get_block, blocks):
            if plane is None:
                continue
            r0, c0 = a * chunks[rem[0]], b * chunks[rem[1]]
            h = min(chunks[rem[0]], shape[rem[0]] - r0)
            w = min(chunks[rem[1]], shape[rem[1]] - c0)
            out[r0:r0 + h, c0:c0 + w] = plane[:h, :w]
    return out


def coronal_preview(t_url: str, tinfo: dict, a_url: str, ainfo: dict | None, orientation: str) -> dict | None:
    """Middle coronal section: contrast-scaled template and annotation labels.

    Returned arrays are oriented for display: rows run superior -> inferior,
    columns follow the stored left/right axis (``left``/``right`` give which
    hemisphere is on each side of the image).
    """
    o = (orientation or "").lower()
    try:
        ap = next(i for i, c in enumerate(o) if c in "ap")
        v = next(i for i, c in enumerate(o) if c in "si")
        hz = next(i for i, c in enumerate(o) if c in "lr")
    except StopIteration:
        return None
    levels = tinfo["levels"]  # fine -> coarse
    wide = [lv for lv in levels if max(lv["shape"][d] for d in range(3) if d != ap) >= PREVIEW_MIN_PLANE]
    tl = wide[-1] if wide else levels[0]
    index = tl["shape"][ap] // 2
    pos = tl["translation"][ap] + index * tl["scale"][ap]  # mm

    def oriented(plane, lv):
        rem = [d for d in range(3) if d != ap]
        if rem.index(v) != 0:
            plane = plane.T  # rows = superior/inferior axis
        if o[v] == "i":
            plane = plane[::-1]  # superior at the top
        return np.ascontiguousarray(plane)

    corrupt = {"template": [], "annotation": []}
    tpl = oriented(read_plane(t_url, tl, ap, index, corrupt["template"]), tl).astype(np.float64)
    nz = tpl[tpl > 0]
    lo, hi = np.percentile(nz, [0.5, 99.5]) if nz.size else (0.0, 1.0)
    grey = np.clip((tpl - lo) / max(hi - lo, 1e-9) * 255, 0, 255).astype(np.uint8)

    labels = None
    if ainfo and ainfo.get("levels"):
        al = min(
            ainfo["levels"],
            key=lambda lv: sum(abs(np.log(a / b)) for a, b in zip(lv["scale"], tl["scale"])),
        )
        ai = int(round((pos - al["translation"][ap]) / al["scale"][ap]))
        ai = min(max(ai, 0), al["shape"][ap] - 1)
        lab = oriented(read_plane(a_url, al, ap, ai, corrupt["annotation"]), al)
        # nearest-neighbour onto the template grid (if the levels differ)
        rows = (np.arange(grey.shape[0]) * lab.shape[0]) // grey.shape[0]
        cols = (np.arange(grey.shape[1]) * lab.shape[1]) // grey.shape[1]
        lab = lab[rows][:, cols]
        labels = lab.astype("<u4")

    b64 = lambda a: base64.b64encode(zlib.compress(a.tobytes(), 9)).decode()  # noqa: E731
    return {
        "level": {"path": tl["path"], "scale": tl["scale"], "translation": tl["translation"]},
        "ap_axis": ap,
        "ap_from": o[ap],
        "index": index,
        "position_mm": pos,
        "width": int(grey.shape[1]),
        "height": int(grey.shape[0]),
        "aspect": (grey.shape[1] * tl["scale"][hz]) / (grey.shape[0] * tl["scale"][v]),
        "left": o[hz].upper(),
        "right": OPPOSITE[o[hz]].upper(),
        "template": b64(grey),
        "labels": b64(labels) if labels is not None else None,
        # chunks in the bucket that could not be decoded (drawn blank)
        "corrupt_chunks": {k: v for k, v in corrupt.items() if v},
    }


def match_level(levels: list[dict], resolution_um: list[float]) -> str | None:
    """Pick the pyramid level whose voxel size matches the atlas resolution."""
    if not levels:
        return None
    unit_factor = 1000.0  # OME-Zarr scales are in millimetres
    best, best_err = None, float("inf")
    for lv in levels:
        sc = [s * unit_factor for s in lv["scale"][-3:]]
        err = sum(abs(a - b) / max(b, 1e-9) for a, b in zip(sc, resolution_um))
        if err < best_err:
            best, best_err = lv["path"], err
    return best


# --------------------------------------------------------------------------
# Terminology
# --------------------------------------------------------------------------
def parse_terminology(text: str) -> list[dict]:
    rows = []
    for r in csv.DictReader(io.StringIO(text)):
        def _int(v):
            try:
                return int(float(v))
            except (TypeError, ValueError):
                return None

        path = r.get("root_identifier_path") or ""
        rows.append(
            {
                "id": _int(r.get("identifier")),
                "parent": _int(r.get("parent_identifier")),
                "value": _int(r.get("annotation_value")),
                "name": (r.get("name") or "").strip(),
                "acronym": (r.get("abbreviation") or "").strip(),
                "color": (r.get("color_hex_triplet") or "").strip(),
                "path": [int(x) for x in re.findall(r"-?\d+", path)],
            }
        )
    return rows


def slug(location: str) -> str:
    return location.strip("/").replace("/", "__")


def list_bucket(prefix: str) -> dict[str, str]:
    """All keys under a prefix with their LastModified time (ISO 8601)."""
    out: dict[str, str] = {}
    token = None
    while True:
        q = f"list-type=2&prefix={urllib.parse.quote(prefix)}&max-keys=1000"
        if token:
            q += f"&continuation-token={urllib.parse.quote(token)}"
        xml = fetch(f"{BUCKET}/?{q}").decode()
        for key, mod in re.findall(r"<Key>([^<]+)</Key><LastModified>([^<]+)</LastModified>", xml):
            out[key] = mod
        m = re.search(r"<NextContinuationToken>([^<]+)</NextContinuationToken>", xml)
        if not m:
            return out
        token = m.group(1)



# --------------------------------------------------------------------------
# Collections (titles, categories and descriptions)
# --------------------------------------------------------------------------
def load_collections(path: Path, atlas_keys: set[str]) -> dict[str, dict]:
    """Map atlas key -> {title, group, description, link} from collections.toml."""
    with path.open("rb") as f:
        data = tomllib.load(f)
    out: dict[str, dict] = {}
    for i, c in enumerate(data.get("collection", [])):
        missing = [f for f in ("title", "group", "atlases") if not c.get(f)]
        if missing:
            raise SystemExit(f"{path}: collection #{i + 1} is missing {', '.join(missing)}")
        if c["group"] not in GROUPS:
            raise SystemExit(f"{path}: {c['title']!r} has unknown group {c['group']!r} (one of {GROUPS})")
        info = {
            "title": c["title"],
            "group": c["group"],
            "description": (c.get("description") or "").strip(),
            "link": c.get("link"),
        }
        for key in c["atlases"]:
            if key in out:
                raise SystemExit(f"{path}: {key} is listed in both {out[key]['title']!r} and {c['title']!r}")
            if key not in atlas_keys:
                print(f"warning: {path.name}: {key} ({c['title']}) is not in the bucket", file=sys.stderr)
            out[key] = info
    for key in sorted(atlas_keys - set(out)):
        print(f"warning: {key} is not listed in {path.name}", file=sys.stderr)
    print(f"{len(out)} atlases described in {path.name}", file=sys.stderr)
    return out


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def build(out_dir: Path, collections_path: Path, workers: int = 16) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    term_dir = out_dir / "terminologies"
    term_dir.mkdir(exist_ok=True)

    conf = configparser.ConfigParser()
    conf.read_string(fetch(f"{ROOT}/atlases/last_versions.conf").decode())
    latest = dict(conf["atlases"])
    docs = load_collections(collections_path, set(latest))
    print(f"{len(latest)} atlases in last_versions.conf", file=sys.stderr)

    # Every published version of those atlases, with its upload time.
    uploaded: dict[tuple[str, str], str] = {}
    for k, mod in list_bucket("atlas/atlases/").items():
        m = re.fullmatch(r"atlas/atlases/([^/]+)/([^/]+)/manifest\.json", k)
        if m and m.group(1) in latest:
            uploaded[(m.group(1), m.group(2).replace("_", "."))] = mod
    for key, version in latest.items():
        uploaded.setdefault((key, version), None)

    def get_manifest(item):
        key, version = item
        vdir = version.replace(".", "_")
        m = fetch_json(f"{ROOT}/atlases/{key}/{vdir}/manifest.json")
        if m is None:
            print(f"  ! missing manifest for {key} {version}", file=sys.stderr)
        return item, m

    with ThreadPoolExecutor(workers) as ex:
        manifests = {k: m for k, m in ex.map(get_manifest, sorted(uploaded)) if m}
    print(f"{len(manifests)} atlas versions", file=sys.stderr)


    template_locs = {m["template"]["location"] for m in manifests.values()}
    annot_locs = {m["annotation_set"]["location"] for m in manifests.values()}
    term_locs = {m["terminology"]["location"] for m in manifests.values()}
    print(
        f"{len(template_locs)} templates, {len(annot_locs)} annotation sets, "
        f"{len(term_locs)} terminologies",
        file=sys.stderr,
    )

    def get_template(loc):
        url = f"{loc_url(loc)}/template.ome.zarr"
        info = inspect_omezarr(url)
        if info and info["levels"]:
            try:
                info["range"] = intensity_range(url, info["levels"][-1])
            except Exception as e:  # noqa: BLE001
                print(f"  ! range failed for {loc}: {e}", file=sys.stderr)
                info["range"] = None
        print(f"  template {loc}", file=sys.stderr, flush=True)
        return loc, info

    def get_annotation(loc):
        base = loc_url(loc)
        ann = inspect_omezarr(f"{base}/annotations_compressed.ome.zarr")
        hemi = inspect_omezarr(f"{base}/hemispheres.ome.zarr")
        pre = fetch_json(f"{base}/annotations.precomputed/info")
        print(f"  annotation set {loc}", file=sys.stderr, flush=True)
        return loc, {
            "annotation": ann,
            "hemispheres": hemi,
            "precomputed": bool(pre),
            "meshes": bool(pre and pre.get("mesh")),
            "segment_properties": bool(pre and pre.get("segment_properties")),
        }

    def get_terminology(loc):
        data = fetch(f"{loc_url(loc)}/terminology.csv")
        if data is None:
            return loc, None
        rows = parse_terminology(data.decode("utf-8-sig"))
        fname = f"{slug(loc)}.json"
        (term_dir / fname).write_text(json.dumps(rows, separators=(",", ":")))
        return loc, {"file": f"terminologies/{fname}", "count": len(rows), "rows": rows}

    # Submit everything up front so slow templates don't serialise the rest.
    with ThreadPoolExecutor(workers) as ex:
        f_t = [ex.submit(get_template, loc) for loc in template_locs]
        f_a = [ex.submit(get_annotation, loc) for loc in annot_locs]
        f_r = [ex.submit(get_terminology, loc) for loc in term_locs]
        templates = dict(f.result() for f in f_t)
        annotations = dict(f.result() for f in f_a)
        terms_full = dict(f.result() for f in f_r)

    # Coronal previews, one per (template, annotation set) pair.
    previews: dict[tuple[str, str], str | None] = {}
    if np is not None:
        prev_dir = out_dir / "previews"
        prev_dir.mkdir(exist_ok=True)
        pairs = {}
        for m in manifests.values():
            pair = (m["template"]["location"], m["annotation_set"]["location"])
            pairs.setdefault(pair, m.get("orientation", "asr"))

        def get_preview(item):
            (t_loc, a_loc), orientation = item
            fname = f"{slug(t_loc)}__{slug(a_loc)}.json"
            path = prev_dir / fname
            if not path.exists():  # previews are keyed by store versions
                tinfo = templates.get(t_loc)
                ainfo = (annotations.get(a_loc) or {}).get("annotation")
                if not tinfo or not tinfo.get("levels"):
                    return (t_loc, a_loc), None
                try:
                    p = coronal_preview(
                        f"{loc_url(t_loc)}/template.ome.zarr", tinfo,
                        f"{loc_url(a_loc)}/annotations_compressed.ome.zarr", ainfo, orientation,
                    )
                except Exception as e:  # noqa: BLE001
                    print(f"  ! preview failed for {t_loc}: {e}", file=sys.stderr)
                    return (t_loc, a_loc), None
                if p is None:
                    return (t_loc, a_loc), None
                path.write_text(json.dumps(p, separators=(",", ":")))
                print(f"  preview {fname}", file=sys.stderr, flush=True)
            return (t_loc, a_loc), f"previews/{fname}"

        # few workers: single-resolution atlases have very large chunks
        with ThreadPoolExecutor(min(workers, 6)) as ex:
            previews = dict(ex.map(get_preview, pairs.items()))
        print(f"{sum(1 for v in previews.values() if v)} coronal previews", file=sys.stderr)
        used = {Path(v).name for v in previews.values() if v}
        for f in prev_dir.glob("*.json"):
            if f.name not in used:  # store replaced by a newer version
                f.unlink()

    # Region-name search index (deduplicated across terminologies).
    terminologies = {}
    for loc, t in terms_full.items():
        if t is None:
            terminologies[loc] = None
            continue
        terminologies[loc] = {
            "file": t["file"],
            "count": t["count"],
            # compact list used for full-text search: "acronym\tname"
            "regions": [f"{r['acronym']}\t{r['name']}" for r in t["rows"]],
        }

    def version_key(v):
        return tuple(int(x) for x in re.findall(r"\d+", v))

    atlases = []
    for key, version in sorted(manifests, key=lambda kv: (kv[0], version_key(kv[1]))):
        m = manifests[(key, version)]
        name = m.get("name")
        res = [float(r) for r in m.get("resolution", [])]
        t_loc = m["template"]["location"]
        a_loc = m["annotation_set"]["location"]
        tinfo = templates.get(t_loc) or {}
        ainfo = annotations.get(a_loc) or {}
        entry = {
            "key": key,
            "name": name,
            "version": m.get("version") or version,
            "latest": latest.get(key) == version,
            "uploaded": uploaded.get((key, version)),
            "species": m.get("species"),
            "citation": m.get("citation"),
            "atlas_link": m.get("atlas_link"),
            "symmetric": m.get("symmetric"),
            "resolution": res,
            "orientation": m.get("orientation"),
            "shape": m.get("shape"),
            "additional_references": m.get("additional_references") or [],
            "atlas_packager": m.get("atlas_packager"),
            "coordinate_space": m.get("coordinate_space", {}).get("name"),
            "manifest": f"/atlases/{key}/{version.replace('.', '_')}/manifest.json",
            "template": {
                **m["template"],
                "level": match_level(tinfo.get("levels", []), res),
            },
            "annotation_set": {
                "name": m["annotation_set"]["name"],
                "version": m["annotation_set"]["version"],
                "location": a_loc,
                "level": match_level(
                    ((ainfo.get("annotation") or {}).get("levels") or []), res
                ),
                "hemispheres_level": match_level(
                    ((ainfo.get("hemispheres") or {}).get("levels") or []), res
                ),
            },
            "terminology": m["terminology"],
            "preview": previews.get((t_loc, a_loc)),
            **({"docs": docs[key]} if key in docs else {}),
        }
        atlases.append(entry)

    # Atlases missing from collections.toml: infer the category from species.
    species_group: dict[str, dict[str, int]] = {}
    for a in atlases:
        g = a.get("docs", {}).get("group")
        if g:
            counts = species_group.setdefault(a["species"], {})
            counts[g] = counts.get(g, 0) + 1
    for a in atlases:
        if "docs" not in a and a["species"] in species_group:
            counts = species_group[a["species"]]
            a["docs"] = {"group": max(counts, key=counts.get)}

    index = {
        "generated": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "root": ROOT,
        "atlases": atlases,
        "templates": templates,
        "annotation_sets": annotations,
        "terminologies": terminologies,
    }
    (out_dir / "index.json").write_text(json.dumps(index, separators=(",", ":")))
    size = (out_dir / "index.json").stat().st_size / 1e6
    print(f"wrote {out_dir/'index.json'} ({size:.1f} MB, {len(atlases)} atlases)", file=sys.stderr)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--out", type=Path, default=Path(__file__).parents[1] / "public" / "data")
    p.add_argument(
        "--collections",
        type=Path,
        default=Path(__file__).parents[1] / "collections.toml",
        help="atlas titles, categories and descriptions (default: collections.toml)",
    )
    p.add_argument("--workers", type=int, default=16)
    args = p.parse_args(argv)
    build(args.out, args.collections, args.workers)


if __name__ == "__main__":
    main()
