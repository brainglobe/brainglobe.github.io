---
html_theme.sidebar_secondary.remove: true
---

(target-atlas-search)=
# Atlas search

<!-- The atlas search runs in the browser: source/_static/atlas-search/ renders into
     #app, reading the index that `make html` builds with docs/make_atlas_index.py. -->
<script type="importmap">{"imports": {"zarrita": "https://cdn.jsdelivr.net/npm/zarrita@0.7.5/+esm"}}</script>
<link rel="stylesheet" href="../_static/atlas-search/style.css">
<div id="atlas-search-app">
<div id="app"><p class="muted">Loading atlas index…</p></div>
<aside id="jobs" class="jobs" aria-live="polite" hidden></aside>
</div>
<script type="module" src="../_static/atlas-search/main.js"></script>

Atlas data are read directly from the public
[BrainGlobe atlas bucket](https://brainglobe.s3.us-west-2.amazonaws.com/atlas/atlases/last_versions.conf).
Please cite the original publication of any atlas you use. <span id="index-date"></span>
