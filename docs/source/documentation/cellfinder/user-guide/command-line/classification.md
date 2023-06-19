# Cell candidate classification

**To change how the cell candidate classification step runs, you can change these options:**

* `--trained-model` To use your own network (not the one supplied with cellfinder) specify the model file.
* `--model-weights` To use pretrained model weights. Ensure that this model matches the `--network-depth` parameter.
* `--network-depth`. Resnet depth \(based on [He et al. \(2015\)](https://arxiv.org/abs/1512.03385)\) **Default: 50**
* `--batch-size` Batch size for classification. Can be adjusted depending on GPU memory. This can often be increased 
on high-memory modern GPUS \(e.g. 128 works well on a Titan RTX\). **Default: 32**

_**You shouldn't need to change these:**_

* `--x-pixel-um-network` The pixel size \(in microns, in the first dimension\) that the machine learning network was 
trained on.  Set this to adjust the pixel sizes of the extracted cubes. **Default 1**
* `--y-pixel-um-network` The pixel size \(in microns, in the second dimension\) that the machine learning network was 
trained on.  Set this to adjust the pixel sizes of the extracted cubes. **Default 1**
* `--z-pixel-um-network` The pixel size \(in microns, in the third dimension\) that the machine learning network was 
trained on.  Set this to adjust the pixel sizes of the extracted cubes. **Default 5**
* `--cube-width` The width of the cubes to extract in pixels \(must be even\). **Default 50**
* `--cube-height` The height of the cubes to extract in pixels \(must be even\). **Default 50**
* `--cube-depth` The depth \(z\)\) of the cubes to extract in pixels\(must be even\). **Default 20**
* `--save-empty-cubes` If a cube cannot be extracted \(e.g. to close to the edge of the image\), save an empty cube 
instead. Useful to keep track of all cell candidates.

