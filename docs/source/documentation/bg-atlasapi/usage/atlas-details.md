# Atlas details

The BrainGlobe atlas API includes a number of atlases in a standardised form that vary based on:
- Species
- Organ
- Developmental stage
- Reference image modality
- Brain region annotations
- Resolution

Sometimes choosing the most appropriate atlas for a specific question is easy (e.g., there is currently only one 
rat atlas in the API). However, in some cases (e.g. adult mouse brains) there are many options. In some cases 
the annotations included with an atlas will dictate the choice — if the brain region you are studying is not included 
in an atlas, it is not much use! In other cases the reference image will be important. If you have imaged your sample 
with lightsheet microscopy (LSFM) it may be useful to use an atlas that also uses this modality. An atlas using a 
different modality (such as serial section two-photon, STP) may produce inferior registration results.

In most software you can choose the atlas from a list, but if using a command line tool, or the API directly, the 
unique key (e.g. `example_mouse_100um` must be used).

# Available atlases

## Mouse
### [Allen Adult Mouse Brain Atlas](https://portal.brain-map.org)
For many researchers working with mice, this is the "default" atlas for a variety of tasks. It is also the basis for 
the most commonly used common coordinate space (CCFv3). It is usually the best mouse atlas to start with, but it has 
some disadvantages. It has a reference image based on STP, which may not produce the best 
results for other imaging modalities, and you may want to try atlases based on other modalities (see below). It also has 
limited annotations in some regions (alternatives such as the Enhanced and Unified Mouse Brain Atlas may be better 
if the Allen Adult Mouse Brain Atlas is not annotated sufficiently).

Available versions:
* `allen_mouse_10um` - 10μm resolution
* `allen_mouse_25um` - 25μm resolution
* `allen_mouse_50um` - 50μm resolution
* `allen_mouse_100um` - 100μm resolution

