"""Generate the atlas search pages from the bucket and ``collections.toml``.

Every atlas name (e.g. ``allen_mouse``, covering all its resolutions) gets a
MyST page, ``atlases/<name>.md``; the search page lists one card per
collection.
"""

from __future__ import annotations

import datetime as dt
import html
import json
import os.path
import re
import tomllib
import unicodedata
from pathlib import Path

from .bucket import BUCKET, ROOT, coronal_preview, version_key

NEUROGLANCER = "https://neuroglancer-demo.appspot.com/"
GROUPS = [
    "Mouse", "Rat", "Other rodent", "Fish", "Lizard", "Amphibian",
    "Human and non-human primate", "Other mammal", "Bird", "Invertebrate",
]
# Display names for the species filter, and extra words to search by.
COMMON_NAMES = {
    "mus musculus": ("Mouse", ""),
    "rattus norvegicus": ("Rat", ""),
    "danio rerio": ("Zebrafish", "fish"),
    "homo sapiens": ("Human", "primate"),
    "macaca mulatta": ("Rhesus macaque", "primate monkey"),
    "microtus ochrogaster": ("Prairie vole", "rodent"),
    "felis catus": ("Cat", ""),
    "ambystoma mexicanum": ("Axolotl", "amphibian salamander"),
    "astyanax mexicanus": ("Mexican cavefish", "fish"),
    "microcebus murinus": ("Grey mouse lemur", "primate"),
    "sepia bandensis": ("Dwarf cuttlefish", "cephalopod"),
    "bombus impatiens": ("Common eastern bumblebee", "bee insect"),
    "drosophila melanogaster": ("Fruit fly", "insect"),
    "ctenophorus decresii": ("Tawny dragon", "lizard reptile"),
    "sylvia atricapilla": ("Eurasian blackcap", "bird"),
    "heterocephalus glaber": ("Naked mole-rat", "mole rat rodent"),
    "fukomys anselli": ("Ansell's mole-rat", "mole rat rodent"),
    "danionella cerebrum": ("Danionella", "fish"),
}
esc = html.escape


def common_name(species: str) -> str:
    return COMMON_NAMES.get((species or "").lower(), ("", ""))[0]


def fmt_res(values) -> str:
    vals = [f"{float(r):g}" for r in values]
    return f"{vals[0]} µm" if len(set(vals)) == 1 else f"{' × '.join(vals)} µm"


def fmt_date(iso: str | None) -> str:
    return dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).strftime("%-d %b %Y") if iso else ""


def legacy_anchor(title: str) -> str:
    """The id that the old atlas details page gave the heading of a collection."""
    s = unicodedata.normalize("NFKD", re.sub(r"['’]", "", title)).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", "-", s.lower())
    return re.sub(r"^[^a-z]+", "", s).rstrip("-")


def load_collections(path: Path) -> list[dict]:
    with path.open("rb") as f:
        data = tomllib.load(f)
    seen: dict[str, str] = {}
    collections = []
    for i, c in enumerate(data.get("collection", [])):
        missing = [f for f in ("title", "group", "atlases") if not c.get(f)]
        if missing:
            raise ValueError(f"{path}: collection #{i + 1} is missing {', '.join(missing)}")
        if c["group"] not in GROUPS:
            raise ValueError(f"{path}: {c['title']!r} has unknown group {c['group']!r} (one of {GROUPS})")
        for name in c["atlases"]:
            if name in seen:
                raise ValueError(f"{path}: {name} is listed in both {seen[name]!r} and {c['title']!r}")
            seen[name] = c["title"]
        collections.append({"title": c["title"], "group": c["group"], "link": c.get("link"),
                            "description": (c.get("description") or "").strip(), "names": list(c["atlases"])})
    return collections


def natural(text: str):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", text)]


