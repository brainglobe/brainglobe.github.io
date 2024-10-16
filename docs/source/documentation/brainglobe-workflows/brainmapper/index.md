# `brainmapper` command line tool

`brainmapper` can:

- Detect labelled cells in 3D in whole-brain images (many hundreds of GB)
- Register the image to an atlas (such as the [Allen Mouse Brain Atlas](https://atlas.brain-map.org/atlas?atlas=602630314))
- Segment the brain based on the reference atlas
- Calculate the volume of each brain area, and the number of labelled cells within it
- Transform everything into standard space for analysis and visualisation

:::{note}
It is possible to detect cells in a whole brain image and register this data to an atlas entirely within a graphical 
user interface. If you have not used `brainmapper` before, we recommend you take a look at the 
[analysing brainwide distribution of cells tutorial](/tutorials/transform-cells-atlas).
:::

## User Guide

```{toctree}
:maxdepth: 1
data-requirements
cli
visualisation
output-files
error-messages
/documentation/cellfinder/user-guide/training/index
```

:::{note}  If you would like to use `brainmapper` offline, you will need to 
[download an appropriate atlas](/documentation/brainglobe-atlasapi/usage/command-line-interface) and 
[download a pre-trained cellfinder model](/documentation/cellfinder/user-guide/cellfinder-download) in advance. 
:::

## Tutorials

```{toctree}
:maxdepth: 1
/tutorials/brainmapper/index
```

## Citing cellfinder

If you find `brainmapper` useful, and use it in your research, please cite the papers outlining the registration and cell detection algorithms:
> Tyson, A. L., V&eacute;lez-Fort, M.,  Rousseau, C. V., Cossell, L., Tsitoura, C., Lenzi, S. C., Obenhaus, H. A., Claudi, F., Branco, T.,  Margrie, T. W. (2022). Accurate determination of marker location within whole-brain microscopy images. Scientific Reports, 12, 867 [doi.org/10.1038/s41598-021-04676-9](https://doi.org/10.1038/s41598-021-04676-9)

> Tyson, A. L., Rousseau, C. V., Niedworok, C. J., Keshavarzi, S., Tsitoura, C., Cossell, L., Strom, M. and Margrie, T. W. (2021) “A deep learning algorithm for 3D cell detection in whole mouse brain image datasets’ PLOS Computational Biology, 17(5), e1009074
[https://doi.org/10.1371/journal.pcbi.1009074](https://doi.org/10.1371/journal.pcbi.1009074)

Lastly, if you can, please cite the BrainGlobe Atlas API that provided the atlas:

>Claudi, F., Petrucco, L., Tyson, A. L., Branco, T., Margrie, T. W. and Portugues, R. (2020). BrainGlobe Atlas API: a common interface for neuroanatomical atlases. Journal of Open Source Software, 5(54), 2668, https://doi.org/10.21105/joss.02668

**Don't forget to cite the developers of the atlas that you used (e.g. the Allen Brain Atlas)!**

## Notes

- As of version `1.0.0` of `brainglobe-workflows`, the Docker image for `brainmapper` has been discontinued.
- Prior to the release of `cellfinder` `v1.0.0`, this workflow and command-line tool was called "cellfinder".
