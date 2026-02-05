---
blogpost: true
date: February 3, 2026
author: Harry Carey
location: London, England
category: brainglobe
language: English
---


# New mouse brain atlas based on gene expression

The CArea atlas has been added to brainglobe. The CArea atlas has regions based on clustering 3D volumes of gene expression, finding voxels with similar "gene expression fingerprints". Data from over 1000 mice was used to generate both volumes of gene expression, and an average Nissl template. This template is a slightly improved and updated version the [CCFv3BBP template](https://doi.org/10.1162/imag_a_00565) (also in brainglobe as [ccfv3augmented_mouse](https://brainglobe.info/documentation/brainglobe-atlasapi/usage/atlas-details.html#ccfv3-augmented-mouse-atlas)). 

In the future, atlases regions may be defined automatically based on cell type, pathology, or other properties which can be mapped to a template. A paper describing this atlas and the accompanying gene expression dataset is now available on [bioRxiv](https://doi.org/10.64898/2026.01.20.700446). 

- **Atlas name:** `carea_mouse_25um`
- **Resolution:** 25 µm isotropic
- **Template space:** Aligned to the CCFv3BBP



![CArea mouse atlas](images/carea_flythrough.gif)


### Availability and collaboration 

The atlas is available via the BrainGlobe Atlas API and can be used seamlessly with tools such as `brainreg`, `brainrender`, `napari`, and `brainrender-napari`.

If you’re interested in using this atlas or collaborating on future developments, feel free to [get in touch](/contact).