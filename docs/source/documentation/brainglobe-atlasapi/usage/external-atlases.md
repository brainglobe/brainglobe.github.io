# External atlases

In addition to the atlases packaged by BrainGlobe (see [Atlas details](atlas-details.md)), the Atlas API
can load atlases that are packaged and hosted by other organisations. These atlases are not maintained by BrainGlobe.

# Allen Institute atlases

The BrainGlobe Atlas API can also read atlases directly from the Allen Institute's
[atlas assets](https://atlas-assets.readthedocs.io) bucket, `s3://allen-atlas-assets`. This bucket is a
built-in remote, so the atlases below can be loaded by name like any other BrainGlobe atlas.

These atlases are named differently from BrainGlobe-packaged atlases:
* The name has **no resolution suffix**. Pick a resolution with the `resolution` argument (in micrometres).
  If you leave it out, the finest available resolution is used.

```python
from brainglobe_atlasapi import BrainGlobeAtlas

atlas = BrainGlobeAtlas("allen-adult-mouse-ccf-atlas", resolution=25)
older = BrainGlobeAtlas("allen-adult-mouse-ccf-atlas", resolution=25, version="2015")
```

Downloaded files are cached in a separate `allen-atlas-assets` directory inside the BrainGlobe directory.
:::{note}
The `resolution` value must match the first axis of the voxel size.
:::

## Allen adult mouse
### Allen Adult Mouse CCF Atlas
The Allen Adult Mouse Brain Atlas (CCFv3), as published by the Allen Institute. The 2011 version uses a Nissl
reference image; later versions use the STPT reference image.

Available versions: `2011`, `2015`, `2016`, `2017`
* `allen-adult-mouse-ccf-atlas` - 10, 25, 50 and 100μm resolution

### Allen Adult Mouse Stereotaxic CCF Atlas
A stereotaxic version of the Allen Adult Mouse Brain Atlas, with an STPT reference image.

Available versions: `2020`, `2026-03`
* `allen-adult-mouse-ccf-stereotaxic-atlas` - 10 and 25μm resolution

## Allen developing mouse
### Allen Developing Mouse Nissl Atlases
Atlases of the developing mouse brain with Nissl reference images. The P56 atlas uses the adult Nissl
reference image. All atlases except P56 are anisotropic.

Available versions: `2012`
* `allen-dev-mouse-e11pt5-nissl-atlas` - (16 × 16 × 20μm)
* `allen-dev-mouse-e13pt5-nissl-atlas` - (16 × 16 × 20μm)
* `allen-dev-mouse-e15pt5-nissl-atlas` - (16 × 16 × 20μm)
* `allen-dev-mouse-e18pt5-nissl-atlas` - (16 × 16 × 20μm)
* `allen-dev-mouse-p4-nissl-atlas` - (16.752 × 16.752 × 20μm)
* `allen-dev-mouse-p14-nissl-atlas` - (16.752 × 16.752 × 25μm)
* `allen-dev-mouse-p28-nissl-atlas` - (16.752 × 16.752 × 25μm)
* `allen-dev-mouse-p56-atlas` - 10, 25, 50 and 100μm resolution

### Allen Developing Mouse LSFM Atlases
Atlases of the developing mouse brain with light-sheet (LSFM) reference images.

Available versions: `2024`
* `allen-dev-mouse-e11pt5-spim-atlas` - 20μm resolution
* `allen-dev-mouse-e13pt5-spim-atlas` - 20μm resolution
* `allen-dev-mouse-e15pt5-spim-atlas` - 20μm resolution
* `allen-dev-mouse-e18pt5-spim-atlas` - 20μm resolution
* `allen-dev-mouse-p4-spim-atlas` - 20μm resolution
* `allen-dev-mouse-p14-spim-atlas` - 20μm resolution

## Allen human and non-human primate
### HMBA Human Atlases
Adult human atlases from the [Human and Mammalian Brain Atlas (HMBA)](https://brain-map.org/consortia/hmba) consortium, with MRI reference images.

Available versions: `2025`
* `hmba-adult-human-homba-atlas` - 700μm resolution
* `hmba-adult-human-ahrav2brodmann-atlas` - 500μm resolution
* `hmba-adult-human-ahrav2gyral-atlas` - 500μm resolution

### HMBA Non-human Primate Atlases
Adult non-human primate atlases from the [HMBA](https://brain-map.org/consortia/hmba) consortium, with MRI reference images.

Available versions: `2025`
* `hmba-adult-rhesusmacaque-homba-atlas` - 160μm resolution
* `hmba-adult-cynomolgusmacaque-homba-atlas` - 160μm resolution
* `hmba-adult-marmoset-homba-atlas` - 70μm resolution
