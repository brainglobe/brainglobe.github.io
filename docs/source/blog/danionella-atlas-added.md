---
blogpost: true
date: August 16, 2026
author: Amirreza Bahramani
location: London, England
category: brainglobe
language: English
---

# A 2.5 µm adult _Danionella cerebrum_ atlas joins BrainGlobe

_Danionella cerebrum_ is a small teleost fish whose brain remains optically accessible throughout adulthood. Unlike zebrafish, whose skull ossifies as they mature, _Danionella_ lack skull ossification above the brain. This makes non-invasive, cellular-resolution imaging across the adult brain possible. This optical access is a key reason that [HHMI's Janelia Research Campus is developing a _Danionella_ research platform](https://www.hhmi.org/news/janelias-two-big-bets-decoding-brain-and-reinventing-how-science-done).

[Kadobianskyi et al. (2026)](https://doi.org/10.64898/2026.03.09.710483) built a mixed-sex reference brain from 21 adult fish (11 male and 10 female). The atlas is now available in BrainGlobe as `danionella_cerebrum_mixed_2.5um`. It provides a 2.5 × 2.5 × 2.5 µm mixed-sex reference brain, a whole-brain annotation, and meshes that can be used in the rest of the BrainGlobe ecosystem.

![Animated dorsal slices through the Danionella cerebrum reference image and its coloured anatomical annotation](./images/danionella-mixed.gif)

**Figure 1. Dorsal view of animated slices through the mixed-sex _Danionella cerebrum_ atlas. The fluorescence reference image is shown on the left and the corresponding anatomical annotation on the right.**


## How do I use the new atlas?

You can use the atlas like all other BrainGlobe atlases. To visualise it, you could follow the steps below:

* Install BrainGlobe ([instructions](/documentation/index)).
* Open napari and follow the steps in our [download tutorial](/tutorials/manage-atlases-in-GUI.md) for the `danionella_cerebrum_mixed_2.5um` atlas.
* Run `napari -w brainrender-napari` and visualise the different parts of the atlas as described in our [visualisation tutorial](/tutorials/visualise-atlas-napari).

You can also load the atlas in Python:

```python
from brainglobe_atlasapi import BrainGlobeAtlas

atlas = BrainGlobeAtlas("danionella_cerebrum_mixed_2.5um")
```

## Why are we adding new atlases?

A key aim of BrainGlobe is to make brain atlases accessible across species, so that researchers can use common analysis and visualisation tools without reimplementing them for every model organism. If you would like to get involved with a similar project, please [get in touch](/contact).
