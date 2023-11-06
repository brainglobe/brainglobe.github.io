# November 2023

This roadmap reflects our current priorities which are to refactor and organise the BrainGlobe codebase. Many of these changes won't add any new features - they are largely aimed at making existing features more accessible (e.g. through a graphical user interface), ensure all tools are easier-to-install and at making BrainGlobe 
easier to maintain and further develop in the long-term.  We hope this will ensure that BrainGlobe is around for years to come, and that we have a solid platform to develop new tools and support a growing community in the future.

## Current status
* BrainGlobe Atlas API provides a consistent interface to multiple anatomical atlases
* Separate tools for 3D cell detection ([`cellfinder-core`](https://github.com/brainglobe/cellfinder-core)), 
3D atlas registration([`brainreg`](https://github.com/brainglobe/brainreg)), bulk segmentation 
([`brainreg-segment`](https://github.com/brainglobe/brainreg-segment)) and 3D 
visualisation ([`brainrender`](https://github.com/brainglobe/brainrender))
* Plugins for 3D cell detection ([`cellfinder-napari`](https://github.com/brainglobe/cellfinder-napari)) and 
registration ([`brainreg-napari`](https://github.com/brainglobe/brainreg-napari))

### Issues
* [`brainrender`](https://github.com/brainglobe/brainrender) has considerable technical debt 
([brainrender/247](https://github.com/brainglobe/brainrender/issues/247))
* Lots of repositories makes it more difficult to understand which tool does what, and to contribute 
(e.g. [`cellfinder`](https://github.com/brainglobe/cellfinder), 
[`cellfinder-core`](https://github.com/brainglobe/cellfinder-core), [`cellfinder-napari`](https://github.com/brainglobe/cellfinder-napari))
* The mix of napari plugins, Python APIs and command line tools make the ecosystem appear more complicated than it should
* It is not yet possible to carry out all analyses and visualisation within a single platform (napari)
    * Some non-image processing steps need to be carried out seperately (e.g. assigning cells to brain regions)
    * Some visualisation relies on exporting data from napari to brainrender

## v1 (Q4 2023)
* brainrender installable alongside analysis tools (cellfinder, brainreg, brainreg-segment)
* All tools installable via `pip install brainglobe` or `conda install brainglobe -c conda-forge`

## v2 (Q2 2024)
* Consistent API, e.g. `from brainglobe import cellfinder` or `from brainglobe import cell_detector_3D` (or both)
* Carry out everything in v1 without leaving napari
    * Atlas registration ([`brainreg-napari`](https://github.com/brainglobe/brainreg-napari))
    * Cell detection ([`cellfinder-napari`](https://github.com/brainglobe/cellfinder-napari))
    * Assign cells to brain regions (TBC)
    * Analyse arbitrary ROIs ([`brainreg-segment`](https://github.com/brainglobe/brainreg-segment))
    * Visualisation ([`brainrender-napari`](https://github.com/brainglobe/brainrender-napari))
* Automated benchmarks for analysis tools (cell detection & 3D atlas registration) on "real" (full size) data
* Combine napari plugins with backend to reduce number of repositories 
([BrainGlobe/3](https://github.com/brainglobe/BrainGlobe/issues/3) & 
([BrainGlobe/4](https://github.com/brainglobe/BrainGlobe/issues/4))
* Remove existing `cellfinder` CLI to simplify naming ([BrainGlobe/6](https://github.com/brainglobe/BrainGlobe/issues/6))
* Release [`brainglobe-workflows`](https://github.com/brainglobe/brainglobe-workflows), a collection of scripts to 
facilitate common tasks (including replacing the `cellfinder` CLI)

## v3 (Q4 2024)
* Intuitive navigation of napari plugins
    * Create "metaplugin"
* Generic layer interpreters ([BrainGlobe/10](https://github.com/brainglobe/BrainGlobe/issues/10))
* Refactored and documented Python API
* Facilitate common analyses/visualisation within napari
    * Plot cells per brain region
* Sample data provided via napari

## Other ongoing projects (release TBC)
* Arbitrary brain subvolume (2D or 3D) registration 
([`brainglobe-registration`](https://github.com/brainglobe/brainglobe-registration))
* Atlas generation tool (from raw data to BrainGlobe atlas), including 
[`brainglobe-template-builder`](https://github.com/brainglobe/brainglobe-template-builder)
* More flexible BrainGlobe atlas API V2 ([bg-atlasapi/141](https://github.com/brainglobe/bg-atlasapi/issues/141))
* New atlases
    * Update Allen adult mouse brain atlas ([bg-atlasgen/46](https://github.com/brainglobe/bg-atlasgen/issues/46))
    * 3D Multimodal Developmental Mouse Brain atlases ([bg-atlasgen/71](https://github.com/brainglobe/bg-atlasgen/issues/71))
    * Human MRI atlases ([bg-atlasgen/85](https://github.com/brainglobe/bg-atlasgen/issues/85))
    * Update Waxholm rat atlas ([bg-atlasgen/84](https://github.com/brainglobe/bg-atlasgen/issues/84))
