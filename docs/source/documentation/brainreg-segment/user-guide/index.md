# Prerequisites

Your data must have been registered to an atlas using [brainreg](../../brainreg/index) (or the brainreg-based 
registration within [cellfinder](../../cellfinder/index)).

Please follow the instructions for these packages, and ensure that the channel that you want to segment is 
downsampled (e.g., using the `--downsample` flag in brainreg).

# Usage

To load the software, firstly open napari (typically by typing `napari` into your command window). You can then 
load `brainreg-segment` by navigating to `Plugins` -> `Add Dock Widget` and selecting `brainreg-segment`.

The plugin will then open, with some options for loading data:

![brainreg interface](../images/brainreg-segment.webp)

## **To load your data**

There are three options for loading your data \(in the `Load data` section of the GUI\):

* `Load project (sample space)` - This is for loading a brainreg project in the coordinate space of your raw data 
(i.e., not warped to the atlas space\). N.B. the data will have been reoriented to the orientation of your chosen 
atlas, but it can be reoriented using the napari button in the bottom left (a cube with an arrow above it). 
**Click this button, then choose your brainreg \(or cellfinder registration\) output directory.**
* `Load project (atlas space)` - As above, but the data loaded will have been warped into the atlas space. 
This is most useful when you want to visualise your segmented structures in [brainrender](../../brainrender/index), 
as they must be in atlas space to do so. **Click this button, then choose your brainreg (or cellfinder registration)
output directory.**
* `Load atlas` If you don't have your own data registered to the atlas, then you can just load the atlas. 
Useful for making visualisations etc. **Click this drop-down menu, then pick an atlas.**

## **Navigating**

Your data will then appear as a napari "Layer" on the right-hand side, and will include your sample data 
(including any additionally downsampled channels), and the atlas. If you select the atlas layer and make it visible 
(by toggling the eye icon), hovering over a brain region will show the region in the bottom left corner**.**

You can navigate around the volume:

* Use the scroll bar at the bottom (or left/right keys) to navigate through the image stack
* Use the mouse scrollwheel to zoom in or out
* Drag with the mouse the pan the view

You can adjust the view of your image, by selecting its "layer" in the sidebar, there you can change the gamma 
enhancement, contrast limits (right-click for finer control) and the colormap used.

The buttons directly below the layers can be used to rotate the data, reset the view and view in 3D.

For information on how to segment specific types of structure, see [Segmenting 1D tracks](./segmenting-1d-tracks) 
, [Segmenting 2/3D structures](segmenting-3d-structures) and [Segmenting external layers](segmenting-external-layers).


