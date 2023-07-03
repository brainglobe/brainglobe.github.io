# brainreg-segment


brainreg-segment is a companion to [brainreg](../brainreg/index) allowing manual segmentation of regions/objects 
within the brain (e.g. injection sites, probes etc.) allowing for automated analysis of brain region distribution, 
and visualisation (e.g. in [brainrender](../brainrender/index)).

## Installation

brainreg-segment comes bundled with brainreg, so see the [brainreg installation instructions](../brainreg/installation). 
brainreg-segment can be installed on its own (see below), but you will need to register your data with brainreg first.

### Standalone installation

If you don't want to install brainreg, brainreg-segment can be installed on its own. brainreg-segment is 
distributed as a plugin for [napari](https://napari.org/), so first follow the 
[napari installation instructions](https://napari.org/). You can then install `brainreg-segment` from the 
napari plugin menu.

![Installing from the napari plugin menu](images/install_plugin.png)

Alternatively, the plugin can be installed into a Python environment with `pip install brainreg-segment`.


## User guide
```{toctree}
:maxdepth: 1
user-guide/index
user-guide/segmenting-1d-tracks
user-guide/segmenting-3d-structures
user-guide/segmenting-external-layers
```


## Citation

If you find brainreg-segment useful and use it in your research, please let us know and also cite the paper:

> Tyson, A. L., V&eacute;lez-Fort, M.,  Rousseau, C. V., Cossell, L., Tsitoura, C., Lenzi, S. C., Obenhaus, H. A., Claudi, F., Branco, T.,  Margrie, T. W. (2022). Accurate determination of marker location within whole-brain microscopy images. Scientific Reports, 12, 867 [doi.org/10.1038/s41598-021-04676-9](https://doi.org/10.1038/s41598-021-04676-9)

Lastly, if you can, please cite the BrainGlobe Atlas API that provided the atlas:

>Claudi, F., Petrucco, L., Tyson, A. L., Branco, T., Margrie, T. W. and Portugues, R. (2020). BrainGlobe Atlas API: a common interface for neuroanatomical atlases. Journal of Open Source Software, 5(54), 2668, https://doi.org/10.21105/joss.02668

**Don't forget to cite the developers of the atlas that you used (e.g. the Allen Brain Atlas)!**

