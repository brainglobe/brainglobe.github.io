# Registering a whole-brain dataset to the Allen Mouse Brain atlas with brainreg


```{hint}
For full information on how to use brainreg, please see the [brainreg page](/documentation/brainreg/index)
```

## Setting up
To test out brainreg, we supply a small mouse brain dataset to get you started. To begin:
* Download the data from [here](https://gin.g-node.org/cellfinder/data/raw/master/brainreg/test\_brain.zip) (the dataset is \~10MB, so it should download quickly).
* Unzip the data to a directory of your choice (doesn't matter where). You should end up with a directory called `test_brain` with 270 `.tif` images

To run brainreg, you need to know:
* Where your data is (in this case, it's the path to the `test_brain` directory)
* Where you want to save the output data (we'll just save it into a directory called `brainreg_output`in the same directory as the `test_brain`)
* The pixel sizes of your data in microns (see [Image definition](/documentation/general/image-definition) for details). 
In this case, our data is 40&mu;m per pixel in the coronal plane, and the spacing of the planes is 50&mu;m.
* The orientation of your data. The software needs to know how you acquired your data (coronal, sagittal etc.). For this 
BrainGlobe uses [bg-space](/documentation/bg-space/index). For this tutorial, the orientation is `psl`, which means 
that the data origin is the most **p**osterior, **s**uperior, **l**eft voxel. For more details see 
[Image definition](/documentation/general/image-definition)
* Which atlas you want to use (the list of available atlases is available [here](/documentation/bg-atlasapi/usage/atlas-details)). 
In this case, we want to use a mouse atlas (as that's what our data is), and we'll use the 50&mu;m version of the [Allen Mouse Brain Atlas](https://mouse.brain-map.org/static/atlas)

:::{hint}
In this tutorial we will use the 50&mu;m version of the [Allen Mouse Brain Atlas](https://mouse.brain-map.org/static/atlas). 
Low-resolution atlases like this are usually only used for testing (the registration will work much quicker at lower resolution).
 In this case, the test input data is very low resolution, so using a higher resolution atlas doesn't make much sense.

When using your own data, you'll probably find that higher resolution atlases provide better results. 
Make sure to test out the different resolutions to see what works best.
:::

## Running the registration
There are two ways to run the registration using brainreg. 
If you're just getting started, we recommend the [napari](https://napari.org/stable) plugin. 
This provides a graphical user interface, and makes it easier to tweak parameters.

If you need to run brainreg on many samples, or on a remote machine 
(e.g., using an institutional high-performance computing system), there is a command-line interface. 

Whichever interface you use, the results will be identical.

:::{admonition} Registration using the napari plugin
:class: dropdown
## Before you start
* [Make sure you have napari installed](https://napari.org/stable/tutorials/fundamentals/installation.html)
* Install the brainreg-napari plugin from within napari (`Plugins` -> `Install/Uninstall Package(s)`, choosing `brainreg-napari`).)
* Open napari

## Run brainreg
To run brainreg, we firstly need to load the data, by dragging and dropping the `test_brain` directory into the main 
napari window. Then load the plugin by selecting `brainreg-register: Atlas registration` from the napari `Plugins` menu.

In the plugin, set all the necessary parameters:

* `Image layer` - Set this to the `test_brain` image layer
* `Atlas` - Set this to `allen_mouse_50um`
* `Data orientation` - Set this to `psl`
* `Voxel size (z)` - Set to 50
* `Voxel size (x)` - Set to 40
* `Voxel size (y)` - Set to 40
* `Output directory` - Click `Choose directory`, and create a new directory in the same directory as 
* `test_brain` called `brainreg_output`

Make sure the image layer is deselected on the left-hand side, and then you should see something like this 
(N.B. the visualised plane and the contrast of the brain has been adjusted):

![brainreg-napari](images/brainreg-napari.webp)

You can then click `Run`, and the registration will start. Lots of stuff will get printed to the 
console as brainreg runs, and when it's done (it should only take a minute or so), you will see something like:

```
INFO - MainProcess cli.py:230 - Finished. Total time taken: 0:00:29.15
```

This means that the registration is complete, but the results will appear in the napari window. 
Toggling the visibility of the `Boundaries` layer (click the eye icon) is the easiest way to assess registration accuracy.
:::

:::{admonition} Registration using the command line tool
:class: dropdown
## Instructions:

### Setting up

* Open a terminal (Linux/macOS) or your command prompt (Windows)
* Activate your [conda environment](/documentation/general/conda)

### Run brainreg
To run brainreg, you need to pass:
* The path to the sample data
* The path to the directory to save the results
* The voxel sizes
* The orientation
* The atlas to use

We put this all together in a single command:

```
brainreg test_brain brainreg_output -v 50 40 40  --orientation psl --atlas allen_mouse_50um
```

Lots of output will get printed to the console as brainreg runs, and when it's done (it should only take a minute or 
so), you will see something like:

```
INFO - MainProcess cli.py:230 - Finished. Total time taken: 0:00:29.15
```

This means that the registration is complete.

### Visualising the results

brainreg comes with a plugin for [napari](https://napari.org/) (see 
[Visualisation](/documentation/brainreg/user-guide/visualisation.md)) for easy visualisation of the results.

To view your data, run `napari` from the same terminal/command as you ran brainreg (or open a new one and activate 
your conda environment). You can then drag and drop the `brainreg_output` directory into napari, and see the results.
:::

:::{note}
The results are likely not perfect because (for speed and simplicity) we:

* Used very low-resolution data
* Use a low-resolution atlas
* Left all the parameters as default (which were optimised for higher resolution atlases)
:::
