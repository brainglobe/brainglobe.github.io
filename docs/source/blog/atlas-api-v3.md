---
blogpost: true
date: Jul 17, 2026
author: Igor Tatarnikov
location: London, England
category: brainglobe
language: English
---

# `brainglobe-atlasapi` V3 pre-release

A pre-release version of `brainglobe-atlasapi` V3 is now available. You can install it using by running:

```bash
pip install brainglobe-atlasapi --pre
```

Please try it in your tools and workflows, in a fresh environment if possible, and report any issues you encounter on either [Zulip](https://brainglobe.zulipchat.com/#narrow/channel/483906-Atlas-API) or [GitHub](https://github.com/brainglobe/brainglobe-atlasapi/issues).

## New file formats and storage

The most significant change is how atlases are stored on disk. Previously, each atlas was a single package, including `reference.tiff`, `annotation.tiff`, `hemispheres.tiff` files, a `structures.json` and a `meshes/` folder, bundled together and downloaded from GIN as one monolithic archive.

V3 moves image data to [OME-Zarr](https://ngff.openmicroscopy.org/), a chunked, pyramidal, cloud-native format, and stores everything on AWS S3.
Further, an atlas is no longer a monolithic bundle. It's now assembled from independently versioned components: templates, annotation sets, coordinate spaces and terminologies. Each of these can be shared between atlases and updated on its own. The directory structure is based on the [Atlas Asset Organization](https://atlas-assets.readthedocs.io/en/latest/index.html) from the Allen Institute.

```{image} ./images/brainglobe-atlasapi_v3_structure_dark.png
:class: only-dark
:alt: An illustration showing the the remote and the local directory structures. The remote directory shows two atlases with their shared components. The total disk usage on the remote is 2.8 GB. The local directory is shown after installing the atlases. Only the necessary components are downloaded and the disk usage is 268 KB.
```

```{image} ./images/brainglobe-atlasapi_v3_structure.png
:class: only-light
:alt: An illustration showing the the remote and the local directory structures. The remote directory shows two atlases with their shared components. The total disk usage on the remote is 2.8 GB. The local directory is shown after installing the atlases. Only the necessary components are downloaded and the disk usage is 268 KB.
```

**Figure 1. An example of the local and remote directory structure for brainglobe-atlasapi V2 and V3.**

Importantly, installing an atlas no longer downloads all components up front. The meshes, template, and annotations are fetched from S3 the first time you access them. That means faster instantiation and a much smaller footprint on disk than the previous monolithic atlases. This also allows the components to be streamed to online viewers such as [neuroglancer](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/columbia_cuttlefish.json).

## What do I need to do?

Ideally, nothing! The Python API is unchanged. You will need to update the atlases you have stored on disk the first time you run your pipelines, but this will happen automatically, as `brainglobe-atlasapi` V3 is not compatible with the previous atlas format. As the old files are no longer used, they can be safely removed. For example, `~/.brainglobe/allen_mouse_25um` can be deleted.

One small note: `atlas.reference` is now a deprecated alias for `atlas.template`. It will continue working, but prints a warning and will be removed in a future version.
