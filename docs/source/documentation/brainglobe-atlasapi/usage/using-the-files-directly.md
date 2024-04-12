# Using the files directly

Although the API should provide you with the tools you need to work with the atlas (and if they don't, please [raise an issue](https://github.com/brainglobe/brainglobe-atlasapi/issues)), you may wish to find the files themselves.

By default, atlases will be downloaded and saved into your home directory in a hidden directory (`~/.brainglobe`), with one directory per atlas e.g. `~/.brainglobe/allen_mouse_10um_v0.3`.

In each atlas directory, there will be the following subdirectories and files:

* `reference.tiff` The "template" brain image, i.e., a structural image of the brain \(or average of brains\) in which the annotations are defined
* `annotation.tiff` An image of the same shape as `reference.tiff` but in which each pixel value corresponds to a unique brain area. A pixel value of 0 typically refers to areas outside the brain
* `hemispheres.tiff` (optional) An image of the same shape as `reference.tiff` but in which each pixel value corresponds to either the left or right hemisphere. They are labeled 0 and 1 respectively
* `meshes` A directory of mesh files \(as `.obj`\) for each brain region, defined by the unique region ID
* `structures.json` A file describing the mapping of brain region ID to region name, and the hierarchy of brain structures
* `metadata.json` A file containing the atlas metadata, such as the shape of the images, the anatomical orientation, and the details of the source of the atlas
* `README.txt` A human-readable version of the metadata and brain region hierarchies
