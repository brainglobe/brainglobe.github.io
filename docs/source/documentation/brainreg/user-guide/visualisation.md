# Visualising brainreg output
If you have used the brainreg command-line interface, or simply want to view results at a later time, 
brainreg comes with a plugin for napari to allow you to easily view registration results.

## Usage
To begin, open napari and drag your brainreg output directory (the one with the log file) onto the napari window.

Various images should then open, including:

* `Registered image` - the image used for registration, downsampled to atlas resolution
* `atlas_name` - e.g. `allen_mouse_25um` the atlas labels, warped to your sample brain
* `Boundaries` - the boundaries of the atlas regions

If you downsampled additional channels, these will also be loaded.

Some of these images will not be visible by default. Click the little eye icon to toggle visibility.

:::{note}
N.B. If you use a high-resolution atlas (such as `allen_mouse_10um`), then the files can take a little while to load.
:::

![Visualisation in sample space](/documentation/brainreg/images/sample_space.gif)
