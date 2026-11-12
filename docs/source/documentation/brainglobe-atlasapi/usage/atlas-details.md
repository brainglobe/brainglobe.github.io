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

The tables of versions below are generated from the BrainGlobe atlas repository each time this website is built, so 
they always list the latest version of every atlas that the BrainGlobe Atlas API can download. Each atlas's manifest 
lists the location of its template and annotation images (OME-Zarr) and its terminology (CSV).

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
```{atlas-versions} allen_mouse
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/allen_mouse.json)


### [Enhanced and Unified Mouse Brain Atlas](https://kimlab.io/brain-map/atlas/) 
This atlas from [Chon et al. (2019)](https://doi.org/10.1038/s41467-019-13057-w) is very similar to the Allen Adult 
Mouse Brain Atlas (it has the same reference image), but it includes additional annotations (e.g. from the 
Franklin-Paxinos atlas). This atlas may be a good choice for those brain regions not annotated sufficiently in the
Allen Adult Mouse Brain Atlas.

Available versions:
```{atlas-versions} kim_mouse
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/kim_mouse.json)


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
```{atlas-versions} kim_mouse_isotropic
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/kim_mouse_isotropic.json)


### [Gubra's LSFM mouse brain atlas](https://doi.org/10.1007/s12021-020-09490-8)
This atlas from [Perens et al. (2020)](https://doi.org/10.1007/s12021-020-09490-8) provides a version of the Allen
Adult Mouse Brain Atlas, based on solvent-cleared brains imaged with LSFM. This atlas may be a 
good choice for registering other similar images. However, please note that this atlas is in a different coordinate 
space to the original Allen atlas (CCFv3). We recommend instead using the second version of this atlas, [Gubra's LSFM 
mouse brain atlas v2](https://brainglobe.info/documentation/brainglobe-atlasapi/usage/atlas-details.html#gubras-lsfm-mouse-brain-atlas-v2).

This atlas is only available at 20μm resolution:
```{atlas-versions} perens_lsfm_mouse
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/perens_lsfm_mouse.json)


### [Gubra's MRI mouse brain atlas](https://doi.org/10.1007/s12021-023-09623-9)
This atlas is an addition to its LSFM version and provides a version of the Allen
Adult Mouse Brain Atlas, based on T2-weighted MRI. This atlas may be a 
good choice for registering other similar images. However, please note that this atlas is in a different coordinate 
space to the original Allen atlas (CCFv3). In addition this atlas is in flat skull position and so it can be used to 
plan stereotaxic surgeries.

This atlas is only available at 25μm resolution:
```{atlas-versions} perens_stereotaxic_mri_mouse
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/perens_stereotaxic_mri_mouse.json)


### [Gubra's LSFM mouse brain atlas v2](https://doi.org/10.1007/s12021-023-09623-9)
This atlas is an addition to its MRI version and provides a version of the Allen Adult Mouse Brain Atlas, based on LSFM. 
This atlas may be a good choice for registering other similar images. This atlas is the second version of 
[perens et al. (2020)](https://doi.org/10.1007/s12021-020-09490-8) and was published in 
[perens et al. (2023)](https://doi.org/10.1007/s12021-023-09623-9).  Please note that this atlas is in a different coordinate
space to the original Allen atlas (CCFv3) and to Perens 2020. 


This atlas is only available at 25μm resolution:
```{atlas-versions} perens_multimodal_lsfm
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/perens_multimodal_lsfm.json)


