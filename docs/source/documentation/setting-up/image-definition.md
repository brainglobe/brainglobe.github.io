# Image space definition

In some BrainGlobe tools, you need to specify the orientation and resolution of the data.

## Orientation
To describe the orientation of 3D brain imaging data in anatomical terms, [brainglobe-space](https://github.com/brainglobe/brainglobe-space) uses a anatomical description of the relative location of **the origin**—the voxel at position [0, 0, 0], which when you open the stack with [napari](https://napari.org/) by default corresponds with the pixel in the upper left corner of the first image in the stack. 

The origin can be described by a three letter string in which each letter corresponds to one of the following **anatomical directions**:
- posterior (`p`) ↔ anterior (`a`)
- superior (`s`) ↔ inferior (`i`) 
- left (`l`) ↔ right (`r`)

The string includes one letter from each opposing pair, specifying the direction towards the origin for axes 0, 1, and 2 respectively.


![allen mouse atlas 50μm](images/anatomical_orientations.png)
*50 μm mouse brain atlas by Wang et al., 2020 (https://doi.org/10.1016/j.cell.2020.04.007), visualised in napari using the [brainrender-napari plugin](https://napari-hub.org/plugins/brainrender-napari.html)*.

### Examples
The examples below assume:
- that the orientation matches that in the panels of the figure above
- default ordering of the axes, i.e. axis 0 (slice depth), axis 1 (image height), axis 2 (image width)

#### Coronal
If the stack of images starts at the olfactory bulb, moving toward the cerebellum, the anatomical directions for each axis are:
- axis 0: anterior → posterior 
- axis 1: superior → inferior 
- axis 2: left → right

The origin voxel corresponds to the most anterior (`a`), superior (`s`), left (`l`) part of the brain, so the origin string is `asl`. 

If the stack would start at the cerebellum and move towards the olfactory bulb, then axis 0 runs posterior → anterior, and the origin string would be `psl`.

#### Horizontal
If the first image in the stack corresponds to the bottom of the brain, the origin voxel corresponds to the most inferior (`i`), anterior (`a`), left (`l`) part of the brain for axis 0, 1, and 2 respectively. In this case the origin string is `ial`.

#### Sagittal
If the stack is sliced from the left side of the brain toward the right, the origin corresponds to the most right (`r`), superior (`s`), posterior (`p`) part of the brain, so the origin string is `rsp`.

## Voxel sizes

You may also need to specify the size of your voxels. These voxel sizes are in microns, and come in the same order 
as your orientation definition.

As an example, we will assume, as above, the origin of your data (first, top left voxel) is the most anterior, superior, 
left part of the brain. If your plane spacing (i.e., the slice depth) is 5 microns, and your in-plane resolution is 2x2 
microns, then the voxel sizes would be `5 2 2`.

## Napari 3D Orientation for brainrender

`napari v0.6.0` and later use a **right-handed 3D coordinate system** by default, however `brainrender` expects a **left-handed system**, so 3D visualisations may appear mirrored (left-right flipped).  

To change to a left-handed system

1. Right-click the **Toggle 2D/3D view** button in the bottom-left corner.  
2. Select the pre-0.6.0 default: **away, down, right**.  

This ensures `napari`'s visualisation matches `brainrender`'s.  
For more details on napari’s 3D axis directions and handedness, see the [napari documentation](https://napari.org/stable/guides/handedness.html).

