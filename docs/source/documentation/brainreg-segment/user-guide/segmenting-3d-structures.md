# Segmenting 2/3D structures

To segment a 3D \(or 2D\) structure, such as an injection site, select the `Region Segmentation` button in the `Segmentation panel`.

![Segmenting a 2/3D structure](../images/segment_3d.webp)

Then:

* Click the `Add region` buttons
* If required, rename this region (by selecting the e.g. `region_0` text)
* Navigate to where you want to draw your region of interest.
* Choose a brush size (top left box). N.B. this is in 3D.
* Make sure painting mode is activated (by selecting the paintbrush, top left). You can go back to the navigation
* mode by selecting the magnifying glass.
* Colour in your region that you want to segment, ensuring that you make a

  solid object.

* Add a new region if required (`Add region`)
* Repeat above for each region you wish to segment.
* Click `Analyse regions` to analyse the spatial distribution of the regions you have drawn.
  * If `Calculate volumes` is selected, the volume of each brain area included in the segmented region will be calculated and saved.
  * If `Summarise volumes` is selected, then each region will be summarised (centers, volumes etc)

You can also use `Save` to save your regions to be reloaded at a later date, and if you loaded your data in atlas 
space, you can also export the regions to [brainrender](/documentation/brainrender/index).
