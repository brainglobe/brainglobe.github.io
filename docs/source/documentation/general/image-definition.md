# Image definition

In some BrainGlobe tools, you need to specify the orientation and resolution of the data.

## Orientation
When you need to specify the orientation of your data, you will usually need to enter a string in the 
[bg-space](https://github.com/brainglobe/bg-space) "initials" form, to describe the origin voxel.

When you work with a stack, the origin is the upper left corner when you show the first element `stack[0, :, :]` with 
matplotlib or when you open the stack with ImageJ. The First dimension is the one that you are slicing, the second is 
the height of the image, and the third is the width of the image.

If the origin of your data (first, top left voxel) is the most anterior, superior, left part of the brain, then the 
orientation string would be "asl" (anterior, superior, left), and you would use `asr`.

The order of the three initials must be the same as the axis order (sliced plane, height, width).

For help with setting the orientation, the brainreg napari plugin comes with a tool to interactively check the orientation 
([see documentation](/documentation/brainreg/user-guide/checking-orientation)).

### Examples

#### Coronal section
If the first plane of this image was olfactory bulb, it would be `asr` (or `asl`). If the first plane was cerebellum, it would be `psr` or `psl`.
![coronal-section](images/orientation-asr.webp)

#### Horizontal section
If the first plane of this image was the top of the brain it would be `sal`/`sar`. If the first plane was the base it would be `ial`/`iar`.

![horizontal-section](images/orientation-sal.webp)


## Voxel sizes

You may also need to specify the size of your voxels. These voxel sizes are in microns, and come in the same order 
as your orientation definition.

As an example, we will assume, as above, the origin of your data (first, top left voxel) is the most anterior, superior, 
left part of the brain. If your plane spacing (i.e., the z-depth is 5 microns), and your in-plane resolution is 2x2 
microns, then the voxel sizes would be `5 2 2`.



