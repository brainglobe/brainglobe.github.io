# Segmenting 1D tracks

:::{hint}
For more information about how to process silicon probe tracks, please see [Silicon probe tracking](/tutorials/silicon-probe-tracking).
:::

To segment a 1D track, such as a fibre track, or a silicone probe track, select the `Track tracing` button in the `Segmentation panel`.

![Segmenting a 1D track](../images/segment_1d.webp)

Then:

* Click the `Add track` button
* If required, rename the track (by selecting the `track_0` text)
* Navigate to where you want to draw your region of interest.
* Make sure the add points mode is activated (by selecting the `+` symbol)
* Trace your track by adding points along it. You can add as many, or as few as you like, and this can be done in 3D by changing the viewer plane as you go along.

:::{caution}
Make sure you select the points in the order you wish them to be joined
:::

* Repeat the above for each track you wish to trace
* If the brain surface is damaged, you may not be able to trace perfectly from the surface. If you want to add an 
additional first point at the surface of the brain, click `Add surface points`. Selecting this option will add an 
additional point at the closest part of the brain surface to the first point, so that the track starts there. &#x20;
* The points can then be joined using spline interpolation by clicking `Trace tracks`. You can change:
  * `Fit degree`- what order spline fit to use (the default is 3, cubic)
  * `Spline smoothing` - how closely or not to fit the points (lower numbers fit more closely, for a less smooth interpolation)
  * `Spline points` - this doesn't affect the interpolation, but determines how many points are sampled from the interpolation (used for the summary)
  * `Summarise`- defaults to on, this will save a csv file, showing the brain area for each part of the interpolated track (determined by `Spline points` )
  * `Add surface point` If the brain surface is damaged, you may not be able to trace perfectly from the surface. 
  Selecting this option will add an additional point at the closest part of the brain surface to the first point, so that the track starts there.

You will then see the track fit appear in the napari window, and a `.csv` file will be saved, showing the brain region 
for every spline point along the track.

You can also use `Save` to save your points to be reloaded at a later date, and if you loaded your data in atlas space, 
you can also export the track to [brainrender](/documentation/brainrender/index). The file will be 
saved as e.g. `track_0.npy`. Using the Python API, you can visualise the track as follows:


```python
from brainrender import Scene
from brainrender.actors import Points
from myterial import blue

file = ("/path/to/track_0.npy")

scene = Scene()
scene.add(Points(file, colors=blue, radius=100, alpha=0.7))
scene.render()
```

:::{note}
All data will be saved into your brainreg output directory
:::

:::{hint}
For more information about how to use automated methods to segment your feature of interest, please see
[Analysing segmentation from other napari plugins](./analysing-external-segmentation).
:::