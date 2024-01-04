# Output files

brainreg will create a number of output files. Many of these are for use with other software (e.g., brainglobe-segmentation 
and cellfinder), but they may be useful for your own software.

:::{note}
N.B. This is not an exhaustive list, as brainreg has many options which may create additional files.
:::

* `boundaries.tiff` - A 3D tiff image of the atlas boundaries, transformed to the space of the raw data.
* `brainreg_DATE_TIME.log` - A log file detailing the registration process. Useful for debugging and raising issues.
* `brainreg.json` - A record of all the input parameters, used by other software, e.g. brainglobe-segmentation.
* `deformation_field_0.tiff` - A 3D tiff describing the deformation from raw data space to atlas space, in the first 
dimension (based on the supplied orientation and voxel sizes).
* `deformation_field_1.tiff` - Deformation in the second dimension.
* `deformation_field_2.tiff` - Deformation in the third dimension.
* `downsampled.tiff` - The raw data, reoriented to the atlas orientation, and downsampled to the atlas resolution.
* `downsampled_standard_IMAGE_NAME.tiff` - The raw data, transformed to the atlas (standard) space.
* `registered_atlas.tiff` - The atlas annotations image, warped to the raw data space. N.B. This is the reoriented, 
downsampled space of `downsampled.tiff.`
* `registered_hemispheres.tiff` - Same as `downsampled_atlas.tiff` but for the image coding the hemispheres.
* `volumes.csv` A CSV file outlining the volumes of each brain area, based on the atlas registration.

Some other files may also be created:

* `downsampled_IMAGE_NAME.tiff` - Similar to `downsampled.tiff` but additional image channels, processed when using the `-d` flag.
* `niftyreg` This directory contains the intermediate files used by the niftyreg registration. Created when using the `--debug` flag.
* `registered_atlas_original_orientation.tiff`Same as `registered_atlas.tiff`, but without the reorientation to the 
atlas orientation. Created when using the `--save-original-orientation` flag.