### [Princeton Mouse Brain Atlas](https://brainmaps.princeton.edu/2020/09/princeton-mouse-brain-atlas-links)
This atlas from [Pisano et al. (2021)](https://doi.org/10.1016/j.celrep.2021.109721) is a version of the Allen
Adult Mouse Brain Atlas with two main differences. Unlike the Allen Adult Mouse Brain Atlas it includes a full 
cerebellum, and the reference image is based on LSFM rather than STP.

This atlas is only available at 20μm resolution:
```{atlas-versions} princeton_mouse
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/princeton_mouse.json)


### [3D Edge-Aware Refined Atlases Derived from the Allen Developing Mouse Brain Atlases](https://doi.org/10.7554/eLife.61408)
These atlases from [Young et al. (2021)](https://doi.org/10.7554/eLife.61408) are 3D reconstructions of the eight 
developmental stages from the 
[Allen Developing Mouse Brain Atlas](https://developingmouse.brain-map.org/). 
This allows them to be used in automated 3D registration pipelines. 

These atlases vary slightly, as the E11.5, E13.5 and E15.5 atlases contain the complete embryo. The other atlases
(E18.5, P4, P14, P28 and P56) only contain the brain. 

Available versions:
```{atlas-versions} admba_3d_*
```

### [Kim Lab Developmental CCF v1.0](https://doi.org/10.6084/m9.figshare.26377171.v1) 
A multi-modal atlas of the developing mouse brain. Reference images from LSFM and MRI (adc, dwi, fa, T2) are available at all developmental stages of the atlas (E11.5, E13.5, E15.5, E18.5, P4, P14, P56). Developmental stages E15.5, P04 and P14 additionally also have versions with a MTR MRI reference image.


Available versions:
```{atlas-versions} kim_dev_mouse_e* kim_dev_mouse_p*
```


### [Kim Lab Developmental CCF v001 (P56)](https://data.mendeley.com/datasets/2svx788ddf/1) 
This atlas is part of a developmental atlas following Luis Puelles' Developmental Vertebrate Ontology. BrainGlobe hosts the original P56 version of this atlas at 10μm resolution with eight different reference 
images - STP, LSFM (iDISCO) and MRI (a0, adc, dwo, fa, MTR, T2). This atlas is now superseded by its 1.0.0 version but continues to be available for reproducibility and archive reasons.

Available versions:
```{atlas-versions} kim_dev_mouse_stp kim_dev_mouse_idisco kim_dev_mouse_mri_*
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/kim_dev_mouse.json)


### [BlueBrain Barrel Cortex Atlas](https://doi.org/10.1162/imag_a_00209)
This atlas from [Bolaños-Puchet et al. (2024)](https://doi.org/10.1162/imag_a_00209) 
is a version of the Allen Adult Mouse Brain Atlas with the addition of annotations of 33 barrels and barrel columns. 
For more details, please see [the blogpost](/blog/barrel-atlas-added).

Available versions:
```{atlas-versions} allen_mouse_bluebrain_barrels
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/allen_mouse_bluebrain_barrels.json)


### [3D version of the Allen mouse spinal cord atlas](https://doi.org/10.1101/2021.05.06.443008)
This atlas from [Fiederling et al. (2021)](https://doi.org/10.1101/2021.05.06.443008) is a 3D reconstruction of the 
[Allen Spinal Cord Atlas](https://mousespinal.brain-map.org/).

This atlas is only available at a single (20 x 10 x 10μm) resolution:
```{atlas-versions} allen_cord
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/allen_cord.json)


### [Smoothed version of the Kim et al. mouse reference atlas](https://doi.org/10.1016/j.celrep.2014.12.014)
This atlas is part of the API to support some existing projects. We do not recommend it for any new projects
(use the Allen Adult Mouse Brain Atlas instead).

Available versions:
```{atlas-versions} osten_mouse
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/osten_mouse.json)

### [Australian Mouse Brain Atlas](https://imaging.org.au/AMBMC/)
This atlas has a very high resolution (15μm) MRI template. It covers the Hippocampus, Cerebellum, Cortex, 
Basal Ganglia, and Diencephalon. It is quite consistent with the parcellation scheme of the Paxinos and Franklin
mouse brain atlas. At present a drawback of this atlas is that the 
segmentations do not cover the entire brain and is limited to the regions previously mentioned. 
This atlas is only available at 15μm resolution:
```{atlas-versions} australian_mouse
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/australian_mouse.json)

### [CCFv3 augmented mouse atlas](https://doi.org/10.1162/imag_a_00565)
This atlas is an extended version of the CCFv3, designed to cover the rostral and caudal tips of the mouse brain. 
This atlas is particularly useful for users who require the whole brain to be represented including the posterior 
third of the cerebellum, the brainstem, and the anterior olfactory bulb. It includes two Nissl reference templates, 
one which is a population average from hundreds of mice and one based on three animals. The Nissl template included
in the CCFv3 is slightly misaligned, here the Nissl template has been more precisely registered into the CCFv3 space.
The CCFv3 Augmented also includes new delineations of the granular layer of the cerebellum.

