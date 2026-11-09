---
blogpost: true
date: November 6, 2026
author: Jung Woo Kim
location: London, England
category: brainglobe
language: English
---

# The first edition of the Allen Mouse Brain Atlas has been added to BrainGlobe

There are few brain atlases as foundational to the field as the first Allen Mouse Brain Atlas, released in 2006. The first edition of the atlas, the Common Coordinate Framework version 1 (CCFv1), was created as part of the inaugural project of the Allen Institute for Brain Sciences which was to create a whole-brain map of gene expression. This framework allowed researchers to align in situ hybridisation (ISH) data to the atlas, which was a valuable tool for neuroscientists. 

The team at BrainGlobe have packaged the CCFv1 mouse brain atlas using data provided by the Allen Institute to preserve this atlas and make it accessible through our ecosystem, and to allow for the reproduction of historical results which used this atlas. The CCFv1 atlas template was created using 528 Nissl-stained OCT-embedded coronal mouse brain sections taken from male C57Bl/6J mice sectioned at 25μm thickness. These were then annotated using the Allen Reference Atlas, which in itself was made of 132 coronal 100μm sections and 21 sagittal 200μm sections, and contained only the left hemisphere. Thus, the CCFv1 atlas is an atlas with 25μm resolution, and with only the left hemisphere annotated. 

The atlas has been packaged under the name `ccfv1_mouse_25um`. 

![coronal sections of the ccfv1 mouse brain atlas](./images/ccfv1_coronal.png)

**Figure 1. Coronal view of the Allen CCFv1 Mouse Brain atlas annotations and reference image.**

## How do I use the new atlases?

You can use the CCFv1 atlas for analysis and visualisation like other BrainGlobe atlases. To visualise the atlases, you can either open them in Neuroglancer for viewing in the browser [here](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/ccfv1_mouse.json), or you can view them locally:

* Install BrainGlobe ([instructions](/documentation/index))
* Open napari and follow the steps in our [download tutorial](/tutorials/manage-atlases-in-GUI.md) for the CCFv1 atlas
* Visualise the different parts of the atlas as described in our [visualisation tutorial](/tutorials/visualise-atlas-napari)

The end result will look something like Figure 2.

![ccfv1 mouse brain atlas visualised in napari](./images/ccfv1_meshes.png)

**Figure 2: The CCFv1 Mouse Brain atlas visualised with `brainrender-napari`: with mesh overlays for the brain (grey) and the hippocampal formation (green).**

## Why are we adding new atlases?

A fundamental aim of the BrainGlobe project is to make various brain atlases easily accessible by users across the globe. The CCFv1 Mouse Brain atlases allow for users to use historical versions of the Allen 3D atlases easily on BrainGlobe. If you would like to get involved with a similar project, please [get in touch](/contact).
