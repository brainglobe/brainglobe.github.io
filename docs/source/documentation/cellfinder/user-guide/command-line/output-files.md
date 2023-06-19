# Output files

When you run cellfinder, depending on the options chosen, a number of files will be created. These may be useful for 
custom analyses (i.e. analysis not currently performed by cellfinder itself). The file descriptions are 
ordered by the subdirectory that they are found in, within the main cellfinder output directory.

## Analysis

* `summary.csv` - This file lists, for each brain area, the number of cells detected, the volume of the brain area, 
* and the density of cells (in cells per mm<sup>3</sup>).
* `all_points.csv` - This file lists every detected cell, and it's coordinate in both the raw data and atlas spaces, 
* along with the brain structure it is found in.

## Figures

* `heatmap.tiff` - This is a heatmap (in the coordinate space of the downsampled, reoriented data) representing cell 
* densities across the brain.

## Points

* `cells.xml` - Cell candidate positions in the coordinate space of the raw data
* `cell_classification.xml` - Same as `cells.xml`, but after classification (i.e., each cell candidate has a 
* cell/no_cell label)
* `downsampled.points` - Detected cell coordinates, in the coordinate space of the raw data, but downsampled and 
* reoriented to match the atlas (but not yet warped to the atlas). This can be loaded with `pandas.read_hdf()`
* `atlas.points` - As above, but warped to the atlas. This can be loaded with `pandas.read_hdf()`
* `points.npy` - Cell coordinates, transformed into atlas space, for visualisation using 
* [brainrender](https://github.com/brainglobe/brainrender)
* `abc4d.npy` - Exported file for use with [abc4d](https://github.com/valeriabonapersona/abc4d)

## Registration

The registration directory is simply a brainreg output directory. To understand these files, please see the 
[brainreg output files](/documentation/brainreg/user-guide/output-files/) page.


Two other files are also saved, `cellfinder.json` and `cellfinder_DATE_TIME.log`. These files contain information 
about how cellfinder was run, and are useful for troubleshooting and debugging. If you ask for help (e.g. 
on the [image.sc. forum](https://forum.image.sc/tag/brainglobe)), we may ask you to send the log file.

