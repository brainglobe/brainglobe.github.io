# Actors

Everything rendered in `brainrender` is first used to create an instance of `brainrender`'s `Actor` class. This 
class handles the 3D mesh data for the object to be rendered and provides a few useful methods for the 
behind-the-scenes work necessary to render your data.

:::{caution}
Before rendering data in brainrender you should ensure that they are registered to  a reference atlas. Check 
how [to use your data in brainrender.](using-your-data/index)
:::

While a general `Actor` class can be used to render any type of data that can be used to create a 
[`vedo Mesh`](https://vedo.embl.es/) object, several specific `Actor` classes are provided for more conveniently 
loading commonly used data types.

## Specific actor classes
* `brainrender.actors.Neuron` is used to render neurons morphology (e.g. downloaded with 
`morphapi` or from a `.swc` file).
* `brainrender.actors.Points` is used to render anything that can be represented as a set of points 
(e.g. labelled cells from `cellfinder`. `Points` can load data directly from a `.npy` file or a numpy array of 
coordinates can be passed to it.
* `brainrender.actors.Streamlines` is used to render streamlines tractography data. It expects the data as a 
`pandas` DataFrame and can load data from a `.json` file.
* `brainrender.actors.Line` is used to render a line. It expects a (N, 3) numpy array of coordinates.
* `brainrender.actors.Volume` renders volumetric data (e.g. gene expression) from a numpy array or from a `.npy` file.
* Other actor classes like `Cylinder`, `Point` and `Ruler` can be used to render other types of data.

In all cases an `actor` instance can be created by passing the data to be rendered to the dedicated `Actor` class. 
For instance, to render the position of labelled cells, a Nx3 numpy array with the cells coordinates has to be passed 
to the `Points` class to create an actor representing the cells' locations. Some actors can also load data directly 
from file.

:::{hint}
Some types of actors (e.g. `Streamlines` and `Neuron)` are generally used to visualize several instances of the 
same neuron at once. For these actors we also provide helper functions that facilitate the generation of multiple 
instances of the same actor class. 
:::

## Visualizing other types of data

While the provided `Actor` classes should support the vast majority of users' needs, occasionally you might need 
to render an unsupported type of data. See [here](using-your-data/index) for details.


## Adding actors to your scene

Rendering actors is as simple as can be: just use the `Scene.add` method and pass to it the actors you would like 
to see added to your rendering. 

