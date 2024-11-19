# BrainGlobe Atlas API (brainglobe-atlasapi)

Many excellent brain atlases exist for different species. Some of them have an API (application programming interface)
to allow users to interact with the data programmatically (e.g. the excellent
[Allen Mouse Brain Atlas](https://portal.brain-map.org)), but many do not, and there is no consistent way to process
data from multiple sources.

The brainglobe atlas API deals with this problem by providing a common interface for programmers to download and process data from multiple sources.

Each atlas consists of data files in a common format:

* A "reference" image of a brain (`.tiff`)
* An "annotation" image, with each brain region defined by a unique pixel value (`.tiff`)
* Meshes defining the surface of each brain region (`.obj`)
* A mapping of brain region pixel value to region name, and structure hierarchy (`.json`)
* Metadata defining the shape, orientation etc. of the data, and other info such as animal species and authors (`.json`)

## Atlases available

A number of atlases are in development, but those available currently are:

| Atlas Name | Resolution | Ages | Reference Images | Name in API
| --- |  --- | --- | --- | --- |
| [Allen Mouse Brain Atlas](https://doi.org/10.1016/j.cell.2020.04.007) | 10, 25, 50, and 100 micron | P56 | STPT | allen_mouse_10um, allen_mouse_25um, allen_mouse_100um
| [Allen Human Brain Atlas](https://www.brain-map.org) | 500 micron | Adult | MRI | allen_human_500um
| [Max Planck Zebrafish Brain Atlas](http://fishatlas.neuro.mpg.de) | 1 micron | 6-dpf | FISH | mpin_zfish_1um
| [Enhanced and Unified Mouse Brain Atlas](https://kimlab.io/brain-map/atlas/) | 10, 25, 50, and 100 micron | P56 | STPT | kim_mouse_10um, kim_mouse_25um, kim_mouse_50um, kim_mouse_100um
| [Smoothed version of the Kim et al. mouse reference atlas](https://doi.org/10.1016/j.celrep.2014.12.014) | 10, 25, 50 and 100 micron | P56 | STPT | osten_mouse_10um, osten_mouse_25um, osten_mouse_50um, osten_mouse_100um
| [Gubra's LSFM mouse brain atlas](https://doi.org/10.1007/s12021-020-09490-8) | 20 micron | 8 to 10 weeks post natal | LSFM | perens_lsfm_mouse_20um
| [3D version of the Allen mouse spinal cord atlas](https://doi.org/10.1101/2021.05.06.443008) | 20 x 10 x 10 micron | Adult | Nissl | allen_cord_20um
| [AZBA: A 3D Adult Zebrafish Brain Atlas](https://doi.org/10.1101/2021.05.04.442625) | 4 micron | 15-16 weeks post natal | LSFM | azba_zfish_4um
| [Waxholm Space atlas of the Sprague Dawley rat brain](https://doi.org/10.1038/s41592-023-02034-3) | 39 micron | P80  | MRI | whs_sd_rat_39um
| [3D Edge-Aware Refined Atlases Derived from the Allen Developing Mouse Brain Atlases](https://doi.org/10.7554/eLife.61408) | 16, 16.75, and 25 micron | E13, E15, E18, P4, P14, P28 & P56 | Nissl | admba_3d_e11_5_mouse_16um, admba_3d_e13_5_mouse_16um, admba_3d_e15_5_mouse_16um, admba_3d_e18_5_mouse_16um, admba_3d_p14_mouse_16.752um, admba_3d_p28_mouse_16.752um, admba_3d_p4_mouse_16.752um, admba_3d_p56_mouse_25um
| [Princeton Mouse Brain Atlas](https://brainmaps.princeton.edu/2020/09/princeton-mouse-brain-atlas-links) | 20 micron | >P56 (older animals included) | LSFM | princeton_mouse_20um
| [Kim Lab Developmental CCF](https://data.mendeley.com/datasets/2svx788ddf/1) | 10 micron | P56  | STP, LSFM (iDISCO) and MRI (a0, adc, dwo, fa, MTR, T2) | kim_dev_mouse_stp_10um, kim_dev_mouse_idisco_10um, kim_dev_mouse_mri_a0_10um, kim_dev_mouse_mri_adc_10um, kim_dev_mouse_mri_dwi_10um, kim_dev_mouse_mri_fa_10um, kim_dev_mouse_mri_mtr_10um, kim_dev_mouse_mri_t2_10um
| [Blind Mexican Cavefish Brain Atlas](https://doi.org/10.7554/eLife.80777) | 2 micron | 6 days post fertilisation | IHC | sju_cavefish_2um
| [BlueBrain Barrel Cortex Atlas](https://doi.org/10.1162/imag_a_00209) | 10 and 25 micron | P56 | STPT | allen_mouse_bluebrain_barrels_10um, allen_mouse_bluebrain_barrels_25um
| [UNAM Axolotl Brain Atlas](https://doi.org/10.1038/s41598-021-89357-3) | 40 micron | ~ 3 months post hatching | MRI | unam_axolotl_40um
| [Prairie Vole Brain Atlas](https://doi.org/10.7554/eLife.87029.3.sa0) | 25 micron | Unknown | LSFM | prairie_vole_25um

## Installation

BrainGlobe AtlasAPI works with Python >=3.10, and can be installed from PyPI with:

```bash
pip install brainglobe-atlasapi
```

## Usage

```{toctree}
:maxdepth: 2
usage/atlas-details
usage/python-api
usage/command-line-interface
usage/using-the-files-directly

```

## More details

```{toctree}
:maxdepth: 1
adding-a-new-atlas
```

## Citation

If you find the BrainGlobe Atlas API useful, please cite the paper in your work:

>Claudi, F., Petrucco, L., Tyson, A. L., Branco, T., Margrie, T. W. and Portugues, R. (2020). BrainGlobe Atlas API: a common interface for neuroanatomical atlases. Journal of Open Source Software, 5(54), 2668, <https://doi.org/10.21105/joss.02668>

**Don't forget to cite the developers of the atlas that you used!**
