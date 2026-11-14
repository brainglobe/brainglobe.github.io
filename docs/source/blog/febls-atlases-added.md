---
blogpost: true
date: November 14, 2026
author: Jung Woo Kim
location: London, England
category: brainglobe
language: English
---

# The FeBls Female Mouse Brain Atlases have been added to BrainGlobe

When using brain atlases, it is vital that the atlas matches specifically to the animal model in question. Many mouse brain atlases are either restricted to male mice, or a combination across all sexes. This can be a problem in comparative research, or research specifically on female mice. To address this shortcoming of existing mouse brain templates, [Stoehrmann et al. (2024)](https://world-wide.org/fens-24/novel-vivo-template-female-c40lw2ab) created a novel in-vivo MRI averaged template of exclusively female mouse brains, called the Female Black six (FeBls) template brain. This was created by imaging 80 female mice with 9.4 T MRI scanners, and using their axial and coronal scans to create a 60μm isotropic brain template. The samples were aligned based on tissue probability maps provided by the Turone Mouse Brain Template and Atlas ([TMBTA](https://doi.org/10.1016/j.neuroimage.2021.117776)). Then, various commonly used mouse brain atlases were registered to the FeBls template space, including the [Allen](https://doi.org/10.1016/j.cell.2020.04.007), [DSURQE](https://doi.org/10.1038/s41467-018-04921-2) and [TMBTA](https://doi.org/10.1016/j.neuroimage.2021.117776) mouse brain atlases. Both their templates and annotations were warped to fit the FeBls template mouse brain, and are all provided as part of this atlas set. We have packaged these atlases into BrainGlobe to make them available through the BrainGlobe ecosystem. 

We have packaged the following atlases: 
* `febls_allen_mouse_60um`
* `febls_dsurqe_mouse_60um`
* `febls_tmbta_mouse_60um`


![coronal sections of the febls female mouse brain atlases](./images/febls_coronal.png)

**Figure 1. Coronal sections of the templates and annotations available as part of these atlases.**


## How do I use the new atlases?

You can use the FeBls female mouse brain atlases for analysis and visualisation like other BrainGlobe atlases. To visualise the atlases, you can either open them in Neuroglancer for viewing in the browser at:
* [`FeBls with Allen annotations`](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/febls_allen_mouse.json)
* [`FeBls with DSURQE annotations`](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/febls_dsurqe_mouse.json)
* [`FeBls with TMBTA annotations`](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/febls_tmbta_mouse.json)

or you can view them locally:

* Install BrainGlobe ([instructions](/documentation/index))
* Open napari and follow the steps in our [download tutorial](/tutorials/manage-atlases-in-GUI.md) for the FeBls female mouse brain atlas
* Visualise the different parts of the atlas as described in our [visualisation tutorial](/tutorials/visualise-atlas-napari)

The end result will look something like Figure 2.


![febls female mouse brain atlas with allen annotations visualised in napari](./images/febls_napari.png)

**Figure 2: The FeBls atlas with Allen annotations visualised with `brainrender-napari`: with mesh overlays for the brain (grey) and the hippocampal formation (green).**

## Why are we adding new atlases?

A fundamental aim of the BrainGlobe project is to make various brain atlases easily accessible by users across the globe. If you would like to get involved with a similar project, please [get in touch](/contact).
