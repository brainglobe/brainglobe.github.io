"""
Download the built atlas search site into the docs source tree.

The atlas search (``atlas-search/`` in this repository) is built by the
"Build atlas search" workflow, which pushes the result to the
``atlas-search-dist`` branch. This script copies that branch into
``source/_atlas_search/atlases/``; Sphinx copies it to ``atlases/`` in the
built website (see ``html_extra_path`` in ``conf.py``).

If the download fails (e.g. offline), a placeholder page is written instead so
the rest of the documentation still builds.
"""

import io
import os
import shutil
import tarfile
import urllib.request
from pathlib import Path

BRANCH = "atlas-search-dist"
REPO = os.environ.get("GITHUB_REPOSITORY", "brainglobe/brainglobe.github.io")
URL = f"https://codeload.github.com/{REPO}/tar.gz/refs/heads/{BRANCH}"
DEST = Path(__file__).parent / "source" / "_atlas_search" / "atlases"

PLACEHOLDER = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Atlas search</title></head>
<body><p>The atlas search was not included in this build of the website.
See the <a href="https://brainglobe.info/atlases/">BrainGlobe atlas search</a>.</p></body></html>
"""

if DEST.exists():
    shutil.rmtree(DEST)
DEST.mkdir(parents=True)

print(f"Fetching atlas search from {REPO}@{BRANCH}...")
try:
    with urllib.request.urlopen(URL, timeout=120) as r:
        data = r.read()
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
        for member in tar.getmembers():
            # strip the "<repo>-<branch>/" directory GitHub adds
            parts = Path(member.name).parts[1:]
            if not parts or not (member.isfile() or member.isdir()):
                continue
            member.name = str(Path(*parts))
            tar.extract(member, DEST, filter="data")
    print(f"Atlas search written to {DEST}")
except Exception as e:  # noqa: BLE001
    print(f"WARNING: could not fetch the atlas search ({e}); writing a placeholder")
    (DEST / "index.html").write_text(PLACEHOLDER)
