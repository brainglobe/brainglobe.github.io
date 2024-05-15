# Image IO submodule

The image IO submodule provides various options to load and save image data. 
It supports common formats like `tiff`, `nrrd` and `nifti`.

## Installation

The image IO submodule is provided as part of `brainglobe_utils` which comes with the one-line BrainGlobe install (`pip install brainglobe`).
It will also be fetched by most of our tools if you decide to install them as standalone.

## Loading images

All options to load images are provided under `brainglobe_utils.IO.image.load`. 
For example, the general purpose `load_any` function which can load many common file formats:

```python
from brainglobe_utils.IO.image import load
load.load_any('mydata.tif')
```

There are also functions specific to particular file formats:

```python
from brainglobe_utils.IO.image import load

# tiff
load.load_img_stack('mydata.tif', x_scaling_factor=1, y_scaling_factor=1, z_scaling_factor=1)

# directory containing a sequence of 2D tiffs
load.load_from_folder('/path/to/dir')

# nrrd
load.load_nrrd('mydata.nrrd')

# nifti
load.load_nii('mydata.nii')
```

Or to load a directory containing a series of 2D tiffs as a dask array:

```python
from brainglobe_utils.IO.image.load import read_with_dask

signal_array = read_with_dask("/path/to/image_directory")
```

## Saving images

All options to save images are provided under `brainglobe_utils.IO.image.save`. 
For example, the general purpose `save_any` function which can save a numpy array to many common file formats:

```python
from brainglobe_utils.IO.image import save
save.save_any(my_array, 'mydata.tif')
```

There are also functions specific to particular file formats:

```python
from brainglobe_utils.IO.image import save

# tiff
save.to_tiff(my_array, 'mydata.tif')

# directory containing a sequence of 2D tiffs
save.to_tiffs(my_array, '/path/to/dir/prefix')

# nrrd
save.to_nrrd(my_array, 'mydata.nrrd')

# nifti
save.to_nii(my_array, 'mydata.nii')
```
