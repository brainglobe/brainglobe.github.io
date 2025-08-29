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
### [Allen Adult Mouse Brain Atlas](https://doi.org/10.1016/j.cell.2020.04.007)
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
space to the original Allen atlas (CCFv3). We recommend instead using the second version of this atlas, [Gubra's LSFM 
mouse brain atlas v2](https://brainglobe.info/documentation/brainglobe-atlasapi/usage/atlas-details.html#gubras-lsfm-mouse-brain-atlas-v2).

This atlas is only available at 20μm resolution:
* `perens_lsfm_mouse_20um`

### [Gubra's MRI mouse brain atlas](https://doi.org/10.1007/s12021-023-09623-9)
This atlas is an addition to its LSFM version and provides a version of the Allen
Adult Mouse Brain Atlas, based on T2-weighted MRI. This atlas may be a 
good choice for registering other similar images. However, please note that this atlas is in a different coordinate 
space to the original Allen atlas (CCFv3). In addition this atlas is in flat skull position and so it can be used to 
plan stereotaxic surgeries.

This atlas is only available at 25μm resolution:
* `perens_stereotaxic_mri_mouse_25um`

### [Gubra's LSFM mouse brain atlas v2](https://doi.org/10.1007/s12021-023-09623-9)
This atlas is an addition to its MRI version and provides a version of the Allen Adult Mouse Brain Atlas, based on LSFM. 
This atlas may be a good choice for registering other similar images. This atlas is the second version of 
[perens et al. (2020)](https://doi.org/10.1007/s12021-020-09490-8) and was published in 
[perens et al. (2023)](https://doi.org/10.1007/s12021-023-09623-9).  Please note that this atlas is in a different coordinate
space to the original Allen atlas (CCFv3) and to Perens 2020. 


This atlas is only available at 25μm resolution:
* `perens_multimodal_lsfm_25um`

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

### [Kim Lab Developmental CCF v1.0](https://doi.org/10.6084/m9.figshare.26377171.v1) 
A multi-modal atlas of the developing mouse brain. Reference images from LSFM and MRI (adc, dwi, fa, T2) are available at all developmental stages of the atlas (E11.5, E13.5, E15.5, E18.5, P4, P14, P56). Developmental stages E15.5, P04 and P14 additionally also have versions with a MTR MRI reference image.


Available versions:
* at E11.5
  *  `kim_dev_mouse_e11-5_lsfm_20um` - LSFM template at 20 μm resolution
  *  `kim_dev_mouse_e11-5_mri-adc_31.5um` - MRI adc template at 31.5 μm resolution
  *  `kim_dev_mouse_e11-5_mri-dwi_31.5um` - MRI dwi template at 31.5 μm resolution 
  *  `kim_dev_mouse_e11-5_mri-fa_31.5um` - MRI fa template at 31.5 μm resolution
  *  `kim_dev_mouse_e11-5_mri-T2_31.5um` - MRI T2 template at 31.5 μm resolution
* at E13.5
  *  `kim_dev_mouse_e13-5_lsfm_20um` - LSFM template at 20 μm resolution
  *  `kim_dev_mouse_e13-5_mri-adc_34um` - MRI adc template at 34 μm resolution
  *  `kim_dev_mouse_e13-5_mri-dwi_34um` - MRI dwi template at 34 μm resolution 
  *  `kim_dev_mouse_e13-5_mri-fa_34um` - MRI fa template at 34 μm resolution
  *  `kim_dev_mouse_e13-5_mri-t2_34um` - MRI T2 template at 34 μm resolution 
* at E15.5
  *  `kim_dev_mouse_e15-5_lsfm_20um` - LSFM template at 20 μm resolution
  *  `kim_dev_mouse_e15-5_mri-adc_37.5um` - MRI adc template at 37.5 μm resolution
  *  `kim_dev_mouse_e15-5_mri-dwi_37.5um` - MRI dwi template at 37.5 μm resolution 
  *  `kim_dev_mouse_e15-5_mri-fa_37.5um` - MRI fa template at 37.5 μm resolution
  *  `kim_dev_mouse_e15-5_mri-t2_37.5um` - MRI T2 template at 37.5 μm resolution 
  *  `kim_dev_mouse_e15-5_mri-mtr_37.5um` - MRI MTR template at 37.5 μm resolution 
* at E18.5
  *  `kim_dev_mouse_e18-5_lsfm_20um` - LSFM template at 20 μm resolution
  *  `kim_dev_mouse_e18-5_mri-adc_40um` - MRI adc template at 40 μm resolution
  *  `kim_dev_mouse_e18-5_mri-dwi_40um` - MRI dwi template at 40 μm resolution 
  *  `kim_dev_mouse_e18-5_mri-fa_40um` - MRI fa template at 40 μm resolution
  *  `kim_dev_mouse_e18-5_mri-t2_40um` - MRI T2 template at 40 μm resolution 
* at P04
  *  `kim_dev_mouse_p04_lsfm_20um` - LSFM template at 20 μm resolution
  *  `kim_dev_mouse_p04_mri-adc_50um` - MRI adc template at 50 μm resolution
  *  `kim_dev_mouse_p04_mri-dwi_50um` - MRI dwi template at 50 μm resolution 
  *  `kim_dev_mouse_p04_mri-fa_50um` - MRI fa template at 50 μm resolution
  *  `kim_dev_mouse_p04_mri-t2_50um` - MRI T2 template at 50 μm resolution 
  *  `kim_dev_mouse_p04_mri-mtr_50um` - MRI MTR template at 50 μm resolution 
* at P14
  *  `kim_dev_mouse_p14_lsfm_20um` - LSFM template at 20 μm resolution
  *  `kim_dev_mouse_p14_mri-adc_50um` - MRI adc template at 50 μm resolution
  *  `kim_dev_mouse_p14_mri-dwi_50um` - MRI dwi template at 50 μm resolution 
  *  `kim_dev_mouse_p14_mri-fa_50um` - MRI fa template at 50 μm resolution
  *  `kim_dev_mouse_p14_mri-t2_50um` - MRI T2 template at 50 μm resolution 
  *  `kim_dev_mouse_p14_mri-mtr_50um` - MRI MTR template at 50 μm resolution 
* at P56
  *  `kim_dev_mouse_p56_lsfm_20um` - LSFM template at 20 μm resolution
  *  `kim_dev_mouse_p56_mri-adc_50um` - MRI adc template at 50 μm resolution
  *  `kim_dev_mouse_p56_mri-dwi_50um` - MRI dwi template at 50 μm resolution 
  *  `kim_dev_mouse_p56_mri-fa_50um` - MRI fa template at 50 μm resolution
  *  `kim_dev_mouse_p56_mri-t2_50um` - MRI T2 template at 50 μm resolution 
  *  `kim_dev_mouse_p56_mri-mtr_50um` - MRI MTR template at 50 μm resolution 


### [Kim Lab Developmental CCF v001 (P56)](https://data.mendeley.com/datasets/2svx788ddf/1) 
This atlas is part of a developmental atlas following Luis Puelles' Developmental Vertebrate Ontology. BrainGlobe hosts the original P56 version of this atlas at 10μm resolution with eight different reference 
images - STP, LSFM (iDISCO) and MRI (a0, adc, dwo, fa, MTR, T2). This atlas is now superseded by its 1.0.0 version but continues to be available for reproducibility and archive reasons.

Available versions:
* `kim_dev_mouse_stp_10um` - "normal" CCF serial 2p template at 10μm resolution
* `kim_dev_mouse_idisco_10um` - iDISCO LSFM template at 10μm resolution
* `kim_dev_mouse_mri_a0_10um` - MRI a0 template at 10μm resolution
* `kim_dev_mouse_mri_adc_10um` - MRI ADC (apparent diffusion coefficient) template at 10μm resolution
* `kim_dev_mouse_mri_dwi_10um` - MRI DWI (diffusion-weighted imaging) template at 10μm resolution
* `kim_dev_mouse_mri_fa_10um` - MRI FA (fractional anisotropy) template at 10μm resolution
* `kim_dev_mouse_mri_mtr_10um` - MRI MTR (magnetic transfer ratio) template at 10μm resolution
* `kim_dev_mouse_mri_t2_10um` - MRI T2 template at 10μm resolution

### [BlueBrain Barrel Cortex Atlas](https://doi.org/10.1162/imag_a_00209)
This atlas from [Bolaños-Puchet et al. (2024)](https://doi.org/10.1162/imag_a_00209) 
is a version of the Allen Adult Mouse Brain Atlas with the addition of annotations of 33 barrels and barrel columns. 
For more details, please see [the blogpost](/blog/barrel-atlas-added).

Available versions:
* `allen_mouse_bluebrain_barrels_10um` - 10μm resolution
* `allen_mouse_bluebrain_barrels_25um` - 25μm resolution

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
### [Australian Mouse Brain Atlas](https://imaging.org.au/AMBMC/)
This atlas has a very high resolution (15μm) MRI template. It covers the Hippocampus, Cerebellum, Cortex, 
Basal Ganglia, and Diencephalon. It is quite consistent with the parcellation scheme of the Paxinos and Franklin
mouse brain atlas. At present a drawback of this atlas is that the 
segmentations do not cover the entire brain and is limited to the regions previously mentioned. 
This atlas is only available at 15μm resolution:
* `australian_mouse_15um`
### [CCFv3 augmented mouse atlas](https://doi.org/10.1162/imag_a_00565)
This atlas is an extended version of the CCFv3, designed to cover the rostral and caudal tips of the mouse brain. 
This atlas is particularly useful for users who require the whole brain to be represented including the posterior 
third of the cerebellum, the brainstem, and the anterior olfactory bulb. It includes two Nissl reference templates, 
one which is a population average from hundreds of mice and one based on three animals. The Nissl template included
in the CCFv3 is slightly misaligned, here the Nissl template has been more precisely registered into the CCFv3 space.
The CCFv3 Augmented also includes new delineations of the granular layer of the cerebellum.

Available versions:
* `ccfv3augmented_mouse_10um` - 10μm resolution
* `ccfv3augmented_mouse_25um` - 25μm resolution
## Rat
### [Waxholm Space atlas of the Sprague Dawley rat brain](https://doi.org/10.1038/s41592-023-02034-3)
The Waxholm Space rat brain atlas features annotations of 222 structures, alongside a 39μm MRI template. It provides detailed delineations 
of the cerebral cortex, hippocampus, striatopallidal areas, midbrain, thalamus, auditory system and fiber tracts.
It is comprehensive, covering the entire rat brain. 
This atlas is only available at 39μm resolution:
* `whs_sd_rat_39um`

## Other rodent
### [Prairie vole brain atlas](https://doi.org/10.7554/eLife.87029.3.sa0)
This is a brain atlas of the Prairie vole (Microtus ochrogaster) from
[Gustison et al. (2024)](https://doi.org/10.7554/eLife.87029.3.sa0).
This atlas is only available at 25μm resolution:
* `prairie_vole_25um`

## Fish
### [Max Planck zebrafish brain atlas](http://fishatlas.neuro.mpg.de)
This atlas is only available at 1μm resolution:
* `mpin_zfish_1um`

### [AZBA: A 3D Adult zebrafish brain atlas](https://doi.org/10.1101/2021.05.04.442625)
This atlas is only available at 4μm resolution:
* `azba_zfish_4um`

### [Blind Mexican cavefish brain atlas](https://elifesciences.org/articles/80777)
This is a brain atlas of the blind Mexican cavefish (Astyanax mexicanus) from 
[Kozol et al. (2023)](https://elifesciences.org/articles/80777). For more details please
see [the blogpost](/blog/cavefish-atlas-added).
This atlas is only available at 2μm resolution:
* `sju_cavefish_2um`

## Amphibian
### [UNAM Axolotl Brain Atlas](https://doi.org/10.1038/s41598-021-89357-3)
This is a magnetic resonance imaging based atlas of the Axolotl (Ambystoma mexicanum) from 
[Lazcano et al. (2021)](https://doi.org/10.1038/s41598-021-89357-3). For more details please 
see [the blogpost](/blog/axolotl-atlas-added).

This atlas is only available at 40μm resolution:
* `unam_axolotl_40um`

## Human and non-human primate
### [Allen Human Brain Atlas](https://www.brain-map.org)
This atlas is included mostly for visualisation and comparison to the other atlases. 
Note that it is also only a single hemisphere. There are many better atlases
(and indeed software tools) for the analysis of human neuroimaging data.

This atlas is only available at 500μm resolution:
* `allen_human_500um`

### [MRI mouse lemur brain atlas](https://doi.org/10.1016/j.dib.2018.10.067) 
This is an MRI atlas of the grey mouse lemur (Microcebus murinus) from 
[Nadkarni et al. (2018)](https://doi.org/10.1016/j.dib.2018.10.067).

This atlas is only available at 91um resolution
* `nadkarni_mri_mouselemur_91um`

## Other mammal
### [Cat brain atlas](https://doi.org/10.1002/cne.24271)

This is an MRI atlas of a cat (Felis catus) from [Stolzberg et al. (2017)](https://doi.org/10.1002/cne.24271)

This atlas is only available at 500um resolution:
* `csl_cat_500um`

## Bird
### [Eurasian blackcap atlas](https://doi.org/10.1101/2025.03.04.641293)
This is a serial section two-photon atlas of the Eurasian blackcap (Sylvia atricapilla) 
built by the BrainGlobe team ([Sirmpilatze et al. (2025)](https://doi.org/10.1101/2025.03.04.641293)). 
For more details please see [the project page](/projects/blackcap/index).

This atlas is only available at 25μm resolution:
* `eurasian_blackcap_25um`

## Invertebrate
### [Kocher Bumblebee Brain Atlas](https://doi.org/10.1016/j.cub.2022.04.066)
This is a confocal microscopy [atlas of the adult bumblebee](https://doi.org/10.1016/j.cub.2022.04.066), made by the Kocher lab.

This atlas has anisotropic resolution (2.542μm in axial direction - along antero-posterior axis - and 1.2407μm in-plane) resolution
* `kocher_bumblebee_2.542um`

