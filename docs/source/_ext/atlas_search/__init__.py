"""BrainGlobe atlas search: pages generated from the public atlas bucket.

At the start of every build this extension reads the BrainGlobe atlas bucket
(``bucket.py``) and the hand-written titles, categories and descriptions in
``atlases/collections.toml``, and writes (``pages.py``):

* ``atlases/<name>.md``: one page per atlas name (all its resolutions), with a
  coronal preview, versions, download locations, brain regions and metadata;
* ``atlases/_previews/``: the preview images. Rendering them reads the volumes,
  so they are kept in a cache (``$BRAINGLOBE_ATLAS_PREVIEWS``, by default
  ``atlases/_previews`` itself) and reused while the atlas stores are unchanged.

Both are generated, not committed. Two directives use the same data:

* ``atlas-search`` (``atlases/index.md``): one card per collection, which
  ``_static/atlas-search/search.js`` filters as you type;
* ``atlas-collections``: every collection by category, with the anchors of the
  old atlas details page.

If the bucket cannot be read the build fails on CI and warns locally.
"""

from __future__ import annotations

import os
from pathlib import Path

from docutils import nodes
from sphinx.errors import ExtensionError
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

from . import bucket, pages

logger = logging.getLogger(__name__)
PAGES_DIR = "atlases"


def generate(app):
    srcdir = Path(app.srcdir)
    outdir = srcdir / PAGES_DIR
    app.atlas_site = None
    try:
        collections = pages.load_collections(outdir / "collections.toml")
        logger.info("atlas search: reading the BrainGlobe atlas bucket")
        site = pages.Site(bucket.crawl(), collections)
    except (OSError, ValueError) as e:
        if os.environ.get("CI"):
            raise ExtensionError(f"atlas search: {e}") from e
        logger.warning(f"atlas search: could not read the atlas bucket ({e}); the atlas pages are not updated")
        return
    for name in site.unknown:
        logger.warning(f"atlas search: {name} is listed in collections.toml but is not in the atlas bucket")
    for name in site.unlisted:
        logger.warning(f"atlas search: {name} is in the atlas bucket but not in collections.toml")
    cache = Path(os.path.expanduser(os.environ.get("BRAINGLOBE_ATLAS_PREVIEWS", outdir / "_previews")))
    names = pages.write_pages(site, outdir, cache, logger)
    logger.info(f"atlas search: {len(names)} atlas pages")
    app.atlas_site = site


def site_or_notice(directive):
    site = getattr(directive.env.app, "atlas_site", None)
    directive.env.atlas_search_docs = getattr(directive.env, "atlas_search_docs", set()) | {directive.env.docname}
    if site is None:
        return None, [nodes.paragraph(text="The atlas list is not available: the atlas bucket could not be read "
                                           "when this page was built.")]
    return site, None


class AtlasSearch(SphinxDirective):
    def run(self):
        site, notice = site_or_notice(self)
        return notice or [nodes.raw("", pages.search_cards(site), format="html")]


class AtlasCollections(SphinxDirective):
    def run(self):
        site, notice = site_or_notice(self)
        return notice or self.parse_text_to_nodes(pages.collections_list(site))


def outdated(app, env, added, changed, removed):
    """Pages with the directives depend on the bucket, so are rebuilt every time."""
    return sorted(getattr(env, "atlas_search_docs", set()) - removed)


def page_assets(app, pagename, templatename, context, doctree):
    if pagename.startswith(f"{PAGES_DIR}/"):
        app.add_css_file("atlas-search/atlas-search.css")
        app.add_js_file("atlas-search/atlas-search.js", defer="defer")


def write_regions(app, exception):
    site = getattr(app, "atlas_site", None)
    if exception is None and site is not None and app.builder.format == "html":
        out = Path(app.outdir) / PAGES_DIR / "regions.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(pages.regions_index(site))


def setup(app):
    app.add_directive("atlas-search", AtlasSearch)
    app.add_directive("atlas-collections", AtlasCollections)
    app.connect("builder-inited", generate)
    app.connect("env-get-outdated", outdated)
    app.connect("html-page-context", page_assets)
    app.connect("build-finished", write_regions)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
