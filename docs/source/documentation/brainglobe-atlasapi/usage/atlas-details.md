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

### [Enhanced and Unified Mouse Brain Atlas v2](https://figshare.com/articles/dataset/Unified_mouse_brain_atlas_v2/25750983) 
The updated version of the Unified Mouse Brain Atlas builds upon 
the work of [Chon et al. (2019)](https://doi.org/10.1038/s41467-019-13057-w), 
which introduced a more finely segmented adult mouse brain atlas with unified anatomical labeling 
based on the Allen Common Coordinate Framework (CCF). The original atlas integrated the Franklin-Paxinos (FP) 
labels into the CCF space, providing consistent and detailed segmentation across brain regions.

Version 2 (2024) contains several key improvements:
* Corrected anatomical labels and updated ontology file to resolve inconsistencies in the original release.
* 20 µm isotropic label volume generated via shape interpolation for high-resolution anatomical accuracy.
* Maintains full compatibility with the original atlas (coordinate space and ontology).

This atlas is only available at 20μm resolution:
* `kim_mouse_isotropic_20um`

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
### [DeMBA Developmental Mouse Brain Atlas](https://doi.org/10.1038/s41467-025-63177-9)
This atlas contains 53 days of development including every day from postnatal day 4 to postnatal day 56. Each time point has two atlases, a 20um version with the STPT, and Allen STPT template and a 25um version with the STPT, the Allen STPT, an MRI, and an LSFM template. The Allen STPT template is a transformed version of the default template provided with the Allen CCFv3, it is useful for comparison with the adult CCFv3.  

Available versions:
* at P4
  * `demba_allen_seg_dev_mouse_p4_20um` 
  * `demba_allen_seg_dev_mouse_p4_25um` 
* at P5
  * `demba_allen_seg_dev_mouse_p5_20um` 
  * `demba_allen_seg_dev_mouse_p5_25um` 
* at P6
  * `demba_allen_seg_dev_mouse_p6_20um` 
  * `demba_allen_seg_dev_mouse_p6_25um` 
* at P7
  * `demba_allen_seg_dev_mouse_p7_20um` 
  * `demba_allen_seg_dev_mouse_p7_25um` 
* at P8
  * `demba_allen_seg_dev_mouse_p8_20um` 
  * `demba_allen_seg_dev_mouse_p8_25um` 
* at P9
  * `demba_allen_seg_dev_mouse_p9_20um` 
  * `demba_allen_seg_dev_mouse_p9_25um` 
* at P10
  * `demba_allen_seg_dev_mouse_p10_20um`
  * `demba_allen_seg_dev_mouse_p10_25um`
* at P11
  * `demba_allen_seg_dev_mouse_p11_20um`
  * `demba_allen_seg_dev_mouse_p11_25um`
* at P12
  * `demba_allen_seg_dev_mouse_p12_20um`
  * `demba_allen_seg_dev_mouse_p12_25um`
* at P13
  * `demba_allen_seg_dev_mouse_p13_20um`
  * `demba_allen_seg_dev_mouse_p13_25um`
* at P14
  * `demba_allen_seg_dev_mouse_p14_20um`
  * `demba_allen_seg_dev_mouse_p14_25um`
* at P15
  * `demba_allen_seg_dev_mouse_p15_20um`
  * `demba_allen_seg_dev_mouse_p15_25um`
* at P16
  * `demba_allen_seg_dev_mouse_p16_20um`
  * `demba_allen_seg_dev_mouse_p16_25um`
* at P17
  * `demba_allen_seg_dev_mouse_p17_20um`
  * `demba_allen_seg_dev_mouse_p17_25um`
* at P18
  * `demba_allen_seg_dev_mouse_p18_20um`
  * `demba_allen_seg_dev_mouse_p18_25um`
* at P19
  * `demba_allen_seg_dev_mouse_p19_20um`
  * `demba_allen_seg_dev_mouse_p19_25um`
* at P20
  * `demba_allen_seg_dev_mouse_p20_20um`
  * `demba_allen_seg_dev_mouse_p20_25um`
* at P21
  * `demba_allen_seg_dev_mouse_p21_20um`
  * `demba_allen_seg_dev_mouse_p21_25um`
* at P22
  * `demba_allen_seg_dev_mouse_p22_20um`
  * `demba_allen_seg_dev_mouse_p22_25um`
* at P23
  * `demba_allen_seg_dev_mouse_p23_20um`
  * `demba_allen_seg_dev_mouse_p23_25um`
* at P24
  * `demba_allen_seg_dev_mouse_p24_20um`
  * `demba_allen_seg_dev_mouse_p24_25um`
* at P25
  * `demba_allen_seg_dev_mouse_p25_20um`
  * `demba_allen_seg_dev_mouse_p25_25um`
* at P26
  * `demba_allen_seg_dev_mouse_p26_20um`
  * `demba_allen_seg_dev_mouse_p26_25um`
* at P27
  * `demba_allen_seg_dev_mouse_p27_20um`
  * `demba_allen_seg_dev_mouse_p27_25um`
* at P28
  * `demba_allen_seg_dev_mouse_p28_20um`
  * `demba_allen_seg_dev_mouse_p28_25um`
* at P29
  * `demba_allen_seg_dev_mouse_p29_20um`
  * `demba_allen_seg_dev_mouse_p29_25um`
* at P30
  * `demba_allen_seg_dev_mouse_p30_20um`
  * `demba_allen_seg_dev_mouse_p30_25um`
* at P31
  * `demba_allen_seg_dev_mouse_p31_20um`
  * `demba_allen_seg_dev_mouse_p31_25um`
* at P32
  * `demba_allen_seg_dev_mouse_p32_20um`
  * `demba_allen_seg_dev_mouse_p32_25um`
* at P33
  * `demba_allen_seg_dev_mouse_p33_20um`
  * `demba_allen_seg_dev_mouse_p33_25um`
* at P34
  * `demba_allen_seg_dev_mouse_p34_20um`
  * `demba_allen_seg_dev_mouse_p34_25um`
* at P35
  * `demba_allen_seg_dev_mouse_p35_20um`
  * `demba_allen_seg_dev_mouse_p35_25um`
* at P36
  * `demba_allen_seg_dev_mouse_p36_20um`
  * `demba_allen_seg_dev_mouse_p36_25um`
* at P37
  * `demba_allen_seg_dev_mouse_p37_20um`
  * `demba_allen_seg_dev_mouse_p37_25um`
* at P38
  * `demba_allen_seg_dev_mouse_p38_20um`
  * `demba_allen_seg_dev_mouse_p38_25um`
* at P39
  * `demba_allen_seg_dev_mouse_p39_20um`
  * `demba_allen_seg_dev_mouse_p39_25um`
* at P40
  * `demba_allen_seg_dev_mouse_p40_20um`
  * `demba_allen_seg_dev_mouse_p40_25um`
* at P41
  * `demba_allen_seg_dev_mouse_p41_20um`
  * `demba_allen_seg_dev_mouse_p41_25um`
* at P42
  * `demba_allen_seg_dev_mouse_p42_20um`
  * `demba_allen_seg_dev_mouse_p42_25um`
* at P43
  * `demba_allen_seg_dev_mouse_p43_20um`
  * `demba_allen_seg_dev_mouse_p43_25um`
* at P44
  * `demba_allen_seg_dev_mouse_p44_20um`
  * `demba_allen_seg_dev_mouse_p44_25um`
* at P45
  * `demba_allen_seg_dev_mouse_p45_20um`
  * `demba_allen_seg_dev_mouse_p45_25um`
* at P46
  * `demba_allen_seg_dev_mouse_p46_20um`
  * `demba_allen_seg_dev_mouse_p46_25um`
* at P47
  * `demba_allen_seg_dev_mouse_p47_20um`
  * `demba_allen_seg_dev_mouse_p47_25um`
* at P48
  * `demba_allen_seg_dev_mouse_p48_20um`
  * `demba_allen_seg_dev_mouse_p48_25um`
* at P49
  * `demba_allen_seg_dev_mouse_p49_20um`
  * `demba_allen_seg_dev_mouse_p49_25um`
* at P50
  * `demba_allen_seg_dev_mouse_p50_20um`
  * `demba_allen_seg_dev_mouse_p50_25um`
* at P51
  * `demba_allen_seg_dev_mouse_p51_20um`
  * `demba_allen_seg_dev_mouse_p51_25um`
* at P52
  * `demba_allen_seg_dev_mouse_p52_20um`
  * `demba_allen_seg_dev_mouse_p52_25um`
* at P53
  * `demba_allen_seg_dev_mouse_p53_20um`
  * `demba_allen_seg_dev_mouse_p53_25um`
* at P54
  * `demba_allen_seg_dev_mouse_p54_20um`
  * `demba_allen_seg_dev_mouse_p54_25um`
* at P55
  * `demba_allen_seg_dev_mouse_p55_20um`
  * `demba_allen_seg_dev_mouse_p55_25um`
* at P56
  * `demba_allen_seg_dev_mouse_p56_20um`
  * `demba_allen_seg_dev_mouse_p56_25um`
### [Dorr MRI Mouse Atlas](https://doi.org/10.1016/j.neuroimage.2008.03.037)
This atlas is a high-resolution, three-dimensional MRI-based atlas of the adult C57Bl/6J mouse brain, providing 
comprehensive anatomical coverage of the cerebrum, cerebellum, and brainstem. The atlas was constructed from 
within-skull, T2-weighted MR images acquired at 32 μm isotropic resolution from forty 12-week-old mice scanned on a 7 T
scanner. Following normalisation, registration, and averaging of individual scans, 62 distinct brain structures were 
manually delineated.

Available versions:
* `dorr_mouse_mri_32um`

### [CArea Mouse Atlas](https://doi.org/10.64898/2026.01.20.700446)
This atlas has regions which are automatically clustered based on three dimensional maps of gene expression. Voxels 
with similar patterns of gene expression are assigned the same region ID. The template is a population average Nissl 
volume, based on the CCFv3BBP atlas (also in 
[brainglobe](https://brainglobe.info/documentation/brainglobe-atlasapi/usage/atlas-details.html#ccfv3-augmented-mouse-atlas)) 
with some improvements. This atlas was constructed from reregistered ISH data from the Allen Institute for Brain Science. 

Available versions:
* `carea_mouse_25um`
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

### [Columbia cuttlefish atlas](https://doi.org/10.1016/j.cub.2023.06.007)
This is an MRI atlas of the dwarf cuttlefish (Sepia bandensis) from [Montague et al. (2023)](https://doi.org/10.1016/j.cub.2023.06.007)

This atlas is only available at 50μm resolution:
* `columbia_cuttlefish_50um`

### [Kocher Bumblebee Brain Atlas](https://doi.org/10.1016/j.cub.2022.04.066)
This is a confocal microscopy [atlas of the adult bumblebee](https://doi.org/10.1016/j.cub.2022.04.066), made by the Kocher lab.

This atlas has anisotropic resolution (2.542μm in axial direction - along antero-posterior axis - and 1.2407μm in-plane) resolution
* `kocher_bumblebee_2.542um`

### Drosophila wing disc instar3 atlas.
This is a confocal microscopy atlas of the fruit fly larva's imaginal wing disc, at the 3rd instar developmental stage. It was built by Kaixiang Shuai as part of his MSc thesis, supervised by [Giulia Paci (Mao Lab at UCL)](https://www.tissuemechanicslab.com/gulia) and Alessandro Felder (BrainGlobe team).
This atlas has 2um isotropic resolution. 
* `drosophila_wingdisc_instar3_2um`



