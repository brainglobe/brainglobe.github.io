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

* [Allen Mouse Brain Atlas](https://portal.brain-map.org/) at 10, 25, 50 and 100 micron resolutions
* [Allen Human Brain Atlas](https://portal.brain-map.org/) at 100 micron resolution
* [Max Planck Zebrafish Brain Atlas](http://fishatlas.neuro.mpg.de) at 1 micron resolution
* [Enhanced and Unified Mouse Brain Atlas](https://kimlab.io/brain-map/atlas/) at 10, 25, 50 and 100 micron resolutions
* [Smoothed version of the Kim et al. mouse reference atlas](https://doi.org/10.1016/j.celrep.2014.12.014) at 10, 25, 50 and 100 micron resolutions
* [Gubra's LSFM mouse brain atlas](https://doi.org/10.1007/s12021-020-09490-8) at 20 micron resolution
* [3D version of the Allen mouse spinal cord atlas](https://doi.org/10.1016/j.crmeth.2021.100074) at 20 x 10 x 10 micron resolution
* [AZBA: A 3D Adult Zebrafish Brain Atlas]( https://doi.org/10.7554/eLife.69988) at 4 micron resolution
* [Waxholm Space atlas of the Sprague Dawley rat brain](https://doi.org/10.1016/j.neuroimage.2014.04.001) at 39 micron resolution
* [3D Edge-Aware Refined Atlases Derived from the Allen Developing Mouse Brain Atlases](https://doi.org/10.7554/eLife.61408) (E13, E15, E18, P4, P14, P28 & P56)
* [Princeton Mouse Brain Atlas](https://brainmaps.princeton.edu/2020/09/princeton-mouse-brain-atlas-links) at 20 micron resolution
* [Kim Lab Developmental CCF (P56)](https://data.mendeley.com/datasets/2svx788ddf/1) at 10 micron resolution with 8 reference images - STP, LSFM (iDISCO) and MRI (a0, adc, dwo, fa, MTR, T2)

## Installation

BrainGlobe AtlasAPI works with Python >3.6, and can be installed from PyPI with:

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
