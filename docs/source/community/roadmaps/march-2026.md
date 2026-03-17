# March 2026

## Current status

### Recent progress

We've created three new software tools, and we've worked on improving and maintaining the BrainGlobe infrastructure.
Specifically we have made
* An alpha version of `brainglobe-registration`, allowing registration of 2D data (e.g. conventional tissue sections)  to an atlas.
* An alpha version of `brainglobe-stitch`, allowing efficient stitching of light-sheet data with a GUI.
* An alpha version of template building tools, which have been used with help of the BrainGlobe team to make three new atlases.
* An updated Pytorch backend for `cellfinder`, simplifying installation and support, and laying the groundwork for new analyses.
* Improvements to test coverage, bencharking tools, documentation and ease of installation.
* Improvements and bug fixes to BrainGlobe atlases and related validation tools.
* Many atlas available via the BrainGlobe Atlas API.

### High-level priorities for the next year

Overall, the team will focus on further expanding access to BrainGlobe through new features, atlases and atlas-registered data.
In particular, we are working towards
* Enabling users to detect and analyse more cells, e.g. from c-Fos experiments.
* Enabling users to detect and analyse cells from larger (e.g. rat) brains.
* Enabling users to create their own templates and annotations and use them within BrainGlobe.
* Making atlas downloads faster and leaner (BrainGlobe Atlas API v2).
* Making diverse atlas-registered data such as gene expression maps accessible via BrainGlobe GUIs (BrainGlobe Data API).
* Allowing easy registration of single histological sections and images of brain subvolumes to BrainGlobe atlases.
* Adding existing API documentation to website.
* Further expanding the number of atlases available via the BrainGlobe Atlas API.

## Future plans

The items below are in our plans, but not currently considered an immediate priority
* Consistent and documented API, e.g. `from brainglobe import cellfinder` or `from brainglobe import cell_detector_3D` (or both)
* A `napari` meta-plugin
