---
blogpost: true
date: February 5, 2025
author: Harry Carey, Carlo Castoldi, Alessandro Felder
location: Oslo, Norway; Paris, France; London, England
category: brainglobe
language: English
---
# What mouse atlas should I use?

Eagle-eyed BrainGlobe enthusiasts will have spotted several new atlases appearing in the BrainGlobe Atlas API in recent weeks. In 2025, we've made 3 mouse brain atlases newly available through BrainGlobe: The Kim developmental mouse brain atlas (version 1), the Gubra multimodal mouse brain atlas and the Australian mouse brain atlas. Mice are widely used as model organisms in neuroscience, so it's no surprise there are many mouse brain atlases. In this blogpost, we describe the newly added atlases in more detail, and suggest potential use cases. This blog covers the new murine atlases only - we have also added the [first non-human primate brain atlas to BrainGlobe](/blog/mouse-lemur-added) (and brain atlases for a cat and a cuttlefish are underway)!

## Kim developmental mouse brain atlas v1 (Kim DevCCF)
The [Kim developmental mouse brain atlas](https://doi.org/10.1038/s41467-024-53254-w) is a multimodal atlas available at 4 embryonic and 3 postnatal timepoints. At each timepoint, the atlas combines a 20um resolution LSFM template with a number of different MRI templates with varying resolution. We illustrate these here by showing the embryonic subset of the LSFM templates (Figure 1.) and all templates for the single E18.5 stage (Figure 2.), but you can find all the available templates in [their detailed documentation](/documentation/brainglobe-atlasapi/usage/atlas-details).


![Kim DevCCF embryonic LSFM templates](./images/kim_dev_embryonic_lsfm.png)

**Figure 1. LSFM templates for embryonic developmental stages (f.l.t.r. E11.5, E13.5, E15.5, E18.5) available in the Kim DevCCF.**

![Coronal sections for all templates for Kim DevCCF template at E18.5](./images/kim_dev_embryonic_18_all_modalities_2d.png)

**Figure 2. Annotations (top left), LSFM template (bottom left) and various MRI templates (T2, FA, ADC, DWI - clockwise from top centre) for KimDevCCF embryonic stage E18.5.**

This is an update to an earlier version of the same lab (v001 - only at P56, and notably in a different coordinate space!). It is an improvement compared to the Allen Developing Mouse Brain atlas (ADMBA), the other developmental mouse brain atlas available through BrainGlobe, because it represents an average of several individuals and is based on fully three-dimensional imaging methods rather than a series of histological sections.

## Gubra's MRI + LSFM atlases
TODO

## Australian mouse brain atlas
High resolution and paxinos annotations.

## How do I use the new atlas?
You can use these atlases for visualisation and analysis, like other BrainGlobe atlases. To visualise the atlas, you could follow the steps below:
* Install BrainGlobe ([instructions](/documentation/index))
* Open napari and follow the steps in our [download tutorial](/tutorials/manage-atlases-in-GUI.md) for your atlas of choice
* Visualise the different parts of the atlas as described in our [visualisation tutorial](/tutorials/visualise-atlas-napari)
To use the atlas with other software such as [brainreg](/documentation/brainreg/index), please follow the instructions for those tools, and simply choose this atlas from the user interface. Note that some MRI atlases might not be good registration targets, because they include tissue outside the brain. And remember to cite the original publication as well as any BrainGlobe tools you used!

## Why are we adding new atlases?
A fundamental aim of the BrainGlobe project is to make various brain atlases easily accessible by users across the globe. If you would like to get involved with a similar project, please [get in touch](/contact).