Available versions:
```{atlas-versions} ccfv3augmented_mouse
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/ccfv3augmented_mouse.json)

### [DeMBA Developmental Mouse Brain Atlas](https://doi.org/10.1038/s41467-025-63177-9)
This atlas contains 53 days of development including every day from postnatal day 4 to postnatal day 56. Each time point has two atlases, a 20um version with the STPT, and Allen STPT template and a 25um version with the STPT, the Allen STPT, an MRI, and an LSFM template. The Allen STPT template is a transformed version of the default template provided with the Allen CCFv3, it is useful for comparison with the adult CCFv3.  

Available versions:
```{atlas-versions} demba_allen_seg_dev_mouse_*
```
### [Dorr MRI Mouse Atlas](https://doi.org/10.1016/j.neuroimage.2008.03.037)
This atlas is a high-resolution, three-dimensional MRI-based atlas of the adult C57Bl/6J mouse brain, providing 
comprehensive anatomical coverage of the cerebrum, cerebellum, and brainstem. The atlas was constructed from 
within-skull, T2-weighted MR images acquired at 32 μm isotropic resolution from forty 12-week-old mice scanned on a 7 T
scanner. Following normalisation, registration, and averaging of individual scans, 62 distinct brain structures were 
manually delineated.

Available versions:
```{atlas-versions} dorr_mouse_mri
```
  
[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/dorr_mouse_mri.json)
### [Duke Mouse Brain Atlas](https://doi.org/10.1126/sciadv.adq8089)
This atlas from [Mansour et al. (2025)](https://doi.org/10.1126/sciadv.adq8089) is a 15 μm isotropic MRH-based stereotaxic atlas of the adult C57BL/6J mouse brain. The source atlas was built from five 90 ± 2 day male mice scanned in skull, limiting tissue deformation from cranial dissection and conventional histology. Micro-CT images of the skull provide bregma and lambda landmarks in the same stereotaxic space.

BrainGlobe includes the mean diffusivity template as the main reference image, the source annotation image, generated meshes, and 11 additional registered reference images. RCCFv3 is the Duke team's reduced version of the Allen CCFv3 label set, in which related structures smaller than 0.1 mm<sup>3</sup> are grouped into larger regions to reduce registration noise from small structures.

Available versions:
```{atlas-versions} duke_mouse
```
  
[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/duke_mouse.json)


### [CArea Mouse Atlas](https://doi.org/10.64898/2026.01.20.700446)
This atlas has regions which are automatically clustered based on three dimensional maps of gene expression. Voxels 
with similar patterns of gene expression are assigned the same region ID. The template is a population average Nissl 
volume, based on the CCFv3BBP atlas (also in 
[BrainGlobe](https://brainglobe.info/documentation/brainglobe-atlasapi/usage/atlas-details.html#ccfv3-augmented-mouse-atlas)) 
with some improvements. This atlas was constructed from reregistered ISH data from the Allen Institute for Brain Science. 

Available versions:
```{atlas-versions} carea_mouse
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/carea_mouse.json)


### [Allen CCFv2 Mouse Brain Atlas](https://doi.org/10.1038/nature13186)
This is a mouse brain atlas using version 2 of the commonly used Allen Common Coordinate Framework, which is included 
here for historical reasons. The template is based on 528 Nissl-stained coronal slices from the mouse specimen used in 
the Allen Reference Atlas. This atlas annotates the grey matter and ventricular systems of the mouse brain. This atlas
provides a common coordinate framework for many other useful mouse atlases based on CCFv2. Note that the additional 
reference is an average template based on serial two-photon tomography, and is misaligned with the original Nissl template.

