"""
BrainGlobe Atlas API
====================
Using the BrainGlobe Atlas API to fetch and inspect an atlas
"""


# %%
# Import the Atlas API and find an atlas
# --------------------------------------

# %%
# Import the API and some other tools

from brainglobe_atlasapi import BrainGlobeAtlas
from pprint import pprint # to format printed data nicely
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

# %%
# To know what atlases are available through BrainGlobe, we can use the `show_atlases` function
# (requires an internet connection):

from brainglobe_atlasapi import show_atlases
show_atlases()

# %%
# Creating a `BrainGlobeAtlas` object
# -----------------------------------
# To instantiate a `BrainGlobeAtlas` object, we need to instantiate it with the atlas name. The first time we use it, a
# version of this atlas files will be downloaded from the `remote GIN repository <http://gin.g-node.org/brainglobe/atlases>`_
# and stored on your local machine (by default, in `~/.brainglobe`):

atlas = BrainGlobeAtlas("allen_mouse_100um", check_latest=False)

# %%
# .. admonition:: Atlas quality
#   :class: note
#
#   Usually BrainGlobe only packages existing atlases. The quality of the underlying images and atlas ontology
#   relies on the original atlas data, and this can vary considerably. In this example, we choose the "allen_mouse_100um"
#   atlas, as it is relatively small, but high quality.




# %%
# Using the atlas
# ---------------
# A BrainGlobe atlas is a convenient API for interacting with an anatomical atlas. BrainGlobe atlases contain:
#
# * Metadata
# * Reference anatomical stack
# * Region annotation stack
# * Hemisphere annotation stack
# * Description of the region hierarchy
# * Meshes for the regions

# %%
# Metadata
# --------
# All atlases have a standard set of metatata describing their source, species, resolution, etc:

metadata = atlas.metadata
pprint(metadata)

# %%
# Anatomical, annotation and hemispheres stacks
# ---------------------------------------------

# %%
# Anatomical reference (or template) image:

reference = atlas.reference

# Get the middle section and plot
middle_section = reference.shape[0] // 2

plt.imshow(reference[middle_section,:,:], cmap='gray')

# %%
# Annotations stack
annotation = atlas.annotation

# Create a cyclic colormap due to the high values in the Allen atlas
N = 512
colors = cm.get_cmap('tab20', N)
lut = colors(np.arange(N))

# Map label image to lookup table and plot
plt.imshow(lut[annotation[middle_section,:,:] % N])


# %%
# Hemisheres stack:

hemispheres = atlas.hemispheres
plt.imshow(hemispheres[middle_section,:,:])

# %%
# Regions hierarchy
# -----------------

# %%
# The atlas comes with the description of a hierarchy of brain structures. To see an overview:

print(atlas.structures)

# %%
# The structures attribute is a custom dictionary that can be queried by region number or acronym, and contains all the information for a given structure:

pprint(atlas.structures["root"])

# %%
# In particular, the `structure_id_path` key contains a list description of the path in the hierarchy up to a particular region, and can be used for queries on the hierarchy.

print(atlas.structures["CH"]["structure_id_path"])

# %%
# We can use the `atlas.get_structure_descendants` and `atlas.get_structure_ancestors` methods to explore the hierarchy:

atlas.get_structure_descendants("VISC")

# %%
atlas.get_structure_ancestors("VISC6a")


# %%
# Region masks
# ------------
#
# Sometimes, we might want to have the mask for a region that is not labelled in the annotation stack as all its voxels
# have the number of some lower level parcellation in the hierarchy (concretely, if the brain is divided in hindbrain,
# midbrain, and forebrain, `annotation == root_id` will be all False).
#
# To get the mask for a region, use

mask = atlas.get_structure_mask(997)
plt.imshow(mask[middle_section,:,:], cmap="gray")

# %%
# Region meshes
# -------------

# %%
# To access the 3D structure mesh for visualisation, this can be queried using the region ID or abbreviation. A `meshio.Mesh` object is returned.

print(atlas.mesh_from_structure("CH"))

# %%
# A list of regions can also be queried:

pprint(atlas.mesh_from_structure(["CH", "VISp"]))

# %%
# The path can also be queried directly, if it's needed to be used within another library

print(atlas.meshfile_from_structure("CH"))



# %%
# Querying the atlas
# ------------------
# A convenient feature of the `BrainGlobeAtlas` is being able to querying the identity of the
# structure at a given location, either from stack indexes or atlas coordinates.

# %%
# Ask for identity of some indexes in the stack:
print(atlas.structure_from_coords((50, 40, 30)))

# %%
# Now with coordinates in microns (and also returning the region acryonym):
print(atlas.structure_from_coords((5000, 4000, 3000), microns=True, as_acronym=True))

# %%
# Query at a specific level of the hierarchy:
print(atlas.structure_from_coords((5000, 4000, 3000), microns=True,  hierarchy_lev=2, as_acronym=True))


# %%
# Querying the hemisphere
# ------------------
# A very similar method can be used for hemispheres. 0 correspond to outside the brain, and 1 and 2 to left and right
# hemispheres, but we can ask for the hemisphere name instead of the number:

# %%
# Ask for the hemisphere of some indexes in the stack:
print(atlas.hemisphere_from_coords((50, 40, 30)))

# %%
# Now give coordinates in microns
print(atlas.hemisphere_from_coords((5000, 4000, 3000), microns=True))

# %%
# Now print hemisphere string
print(atlas.hemisphere_from_coords((5000, 4000, 3000), microns=True, as_string=True))
