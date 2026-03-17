# March 2026

## Current status

### High-level priorities for the next year

* enable users to detect and analyse more cells, e.g. from c-Fos experiments
* enable users to detect and analyse cells from larger (e.g. rat) brains
* enable users to create their own templates and annotations and use them within BrainGlobe
* make atlas downloads faster and leaner (BrainGlobe Atlas API v2)
* make diverse atlas-registered data such as gene expression maps accessible via BrainGlobe GUIs (BrainGlobe Data API)
* allow registration of single histological sections and images of brain subvolumes to BrainGlobe atlases
* add existing API documentation to website

### Recent progress

* PyTorch backend for cellfinder, enabling use with the latest versions of Python & release on conda-forge.
* Registration of 2D (e.g. conventional sections) data to an atlas (in alpha)
* Template building tools have been used with help of the BrainGlobe team to make three new atlases.
* Improvements to test coverage, bencharking tools, documentation and ease of installation
* Many atlas bugs were fixed, and validation improved

## Future plans

* Consistent and documented API, e.g. `from brainglobe import cellfinder` or `from brainglobe import cell_detector_3D` (or both)
* A `napari` meta-plugin
