# Visualising brainreg output
If you have used the brainreg command-line interface, or simply want to view results at a later time, 
brainreg comes with a plugin for napari to allow you to easily view registration results.

## Basic usage
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

## Choosing a different space or resolution
By default, dragging the output folder into napari (as described [above](#basic-usage)) will load the results in sample space, at the **downsampled** resolution used for registration. 

However, it might be useful to load the registration results in atlas space, or at a different resolution. For this we have implemented a series of submenus in the `File > IO Utilities` menu.

![Load Brainreg Results via Napari IO Utilities](/documentation/brainreg/images/load_brainreg_result_napari.png)

Simply select the appropriate submenu, and then select the brainreg output folder. The options are:

* `Sample Space, Atlas Resolution` - this is the default behaviour described [above](#basic-usage)
* `Atlas Space, Atlas Resolution` - opens the registered image and atlas at the atlas (**downsampled**) resolution and orientation.
* `Sample Space, Sample Resolution` - opens the registered atlas, boundaries and hemispheres scaled and oriented to the **original sample resolution**. Original high-resolution images are not opened.

:::{note}
It's important to note that choosing `Sample Space, Sample Resolution` will not open the original high-resolution images, as these can be very large. The user is expected to manually load these images into Napari.
:::

These submenus will simply load, orient and scale different images from the brainreg output folder to reflect the corresponding space and resolution. For further information on the output files, see the [brainreg output files page](/documentation/brainreg/user-guide/output-files.md).