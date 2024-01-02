# `brainmapper` command line tool

`brainmapper` can:

- Detect labelled cells in 3D in whole-brain images (many hundreds of GB),
- Register the image to an atlas (such as the [Allen Mouse Brain Atlas](https://atlas.brain-map.org/atlas?atlas=602630314)),
- Segment the brain based on the reference atlas,
- Calculate the volume of each brain area, and the number of labelled cells within it,
- Transform everything into standard space for analysis and visualisation.

## User Guide

```{toctree}
:maxdepth: 1
data-requirements
cli
visualisation
output-files
training/index
```

## Tutorials

```{toctree}
:maxdepth: 1
/tutorials/brainmapper/index
```

## Troubleshooting

Since `brainmapper` uses `cellfinder`, you may encounter issues when using the command-line tool that are [documented on the `cellfinder` page](../cellfinder/troubleshooting/index.md).
[Head there](../cellfinder/troubleshooting/index.md) for more information on some common issues and debugging tips.

## Notes

- As of version `1.0.0` of `brainglobe-workflows`, the Docker image for `brainmapper` has been discontinued.
- Prior to the release of `cellfinder` `v1.0.0`, this workflow and command-line tool was called "cellfinder".