class Site:
    """The bucket contents arranged by collection, atlas name and resolution."""

    def __init__(self, crawled: dict, collections: list[dict]):
        self.terminologies = crawled["terminologies"]
        self.meshes = crawled["meshes"]
        self.versions: dict[str, list[dict]] = {}  # key -> every version, newest first
        for a in crawled["atlases"]:
            self.versions.setdefault(a["key"], []).append(a)
        for vs in self.versions.values():
            vs.sort(key=lambda a: version_key(a["version"]), reverse=True)
        # name -> latest version of each of its resolutions, finest first
        self.names: dict[str, list[dict]] = {}
        for vs in self.versions.values():
            latest = next((a for a in vs if a["latest"]), vs[0])
            self.names.setdefault(latest["name"], []).append(latest)
        for keys in self.names.values():
            keys.sort(key=lambda a: (min(a["resolution"]), natural(a["key"])))

        listed = {n for c in collections for n in c["names"]}
        self.unknown = sorted(listed - set(self.names))  # listed but not in the bucket
        self.unlisted = sorted(set(self.names) - listed)
        self.collections = [dict(c, names=[n for n in c["names"] if n in self.names]) for c in collections]
        self.collections = [c for c in self.collections if c["names"]]
        # atlases missing from collections.toml: their own collection, grouped like their species
        group_of = {self.names[n][0]["species"]: c["group"] for c in self.collections for n in c["names"]}
        for name in self.unlisted:
            species = self.names[name][0]["species"]
            self.collections.append({"title": name, "group": group_of.get(species, "Invertebrate"),
                                     "link": None, "description": "", "names": [name]})
        for c in self.collections:
            c["names"].sort(key=natural)
            c["anchor"] = legacy_anchor(c["title"])
        self.collection_of = {n: c for c in self.collections for n in c["names"]}
        # the initial bulk upload: atlases from then predate the bucket, so show no "added" date
        firsts = [vs[-1]["uploaded"][:10] for vs in self.versions.values() if vs[-1]["uploaded"]]
        self.bulk_day = max(set(firsts), key=firsts.count) if firsts else ""

    def added(self, collection: dict) -> str:
        """When a collection's newest atlas was first uploaded (ISO), unless in the initial bulk upload."""
        firsts = [self.versions[k["key"]][-1]["uploaded"] for n in collection["names"] for k in self.names[n]]
        newest = max((f for f in firsts if f), default="")
        return "" if newest[:10] == self.bulk_day else newest

    def variant(self, name: str) -> str:
        """Short label of an atlas within its collection (the name without the shared prefix)."""
        names = self.collection_of[name]["names"]
        if len(names) == 1:
            return ""
        prefix = os.path.commonprefix(names)
        prefix = prefix[: prefix.rfind("_") + 1] if "_" in prefix else ""
        return name[len(prefix):] or name


# --------------------------------------------------------------------------
# Atlas pages
# --------------------------------------------------------------------------
def table(header: list[str], rows: list[list[str]]) -> str:
    def cell(s):
        return str(s).replace("|", "\\|").replace("\n", " ")
    return "\n".join(["| " + " | ".join(header) + " |", "|" + " --- |" * len(header),
                      *("| " + " | ".join(cell(c) for c in r) + " |" for r in rows)])


def state_url(name: str, version: str | None = None) -> str:
    """BrainGlobe's neuroglancer state for an atlas name, latest or pinned to a version."""
    return f"{BUCKET}/ng_state_files/{name}{f'_v{version}' if version else ''}.json"


def region_tree(rows: list[dict]) -> str:
    """Nested <details> of the regions, top level open."""
    children: dict = {}
    ids = {r["id"] for r in rows}
    for r in rows:
        children.setdefault(r["parent"] if r["parent"] in ids else None, []).append(r)

    def label(r):
        colour = esc("#" + r["color"].lstrip("#")) if r["color"] else "#ccc"
        return (f'<span class="swatch" style="background:{colour}"></span>{esc(r["name"])}'
                f'<span class="acr">{esc(r["acronym"])}</span><span class="val">{esc(str(r["value"]))}</span>')

    def node(r, depth):
        kids = children.get(r["id"], [])
        if not kids:
            return f'<li class="leaf">{label(r)}</li>'
        inner = "".join(node(k, depth + 1) for k in kids)
        return f'<li><details{" open" if depth == 0 else ""}><summary>{label(r)}</summary><ul>{inner}</ul></details></li>'

    return "<ul>" + "".join(node(r, 0) for r in children.get(None, [])) + "</ul>"


