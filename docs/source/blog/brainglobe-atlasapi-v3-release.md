---
blogpost: true
date: Aug 7, 2026
author: Igor Tatarnikov
location: London, England
category: brainglobe
language: English
---


# `brainglobe-atlasapi` V3 is Here!

We're excited to announce the full release of `brainglobe-atlasapi` version 3. You can install it (or upgrade) with:

```{bash}
pip install -U brainglobe-atlasapi
```

## Major changes

### Smaller downloads

Previously, atlases were a single, large download. All images, meshes, and metadata files were bundled together. This resulted in large
monolithic archives that were slow to download. In V3, the initial download of an atlas only fetches the associated metadata. Each component
is downloaded on demand when first accessed. This makes atlas instantiation much faster, with a much smaller disk footprint. Visualising the root mesh
for all BrainGlobe atlases now only fetches that specific mesh (~100 MB) instead of downloading all images and meshes (500+ GBs!).

```{image} ./images/task_figure.png
:alt: Two routes to the same result for the task "visualise the hippocampus inside the brain". The old route downloads the whole atlas as a single 7.4 GB TAR archive containing every image and mesh. The new route downloads only the requested hippocampus and root meshes, 2.3 MB. Both end at the same rendering of a green hippocampus inside a transparent brain.
```

### File format changes

Atlases are now no longer shipped as one monolithic archive. Each atlas is now assembled from smaller, independently versioned pieces: templates, annotations, coordinate spaces, and terminologies. Components that are shared across multiple atlases (for example two atlases that have different annotations for the same template) are stored and uploaded once rather than duplicated.

Meshes are now stored in the [precomputed](https://github.com/google/neuroglancer/blob/576c94b08ad7609919eb42f8a93b9cf0e161df14/src/datasource/precomputed/meshes.md#multi-resolution-mesh-format) format. Combined with the new cloud friendly methods of storing the image data, this allows all atlases to be viewed in online viewer such as [neuroglancer](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/allen_mouse.json).

Image data are now stored as [OME-Zarr](https://ngff.openmicroscopy.org/), chunked, pyramidal, cloud-native format.

```{image} ./images/brainglobe-atlasapi_v3_structure_dark.png
:class: only-dark
:alt: An illustration showing the the remote and the local directory structures. The remote directory shows two atlases with their shared components. The total disk usage on the remote is 2.8 GB. The local directory is shown after installing the atlases. Only the necessary components are downloaded and the disk usage is 268 KB.
```

```{image} ./images/brainglobe-atlasapi_v3_structure.png
:class: only-light
:alt: An illustration showing the the remote and the local directory structures. The remote directory shows two atlases with their shared components. The total disk usage on the remote is 2.8 GB. The local directory is shown after installing the atlases. Only the necessary components are downloaded and the disk usage is 268 KB.
```

### Individually versioned components

The new version introduces individually versioned components. This not only allows reuse across multiple atlases, but also greatly simplifies the packaging process for new atlas versions. Previously, all components had to be regenerated and packaged even if the change only involved a small update to the metadata. This could take hours for high resolution atlases. With the new version only the updated component needs to be generated and repackaged with the unchanged components.
