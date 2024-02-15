# Adding a new atlas

## How are BrainGlobe atlases distributed?

BrainGlobe atlases are downloaded locally to the user’s machine whenever they try to use an atlas that has not yet been 
downloaded.
By default, they will end up in the `~/.brainglobe` folder,
unless differently specified in the `bg-atlasapi` configuration.

The BrainGlobeAtlas class fetches those atlases from a dedicated GIN repository
([https://gin.g-node.org/brainglobe/atlases](https://gin.g-node.org/brainglobe/atlases)). GIN repos are very similar 
to GitHub repos, but support storage of large datasets, using git-annex.
Only members of the BrainGlobe initiative can upload new atlases to the GIN repo,
and this is essential to ensure the interoperability of all atlases that are part of the BrainGlobe suite.
Still, we want to keep the process open to external contribution,
and we tried to streamline the process for people who want to expand the list of BrainGlobe supported atlases.
Here’s some information on how the process works, and how you can contribute a new atlas to the initiative:

The repository of atlases is automatically updated by scripts that reformat atlas data, create a bundled atlas archive 
and upload them. This process will be run every time a new atlas is added or an old atlas is updated. Each atlas is 
generated in a separate script, so if you want to contribute with a new atlas:

* Fork [github.com/brainglobe/bg-atlasgen](https://github.com/brainglobe/bg-atlasgen)
* Create an atlas generation script in the `atlas_scripts` directory (see below)
* Submit a pull request back to the original repository.

If you are new to GitHub, or you have any questions about writing your script, feel free to reach out via a 
[GitHub issue](https://github.com/brainglobe/bg-atlasgen/issues) or by starting a discussion using the 
[BrainGlobe tag over at the image.sc forum](https://forum.image.sc/tag/brainglobe) and we’ll be very happy to provide 
you with all the assistance you need to contribute to the project!

## What data do you need to contribute an atlas to the BrainGlobe Initiative?

To contribute your favourite atlas in a BrainGlobe-compatible format, these are the fundamental ingredients you’ll 
need to have before starting:

* Information to credit the atlas: a publication, if available, and a website of the atlas, if available.
* A reference 3D stack in your favorite format, as long as you can load it to a numpy array. This will be the reference 
stack, used to represent the anatomy of the brain. If you have more than one reference brain (e.g., multiple transgenic 
lines that people can use for registrations), don’t worry: just choose the most important one, and the others can be 
distributed via BrainGlobe as well.
* An annotation 3D stack that contains 0s in all non-annotated voxels, and integer numbers that correspond to the ids 
of all the different regions. IDs should refer to the finest level of your region hierarchy. For example, in a brain 
where the telecephalon has ID 1, the cortex ID 2, and the visual cortex ID 3, a voxel in the visual cortex should just 
have 3. The BrainGlobe Atlas API will know how to take care of pooling all voxels that belong to the cortex using the 
annotation and the region hierarchy information (more on that later).
* A description of all the structures of the brain and their hierarchy. This represented in BrainGlobe with a list of 
dictionaries where each dictionary describes a region with the following keys:

```
STRUCTURE_TEMPLATE = {
   "acronym": "VIS",  # shortened name of the region
   "id": 3,  # region id
   "name": "visual cortex",  # full region name
   "structure_id_path": [1, 2, 3],  # path to the structure in the structures hierarchy, up to current id
   "rgb_triplet": [255, 255, 255],  # default color for visualizing the region, feel free to leave white or randomize it
}
```

The `structure_id_path` is the fundamental key argument for bg-atlasapi to understand the hierarchy of your regions. 
Going back to our example above, if telencephalon is 1, cortex 2, and visual cortex 3, `structure_id_path` for the 
cortex region will be \[1, 2], and for the visual cortex region will be \[1, 2, 3]. you don’t necessarily need a fixed 
number of levels in your hierarchy. You should just make sure that there is one and only one root region (i.e., a region 
with `structure_id_path` of length 1). If your atlas does not have a multilevel hierarchy, just create a root region 
that all other regions are children of. How to generate the region hierarchy is up to you; just make sure you have a 
way of generating this list of dictionaries in python when you’ll start creating the atlas.

:::{caution}
Do not use 0 (zero) as the id of a structure, because the annotation stack will contain zeros where no structure is defined!
:::

## How to generate an atlas programmatically?

**Atlas generation takes place in two steps:**

1. Generate an “Atlas script” written in python
2. Use the atlas generation code [available from BrainGlobe](https://github.com/brainglobe/bg-atlasgen/tree/main/bg\_atlasgen) 
3. to generate the atlas from the atlas script.

### Atlas scripts

**Each atlas to be generated has a dedicated atlas script. This has two main functions:**&#x20;

1. To set important atlas metadata (e.g., name, resolution..) and&#x20;

2. To load the atlas data (e.g. reference image).


**The metadata that needs to be specified in the atlas script is:**

* RES\_UM: resolution of the atlas in micrometers (voxel spacing)
* ATLAS\_NAME: the name
* SPECIES: e.g. “Mus musculus”
* ATLAS\_LINK: a link to a website describing the atlas or any other relevant online resource
* CITATION: the details of a published paper/preprint in which the atlas was first described
* ATLAS\_PACKAGER: contact (name / email) of the person who packaged the atlas in BrainGlobe
* ORIENTATION: a string specifying the orientation in bg-space format
* \_\_version\_\_: the version number of the atlas: when atlases get updated/modified new versions are released.
* root structure id: ID of the root (base) brain region in the hierarchy of brain regions.

This metadata is used to provide information about the atlas (e.g., which species is it about), to give credit to the 
original creators of the atlas data and to provide data used by other BrainGlobe tools (e.g., the atlas orientation).


**In addition to laying out the metadata, atlas scripts are being used to load (or download) the actual atlas data:**

* Template image volume: a 3D image with the atlas’ template
* Annotated image volume: a 3D image where each voxel is annotated with the ID of the atlas brain region at that point
* hemispheres stack (optional): a 3D image where each voxel is annotated with the ID of the hemisphere it belongs to
* Structures list: a list of brain regions (structures) names
* Meshes dict: a dictionary with entries of the type structure->file path specifying the path to the .obj mesh file 
of each brain region

### Atlas generation
Once an atlas script has been written which sets out all the necessary metadata and loads all the files required, 
code provided by BrainGlobe’s atlas generation repository can be used to format the data as needed by the BrainGlobe 
AtlasAPI. Atlasgen provides one convenient function `wrapup_atlas_from_data`  which takes all the metadata and data 
from above and creates the data structures required. These data structures include .tiff files with the various images, 
csv files with the structures metadata information, a README file laying out the atlas content, etc. The same function 
creates a compressed folder which can be loaded to GIN for distribution (see above).

### Extracting meshes
While most atlases will have a set of 3D images that can be used as annotated and template stacks,
not all atlases will have mesh (.obj) files for each brain region in the atlas.
However, regions’ meshes are used frequently by BrainGlobe tools,
especially in `brainrender` for visualizing anatomical data in 3D.
For this reason,
the atlas generation code from BrainGlobe provides functionality that can be used to generate such mesh files.
A mask image is created which only contains the annotation for the brain region of interest,
and a marching cubes algorithm is used to identify the surface of the region;
 finally, a mesh is created from the output of the marching cubes algorithm, and the results are saved to a .obj file.
Repeating the process for each region in the atlas, it is possible to easily create all the necessary meshes.

### How can I be sure I get credited for the atlas I contributed?
Included with the atlas metadata, which is specified during atlas creation (see above), is a link to any online 
resource describing the atlas and to a publication associated with the atlas.

This ensures that information about the original creators of the atlas data accompanies the atlas data at all time, 
so that credit can easily be given to the atlas creators.

Sometimes, the atlas creator and the person contributing the atlas to BrainGlobe (i.e., going through the atlas 
generation process laid out here) may not be the same. The `ATLAS_PACKAGER` argument in the metadata allow 
specifying the name and contact of the person who curated the BrainGlobe atlas creation.

### Inspecting results
To check if everything went smoothly,
you can just go to the folder with the atlas content
(named `atlasname_resolutionum` in the directory you were generating the atlas in) and check out its content.&#x20;

For the metadata, you can just open the json file and inspect it.

To inspect the reference.tiff file and the annotation.tiff file, you can just drag and drop them in napari 
(to install napari, see [here](https://napari.org/stable/tutorials/fundamentals/installation)), 
and they will open as an image layer, and a label layer, respectively. You know the orientation is correct if you are 
looking at upright (dorsal top, ventral bottom) frontal sections, and when you scroll the slider to inspect sections 
with a higher index, you are moving from anterior to posterior.

To inspect the meshes, BrainGlobe provides a simple tool
load and visualize a set of .obj files for quick inspection, e.g.:

```python
from bg_atlasgen.mesh_utils import inspect_meshes_folder

inspect_meshes_folder("~/.brainglobe/temp/allen_mouse_10um_v1.0/meshes")
```


Once an atlas is created with BrainGlobe’s atlas generation tools, 
it can be used with most software from the BrainGlobe software suite, including [brainrender](/documentation/brainrender/index) 
which provides a convenient GUI for visually inspecting the generated atlas meshes.

## Uploading the atlas

After the pull request is merged, one of the BrainGlobe core developers will run the script and upload the packaged 
atlas (`.tar.gz` archive) to [the GIN repository](https://gin.g-node.org/BrainGlobe/atlases). The 
[`latest_versions.conf`](https://gin.g-node.org/BrainGlobe/atlases/src/master/last_versions.conf) file will also be 
updated to include the new atlas. At this point, the atlas will be available for use in the API.

## Updating an existing atlas
To update an existing atlas, a pull request must be raised to change the existing script. Once this pull request is 
merged, the new atlas will be generated and uploaded to the GIN repository as normal. The 
[`latest_versions.conf`](https://gin.g-node.org/BrainGlobe/atlases/src/master/last_versions.conf) can then be updated 
to reflect the latest version. 