def atlas_page(site: Site, name: str, preview: tuple[str, dict] | None) -> str:
    c = site.collection_of[name]
    keys = site.names[name]
    a = keys[0]  # finest resolution, latest version
    variant = site.variant(name)
    title = f"{c['title']} ({variant})" if variant else c["title"]
    common = common_name(a["species"])
    rows = site.terminologies.get(a["terminology"]["location"])
    resolutions = ", ".join(fmt_res(k["resolution"]).replace(" µm", "") for k in keys) + " µm"
    out = [
        "---",
        "html_theme.sidebar_secondary.remove: false",
        "myst:",
        "  html_meta:",
        f"    description: {json.dumps(f'{title}: {resolutions} {a['species']} atlas in BrainGlobe')}",
        "---",
        "",
        "<!-- Generated by _ext/atlas_search from collections.toml and the atlas bucket; do not edit. -->",
        "",
        f"# {title}",
        "",
        f'<p class="atlas-line">{esc(common) + ", " if common else ""}<em>{esc(a["species"])}</em> · {esc(resolutions)}'
        f' · <a href="index.html">all atlases</a></p>',
        "",
    ]
    others = c["names"]
    if len(others) > 1:
        links = " ".join(
            f'<a href="{n}.html"{" aria-current=page" if n == name else ""}><code>{esc(n)}</code></a>' for n in others)
        out += [f'<details class="atlas-variants"><summary>One of {len(others)} atlases in this collection</summary>'
                f"<p>{links}</p></details>", ""]
    out += ["```{button-link} " + f"{NEUROGLANCER}#!{state_url(name)}", ":color: primary", "",
            "Open in neuroglancer", "```", ""]

    # About
    out += ["## About", ""]
    if preview:
        png, info = preview
        caption = (f"Coronal section {info['index']} of {info['count']} of `{a['key']}` version {a['version']} "
                   f"(0-based index along the anterior–posterior axis, {info['from_anterior_mm']:.2f} mm from the "
                   f"anterior edge). Left: template."
                   + (" Right: annotation in the atlas colours over the template." if info["annotation"] else "")
                   + f" Shown at {info['shown_um']:g} µm, viewed from the front, with the {info['left']} "
                   "hemisphere on the left of the image.")
        out += ["```{figure} " + png, ":class: atlas-preview dark-light", f":alt: Coronal section of {a['key']}", "",
                caption, "```", ""]
    if c["description"]:
        out += [c["description"], ""]
    if c["link"]:
        out += [f"More information: <{c['link']}>", ""]

    # Resolutions and versions
    out += ["## Resolutions", "",
            table(["Atlas name", "Resolution", "Shape (z, y, x)", "Version", "Released", "Manifest"],
                  [[f"`{k['key']}`", fmt_res(k["resolution"]), " × ".join(map(str, k["shape"])), k["version"],
                    fmt_date(k["uploaded"]), f"[manifest.json]({ROOT}{k['location']}/manifest.json)"]
                   for k in keys]), ""]
    older = [v for k in keys for v in site.versions[k["key"]] if not v["latest"]]
    if older:
        out += ["### Earlier versions", "",
                "Earlier versions stay available for reproducibility. Load one with "
                f'`BrainGlobeAtlas("{older[0]["key"]}", version="{older[0]["version"]}")`.', "",
                table(["Atlas name", "Version", "Released", "Manifest", "Neuroglancer"],
                      [[f"`{v['key']}`", v["version"], fmt_date(v["uploaded"]),
                        f"[manifest.json]({ROOT}{v['location']}/manifest.json)",
                        f"[view]({NEUROGLANCER}#!{state_url(name, v['version'])})"] for v in older]), ""]

    # Download (the files as BrainGlobe publishes them)
    stores: dict[tuple[str, str, str], list[str]] = {}
    for k in keys:
        ann = f"{ROOT}{k['annotation_set']['location']}"
        for label, fmt, url in [
            ("Template", "OME-Zarr", f"{ROOT}{k['template']['location']}/template.ome.zarr"),
            ("Annotation", "OME-Zarr", f"{ann}/annotations_compressed.ome.zarr"),
            ("Hemispheres", "OME-Zarr", f"{ann}/hemispheres.ome.zarr"),
            ("Brain regions", "CSV", f"{ROOT}{k['terminology']['location']}/terminology.csv"),
            *([("Meshes", "Neuroglancer precomputed", f"{ann}/annotations.precomputed")]
              if site.meshes.get(k["annotation_set"]["location"]) else []),
        ]:
            stores.setdefault((label, fmt, url), []).append(k["key"])
    per_key = any(len(v) < len(keys) for v in stores.values())
    out += ["## Download", "",
            "BrainGlobe publishes images as OME-Zarr, with every resolution as a level of one multiscale image, "
            "and brain regions as CSV. The [BrainGlobe Atlas API](/documentation/brainglobe-atlasapi/index.md) "
            "downloads them for you (see [Use from code](#use-from-code)); any OME-Zarr reader can also open "
            "the images directly from these locations.", "",
            table(["Component", "Format", *(["Atlas name"] if per_key else []), "Location"],
                  [[label, fmt, *([", ".join(f"`{k}`" for k in ks)] if per_key else []),
                    f"[terminology.csv]({url})" if fmt == "CSV" else f"`{url}`"]
                   for (label, fmt, url), ks in stores.items()]), ""]

    # Brain regions
    out += ["## Brain regions", ""]
    if rows:
        out += [f"{len(rows)} regions in `{a['terminology']['name']}` version {a['terminology']['version']}, "
                "with their acronym and annotation value.", "",
                '<div class="region-filter" hidden><input type="search" placeholder="Filter by name or acronym" '
                'aria-label="Filter regions"> <span class="region-status" aria-live="polite"></span></div>',
                f'<div class="region-tree">{region_tree(rows)}</div>', ""]
    else:
        out += ["No terminology is available for this atlas.", ""]

    # Use from code
    other = f" Replace `{a['key']}` with the name of another resolution if needed." if len(keys) > 1 else ""
    out += ["## Use from code", "", "Python:", "", "```python",
            "from brainglobe_atlasapi import BrainGlobeAtlas", "",
            f'atlas = BrainGlobeAtlas("{a["key"]}")',
            "template = atlas.template        # numpy array (z, y, x)",
            "annotation = atlas.annotation", "hemispheres = atlas.hemispheres",
            "print(atlas.lookup_df)           # brain regions", "```", "",
            "Command line:", "", "```bash", f"brainglobe install -a {a['key']}", "```", "", other.strip(), ""]

    # Metadata
    def ref(r):
        return r if isinstance(r, str) else f"`{r.get('name')}`" + (f" v{r['version']}" if r.get("version") else "")
    meta = [
        ["Species", f"*{a['species']}*"],
        ["Orientation", f"`{a['orientation']}`"],
        ["Symmetric", "yes" if a.get("symmetric") else "no"],
        ["Citation", a.get("citation") or ""],
        ["Atlas link", a.get("atlas_link") or ""],
        *([["Additional templates", "<br>".join(ref(r) for r in a["additional_references"])]]
          if a.get("additional_references") else []),
        *([["Packager", a["atlas_packager"]]] if a.get("atlas_packager") else []),
        ["Coordinate space", f"`{a.get('coordinate_space', {}).get('name', '')}`"],
        ["Template", f"`{a['template']['name']}` v{a['template']['version']}"],
        ["Annotation set", f"`{a['annotation_set']['name']}` v{a['annotation_set']['version']}"],
        ["Terminology", f"`{a['terminology']['name']}` v{a['terminology']['version']}"],
        ["Meshes", "yes" if site.meshes.get(a["annotation_set"]["location"]) else "no"],
        ["Neuroglancer state", f"[{name}.json]({state_url(name)})"],
    ]
    out += ["## Metadata", "", table(["Field", "Value"], meta), ""]
    return "\n".join(out)


