# Python API

## Creating a `BrainGlobeAtlas` object

To instantiate a `BrainGlobeAtlas` object, we need to instantiate it with the atlas name. The first time we use it, a 
version of this atlas files will be downloaded from the [remote GIN repository](http://gin.g-node.org/brainglobe/atlases) 
and stored on your local machine (by default, in `~/.brainglobe`):

```python
from brainglobe_atlasapi import BrainGlobeAtlas
from pprint import pprint

bg_atlas = BrainGlobeAtlas("allen_mouse_100um", check_latest=False)
```

To know what atlases are available through BrainGlobe, we can use the `show_atlases` function
(requires an internet connection):

```python
from brainglobe_atlasapi import show_atlases
show_atlases()
```

## Using the atlas

A BrainGlobe atlas is a convenient API for interacting with an anatomical atlas. BrainGlobe atlases contain:

* Metadata
* Reference anatomical stack
* Region annotation stack
* Hemisphere annotation stack
* Description of the region hierarchy
* Meshes for the regions

### Metadata

All atlases have a standard set of metatata describing their source, species, resolution, etc:

```python
bg_atlas.metadata
```

### Anatomical, annotation and hemispheres stack

```python
from matplotlib import pyplot as plt
```

Anatomical reference:

```python
stack = bg_atlas.reference
```

Annotations stack:

```python
stack = bg_atlas.annotation
```

Hemisheres stack:

```python
stack = bg_atlas.hemispheres
```

### Regions hierarchy

The atlas comes with the description of a hierarchy of brain structures. To have an overview:

bg\_atlas.structures

The structures attribute is a custom dictionary that can be queried by region number or acronym, and contains all the information for a given structure:

```python
bg_atlas.structures["root"]
```

In particular, the `structure_id_path` key contains a list description of the path in the hierarchy up to a particular region, and can be used for queries on the hierarchy.

```python
bg_atlas.structures["CH"]["structure_id_path"]
```

We can use the `bg_atlas.get_structure_descendants` and `bg_atlas.get_structure_ancestors` methods to explore the hierarchy:

```python
bg_atlas.get_structure_descendants("VISC")
```

```python
bg_atlas.get_structure_ancestors("VISC6a")
```

**NOTE**: the levels of the hierarchy depend on the underlying atlas, so we cannot ensure the goodness and consistency of their hierarchy three.

There is a higher level description of the structures hierarchy that is built using the 
[treelib](https://treelib.readthedocs.io/en/latest/) package, and is available as:

```python
bg_atlas.structures.tree
```

For most applications, though, the methods described above and the list path of each region should be enough to query 
the hierarchy without additional layers of complication.

### Region masks

Sometimes, we might want to have the mask for a region that is not labelled in the annotation stack as all its voxels 
have the number of some lower level parcellation in the hierarchy (concretely, if the brain is divided in hindbrain, 
midbrain, and forebrain, `annotation == root_id` will be all False).

To get the mask for a region, simply type:

```python
stack = bg_atlas.get_structure_mask(997)
```

### Regions meshes

If we need to access the structure meshes, we can either query for the file (e.g., if we need to load the file 
through some library like `vedo`):

```python
bg_atlas.meshfile_from_structure("CH")
```

Or directly obtain the mesh, as a mesh object of the `meshio` library:

```python
bg_atlas.mesh_from_structure("CH")
```

## Query the atlas

### Query for structures

A very convenient feature of the `BrainGlobeAtlas` API is the simplicity of querying for the identity of the 
structure or the hemisphere at a given location, either from stack indexes or space coordinates, and even cutting 
the hierarchy at some higher level:

```python
# Ask for identity of some indexes in the stack:
bg_atlas.structure_from_coords((50, 40, 30), as_acronym=True)

# Now give coordinates in microns:
bg_atlas.structure_from_coords((5000, 4000, 3000), as_acronym=True, 
                               microns=True)

# Now cut hierarchy at some level:
bg_atlas.structure_from_coords((5000, 4000, 3000), as_acronym=True,
                               microns=True,  hierarchy_lev=2)
```

### Query for hemispheres

A very similar method can be used for hemispheres. 0 correspond to outside the brain, and 1 and 2 to left and right 
hemispheres, but we can just ask for the side name instead of the number:

```python
# Ask for identity of some indexes in the stack:
bg_atlas.hemisphere_from_coords((50, 40, 30))

# Now give coordinates in microns
bg_atlas.hemisphere_from_coords((5000, 4000, 3000), microns=True)

# Now print side string
bg_atlas.hemisphere_from_coords((5000, 4000, 3000), microns=True)
```

