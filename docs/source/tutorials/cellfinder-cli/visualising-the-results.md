---
description: How to inspect the results in napari
---

# Visualising the results

cellfinder comes with a plugin for [napari](https://napari.org/) for easily visualising the results.
For more information, see [Visualisation](/documentation/cellfinder/user-guide/command-line/visualisation). 
To quickly view your data:

* Open napari (type `napari` into a command window)
* Into the window then drag and drop:
  * The signal channel directory (`test_brain/ch00`)
  * The entire cellfinder output directory

![cellfinder results viewed in napari](../images/cellfinder_results.png)

The napari window then will then be populated with different layers (left-hand side) that can be toggled:

* `ch00` The raw image data
* `allen_mouse_10um` The atlas annotations
* `Boundaries` The boundaries of the segmented regions
* `Non cells` The cell candidates classfied as artefacts (blue)
* `Cells` The cell candidates classified as cells (yellow)

If you click on the image above to enlarge, you should get a good idea of how cellfinder works:

* The coloured regions and the outlines show the segmentation of the brain (following atlas registration).
* The yellow circles show the detected cells (mostly in retrosplenial cortex and thalamus). There are also a few 
false positives (such as three on the surface of the brain and one outside the brain). This shows that the cell 
classification network (trained on other brains) is not quite 100%, and should be retrained with the addition of some 
data from this brain.
* The blue circles show those cell candidates classed as artefacts by the cell classification network. 
The majority of these are outside the brain, on the brain surface, or are blood vessels. A small number are 
cells, again indicating that the classification network could be retrained.

:::{hint}
To make the results a bit more obvious when zoomed out, the contrast of the raw data (`ch00`), has been adjusted 
along with changing the symbol for the cells to `disc` and increasing the size.
::

These images are useful to assess how well cellfinder performed, but not much use for any kind of numerical 
analysis. To see what data is exported from cellfinder, take a look at 
[Exploring the numerical results](exploring-the-numerical-results).

