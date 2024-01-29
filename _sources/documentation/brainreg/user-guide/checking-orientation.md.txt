# Checking orientation

To ensure that the orientation is set correctly, `napari-brainreg` comes with a tool to interactively check the input 
orientation (thanks to [Jules Scholler](https://github.com/JulesScholler)!).

Once you've loaded your data, fill in the input orientation in the GUI based on the 
[brainglobe-space definition](/documentation/setting-up/image-definition) and click `Check orientation`. 
This will generate a number of new images that are displayed to the user. The top row of displayed images are the 
projections of the reference atlas. The bottom row are the projections of the aligned input data. If the two rows are 
similarly oriented, the orientation is correct. If not, change the orientation and try again.

## Incorrect orientation
Top is the reference atlas, averaged for all directions and bottom is the aligned input data with wrong input
![incorrect-orientation](../images/incorrect_orientation.png)

## Correct orientation
Top is the reference atlas, averaged for all directions and bottom is the aligned input data with correct input
![correct-orientation](../images/correct_orientation.png)
