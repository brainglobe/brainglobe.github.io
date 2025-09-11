---
blogpost: true
date: September 11, 2025
author: Harry Carey
location: Oslo, Norway
category: brainglobe
language: English
---
# DeMBA, A 4D atlas representing mouse brain development from adolescence to adulthood 

[Carey & Kleven et al., 2025](https://doi.org/10.1038/s41467-025-63177-9) recently published DeMBA (The Developmental Mouse Brain Atlas), an atlas of postnatal mouse brain development. This atlas covers 53 days of development, from day 4 after birth through to day 56. It provides the annotations from the Allen CCFv3 transformed down to the younger ages. With this atlas researchers who study development can choose an atlas specific to the postnatal day they are interested in. Another key feature of this atlas is its integration into the [BrainGlobe CCF Translator](https://github.com/brainglobe/brainglobe-ccf-translator), which allows data to be transformed from any of the ages to any of the other ages.  


![Coronal views of the demba atlas at different timepoints](./images/demba.png)
**Figure 1: Various coronal views of the demba atlas at different timepoints. Each cross section shows the STPT template on the left side and the transformed CCFv3 segmentations on the right.**


DeMBA is available in both 20µm and 25µm. At 25µm STPT, MRI and LSFM templates are provided whereas only STPT at 20µm. All ages from 4 to 56 are available through the BrainGlobeAPI. For instance the 20µm p4 atlas can be accessed through BrainGlobe as ```demba_allen_seg_dev_mouse_p4_20um```. For more information see the  [atlas documentation](https://brainglobe.info/documentation/brainglobe-atlasapi/usage/atlas-details.html#demba-developmental-mouse-brain-atlas).

## How do I use the new atlas?

You can use the DeMBA for visualisation like other BrainGlobe atlases. To visualise the atlas, you could follow the steps below:

* Install BrainGlobe ([instructions](/documentation/index))
* Open napari and follow the steps in our [download tutorial](/tutorials/manage-atlases-in-GUI.md) for the extended and improved CCF atlas.
* Visualise the different parts of the atlas as described in our [visualisation tutorial](/tutorials/visualise-atlas-napari)

## Why are we adding new atlases?

A fundamental aim of the BrainGlobe project is to make various brain atlases easily accessible by users across the globe. If you would like to get involved with a similar project, please [get in touch](/contact).
