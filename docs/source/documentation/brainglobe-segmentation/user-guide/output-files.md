# Output files

## 1D segmentation
all files will be saved in `reg_result_path/segmentation/atlas_space/tracks` if you loaded the data from atlas space, otherwise, it will be in the folder of `sample_space`.

three files will be saved for each 1D tracks:
+ `xxx.csv` a csv table that summrize the depth, brain area, brain region ID (based on allen atlas) for each point of the fitted spline. [example](https://github.com/brainglobe/brainglobe-segmentation/blob/main/tests/data/brainreg_output/segmentation/atlas_space/tracks/test_track.csv). 
+ `xxx.npy` a n-col numpy array that saved the coordination(as index in 3D volume space) for each point of the fitted spline. This array can be imported to [brainrender](https://github.com/brainglobe/brainrender) for visualization. [example](https://github.com/brainglobe/brainglobe-segmentation/blob/main/tests/data/brainreg_output/segmentation/atlas_space/tracks/test_track.npy) This file will be saved after you click the `to brainrender` button.
+ `xxx.points` a n-col [panda HDF5 dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_hdf.html) that saved the coordination(as index in 3D volume space) for each point that user manually labled to create the track. [example](https://github.com/brainglobe/brainglobe-segmentation/blob/main/tests/data/brainreg_output/segmentation/atlas_space/tracks/test_track.points)

## 2D segmentation