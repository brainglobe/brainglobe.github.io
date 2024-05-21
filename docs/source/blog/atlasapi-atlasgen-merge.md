---
blogpost: true
date: Feb 14, 2024
author: Will Graham
location: London, England
category: brainglobe
language: English
---

# `bg-atlasapi` and `bg-atlasgen` have merged under a new name

`bg-atlasapi` and `bg-atlasgen` have merged into a single package, now called `brainglobe-atlasapi`.
`brainglobe-atlasapi` now provides the same API that `bg-atlasapi` provided, in exactly the same way - all that needs to happen is a name change in your scripts.

`bg-atlasgen` used to provide the developer code for adding a new atlas to the collection of BrainGlobe atlases that are available for download.
This code was exclusively used by developers, however it hinges on the functionality of `bg-atlasapi` to complete the generation and upload process.
As such, it has now been moved into a submodule, `brainglobe_atlasapi.atlas_generation`, but again the way one interacts with this submodule is the same as they would have with `bg-atlasgen`.

## What do I need to do?

If you are using an install of `bg-atlasapi` that you got through `pip install brainglobe`, then all you need to do is update `brainglobe` to the latest version with

```bash
pip install --upgrade brainglobe
```

This will remove the old packages from your environment, install `brainglobe-atlasapi`, and also update all your other BrainGlobe tools to use the new package rather than the old `bg-atlasapi`.

If you were previously using a standalone install of `bg-atlasapi`, to continue receiving updates you should perform the following changes to your environment:

- Uninstall `bg-atlasapi` (and `bg-atlasgen` if you have it).
- Install the latest version of `brainglobe-atlasapi`.
- Update all of the following BrainGlobe tools that you also have in your environment:
  - `brainrender-napari`
  - `brainglobe-utils`
  - `brainglobe-segmentation`
  - `brainreg`
  - `brainglobe-napari-io`
  - `cellfinder`
  - `morphapi`
  - `brainrender`
  - `brainglobe-heatmap`
