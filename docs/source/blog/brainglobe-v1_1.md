---
blogpost: true
date: May 16, 2024
author: Adam Tyson
location: London, England
category: brainglobe
language: English
---

# BrainGlobe version 1.1 is released!

A new version of the BrainGlobe metapackage has been released following updates to lots of BrainGlobe tools 
(details below). 

## Main updates
Most updates are relatively minor, but if you use `cellfinder`, `brainmapper` or `brainrender` the 
location of data automatically downloaded by the software has moved. Please see those sections for more details.

We would like to thank [Matt Einhorn](https://github.com/matham) who has contributed greatly to this 
release. In particular, he has made many contributions to `cellfinder`, including by speeding up cell detection. 

## What do I need to do?
If you have an installation of the metapackage (recommended) then all you need to do is update `brainglobe` to the 
latest version with:
```bash
pip install --update brainglobe
```

If you use `brainglobe-workflows` (e.g. for `brainmapper`) you will need to update it individually, as it is not 
included within the metapackage:
```bash
pip install --update brainglobe-workflows
```

If you have a single tool installed, you can just update that tool. For example to update `brainrender`, run:
```bash
pip install --update brainrender
```

## Details
### `brainglobe-atlasapi`
- Updated, fixed versions of the `kim_mouse` (50, 25 & 10 micron) and `perens_lsfm_mouse` (20 micron) atlases have 
been released.
- Minor fixes and updates to the atlas update workflow.

### `brainglobe-segmentation`
- Minor updates to be compatible with the latest version of `brainglobe-utils`.

### `brainglobe-utils`
- Code for data loading (e.g. `read_with_dask`) has been moved from `cellfinder`. If you use this in your code,
  please change your import from `from cellfinder.core.tools.IO import read_with_dask` to
  `from brainglobe_utils.IO.image.load import read_with_dask`.

### `brainglobe-workflows`
- `brainmapper` has been updated to the latest version of cellfinder. Please see the [`cellfinder`](cellfinder) section 
for more details.

### `brainreg`
- A bug was fixed causing registration performance in the napari plugin to be slightly worse than via the command line.
- The number of CPU cores to leave free can now be set in the napari plugin.
- Some parameter names in the napari plugin have been given more descriptive names.
- Minor updates to be compatible with the latest version of `brainglobe-utils`.

### `brainrender`
- Automatically downloaded data are now saved to `.brainglobe/brainrender` in your home directory. Previously data were 
saved to `.brainglobe`. Some scripts may take slightly longer the next time you run them as data is re-downloaded. You 
can safely delete the `.brainrender` directory in your home directory if you would like to clear space. Be aware this 
directory is usually hidden by default in most file navigation applications.
- [Screenshots can now be saved into multiple formats](/documentation/brainrender/usage/videos-animations-and-exporting-to-html).
- A bug in the default (cartoon) shader mode which caused the scene to appear jagged when rotated has been fixed.
- Minor updates to be compatible with the latest version of `brainglobe-utils`.
- SWC files without a soma can now be loaded (via [`morphapi`](/documentation/morphapi/index)).

(cellfinder)=
### `cellfinder`
- The napari plugin has been sped up and is now more responsive when an image is open.
- Detection and classification can now be run independently in the napari plugin. This is useful for parameter 
optimisation, and in some cases, classification is not needed at all (e.g. nuclear labelled cells).
- Cell detection has been optimised and should now be considerably faster. On a c-Fos stained whole mouse brain image 
with ~3.5 million cell candidates, cell detection went from 8.5 to 5.5 hours.
- Code for data loading (e.g. `read_with_dask`) has been moved to `brainglobe-utils`. If you use this in your code, 
please change your import from `from cellfinder.core.tools.IO import read_with_dask` to 
`from brainglobe_utils.IO.image.load import read_with_dask`.
- Downloaded pre-trained models are now saved to `.brainglobe/cellfinder/models` in your home directory. Previously data were
  saved to `.cellfinder`. You can safely delete the `.cellfinder` directory in your home directory if you would 
like to clear space. Be aware this directory is usually hidden by default in most file navigation applications. If you 
would like to download the models to the new directory in advance of using the software, please see 
[the guide to the `cellfinder_download` tool](/documentation/cellfinder/user-guide/cellfinder-download).
