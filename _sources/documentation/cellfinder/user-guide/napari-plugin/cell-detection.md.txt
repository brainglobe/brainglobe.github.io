# Cell detection

## Loading data

Once napari, and the `cellfinder` plugin is installed, open napari, and load the plugin (`Plugins` -> `cellfinder` -> `Cell detection`).

:::{hint}
A widget should then be docked into the side of your napari window.
If this doesn't happen, check for any errors (`Plugins` -> `Plugin Errors`, then select the cellfinder plugin from the drop-down menu).
This error can be used to report problems on the GitHub page, or the help forum, see sidebar for links.
:::

Then load your data (e.g. using the `File`-> menu, or by dragging and dropping data).
There must be two registered channels; a signal channel (containing fluorescently labelled cells), and a background channel (containing only autofluorescence).

:::{hint}
There are many napari plugins for loading data.
By default, single 3D tiffs, and directories of tiffs can be loaded.
:::

## Setting parameters

There are many parameters that can be set (see [All cell detection parameters](all-cell-detection-parameters)), but the following options must be set before running the plugin.

### Mandatory parameters

* **Signal image** - set this to the image layer containing the labelled cells
* **Background image** - set this to the image layer without cells
* **Voxel size (z)** - in microns, the plane-spacing (from one 2D section to the next)
* **Voxel size (y)** - in microns, the voxel size in the vertical (top to bottom) dimension
* **Voxel size (x)** - in microns, the voxel size in the horizontal (left to right) dimension

## Running `cellfinder`

Click the **Run** button.
The plugin will then run (this may take a while if you're analysing a large dataset), and will produce two additional image layers:

* **Detected** - these are the cell candidates classified as cells
* **Rejected** (hidden by default) - these are the cell candidates classified as artefacts.

:::{hint}
It is likely that the classification will not perform well on new data, to improve this, see [Training data generation](training-data-generation).
:::

## Saving data

The cell coordinates can be saved using any napari plugin (e.g., to csv).
To save the cell coordinates in the cellfinder XML format:

* Select the Points layers (e.g. **Detected** and **Rejected**)
* Click `File` -> `Save Selected Layer(s)`
* Save with `.xml` extension (e.g. `cells.xml`)
