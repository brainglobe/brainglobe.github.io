---
blogpost: true
date: Nov 1, 2023
author: Will Graham
location: London, England
category: BrainGlobe-v1
language: English
---

# Version 1 of `brainreg` and `brainglobe-segmentation` released

The [restructuring of BrainGlobe](./version_1_announcement.md) is underway, beginning with the release of version 1 of `brainreg` and `brainglobe-segmentation` (previously known as `brainreg-segment`).
Previously, there were three tools with the prefix `brainreg` ("brain registration") that were split across three packages:

- `brainreg` was the core Python package that contained the functional code for performing registration of an atlas to a sample image (sequence).
- `brainreg-napari` provided a plugin to perform the registration steps interactively through napari. It depended on `brainreg` for the core functionality.
- `brainreg-segment` was a companion to `brainreg` that allowed for segmentation of regions/objects within the brain. However it was not necessarily involved with the registration process itself.

This release sees `brainreg` come bundled with its napari plugin as an optional package extra, rather than requiring users to install the two packages separately.
Consequently, `brainreg-napari` has been retired; we recommend you uninstall this package from your environments when you update.
The "combined" `brainreg` is now tagged as `brainreg v1.0.0` and should be considered a stable first release of this tool.

`brainglobe-segmentation` is the new name of the `brainreg-segment` tool.
With the forthcoming release of BrainGlobe version 1 and the development of `brainglobe-registration`, the decision was made to disambiguate the role of the segmentation functionality and combine the napari plugin with the core functionality.

## What do I need to do?

If you were previously using any of the affected tools; you don't need to do anything right now if you want to wait for the full release of BrainGlobe version 1, which will take care of these dependencies for you.
In the time between now and then, the tools as installed will still work but be aware that they will no longer receive updates due to the restructuring.

If you would like to update your packages now, or would like to know how this will affect your scripts or workflows, [see the full changelog](#full-changelog) which covers API changes and the installation process.

## Full changelog

You can find the [full changelog on the releases page](../../community/releases/v1/brainreg.md).
