---
blogpost: true
date: August 16, 2026
author: Amirreza Bahramani
location: London, England
category: brainglobe
language: English
---

# Duke Mouse Brain Atlas has been added to BrainGlobe

[Mansour et al. (2025)](https://doi.org/10.1126/sciadv.adq8089) introduced the Duke Mouse Brain Atlas (DMBA), a high-resolution 15 µm isotropic stereotaxic atlas of the adult mouse brain. The atlas combines magnetic resonance histology (MRH), diffusion MRI-derived contrasts, micro-CT, light sheet microscopy, and registered anatomical annotations in a common reference space.

The atlas is now available through BrainGlobe via `duke_mouse_15um` for the 15 micron version, with downsampled versions available at 25, 50, 75, 100, and 150 µm isotropic resolution.

One useful feature of the DMBA is how it was built. The MRH data were acquired from perfusion-fixed specimens with the brains still in the skull. This makes the reference less affected by global or regional swelling, shrinkage, and deformation than atlases built after cranial dissection or conventional histological sectioning.

For BrainGlobe, the main reference image is the unmasked multigradient-echo (mGRE) template, and the annotation image uses the RCCFv3 labels supplied with the atlas data. RCCFv3 is the Duke team's reduced version of the Allen CCFv3 label set: related structures smaller than 0.1 mm<sup>3</sup> were grouped into larger anatomical regions, reducing registration noise from small regions that are difficult to align reliably.

The packaged atlas includes 12 registered reference images. These templates present the same anatomy through complementary MRI contrasts: diffusion-derived images are sensitive to water movement and tissue microstructure, while multigradient-echo images capture magnetic relaxation properties. Together, they can make different anatomical structures and tissue properties easier to inspect.

The atlas is stereotaxic, and information about stereotaxic landmarks is available with the source DMBA data.

![The 12 reference images included with the Duke Mouse Brain Atlas](./images/duke_mouse_12_references.gif)

**Figure 1. The 12 registered reference images included in the `duke_mouse_15um` atlas package.**


## How do I use the new atlas?

You can use the Duke Mouse Brain Atlas like all other BrainGlobe atlases. To visualise the atlas, you could follow the steps below:

* Install BrainGlobe ([instructions](/documentation/index)).
* Open napari and follow the steps in our [download tutorial](/tutorials/manage-atlases-in-GUI.md) for the `duke_mouse_15um` atlas.
* Run `napari -w brainrender-napari` and visualise the different parts of the atlas as described in our [visualisation tutorial](/tutorials/visualise-atlas-napari).

You can also load the atlas programmatically with BrainGlobe Atlas API:

```python
from brainglobe_atlasapi import BrainGlobeAtlas

atlas = BrainGlobeAtlas("duke_mouse_15um")
```

## Why are we adding new atlases?

A fundamental aim of the BrainGlobe project is to make various brain atlases easily accessible by users across the globe. If you would like to get involved with a similar project, please [get in touch](/contact).
