# cellfinder-core API

The API is not yet fully documented. For an idea of what the parameters do, see the 
[documentation for the napari plugin](napari-plugin/index).

## To run the full pipeline (cell candidate detection and classification)
```python
from cellfinder_core.main import main as cellfinder_run
import tifffile

signal_array = tifffile.imread("/path/to/signal_image.tif")
background_array = tifffile.imread("/path/to/background_image.tif")

voxel_sizes = [5, 2, 2] # in microns
detected_cells = cellfinder_run(signal_array,background_array,voxel_sizes)
```

The output is a list of
[imlib Cell objects](https://github.com/brainglobe/brainglobe-utils/blob/main/brainglobe_utils/cells/cells.py).
Each `Cell` has a centroid coordinate, and a type:

```python
print(detected_cells[0])
# Cell: x: 132, y: 308, z: 10, type: 2
```

Cell type 2 is a "real" cell, and Cell type 1 is a "rejected" object (i.e.,
not classified as a cell):

```python
from imlib.cells.cells import Cell
print(Cell.CELL)
# 2

print(Cell.NO_CELL)
# 1
```

## Saving the results
If you want to save the detected cells for use in other BrainGlobe software (e.g. the napari plugin) 
you can save in the cellfinder XML standard:
```python
from imlib.IO.cells import save_cells
save_cells(detected_cells, "/path/to/cells.xml")
```
You can load these back with:
```python
from imlib.IO.cells import get_cells
cells = get_cells("/path/to/cells.xml")
```


## Using dask for lazy loading
`cellfinder-core` supports most array-like objects. Using
[Dask arrays](https://docs.dask.org/en/latest/array.html) allows for lazy
loading of data, allowing large (e.g. TB) datasets to be processed.
`cellfinder-core` comes with a function
(based on [napari-ndtiffs](https://github.com/tlambert03/napari-ndtiffs)) to
load a series of image files (e.g. a directory of 2D tiff files) as a Dask
array. `cellfinder-core` can then be used in the same way as with a numpy array.

```python
from cellfinder_core.main import main as cellfinder_run
from cellfinder_core.tools.IO import read_with_dask

signal_array = read_with_dask("/path/to/signal_image_directory")
background_array = read_with_dask("/path/to/background_image_directory")

voxel_sizes = [5, 2, 2] # in microns
detected_cells = cellfinder_run(signal_array,background_array,voxel_sizes)
```

## Running the cell candidate detection and classification separately.
```python
import tifffile
from pathlib import Path

from cellfinder_core.detect import detect
from cellfinder_core.classify import classify
from cellfinder_core.tools.prep import prep_classification

signal_array = tifffile.imread("/path/to/signal_image.tif")
background_array = tifffile.imread("/path/to/background_image.tif")
voxel_sizes = [5, 2, 2] # in microns

home = Path.home()
install_path = home / ".cellfinder" # default

start_plane=0
end_plane=-1
trained_model=None
model_weights=None
model="resnet50_tv"
batch_size=32
n_free_cpus=2
network_voxel_sizes=[5, 1, 1]
soma_diameter=16
ball_xy_size=6
ball_z_size=15
ball_overlap_fraction=0.6
log_sigma_size=0.2
n_sds_above_mean_thresh=10
soma_spread_factor=1.4
max_cluster_size=100000
cube_width=50
cube_height=50
cube_depth=20
network_depth="50"

model_weights = prep_classification(
    trained_model, model_weights, install_path, model, n_free_cpus
)

cell_candidates = detect.main(
    signal_array,
    start_plane,
    end_plane,
    voxel_sizes,
    soma_diameter,
    max_cluster_size,
    ball_xy_size,
    ball_z_size,
    ball_overlap_fraction,
    soma_spread_factor,
    n_free_cpus,
    log_sigma_size,
    n_sds_above_mean_thresh,
)

if len(cell_candidates) > 0: # Don't run if there's nothing to classify
    classified_cells = classify.main(
        cell_candidates,
        signal_array,
        background_array,
        n_free_cpus,
        voxel_sizes,
        network_voxel_sizes,
        batch_size,
        cube_height,
        cube_width,
        cube_depth,
        trained_model,
        model_weights,
        network_depth,
    )
```
## Training the network
The training data needed are matched pairs (signal & background) of small
(usually 50 x 50 x 100&#956;m) images centered on the coordinate of candidate cells.
These can be generated however you like, but we recommend the [napari plugin](napari-plugin/training-data-generation).

`cellfinder-core` comes with a 50-layer ResNet trained on ~100,000 data points
from serial two-photon microscopy images of mouse brains
(available [here](https://gin.g-node.org/cellfinder/training_data)).

Training the network is likely simpler using the 
[napari plugin](napari-plugin/training-the-network),
but it is possible through the Python API.

```python
from pathlib import Path
from cellfinder_core.train.train_yml import run as run_training

# list of training yml files
yaml_files = [Path("/path/to/training_yml.yml)]

# where to save the output
output_directory = Path("/path/to/saved_training_data")

home = Path.home()
install_path = home / ".cellfinder"  # default

run_training(
    output_directory,
    yaml_files,
    install_path=install_path,
    learning_rate=0.0001,
    continue_training=True, # by default use supplied model
    test_fraction=0.1,
    batch_size=32,
    save_progress=True,
    epochs=10,
)
```
