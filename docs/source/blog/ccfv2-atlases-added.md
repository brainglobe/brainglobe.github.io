---
blogpost: true
date: May 19, 2026
author: Jung Woo Kim
location: London, England
category: brainglobe
language: English
---

# Three Atlases for the Allen Common Coordinate Framework v2 Mouse Brain have been added to BrainGlobe

The mouse brain atlases provided by the Allen Institute for Brain Science (AIBS) are widely used in the neuroscience community, and as of the writing of this blog post, the most updated version of their atlas is version 3 of the Common Coordinate Framework (CCF). However, there are many benefits from adding older versions of atlases, namely in terms of keeping a record of the history of atlas versions, as well as reproducing historical results which used older atlases. Therefore, we have packaged the CCFv2 mouse brain atlases provided by the Allen Institute. These include an adult mouse brain atlas with all grey matter regions without fiber tracts, an adult mouse brain atlas with only the fiber tracts, and a developmental adult mouse brain atlas containing information on the developmental taxonomy of various regions. The CCFv2 is a symmetric atlas constructed from the same 528 Nissl stained 25um coronal slices as in CCFv1, but reprocessed for symmetry and to introduce more annotations based on the Allen Reference Atlas. 

We have packaged the following three atlases: 
### 1. CCFv2 Mouse Brain Atlas
<img src="./images/ccfv2_mouse_brain.png" alt="ccfv2 mouse brain atlas annotations" >

**Figure 1. Anterior view of the CCFv2 Mouse Brain atlas annotations and reference image.**

### 2. CCFv2 Mouse Fiber Tracts Atlas
<img src="./images/ccfv2_fiber_mouse.png" alt="ccfv2 mouse fiber tracts atlas annotations" >

**Figure 2. Anterior view of the CCFv2 Mouse Fiber Tracts atlas annotations and reference image.**

### 3. CCFv2 Developmental Mouse Brain Atlas
<img src="./images/ccfv2_dev_mouse.png" alt="ccfv2 developmental mouse brain atlas annotations">

**Figure 3. Anterior view of the CCFv2 Developmental Mouse Brain atlas annotations and reference image.**


The BrainGlobe team re-packaged the data generated and made public by the Allen Institute, making it now possible to use the CCFv2 mouse atlases within the BrainGlobe ecosystem. The atlas names are `ccfv2_mouse_25um`, `ccfv2_fiber_mouse_25um`, and `ccfv2_dev_mouse_25um`.

## How do I use the new atlases?

You can use the CCFv2 atlases for visualisation like other BrainGlobe atlases, as written below:

* Install BrainGlobe ([instructions](/documentation/index))
* Open napari and follow the steps in our [download tutorial](/tutorials/manage-atlases-in-GUI.md) for the CCFv2 atlas
* Visualise the different parts of the atlas as described in our [visualisation tutorial](/tutorials/visualise-atlas-napari)

The end result will look something like Figure 4.

![ccfv2 mouse brain atlas visualised in napari](./images/ccfv2_mouse_brain_napari.png)

**Figure 4: The CCFv2 Mouse Brain atlas visualised with `brainrender-napari`: with mesh overlays for the brain (grey), the hippocampal formation (green) and the cerebellum (yellow).**

## Why are we adding new atlases?

A fundamental aim of the BrainGlobe project is to make various brain atlases easily accessible by users across the globe. The CCFv2 Mouse Brain atlases allow for users to use historical versions of the Allen 3D atlases easily on BrainGlobe. If you would like to get involved with a similar project, please [get in touch](/contact).
