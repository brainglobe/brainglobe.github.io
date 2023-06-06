# cellfinder napari plugin

The cellfinder algorithm is in two stages. Firstly, cell candidates (objects of roughly the correct size and intensity 
to be a cell) are detected, and then a deep learning network classifies these cell candidates as being cells or 
artefacts. Because this classification step will need to be retrained for new data, the napari plugin is split 
into three sections:

```{toctree}
:maxdepth: 1
cell-detection
training-data-generation
training-the-network
```

```{toctree}
:maxdepth: 1
:hidden:
all-cell-detection-parameters
```

:::{hint}
To understand how cellfinder works, it may be useful to take a look at the 
[original paper](https://doi.org/10.1371/journal.pcbi.1009074).
:::





