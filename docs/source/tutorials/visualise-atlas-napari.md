# Visualise an atlas in napari

BrainGlobe atlases are made of different components. These include the annotations image, the (default) reference image, 3D atlas region meshes and, optionally, additional reference images. In this tutorial, you will use `brainrender-napari` to visualise each of these components in the 3D viewer napari through a series of simple clicks. The [`mpin_zfish_1um` zebrafish brain atlas](https://doi.org/10.1016/j.neuron.2019.04.034) will serve as an example. 

:::{note}
You will need `napari` installed on your computer - please follow [`napari`'s installation instructions to do so](https://napari.org/stable/tutorials/fundamentals/installation.html).
:::

1. Open `napari`.
2. Install `brainrender-napari` by selecting `Plugins > Install/Uninstall plugins` and searching for `brainrender-napari` in the searchbox. Then click on the `Install` button.

:::{note}
If you've not used BrainGlobe atlases before, you will need to download those you need. You can do this through the [command line](/documentation/brainglobe-atlasapi/usage/command-line-interface), or by following our (very short) ["Download an atlas in napari" tutorial](./manage-atlases-in-GUI).
:::


3. Open the `brainrender` widget by selecting `Plugins > brainrender > Brainrender` in the napari menu bar near the top left of the window. 
![brainrender widget](./images/brainrender-napari/plugin-menu-brainrender-napari.png)

**The brainrender widget appears on the right hand side of the window, listing all atlases you have downloaded**

4. In the `brainrender` widget's `Atlas Viewer` section, double-click the row which contains the `mpin_zfish_1um` atlas (you may have to scroll down slightly, if you've downloaded many atlases).

![brainrender widget with added annotations](./images/brainrender-napari/added-brainrender-napari.png)

**You have now added the annotations image and the default reference image to napari: They appear as layers in the napari layers list on the lower left of the window. A `3D Atlas region meshes` section appears below the `Atlas Viewer` section.**

5. Hover your mouse over any brain region in the `3D Atlas region meshes` section to see a tooltip with information about that region.
![hover tooltip showing brain region information](./images/brainrender-napari/hover_tooltip.jpg)

6. Toggle the napari display from 2D to 3D by pressing the button with the square icon on the lower left of the window.

![brainrender widget with 3d display](./images/brainrender-napari/toggle-ndisplay-brainrender-napari.png)

**The annotations image should now be displayed in 3D.**

7. Navigate the brain region tree in the `3D Atlas region meshes` section by opening "forebrain". Double-click on `telencephalon`.

![brainrender widget with region mesh](./images/brainrender-napari/add-region-brainrender-napari.png)

 **You have now added a 3D atlas region mesh layer, which appears as a mesh in the viewer and as a new layer in the layers list.**

8. Back in the "Atlas Viewer" section, right-click on the `mpin_zfish_1um` row. In the menu that appears, select `GAD1b`.

![brainrender widget with additional reference](./images/brainrender-napari/additional-reference-brainrender-napari.png)

**You have now added an additional reference image, which appears as a grey scale image in the viewer and as a new layer in the layers list.**

You have now added all possible kinds of BrainGlobe atlas components (annotations image, reference image, 3D atlas region mesh, additional reference) to napari! You can now add any of the other atlases listed in the `Atlas Viewer` section if you like (note that not all atlases have additional references!). 

:::{note}
Hover over any of the elements in the `brainrender` widget to get additional hints about how to use them!
:::
