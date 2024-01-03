# Generating data to retrain the cellfinder classification network

Before generating training data, please see the guide to [retraining the pre-trained network](/documentation/cellfinder/user-guide/training-strategy).

## Loading data

If you've just run the cell detection step, proceed to **Annotating data.**
Otherwise:

- If you're starting from scratch, open napari, and load the plugin (`Plugins` -> `Curation`).
- As the curation step is based on previous results, load an XML file from a previous analysis (e.g. saved from napari, or from the cellfinder command line software). This can just be dragged onto the main napari canvas.
- Load the raw image data corresponding to the XML file (both signal and background channels).

## Annotating data

- Set the **signal image** and **background image** layers from the dropdown boxes.
- Either load previous training data layers, and set these in **Training data (cells)** and
**Training data (non cells)**, or click **Add training data layers** which will add two new layers,
and set them for you.
- Go through your data, selecting both correctly, and incorrectly classified cell candidates by:
  - Highlighting the Points layer they're in
  - Selecting points
  - Clicking **Mark as cell(s)** or **Mark as non-cell(s)**
  - Repeat until you are finished labelling
- Save your training data annotations in case you want to come back to them later:
  - Select the points layers (e.g. **Training data (cells)** and **Training data (non-cells**)
  - Click `File` -> `Save Selected Layer(s)`
  - Save with `.xml` extension (e.g. `curated_cells.xml`)

## Exporting data for training

To retrain the network, the training data (small 3D images centered on each annotated cell candidate) must be saved.
To do this:

- Click **Save training data**
- Choose (or create a new) directory

This may take a while if you have lots of training data, or your data is slow to access (e.g. network drive).

:::{hint}
Once your training data is created, you can start [Training the network](training-the-network).
:::