### [Enhanced and Unified Mouse Brain Atlas](https://kimlab.io/brain-map/atlas/) 
This atlas from [Chon et al. (2019)](https://doi.org/10.1038/s41467-019-13057-w) is very similar to the Allen Adult 
Mouse Brain Atlas (it has the same reference image), but it includes additional annotations (e.g. from the 
Franklin-Paxinos atlas). This atlas may be a good choice for those brain regions not annotated sufficiently in the
Allen Adult Mouse Brain Atlas.

Available versions:
* `kim_mouse_10um` - 10μm resolution
* `kim_mouse_25um` - 25μm resolution
* `kim_mouse_50um` - 50μm resolution
* `kim_mouse_100um` - 100μm resolution



### [Gubra's LSFM mouse brain atlas](https://doi.org/10.1007/s12021-020-09490-8)
This atlas from [Perens et al. (2020)](https://doi.org/10.1007/s12021-020-09490-8) provides a version of the Allen
Adult Mouse Brain Atlas, based on solvent-cleared brains imaged with LSFM. This atlas may be a 
good choice for registering other similar images. However, please note that this atlas is in a different coordinate 
space to the original Allen atlas (CCFv3).

This atlas is only available at 20μm resolution:
* `perens_lsfm_mouse_20um`

### [Princeton Mouse Brain Atlas](https://brainmaps.princeton.edu/2020/09/princeton-mouse-brain-atlas-links)
This atlas from [Pisano et al. (2021)](https://doi.org/10.1016/j.celrep.2021.109721) is a version of the Allen
Adult Mouse Brain Atlas with two main differences. Unlike the Allen Adult Mouse Brain Atlas it includes a full 
cerebellum, and the reference image is based on LSFM rather than STP.

This atlas is only available at 20μm resolution:
* `princeton_mouse_20um`

### [3D Edge-Aware Refined Atlases Derived from the Allen Developing Mouse Brain Atlases](https://doi.org/10.7554/eLife.61408)
These atlases from [Young et al. (2021)](https://doi.org/10.7554/eLife.61408) are 3D reconstructions of the eight 
developmental stages from the 
[Allen Developing Mouse Brain Atlas](https://developingmouse.brain-map.org/). 
This allows them to be used in automated 3D registration pipelines. 

These atlases vary slightly, as the E11.5, E13.5 and E15.5 atlases contain the complete embryo. The other atlases
(E18.5, P4, P14, P28 and P56) only contain the brain. 

Available versions:
* `admba_3d_e11_5_mouse_16um` - E11.5 at 16μm resolution
* `admba_3d_e13_5_mouse_16um` - E13.5 at 16μm resolution
* `admba_3d_e15_5_mouse_16um` - E15.5 at 16μm resolution
* `admba_3d_e18_5_mouse_16um` - E18.5 at 16μm resolution
* `admba_3d_p4_mouse_16.752um` - P4 at 16.752μm resolution
* `admba_3d_p14_mouse_16.752um` - P14 at 16.752μm resolution
* `admba_3d_p28_mouse_16.752um` - P28 at 16.752μm resolution
* `admba_3d_p56_mouse_25um` - P56 at 25μm resolution


### [Kim Lab Developmental CCF (P56)](https://data.mendeley.com/datasets/2svx788ddf/1) 
This atlas is part of a new developmental atlas following Luis Puelles' Developmental Vertebrate Ontology. BrainGlobe 
currently hosts the P56 version of this atlas at 10μm resolution with eight versions, each with a different reference 
image - STP, LSFM (iDISCO) and MRI (a0, adc, dwo, fa, MTR, T2).

Available versions:
* `kim_dev_mouse_stp_10um` - "normal" CCF serial 2p template at 10μm resolution
* `kim_dev_mouse_idisco_10um` - iDISCO LSFM template at 10μm resolution
* `kim_dev_mouse_mri_a0_10um` - MRI a0 template at 10μm resolution
* `kim_dev_mouse_mri_adc_10um` - MRI ADC (apparent diffusion coefficient) template at 10μm resolution
* `kim_dev_mouse_mri_dwi_10um` - MRI DWI (diffusion-weighted imaging) template at 10μm resolution
* `kim_dev_mouse_mri_fa_10um` - MRI FA (fractional anisotropy) template at 10μm resolution
* `kim_dev_mouse_mri_mtr_10um` - MRI MTR (magnetic transfer ratio) template at 10μm resolution
* `kim_dev_mouse_mri_t2_10um` - MRI T2 template at 10μm resolution

### [3D version of the Allen mouse spinal cord atlas](https://doi.org/10.1101/2021.05.06.443008)
This atlas from [Fiederling et al. (2021)](https://doi.org/10.1101/2021.05.06.443008) is a 3D reconstruction of the 
[Allen Spinal Cord Atlas](https://mousespinal.brain-map.org/).

This atlas is only available at a single (20 x 10 x 10μm) resolution:
* `allen_cord_20um`

### [Smoothed version of the Kim et al. mouse reference atlas](https://doi.org/10.1016/j.celrep.2014.12.014)
This atlas is part of the API to support some existing projects. We do not recommend it for any new projects
(use the Allen Adult Mouse Brain Atlas instead).

Available versions:
* `osten_mouse_10um` - 10μm resolution
* `osten_mouse_25um` - 25μm resolution
* `osten_mouse_50um` - 50μm resolution
* `osten_mouse_100um` - 100μm resolution

## Rat
### [Waxholm Space atlas of the Sprague Dawley rat brain](https://doi.org/10.1016/j.neuroimage.2014.04.001) at 39 micron resolution
This atlas is only available at 39μm resolution:
* `whs_sd_rat_39um` - 39μm resolution

## Zebrafish
### [Max Planck Zebrafish Brain Atlas](http://fishatlas.neuro.mpg.de)
This atlas is only available at 1μm resolution:
* `mpin_zfish_1um`

### [AZBA: A 3D Adult Zebrafish Brain Atlas](https://doi.org/10.1101/2021.05.04.442625)
This atlas is only available at 4μm resolution:
* `azba_zfish_4um`

## Human
### [Allen Human Brain Atlas](https://www.brain-map.org)
This atlas is included mostly for visualisation and comparison to the other atlases. 
Note that it is also only a single hemisphere. There are many better atlases
(and indeed software tools) for the analysis of human neuroimaging data.

This atlas is only available at 500μm resolution:
* `allen_human_500um`







