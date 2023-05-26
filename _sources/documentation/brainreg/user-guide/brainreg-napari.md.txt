# Napari plugin
How to use the brainreg napari plugin

## Getting started

To register your data, you will need a whole-brain image, i.e., not a part of a brain, and not some individual 2D 
sections. The format doesn't matter, as long as it can be loaded into napari, and the orientation etc. is dealt with by brainreg.

## Loading data

Loading your data into napari will vary depending on the data type, but with most types, you should be able to drag 
and drop your data into the main napari window.

:::{note}
If you are having trouble loading your data into napari, first check the [napari hub](https://www.napari-hub.org/) to 
see if there's a plugin to help. If that fails, go ahead and ask the nice people at the 
[image.sc](https://forum.image.sc/tag/napari) forum to see if anybody can help.
:::

## Starting the plugin

Click `Plugins` at the top of the main napari window, and then click `brainreg-register: Atlas registration`. A new 
docked widget will appear in your napari window.

## Setting up registration

Choose the napari image layer you wish to be registered from `Image layer`, along with the atlas you want to use from 
`Atlas`. You must also set the voxel sizes in the axial (z) and in-plane (x, y) dimensions, along with the data 
orientation. The orientation is defined by three letters, based on [bg-space](https://github.com/brainglobe/bg-space), 
e.g. `psl`. For more details on this, see the outline 
[here](https://docs.brainglobe.info/cellfinder/image-orientation#orientation). Lastly, set an `Output directory` 
(where you want to save the data).

:::{caution}
Make sure that the image layer you are registering is not selected in the list of napari image layers on the left-hand 
side. Any images that are selected will also be registered along with the image layer chosen in `Image layer`.
:::

## Setting additional parameters
There are many parameters that can be set to improve registration performance. For more details on these, see 
the documentation [here](./parameters).

## Running brainreg

You can then click `Run`, and the registration will start. Lots of stuff will get printed to the console as 
brainreg runs, and when it's done (it should only take a minute or so), you will see something like:

```
INFO - MainProcess cli.py:230 - Finished. Total time taken: 0:00:29.15
```

This means that the registration is complete, but you should see the results appear in the napari window.

Once the registration is complete, some new image layers will appear:

* Atlas annotations - this the annotations image from the atlas (where each brain region has a unique value) warped to the data
* Boundary image - this is a binary image, showing the boundaries between atlas regions.

These files are not the only ones created; they will all be saved in the output directory. 
These can be loaded into napari at any time, see the [main visualisation page](visualisation). 
For more details of the output files created, please see [output files](output-files).
