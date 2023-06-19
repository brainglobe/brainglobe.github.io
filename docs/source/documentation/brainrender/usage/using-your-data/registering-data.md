# Registering data

To get the most out of brainrender, your data should be registered to one of the atlases supported by
the [BrainGlobe Atlas API](/documentation/bg-atlasapi/index). If you've used BrainGlobe's software for processing your 
raw data (e.g. [brainreg](/documentation/brainreg/index)) your data will already be registered, and you need not 
worry about any of this. If not, then some steps are necessary for registering your data. 

:::{hint}
This section assumes that your data were registered to an atlas already, but they are currently in a different 
orientation or resolution to the atlas you are intending to use. If that is not the case, you register your data 
first (e.g. with [brainreg](/documentation/brainreg/index)). 

Please note that although software tools like brainreg make it increasingly easy to register anatomical data 
to atlases, this is still a not-trivial steps in the analysis of any anatomical data.
:::

## Aligning to atlas's space

Brainglobe's Atlas API relies on [bg-space](/documentation/bg-space/index) for transforming data (e.g. image stacks) 
so that they are all oriented the same way. Bg-space provides a convenient naming convection to define the orientation 
of your data based on where the origin is and the direction that the three main axes (first three dimensions of your 
image data) point towards.

The process of transforming data from one axes system requires knowing the "space" of your target (i.e. of brainrender's 
atlas data\) and of the source \(your data\). The orientation of your data depends on your experimental set-up and 
subsequent pre-processing steps. To know what brainrender's target space is:

```python
from brainrender import Scene

scene = Scene()
print(scene.atlas.space)
"""
<BGSpace AnatomicalSpace object>
origin: ('Anterior', 'Superior', 'Right')
sections: ('Frontal plane', 'Horizontal plane', 'Sagittal plane')
shape: (528, 320, 456)
"""
```

Check the [bg-space documentation](/documentation/bg-space/index)) for more details.

## Matching resolution and offset

The section above described how to sort your image axes to that the coordinates order matches brainrender's. However, 
you might need additional steps to ensure that your data are registered to the atlases: your data might be at a 
different resolution or to a different offset. Resolution refers to how many microns (all units in brainrender are in 
microns) the side of the voxels in your image correspond to. Offset refers to the fact that the origin of your 
image might be offset from the origin of the atlas space (e.g. if you didn't image the entire brain). 

Here too bg-space provides tools to address mismatches in these two aspects.