Available versions:
```{atlas-versions} ccfv2_mouse
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/ccfv2_mouse.json)

### [Allen CCFv2 Mouse Fiber Tracts Atlas](https://doi.org/10.1038/nature13186)
This is a mouse brain fiber tract atlas using version 2 of the commonly used Allen Common Coordinate Framework. Where
the CCFv2 Mouse Brain atlas only provides information on the grey matter and ventricular systems of the mouse brain, 
this atlas contains fiber tract structural annotation information. as delineated in the Allen Reference Atlas. The 
template is based on 528 Nissl-stained coronal slices from the mouse specimen used in the Allen Reference Atlas. 
Note that the additional reference is an average template based on serial two-photon tomography, and is misaligned with 
the original Nissl template.

Available versions:
```{atlas-versions} ccfv2_fiber_mouse
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/ccfv2_fiber_mouse.json)

### [Allen CCFv2 Developmental Mouse Brain Atlas](https://doi.org/10.1038/nature13186)
This is a developmental mouse brain atlas using version 2 of the commonly used Allen Common Coordinate Framework. 
The template is based on 528 Nissl-stained coronal slices from the mouse specimen used in the Allen Reference Atlas. 
The annotations contain the developmental taxonomy of mouse brain structures as given in the Allen Developing Mouse
Brain atlas. Note that the additional reference is an average template based on serial two-photon tomography, and is 
misaligned with the original Nissl template.

Available versions:
```{atlas-versions} ccfv2_dev_mouse
```
  
[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/ccfv2_dev_mouse.json)

### [LAMBADA Developmental Mouse Brain Atlas](https://doi.org/10.1016/j.cell.2026.03.013)
This atlas tracks brain development in the mouse at 7 timepoints (P3, P5, P7, P9, P12, P14, P21). Each template is averaged from 20 to 30 LSFM images of iDISCO+ cleared brains of either sex, which were then aligned to an averaged in-vivo MRI scan of three mice per timepoint to correct for any ex-vivo deformation. This is useful for researchers seeking to study the in-vivo volumetric changes of the brain during development. Annotations are based on the CCFv3 Allen annotations. 

Available versions:
```{atlas-versions} lambada_dev_mouse_*
```
 
### [Allen CCFv1 Mouse Brain Atlas](https://doi.org/10.1038/nature05453)
This is the first edition of the mouse brain atlas in the commonly used Allen Common Coordinate Framework, which is included 
here for historical reasons. The template is based on the 528 Nissl-stained coronal slices from a male P56 mouse brain frozen
in OCT, which was annotated only on the left hemisphere based on the Allen Reference Atlas. This atlas provides a common 
coordinate framework for many other useful mouse atlases and data based on CCFv1. 

Available versions:
```{atlas-versions} ccfv1_mouse
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/ccfv1_mouse.json)

## Rat
### [Waxholm Space atlas of the Sprague Dawley rat brain](https://doi.org/10.1038/s41592-023-02034-3)
The Waxholm Space rat brain atlas features annotations of 222 structures, alongside a 39μm MRI template. It provides detailed delineations 
of the cerebral cortex, hippocampus, striatopallidal areas, midbrain, thalamus, auditory system and fiber tracts.
It is comprehensive, covering the entire rat brain. 
This atlas is only available at 39μm resolution:
```{atlas-versions} whs_sd_rat
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/whs_sd_rat.json)


### [SWC Female Rat Brain Atlas](https://brainglobe.info/blog/swc-female-rat-atlas.html#native-female-rat-atlas)
This atlas is a population-based anatomical template generated from female Lister Hooded rats (5–8 weeks old) using automated serial two-photon tomography. 
It provides a three-dimensional template derived from juvenile female animals, addressing gaps in both resolution and biological diversity in existing rat atlases. 
The atlas is particularly well suited for users who want to work in a native, microscopy-derived female rat brain space. The annotations are curated and adapted from the Waxholm Space rat brain atlas.

This atlas is only available at 50μm resolution:
```{atlas-versions} swc_female_rat
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/swc_female_rat.json)


### [Waxholm-aligned SWC Female Rat Atlas](https://brainglobe.info/blog/swc-female-rat-atlas.html#waxholm-space-registered-female-rat-atlas)
To support interoperability with existing rat resources, this atlas provides a version of the SWC female rat template registered to Waxholm Space. 
The template is resampled from 50μm to 39μm during registration to Waxholm Space, enabling direct comparison and integration with datasets and tools that already rely on Waxholm Space, while retaining the fine anatomical detail of the SWC template. The annotations are from the Waxholm Space rat brain atlas.

This atlas is only available at 39μm resolution (resampled from 50 µm during registration to Waxholm Space):
```{atlas-versions} whs_sd_swc_female_rat
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/whs_sd_swc_female_rat.json)

