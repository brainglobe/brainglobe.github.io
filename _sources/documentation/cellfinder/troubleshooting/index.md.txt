# Troubleshooting

## Improving algorithm performance
cellfinder detects cells in a two-stage process, firstly cell candidates are detected. These are cell-like 
objects of approximately the correct intensity and size. These cell candidates are then classified into 
cells and artefacts by a deep learning step. 

### Cell candidate detection
If the initial cell candidate detection is not performing well, 
then we suggest adjusting the 
[cell detection parameters](/documentation/cellfinder/user-guide/napari-plugin/all-cell-detection-parameters). For a 
better understanding of what these parameters do, it may be useful to consult the 
[original PLOS Computational Biology paper](https://doi.org/10.1371/journal.pcbi.1009074).

:::{hint}
In general, false positives (non-cells being detected) is generally ok, as these will be refined in the 
classification step.
:::

### Cell candidate classification
The classification will use a pre-trained network by default that is included with the software. This network will 
usually need to be retrained. For more details, please see the guide to 
[retraining the pre-trained network](/documentation/cellfinder/user-guide/training-strategy).

## Fixing technical problems
As cellfinder relies on a number of third party libraries (notably [TensorFlow](https://www.tensorflow.org/),
[CUDA](https://developer.nvidia.com/cuda-zone) and [cuDNN](https://developer.nvidia.com/cudnn))
there may be issues while running the software.

If you are having any issues, please see the following sections:

```{toctree}
:maxdepth: 1
speed-up
error-messages
```

## Anything else

If you are still having trouble, please [get in touch](/contact).

