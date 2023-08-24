## Visualise an atlas in napari

In this tutorial, you will use `brainrender-napari` to visualise parts of the [`mpin_zfish_1um` zebrafish brain atlas](https://doi.org/10.1016/j.neuron.2019.04.034) in the 3D viewer napari through a series of simple clicks. You will need `napari` installed on your computer - please follow [`napari`'s installation instructions to do so](https://napari.org/stable/tutorials/fundamentals/installation.html).

1. Open `napari`
1. Install `brainrender-napari` by selecting `Plugins > Install/Uninstall plugins` and searching for `brainrender-napari` in the searchbox. Then click on the "Install" button.
1. Open the `Brainrender` widget by selecting `Plugins > Brainrender (brainrender-napari)`. 
    * A widget should appear on the right hand side.
1. (You can skip this step if you've already used the `mpin_zfish_atlas` in Brainglobe before) In the `Brainrender` widget's "Atlas table view", double-click the 6th row, which contains the `mpin_zfish_1um` atlas. Answer "Yes" to the appearing dialog (this may take a while). 
    * You have now downloaded the atlas.
1. In the `Brainrender` widget's "Atlas table view", double-click the 6th row, which contains the `mpin_zfish_1um` atlas (again). 
    * You have now added the annotations image and the reference image to napari.
    * A "Structures" widget appears below the existing widget.
1. Toggle the visualisation to a 3D view by pressing `Ctrl+Y` (`Cmd+Y` on Mac) on your keyboard.
1. Navigate the structures tree in the "Structures" widget by opening "forebrain". Double-click on "telencephalon".
    * You have now added a mesh layer of a brain structure to napari.
1. Back in the "Atlas table view", right-click on the 6th row. In the appearing context menu, select "GAD1b"
    * You have now added an additional reference image to napari

You have now added all possible types of brainglobe atlas parts (annotations image, reference image, structure mesh, additional reference) to napari - well done! You can now add any of the other atlases listed in the "Atlas table view" if you like (note that not all atlases have additional references!). Hover over any of the elements in the `Brainrender` widget to get additional hints about how to use them!