### [Duke Developmental Rat Brain Atlas](https://doi.org/10.1016/j.neuroimage.2013.01.017)
These atlases from [Calabrese et al. (2013)](https://doi.org/10.1016/j.neuroimage.2013.01.017) were obtained from 5 specimens each from 9 different time
points using a 7T MRI. The earliest 5 timepoints were registered to the Ashwell and Paxinos neonatal rat atlas and the last 4 timepoints were registered
to the Paxinos and Watson adult rat atlas to give a consistent view of the structural changes that occur over development. 

These atlases are only available at 25μm resolution:
```{atlas-versions} duke_dev_rat_*
```

## Other rodent
### [Prairie vole brain atlas](https://doi.org/10.7554/eLife.87029.3.sa0)
This is a brain atlas of the Prairie vole (Microtus ochrogaster) from
[Gustison et al. (2024)](https://doi.org/10.7554/eLife.87029.3.sa0).
This atlas is only available at 25μm resolution:
```{atlas-versions} prairie_vole
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/prairie_vole.json)


## Fish
### [Max Planck zebrafish brain atlas](http://fishatlas.neuro.mpg.de)
This atlas is only available at 1μm resolution:
```{atlas-versions} mpin_zfish
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/mpin_zfish.json)


### [AZBA: A 3D Adult zebrafish brain atlas](https://doi.org/10.1101/2021.05.04.442625)
This atlas is only available at 4μm resolution:
```{atlas-versions} azba_zfish
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/azba_zfish.json)


### [Blind Mexican cavefish brain atlas](https://elifesciences.org/articles/80777)
This is a brain atlas of the blind Mexican cavefish (Astyanax mexicanus) from 
[Kozol et al. (2023)](https://elifesciences.org/articles/80777). For more details please
see [the blogpost](/blog/cavefish-atlas-added).
This atlas is only available at 2μm resolution:
```{atlas-versions} sju_cavefish
```
[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/sju_cavefish.json)


### [Danionella cerebrum Brain Atlas](https://doi.org/10.64898/2026.03.09.710483)
This is a multimodal, mixed-sex reference atlas of the adult _Danionella cerebrum_
brain from [Kadobianskyi et al. (2026)](https://doi.org/10.64898/2026.03.09.710483).
It contains a whole-brain annotation for 276 regions, a two-photon fluoresence reference 
image and an additional confocal reflectance reference image highlighting larger myelinated 
fibre tracts. For more details, see the [blog post](/blog/danionella-atlas-added).

This atlas is only available at 2.5μm resolution:
```{atlas-versions} danionella_cerebrum_mixed
```

## Lizard
### [Hoops Tawny Dragon Brain Atlas](https://doi.org/10.1007/s00429-021-02282-z)
This is a symmetric atlas of the tawny dragon lizard (Ctenophorus decresii) brain from 
[Hoops et al. (2021)](https://doi.org/10.1007/s00429-021-02282-z) with 224 segmentations, 
made from averaged MRI images of 13 male tawny dragon lizards. 
This atlas is only available at 20μm resolution:
```{atlas-versions} hoops_tawny_dragon
```
  
[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/hoops_tawny_dragon.json)



## Amphibian
### [UNAM Axolotl Brain Atlas](https://doi.org/10.1038/s41598-021-89357-3)
This is a magnetic resonance imaging based atlas of the Axolotl (Ambystoma mexicanum) from 
[Lazcano et al. (2021)](https://doi.org/10.1038/s41598-021-89357-3). For more details please 
see [the blogpost](/blog/axolotl-atlas-added).

This atlas is only available at 40μm resolution:
```{atlas-versions} unam_axolotl
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/unam_axolotl.json)


## Human and non-human primate
### [Allen Human Brain Atlas](https://www.brain-map.org)
This atlas is included mostly for visualisation and comparison to the other atlases. 
There are many better atlases (and indeed software tools) for the analysis of human 
neuroimaging data.

