# image_io

`image_io` provides various options to load and save image data. 
It supports common formats like `tiff`, `nrrd` and `nifti`.

## Installation

`image_io` is provided as part of `brainglobe_utils` which comes with the one-line BrainGlobe install (`pip install brainglobe`).
It will also be fetched by most of our tools if you decide to install them as standalone.

## Loading images

All options to load images are provided under `brainglobe_utils.image_io.load`. 
For example, the general purpose `load_any` function which can load many common file formats:

```python
from brainglobe_utils.image_io import load
load.load_any('mydata.tif')
```

There are also functions specific to particular file formats:

```python
from brainglobe_utils.image_io import load

# tiff
load.load_img_stack('mydata.tif', x_scaling_factor=1, y_scaling_factor=1, z_scaling_factor=1)

# directory containing a sequence of 2D tiffs
load.load_from_folder('/path/to/dir')

# nrrd
load.load_nrrd('mydata.nrrd')

# nifti
load.load_nii('mydata.nii')
```

## Saving images

All options to save images are provided under `brainglobe_utils.image_io.save`. 
For example, the general purpose `save_any` function which can save a numpy array to many common file formats:

```python
from brainglobe_utils.image_io import save
save.save_any(my_array, 'mydata.tif')
```

There are also functions specific to particular file formats:

```python
from brainglobe_utils.image_io import save

# tiff
save.to_tiff(my_array, 'mydata.tif')

# directory containing a sequence of 2D tiffs
save.to_tiffs(my_array, '/path/to/dir/prefix')

# nrrd
save.to_nrrd(my_array, 'mydata.nrrd')

# nifti
save.to_nii(my_array, 'mydata.nii')
```