def write_pages(site: Site, outdir: Path, cache: Path, logger) -> list[str]:
    """Write one page per atlas name, with its coronal preview; return the page names.

    Previews are rendered into ``cache`` and copied to ``outdir/_previews``.
    """
    import shutil
    from concurrent.futures import ThreadPoolExecutor

    cache.mkdir(parents=True, exist_ok=True)
    previews_dir = outdir / "_previews"
    previews_dir.mkdir(exist_ok=True)

    def preview(name):
        a = site.names[name][0]
        stem = f"{a['template']['location']}__{a['annotation_set']['location']}".strip("/").replace("/", "_")
        png, meta = cache / f"{stem}.png", cache / f"{stem}.json"
        if not meta.exists():  # previews are named after the store versions, so never go stale
            try:
                info = coronal_preview(a, site.terminologies.get(a["terminology"]["location"]), png)
            except Exception as e:  # noqa: BLE001
                logger.warning(f"atlas search: no coronal preview for {a['key']} ({e!r})")
                return name, None
            meta.write_text(json.dumps(info))
        info = json.loads(meta.read_text())
        if not info:
            return name, None
        if cache != previews_dir:
            shutil.copyfile(png, previews_dir / png.name)
        return name, (f"/{outdir.name}/_previews/{png.name}", info)

    try:
        import numpy  # noqa: F401
        import PIL  # noqa: F401
        import zstandard  # noqa: F401
        with ThreadPoolExecutor(6) as ex:  # few workers: single-resolution atlases have large chunks
            previews = dict(ex.map(preview, site.names))
    except ImportError as e:
        logger.warning(f"atlas search: no coronal previews ({e})")
        previews = {}
    used = {Path(p[0]).stem for p in previews.values() if p}
    for f in [*previews_dir.glob("*.*"), *cache.glob("*.*")]:
        if f.stem not in used and f.suffix in (".png", ".json"):
            f.unlink()  # an atlas store replaced by a newer version

    written = set()
    for name in site.names:
        path = outdir / f"{name}.md"
        text = atlas_page(site, name, previews.get(name))
        if not path.exists() or path.read_text() != text:  # unchanged pages are not rebuilt
            path.write_text(text)
        written.add(path.name)
    for f in outdir.glob("*.md"):
        if f.name not in written and f.name != "index.md":
            f.unlink()
    return sorted(site.names)