This atlas is only available at 500μm resolution:
```{atlas-versions} allen_human
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/allen_human.json)


### [MRI mouse lemur brain atlas](https://doi.org/10.1016/j.dib.2018.10.067) 
This is an MRI atlas of the grey mouse lemur (Microcebus murinus) from 
[Nadkarni et al. (2018)](https://doi.org/10.1016/j.dib.2018.10.067).

This atlas is only available at 91um resolution
```{atlas-versions} nadkarni_mri_mouselemur
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/nadkarni_mri_mouselemur.json)


## Other mammal
### [Cat brain atlas](https://doi.org/10.1002/cne.24271)

This is an MRI atlas of a cat (Felis catus) from [Stolzberg et al. (2017)](https://doi.org/10.1002/cne.24271)

This atlas is only available at 500um resolution:
```{atlas-versions} csl_cat
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/csl_cat.json)


## Bird
### [Eurasian blackcap atlas](https://doi.org/10.1101/2025.03.04.641293)
This is a serial section two-photon atlas of the Eurasian blackcap (Sylvia atricapilla) 
built by the BrainGlobe team ([Sirmpilatze et al. (2025)](https://doi.org/10.1101/2025.03.04.641293)). 
For more details please see [the project page](/projects/blackcap/index).

This atlas is only available at 25μm resolution:
```{atlas-versions} eurasian_blackcap
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/eurasian_blackcap.json)


## Invertebrate

### [Columbia cuttlefish atlas](https://doi.org/10.1016/j.cub.2023.06.007)
This is an MRI atlas of the dwarf cuttlefish (Sepia bandensis) from [Montague et al. (2023)](https://doi.org/10.1016/j.cub.2023.06.007)

This atlas is only available at 50μm resolution:
```{atlas-versions} columbia_cuttlefish
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/columbia_cuttlefish.json)


### [Kocher Bumblebee Brain Atlas](https://doi.org/10.1016/j.cub.2022.04.066)
This is a confocal microscopy [atlas of the adult bumblebee](https://doi.org/10.1016/j.cub.2022.04.066), made by the Kocher lab.

This atlas has anisotropic resolution (2.542μm in axial direction - along antero-posterior axis - and 1.2407μm in-plane) resolution
```{atlas-versions} kocher_bumblebee
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/kocher_bumblebee.json)


### Drosophila wing disc instar3 atlas.
This is a confocal microscopy atlas of the fruit fly larva's imaginal wing disc, at the 3rd instar developmental stage. It was built by Kaixiang Shuai as part of his MSc thesis, supervised by [Giulia Paci (Mao Lab at UCL)](https://www.tissuemechanicslab.com/gulia) and Alessandro Felder (BrainGlobe team).
This atlas has 2um isotropic resolution. 
```{atlas-versions} drosophila_wingdisc_instar3
```

[![View in neuroglancer](https://img.shields.io/badge/Neuroglancer-View%20atlas-blue)](https://neuroglancer-demo.appspot.com/#!https://brainglobe.s3.amazonaws.com/ng_state_files/drosophila_wingdisc_instar3.json)


### [Virtual Fly Brain JRC2018Unisex neuropils atlas](https://www.virtualflybrain.org/blog/2022/01/01/jrc-2018-templates-rois-jrc2018/)

This atlas packages the JRC2018Unisex adult _Drosophila melanogaster_ brain
template with 46 VFB-painted neuropil ROI annotations. The annotations form a
flat structure list and include source meshes provided by Virtual Fly Brain.

This atlas has anisotropic 0.5189161 × 1.0 × 0.5189161 µm resolution:
```{atlas-versions} vfb_jrc2018u_neuropils_fly
```

### [Virtual Fly Brain JRC2018Unisex VNC atlas](https://www.virtualflybrain.org/term/adult-vnc-neuropils-court2020-court2020/)

This atlas packages the JRC2018UnisexVNC adult _Drosophila melanogaster_
template with VFB neuropil and domain annotations based on
[Court et al. (2020)](https://doi.org/10.1016/j.neuron.2020.08.005). It has 20
visible non-root regions in a flat structure list and includes source meshes
provided by Virtual Fly Brain.

This atlas has 0.4 µm isotropic resolution:
```{atlas-versions} vfb_jrc2018u_vnc_fly
```


