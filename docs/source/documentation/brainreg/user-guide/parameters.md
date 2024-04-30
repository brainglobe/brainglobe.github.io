# Registration parameters
To change how the image registration performs, you can change the options that are passed to the registration backend.

## NiftyReg

If using the [NiftyReg](http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg) backend, the following options can be changed:

### **Affine registration**

* `--affine-n-steps` Registration starts with further downsampled versions of the original data to optimize the global fit of the result and prevent "getting stuck" in local minima of the similarity function. This parameter determines how many downsampling steps are being performed, with each step halving the data size along each dimension. **Default: 6**
* `--affine-use-n-steps` Determines how many of the downsampling steps defined by `-affine-n-steps` will have their registration computed. The combination `--affine-n-steps 3 --affine-use-n-steps 2` will e.g. calculate 3 downsampled steps, each of which is half the size of the previous one but only perform the registration on the 2 smallest resampling steps, skipping the full resolution data.  Can be used to save time if running the full resolution doesn't result in noticeable improvements. **Default: 5**

### **Freeform registration**

* `--freeform-n-steps` Registration starts with further downsampled versions of the original data to optimize the global fit of the result and prevent "getting stuck" in local minima of the similarity function. This parameter determines how many downsampling steps are being performed, with each step halving the data size along each dimension. **Default: 6**
* `--freeform-use-n-steps` Determines how many of the downsampling steps defined by `--freeform-n-steps` will have their registration computed. The combination `--freeform-n-steps 3 --freeform-use-n-steps 2` will e.g. calculate 3 downsampled steps, each of which is half the size of the previous one but only perform the registration on the 2 smallest resampling steps, skipping the full resolution data. Can be used to save time if running the full resolution doesn't result in noticeable improvements. **Default: 4**
* `--bending-energy-weight` Sets the bending energy, which is the coefficient of the penalty term, preventing the freeform registration from over-fitting. The range is between 0 and 1 \(exclusive\) with higher values leading to more restriction of the registration. **Default: 0.95**
* `--grid-spacing` Sets the control point grid spacing in x, y & z. Positive values are interpreted as real values in mm, negative values are interpreted as the \(positive\) distances in voxels. Smaller grid spacing allows for more local deformations but increases the risk of over-fitting. **Default: -10**
* `--smoothing-sigma-floating` Adds a Gaussian smoothing to the floating image \(the one being registered\), with the sigma defined by the number. Positive values are interpreted as real values in mm, negative values are interpreted as distance in voxels. **Default: -1.0**
* `--smoothing-sigma-reference` Adds a Gaussian smoothing to the reference \(the one being registered to\) image, with the sigma defined by the number. Positive values are interpreted as real values in mm, negative values are interpreted as distance in voxels. **Default: -1.0**
* `--histogram-n-bins-floating` Number of bins used for the generation of the histograms used for the calculation of Normalized Mutual Information on the floating image. **Default: 128**
* `--histogram-n-bins-reference` Number of bins used for the generation of the histograms used for the calculation of Normalized Mutual Information on the reference image. **Default: 128**

