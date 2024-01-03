# All cell detection parameters

Details on all the cellfinder cell detection parameters.

## Mandatory

- **Signal image** - set this to the image layer containing the labelled cells
- **Background image** - set this to the image layer without cells
- **Voxel size (z)** - in microns, the plane-spacing (from one 2D section to the next)
- **Voxel size (y)** - in microns, the voxel size in the vertical (top to bottom) dimension
- **Voxel size (x)** - in microns, the voxel size in the horizontal (left to right) dimension

## Optional

- **Soma diameter** - The expected soma size in um in the x/y dimensions. **Default 16**
- **Ball filter (xy)** - The size in um of the ball used for the morphological filter in the x/y dimensions. **Default: 6**
- **Ball filter (x)** - The size in um of the ball used for the morphological filter in the z dimension. **Default: 15**
- **Filter width** - The filter size used in the Laplacian of Gaussian filter to enhance the cell intensities. Given as a fraction of the soma-diameter. **Default: 0.2**
- **Threshold** - The cell intensity threshold, in multiples of the standard deviation above the mean. **Default: 10**
- **Cell spread** - Soma size spread factor (for splitting up cell clusters). **Default: 1.4**
- **Max cluster** -  Largest putative cell cluster (in cubic um) where splitting should be attempted.  **Default: 100000**
- **Trained model** - To use your own network (not the one supplied with cellfinder) specify the model file.

## Misc options

- To only analyse a limited number of planes (e.g., for speed during optimisation) you can:
  - Tick the **Analyse local** box. This will only process the planes around the currently selected plane
  - Set the **Start plane** and **End plane**, to e.g. 1000 and 1100, to only process the 100 planes between 1000 and 1100.
- To ensure that cellfinder doesn't use all the CPU cores on a machine, the **Number of free cpus** can be set. **Default: 2**
- To increase the logging (e.g. for troubleshooting), tick the **Debug** box.

:::{hint}
The parameter values will be saved between sessions.
The values can be reset by clicking the **Reset defaults** button.
:::
