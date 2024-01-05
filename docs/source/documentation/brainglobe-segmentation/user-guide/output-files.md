# Output files

## 1D segmentation
All files will be saved into your `brainreg` output directory (the one loaded by the plugin) at `/segmentation/atlas_space/tracks` if you loaded the data from atlas space, otherwise, it will be in the `sample_space folder.

Three files will be saved for each 1D track:
+ `xxx.csv` a csv table that summrize the depth, brain area, brain region ID (based on allen atlas) for each point of the fitted spline. [example](https://github.com/brainglobe/brainglobe-segmentation/blob/main/tests/data/brainreg_output/segmentation/atlas_space/tracks/test_track.csv). 
+ `xxx.npy` a n-col numpy array that saved the coordination(as index in 3D volume space) for each point of the fitted spline. This array can be imported to [brainrender](https://github.com/brainglobe/brainrender) for visualization. [example](https://github.com/brainglobe/brainglobe-segmentation/blob/main/tests/data/brainreg_output/segmentation/atlas_space/tracks/test_track.npy) This file will be saved after you click the `to brainrender` button.
+ `TRACK_NAME.points` - a [pandas HDF5 dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_hdf.html) containing the coordinates for each point used to create the track (e.g., from manual annotation).

## 2D segmentation