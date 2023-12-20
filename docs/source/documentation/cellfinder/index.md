# cellfinder

cellfinder is software for automated 3D cell detection in very large 3D images (e.g., serial two-photon or lightsheet volumes of whole mouse brains).

![Detected labelled cells, overlaid on a segmented coronal brain section](images/cells.png)
**Detected labelled cells, overlaid on a segmented coronal brain section**

## Ways to use cellfinder

cellfinder can be used in three ways, each with different user interfaces and different aims.

:::{hint}
If you don't know how to start, we recommend the cellfinder napari plugin.
We also recommend you install cellfinder by installing `brainglobe-workflows` - see the [installation instructions](./installation#one-step-installation) for details.
:::

### cellfinder.core

`cellfinder.core` is a Python submodule implementing the core algorithm for efficient cell detection in large images.

The submodule exists to allow developers to implement the algorithm in their own software.
For now, the only API documentation is in the [GitHub README](https://github.com/brainglobe/cellfinder/blob/main/README.md), please see the documentation for the napari plugin [here](user-guide/napari-plugin/index) for an explanation of the parameters.
Alternatively, please [get in touch](/contact).

### cellfinder napari plugin

This is a thin wrapper around the `cellfinder.core` submodule and aims to:

- Provide the cell detection algorithm in a user-friendly form
- Allow the cell detection algorithm to be chained together with other tools in the napari ecosystem
- Allow easier parameter optimisation for users of the other cellfinder tools.

![Visualising detected cells in the cellfinder napari plugin](images/napari-cellfinder.gif)
**Visualising detected cells in the cellfinder napari plugin**

### `brainmapper` command-line tool

The `brainmapper` command-line tool exists to combine the `cellfinder.core` cell detection algorithm and [brainreg](/documentation/brainreg/index).
See the [documentation for `brainglobe-workflows`](/documentation/brainglobe-workflows/index) for more information.

## Installation

```{toctree}
:maxdepth: 1
installation
```

## User guide

```{toctree}
:maxdepth: 1
user-guide/napari-plugin/index
user-guide/cellfinder-core
user-guide/training-strategy
```

If you are experiencing issues with `cellfinder`'s speed or configuration, you may want to take a look at the [troubleshooting guide for `brainmapper`](../brainglobe-workflows/brainmapper/troubleshooting/index.md).
`brainmapper` uses your `cellfinder` installation when it runs, and many of the problems you encounter with `cellfinder` will be solved in the same way as those for `brainmapper`.

## Citing cellfinder

If you find `cellfinder` useful, and use it in your research, please cite the paper outlining the cell detection algorithm:
> Tyson, A. L., Rousseau, C. V., Niedworok, C. J., Keshavarzi, S., Tsitoura, C., Cossell, L., Strom, M. and Margrie, T. W. (2021) “A deep learning algorithm for 3D cell detection in whole mouse brain image datasets’ PLOS Computational Biology, 17(5), e1009074
[https://doi.org/10.1371/journal.pcbi.1009074](https://doi.org/10.1371/journal.pcbi.1009074)
>

If you use any of the image registration functions in cellfinder, please also cite [brainreg](/documentation/brainreg/index).
