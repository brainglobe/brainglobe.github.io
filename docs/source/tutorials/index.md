# Tutorials

## Getting started

::::{grid} 1 2 2 3
:gutter: 3

:::{grid-item-card} {fas}`brain;sd-text-primary` Atlas visualisation
:img-bottom: images/visualise-atlas-napari.png
:link: visualise-atlas-napari
:link-type: doc
Visualise atlas data in napari
:::

:::{grid-item-card} {fas}`brain;sd-text-primary` 3D registration
:img-bottom: images/brainreg.png
:link: tutorial-whole-brain-registration
:link-type: doc
Registering a whole-brain dataset to an atlas.
:::

:::{grid-item-card} {fas}`brain;sd-text-primary` Track segmentation
:img-bottom: images/brainglobe-segmentation-1d-icon.png
:link: segmenting-1d-tracks
:link-type: doc
Manually segmenting a 1d track.
:::

:::{grid-item-card} {fas}`brain;sd-text-primary` Structure segmentation
:img-bottom: images/brainglobe-segmentation-3d-icon.png
:link: segmenting-3d-structures
:link-type: doc
Manually segmenting a 3d structure
:::

:::{grid-item-card} {fas}`brain;sd-text-primary` 3D cell detection
:img-bottom: images/cellfinder-detection-icon.png
:link: cellfinder-detection
:link-type: doc
Detecting cells in 3D with cellfinder in napari
:::

:::{grid-item-card} {fas}`brain;sd-text-primary` Analysing cell distributions
:img-bottom: images/brainmapper-widget/cell-counts.png
:link: transform-cells-atlas
:link-type: doc
Analysing cell distributions in the brain with napari
:::

:::{grid-item-card} {fas}`brain;sd-text-primary` Retraining cellfinder
:img-bottom: images/cellfinder-retraining-icon.png
:link: cellfinder-retraining
:link-type: doc
Retraining the cellfinder cell classification network in napari
:::

:::{grid-item-card} {fas}`brain;sd-text-primary` Atlas download
:img-bottom: images/atlas-versions.png
:link: manage-atlases-in-GUI
:link-type: doc
Download an atlas with napari
:::
::::

## Specific applications

::::{grid} 1 2 2 3
:gutter: 3

:::{grid-item-card} {fas}`brain;sd-text-primary` Probe segmentation
:img-bottom: images/probes.png
:link: silicon-probe-tracking
:link-type: doc
Analysis of silicon probe tracks (e.g. Neuropixels)
:::

:::{grid-item-card} {fas}`brain;sd-text-primary` Bulk tracing analysis
:img-bottom: images/bulkaxons.png
:link: tracing-tracking
:link-type: doc
Analyze and visualize bulk fluorescence tracing data
:::

:::{grid-item-card} {fas}`brain;sd-text-primary` Cell detection via brainmapper
:img-bottom: images/cellfinder.png
:link: brainmapper/index
:link-type: doc
Whole brain cell detection and registration
:::

:::{grid-item-card} {fas}`brain;sd-text-primary` Aligning samples
:img-bottom: images/brainglobe-template-builder/template-builder-header.png
:link: template-builder-pre-align
:link-type: doc
Aligning samples to image axes for template building (experimental!)
:::

:::{grid-item-card} {fas}`brain;sd-text-primary` Exploring atlas data
:img-bottom: ../aws_examples/images/thumb/sphx_glr_explore_atlas_thumb.png
:link: ../aws_examples/explore_atlas.html
:link-type: url
Deepening understanding of atlas data and metadata (experimental!)
:::

::::

## API tutorials
::::{grid} 1 2 2 3
:gutter: 3

:::{grid-item-card} {fas}`brain;sd-text-primary` BrainGlobe Atlas API
:img-bottom: ../api_examples/images/thumb/sphx_glr_brainglobe_atlasapi_thumb.png
:link: ../api_examples/brainglobe_atlasapi.html
:link-type: url
Using the BrainGlobe Atlas API to fetch and inspect an atlas
:::
::::

## Downloads
- [⬇️ Download all examples in Python source code (.zip)](/api_examples/api_examples_python.zip)
- [⬇️ Download all examples in Jupyter notebooks (.zip)](/api_examples/api_examples_jupyter.zip)



## Related tutorials
These are tutorials hosted elsewhere that may be useful to BrainGlobe users.

::::{grid} 1 2 2 3
:gutter: 3

:::{grid-item-card} {fas}`brain;sd-text-primary` Cell detection with BiaPy
:img-bottom: images/biapy.png
:link: https://biapy.readthedocs.io/en/latest/tutorials/detection/brain_cell_detection.html
:link-type: url
Whole-brain microscopy analysis with BrainGlobe and BiaPy
:::
::::

```{toctree}
:maxdepth: 2
:caption: Index
:hidden:
visualise-atlas-napari
manage-atlases-in-GUI
tutorial-whole-brain-registration
segmenting-1d-tracks
segmenting-3d-structures
transform-cells-atlas
cellfinder-detection
cellfinder-retraining
silicon-probe-tracking
tracing-tracking
brainmapper/index
template-builder-pre-align
../api_examples/brainglobe_atlasapi
../aws_examples/explore_atlas
```
