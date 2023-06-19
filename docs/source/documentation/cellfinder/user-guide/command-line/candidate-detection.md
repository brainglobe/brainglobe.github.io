# Cell candidate detection

**To change how the cell candidates are detected, you can change the following options:**

* `--save-planes` Whether to save the individual planes after processing and thresholding. Useful for debugging.
* `--outlier-keep` Don't remove putative cells that fall outside initial clusters
* `--artifact-keep` Save artifacts into the initial `xml` file
* `--max-cluster-size` Largest putative cell cluster \(in cubic um\) where splitting should be attempted.  **Default: 100000**
* `--soma-diameter` The expected soma size in um in the x/y dimensions. **Default: 16**
* `--ball-xy-size` The size in um of the ball used for the morphological filter in the x/y dimensions. **Default: 6**
* `--ball-z-size` The size in um of the ball used for the morphological filter in the z dimension.  **Default: 15**
* `--ball-overlap-fraction` The fraction of the ball that has to cover thresholded pixels for the centre pixel to be 
considered a nucleus pixel. **Default: 0.6**
* `--log-sigma-size` The filter size used in the Laplacian of Gaussian filter to enhance the cell intensities. 
Given as a fraction of the soma-diameter. **Default: 0.2**
* `--threshold` The cell threshold, in multiples of the standard deviation above the mean. **Default: 10**
* `--soma-spread-factor` Soma size spread factor \(for splitting up cell clusters\). **Default: 1.4**

