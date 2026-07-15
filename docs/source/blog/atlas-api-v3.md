---
blogpost: true
date: Jul 15, 2026
author: Igor Tatarnikov
location: London, England
category: brainglobe
language: English
---

# `brainglobe-atlasapi` V3

A pre-release version of `brainglobe-atlasapi` V3 is now available.

## New file formats and storage

The most significant change is how atlases are stored on disk. In the current version, each atlas is a single package: `reference.tiff`, `annotation.tiff`, `hemispheres.tiff`, a `structures.json` and a `meshes/` folder, bundled together and downloaded from GIN as one monolithic archive.

V3 moves image data to [OME-Zarr](https://ngff.openmicroscopy.org/), a chunked, pyramidal, cloud-native format, and stores everything on AWS S3.
Further, an atlas is no longer a monolithic bundle. It's now assembled from independently versioned components: templates, annotation sets, coordinate spaces and terminologies. Each of these can be shared between atlases and updated on its own.

Importantly, installing an atlas no longer downloads all components up front. The meshes, template, and annotations are streamed from S3 the first time you access them. That means faster instantiation and a much smaller footprint on disk and bandwidth than the previous monolithic atlases.

## What do I need to do?

Ideally, nothing! The Python API is unchanged. You will need to update the atlases you have stored on disk the first time you run your pipelines, but this will happen automatically, as `brainglobe-atlasapi` V3 is not compatible with the previous atlas format.

```python
from brainglobe_atlasapi import BrainGlobeAtlas

atlas = BrainGlobeAtlas("allen_mouse_25um")
atlas.annotation   # numpy array, as before
atlas.structures   # structures dictionary
atlas.root_mesh()  # meshio.Mesh object
```

One small note: `atlas.reference` is now a deprecated alias for `atlas.template`. It will continue working, but prints a warning and will be removed in a future version.
