"""List the atlases in the BrainGlobe atlas bucket on the atlas details page.

The ``atlas-versions`` directive takes one or more atlas names (the ``name`` in
an atlas manifest, e.g. ``allen_mouse``; glob patterns such as
``demba_allen_seg_dev_mouse_*`` also work) and renders a table of every atlas in
the bucket with those names, so the resolutions and versions listed on the
website are always those that the BrainGlobe Atlas API will download::

    ```{atlas-versions} allen_mouse
    ```

The bucket is read once per build. At the end of the build a warning lists
every atlas name in the bucket that no directive shows, i.e. atlases that still
need a section on the atlas details page.
"""

from __future__ import annotations

import configparser
import fnmatch
import json
import os
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from functools import cache

from sphinx.errors import ExtensionError
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

BUCKET = "https://brainglobe.s3.us-west-2.amazonaws.com"
ROOT = f"{BUCKET}/atlas"
NEUROGLANCER = "https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files"
logger = logging.getLogger(__name__)


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=60) as response:
        return response.read()


@cache
def bucket_atlases() -> dict[str, list[dict]]:
    """Map atlas name -> manifests of the latest version of each of its atlases."""
    conf = configparser.ConfigParser()
    conf.read_string(fetch(f"{ROOT}/atlases/last_versions.conf").decode())

    def manifest(item):
        key, version = item
        location = f"/atlases/{key}/{version.replace('.', '_')}"
        return {"key": key, **json.loads(fetch(f"{ROOT}{location}/manifest.json"))}

    with ThreadPoolExecutor(16) as pool:
        manifests = list(pool.map(manifest, conf["atlases"].items()))
    by_name: dict[str, list[dict]] = {}
    for m in manifests:
        by_name.setdefault(m["name"], []).append(m)
    return by_name


@cache
def neuroglancer_views() -> set[str]:
    """Names of the atlases that have a neuroglancer view (ng_state_files/<name>.json)."""
    listing = fetch(f"{BUCKET}/?list-type=2&prefix=ng_state_files/").decode()
    return set(re.findall(r"<Key>ng_state_files/([^<]+)\.json</Key>", listing))


def matching(patterns, names):
    return {n for n in names if any(fnmatch.fnmatchcase(n, p) for p in patterns)}


def natural(text: str):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", text)]


def resolution(m: dict) -> str:
    res = [f"{r:g}" for r in m["resolution"]]
    return f"{res[0]} µm" if len(set(res)) == 1 else f"{' × '.join(res)} µm"


class AtlasVersions(SphinxDirective):
    required_arguments = 1
    optional_arguments = 50

    def run(self):
        patterns = self.arguments
        self.env.brainglobe_atlas_names.setdefault(self.env.docname, set()).update(patterns)
        try:
            atlases = bucket_atlases()
            views = neuroglancer_views()
        except OSError as e:
            if os.environ.get("CI"):
                raise ExtensionError(f"could not read the BrainGlobe atlas bucket: {e}") from e
            logger.warning(f"could not read the BrainGlobe atlas bucket ({e}); "
                           "atlas versions are not listed", location=self.get_location())
            return []

        for p in patterns:
            if not matching([p], atlases):
                logger.warning(f"no atlas named {p!r} in the BrainGlobe atlas bucket",
                               location=self.get_location())
        manifests = [m for n in matching(patterns, atlases) for m in atlases[n]]
        if not manifests:
            return []
        # One atlas name has one neuroglancer view, linked from its section;
        # tables covering several names (e.g. ages) link each one.
        per_name = len({m["name"] for m in manifests}) > 1
        header = ["Name in API", "Resolution", "Version", *(["Neuroglancer"] if per_name else []), "Files"]
        table = ["| " + " | ".join(header) + " |", "|" + " --- |" * len(header)]
        for m in sorted(manifests, key=lambda m: natural(m["key"])):
            view = f"[View]({NEUROGLANCER}/{m['name']}.json)" if m["name"] in views else ""
            files = (f"[manifest]({ROOT}{m['location']}/manifest.json) · "
                     f"[terminology]({ROOT}{m['terminology']['location']}/terminology.csv)")
            cells = [f"`{m['key']}`", resolution(m), m["version"], *([view] if per_name else []), files]
            table.append("| " + " | ".join(cells) + " |")
        return self.parse_text_to_nodes("\n".join(table))


def init_env(app, env, docnames):
    if not hasattr(env, "brainglobe_atlas_names"):
        env.brainglobe_atlas_names = {}


def purge_doc(app, env, docname):
    getattr(env, "brainglobe_atlas_names", {}).pop(docname, None)


def merge_info(app, env, docnames, other):
    env.brainglobe_atlas_names.update(other.brainglobe_atlas_names)


def check_listed(app, env):
    """Warn about atlases in the bucket that the website does not list."""
    patterns = set().union(*env.brainglobe_atlas_names.values())
    if not patterns:
        return
    try:
        unlisted = sorted(set(bucket_atlases()) - matching(patterns, bucket_atlases()))
    except OSError:
        return  # already reported by the directive
    for name in unlisted:
        keys = ", ".join(m["key"] for m in bucket_atlases()[name])
        logger.warning(f"atlas {name!r} ({keys}) is in the BrainGlobe atlas bucket "
                       "but has no atlas-versions directive")


def setup(app):
    app.add_directive("atlas-versions", AtlasVersions)
    app.connect("env-before-read-docs", init_env)
    app.connect("env-purge-doc", purge_doc)
    app.connect("env-merge-info", merge_info)
    app.connect("env-check-consistency", check_listed)
    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True,
            "env_version": 1}