# --------------------------------------------------------------------------
# Search page
# --------------------------------------------------------------------------
def search_cards(site: Site) -> str:
    """The search page: facets and one card per collection, newest first."""
    # newest first; collections from the initial upload by category and title
    new = sorted((c for c in site.collections if site.added(c)), key=site.added, reverse=True)
    old = sorted((c for c in site.collections if not site.added(c)), key=lambda c: (GROUPS.index(c["group"]), c["title"]))
    order = new + old

    species_count: dict[str, int] = {}
    cards = []
    for c in order:
        keys = [k for n in c["names"] for k in site.names[n]]
        a = keys[0]
        species = a["species"]
        species_count[species] = species_count.get(species, 0) + 1
        common, alias = COMMON_NAMES.get(species.lower(), ("", ""))
        res = sorted({min(k["resolution"]) for k in keys})
        added = site.added(c)
        text = " ".join([c["title"], *c["names"], *(k["key"] for k in keys), species, common, alias, c["group"],
                         c["description"], a.get("citation") or "", a.get("orientation") or ""]).lower()
        summary = c["description"].split("\n\n")[0] if c["description"] else (a.get("citation") or "")
        names = "".join(f' <a href="{n}.html"><code>{esc(n)}</code></a>' for n in c["names"])
        terms = " ".join(sorted({site.names[n][0]["terminology"]["location"] for n in c["names"]}))
        cards.append(
            f'<article class="atlas-card" data-species="{esc(species)}" data-res="{" ".join(f"{r:g}" for r in res)}"'
            f' data-sym="{int(bool(a.get("symmetric")))}" data-names="{esc(" ".join(c["names"]))}" data-terms="{esc(terms)}" data-text="{esc(text)}">'
            f'<h2><a href="{c["names"][0]}.html">{esc(c["title"])}</a></h2>'
            f'<p class="species">{esc(common) + " · " if common else ""}<em>{esc(species)}</em>'
            f' · {esc(", ".join(f"{r:g}" for r in res))} µm'
            f'{f" · <span class=added>Added {esc(fmt_date(added))}</span>" if added else ""}</p>'
            f'<p class="summary">{esc(summary)}</p>'
            + (f'<p class="keys">{names}</p>' if len(c["names"]) > 1 else "")
            + '<p class="regions-hit" hidden></p></article>')

    all_res = sorted({min(k["resolution"]) for keys in site.names.values() for k in keys})
    options = "".join(f'<option value="{r:g}">{r:g} µm</option>' for r in all_res)
    species = "".join(
        f'<label class="facet-item"><input type="checkbox" value="{esc(s)}"><span>'
        f'{esc(common_name(s)) or f"<em>{esc(s)}</em>"}</span><span class="count">{n}</span></label>'
        for s, n in sorted(species_count.items(), key=lambda x: (-x[1], x[0])))
    n_names = len(site.names)
    return f"""<div class="atlas-search">
<aside class="atlas-facets" hidden aria-label="Filters">
<h2>Species</h2><div class="facet-list">{species}</div>
<h2>Resolution</h2>
<div class="res-range"><label>From <select class="res-min"><option value="">any</option>{options}</select></label>
<label>to <select class="res-max"><option value="">any</option>{options}</select></label></div>
<button class="clear-facets" type="button" hidden>Clear filters</button>
</aside>
<div class="atlas-results">
<div class="atlas-searchbar" hidden><input type="search" autocomplete="off" spellcheck="false" placeholder="Search atlases" aria-label="Search atlases"></div>
<details class="atlas-syntax" hidden><summary>Search syntax</summary><table>
<tr><td><code>allen mouse</code></td><td>atlases matching every word</td></tr>
<tr><td><code>"light sheet"</code></td><td>exact phrase</td></tr>
<tr><td><code>region:CA1</code></td><td>atlases with a matching brain region (name or acronym); plain words also search regions</td></tr>
<tr><td><code>res:&lt;=25</code>, <code>res:10-50</code></td><td>available at a resolution, in µm</td></tr>
<tr><td><code>species:rattus</code></td><td>species (latin or common name)</td></tr>
<tr><td><code>sym:no</code></td><td>asymmetric atlases only</td></tr>
</table></details>
<p class="result-meta">{n_names} atlases in {len(site.collections)} collections, newest first</p>
{"".join(cards)}
<p class="no-results" hidden>No atlases match. Try fewer words or clear the filters.</p>
</div>
</div>"""


def regions_index(site: Site) -> str:
    """Brain regions of every terminology, for region search: {location: ["acronym\\tname", ...]}."""
    return json.dumps({loc: [f"{r['acronym']}\t{r['name']}" for r in rows]
                       for loc, rows in site.terminologies.items() if rows}, separators=(",", ":"))


def collections_list(site: Site) -> str:
    """MyST list of every collection by category, with the ids the old atlas details page used."""
    out = []
    for group in GROUPS:
        cs = sorted((c for c in site.collections if c["group"] == group), key=lambda c: c["title"])
        if not cs:
            continue
        out += [f"**{group}**", ""]
        out += [f'- <span id="{c["anchor"]}"></span>[{c["title"]}](/atlases/{c["names"][0]}.md)'
                + (f" ({len(c['names'])} atlases)" if len(c["names"]) > 1 else "") for c in cs]
        out.append("")
    return "\n".join(out)
