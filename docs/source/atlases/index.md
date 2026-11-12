---
html_theme.sidebar_secondary.remove: true
---

(target-atlas-search)=
# Atlas search

Search the atlases available through the [BrainGlobe Atlas API](/documentation/brainglobe-atlasapi/index.md) by
name, species, resolution or brain region. Each atlas page has a preview, its versions and brain regions, and
links to view it in neuroglancer or download it.

```{atlas-search}
```

Atlas data are read from the public
[BrainGlobe atlas bucket](https://brainglobe.s3.us-west-2.amazonaws.com/atlas/atlases/last_versions.conf)
each time this website is built. Please cite the original publication of any atlas you use.

```{toctree}
:hidden:
:glob:

*
```
