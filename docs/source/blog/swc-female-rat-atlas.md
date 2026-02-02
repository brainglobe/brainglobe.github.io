---
blogpost: true
date: February 2, 2026
author: Viktor Plattner
location: London, England
category: brainglobe
language: English
---


# New female rat brain atlases added to BrainGlobe

We’re excited to announce the release of two rat brain atlases generated at the Sainsbury Wellcome Centre (SWC), now available through the BrainGlobe ecosystem.

These atlases expand the available rat resources by providing **two-photon microscopy–based, three-dimensional templates derived from juvenile female animals**, addressing gaps in both resolution and biological diversity in existing rat atlases.


### Native female rat atlas

This atlas is a population-based anatomical template generated from female Lister Hooded rats (5–8 weeks old) using automated serial two-photon tomography.

- **Atlas name:** `swc_female_rat_50um`
- **Resolution:** 50 µm isotropic
- **Template space:** Original SWC template space (a population-based anatomical template generated from 15 female animals, representing typical group morphology)
- **Brain shape:** Native female rat brain morphology
- **Annotations:** Curated and adapted from the Waxholm Space rat brain atlas

This atlas is particularly well suited for users who want to work in a **native, microscopy-derived female rat brain space**.

![SWC female rat atlas](images/swc_female_rat.gif)

### Waxholm Space–registered female rat atlas

To support interoperability with existing rat resources, we also provide a version of the SWC female rat template registered to Waxholm Space.

- **Atlas name:** `whs_sd_swc_female_rat_39um`
- **Resolution:** 39 µm isotropic (resampled from 50 µm during registration to Waxholm Space)
- **Template space:** Waxholm Space
- **Brain shape:** Waxholm Sprague Dawley male brain morphology
- **Annotations:** Waxholm Space rat brain atlas

This atlas enables **direct comparison and integration** with datasets and tools that already rely on Waxholm Space, while retaining the fine anatomical detail of the SWC template.

![Waxholm SWC female rat atlas](images/whs_swc_female_rat.gif)

### Future plans

Work is ongoing to generate a higher-resolution version of the atlas:

- **`swc_female_rat_25um`** — coming soon 🚀

This upcoming release will further improve anatomical detail and support fine-scale analyses.


### Availability and collaboration 

Both atlases are available via the BrainGlobe Atlas API and can be used seamlessly with tools such as `brainreg`, `brainrender`, `napari`, and `brainrender-napari`.

If you’re interested in using these atlases or collaborating on future developments, feel free to get in touch via the BrainGlobe GitHub or SWC
