# morphapi

`morphapi` is a lightweight python package for downloading neuronal morphological reconstructions from publicly 
available datasets. It provides a number of APIs that facilitate the download of selected neurons and functionality 
to create 3d meshes with the neuronal reconstruction for visualization with packages like `brainrender`.

`morphapi` relies on the [`neurom`](https://github.com/BlueBrain/NeuroM) package from the BlueBrain 
project \([github](https://github.com/BlueBrain/NeuroM)\) to reconstruct morphology from `.swc` files and on 
[`vedo`](https://github.com/marcomusy/vedo) to create 3d rendering from morphological data.

## Currently supported datasets

* [Allen brain atlas - Cell Types](https://celltypes.brain-map.org/)
* [neuromorpho.org](https://neuromorpho.org/)
* [Janelia Campus - Mouse Light project](https://www.janelia.org/project-team/mouselight)
* [Kunst et al 2019 - Zebrafish neurons](https://mapzebrain.org)

## Installation

To install `morphapi` in a python environment with `python >= 3.6` simply:

```text
pip install morphapi
```

## Usage
```{toctree}
:maxdepth: 1
usage/downloading-data
usage/rendering-data
```

