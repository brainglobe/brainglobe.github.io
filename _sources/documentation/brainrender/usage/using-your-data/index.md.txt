# Using your own data in brainrender

brainrender provides the [`Actor`](../actors) class for many commonly-used data types. However, before you can use 
brainrender to visualize your data, you'll have to load and process them to put them into a format that 
brainrender accepts. These are the main steps you'll have to undertake to visualize your data.

:::{hint}
If your data is saved as mesh data in a .obj, you don't need to do anything  (provided your data are registered to 
the atlases)! `Scene.add()` accepts paths to files and takes care of loading/rendering them.
:::

You can find a lot of examples in the [brainrender GitHub repository](https://github.com/brainglobe/brainrender/tree/master/examples), 
some of these are focused on showing how to load and use your data in brainrender.  Head there for more details. 


## Registering your data

In order to visualize your data in brainrender, it has to be in register with the axes system in brainrender. If 
you used tools like [brainreg](/documentation/brainreg/index) your data will already be registered, and you can skip 
this step. If not, you will have to transform your data so that its axes match brainrender's.  
BrainGlobe includes [brainglobe-space](/documentation/brainglobe-space/index), software that aims at facilitating the operation of 
swapping axes around, which can get confusing rapidly otherwise. 

Check [Registering data](registering-data) for more details.

## Cell coordinates
If you have cells coordinates (or the coordinates of any other set of points in the brain) saved in a file 
(e.g. as .csv), you can use many popular python packages for loading them as python arrays. These include 
pandas for `.csv` and `.h5` files, numpy for `.npy` etc.

## Neuron morphology

Neuron morphologies are generally saved as `.swc` files. Brainrender's `Neuron` class can load morphology data 
directly from this file format, but head to [morphapi](/documentation/morphapi/index) for more details about to load 
and process neuron morphology data.

## Image data

### Loading the data

Given the popularity of python for scientific research, there are tools to load almost all data formats. These include 
numpy to load `.npy` files,  `tiffiles` for `.tiff` etc. BrainGlobe provides a general purpose software tool for 
loading and saving image data ([image_io](/documentation/brainglobe-utils/image_io)). You can use `image_io` to load most types of 
data (e.g.  `.nrrd`, `.tiff`, `.nifti` etc), e.g.:

```python
from brainglobe_utils.image_io import load
load.load_any('mydata.tif')
```

:::tip
If your data are saved as a `.npy` file,  brainrender's `Volume` actor can load the file directly:
:::

```python
from brainrender.actors import Volume
import numpy as np
vol = Volume(np.load('data.npy')) #  this will work
vol = Volume('data.npy')  # this will work too :)
```

### volume -> surface

If your data is as volumetric (3D voxels) image,  you might want to extract mesh information from your data. 
If that's the case, `vedo` provides code to go from volumes to meshes:

```python
from vedo import Volume
from brainrender import Scene

vol = Volume(mydata)
mesh = vol.isosurface()

scene = Scene()
scene.add(mesh)
```

Vedo provides many more methods to go from volume to mesh and vice versa: check 
[its awesome documentation ](https://vedo.embl.es) for more details.

:::{hint}
Brainrender's Volume actor class has access to all methods of Vedo's Volume class, so this would work too:
:::

```python
from brainrender.actors import Volume
mesh = Volume('data.npy').isosurface()
```

You can also render your data directly as a brainrender `Volume` class: 

```python
from brainrender import Scene, actors
scene = Scene()
scene.add(actors.Volume(mydata))
```

## Streamlines

Brainrender can create streamlines visualizations for connectomics data. Data for streamlines can be saved as 
`.json` and loaded with pandas `read_json` function. Data should be organized in a hierarchical structure with two 
main entries (`points` and `lines`) denoting the injection points and the coordinates of points along each "line" of 
the streamlines.  Each line should be a list of dictionaries with "x", "y" and "z" coordinates.

## Supported data types

| Data type | Actor | Accepted data format | File formats |  |
| :--- | :--- | :--- | :--- | :--- |
| Cell coordinates | Point, Points | numpy array | **.npy**, .h5 |  |
| Neuron morphology | Neuron | Mesh, morphapi.Neuron | **.swc** |  |
| Image \(3D\) | Volume,  Actor | numpy array | .**npy**,  .tiff |  |
| Streamlines | Streamlines | pandas DataFrame | .**json**, .h5 |  |

**Accepted data format:** the `Actor` classes for the data type expect the data in specific formats, this column
illustrates what they expect.

**File formats:** example file formats that data can be stored in. When bold it means that the class can load the data
from files directly. 



```{toctree}
:maxdepth: 1
:hidden:
registering-data
```