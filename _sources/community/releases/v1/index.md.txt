# BrainGlobe version 1 overview

## Changes at-a-glance

Below is a high-level overview of the changes to the brainglobe suite of tools that we offer.
You can follow the links provided for more information; including a listing of relocated and/or renamed tools.

| Change |   |
|--------|:-:|
brainreg and brainreg-napari have been merged into a single package | [Further info](brainreg.md#brainreg-and-brainreg-napari) |
brainreg-segment has been renamed to brainglobe-segmentation | [Further info](brainreg.md#brainreg-segment) |
The `cellfinder` command-line-interface has been moved into `brainglobe-workflows` | [Further info](cellfinder-migration.md) |
The cellfinder package is deprecated - it will later be recycled to merge some backend functionality | [Further info](cellfinder-migration.md#cellfinder-repository) |
The cellfinder Docker image is discontinued | [Further info](cellfinder-migration.md#cellfinder-docker-image) |
cellfinder-core and cellfinder-napari merged into "new cellfinder" | [Further info](cellfinder-core-and-plugin-merge.md) |

## Complete index

```{toctree}
:maxdepth: 1
:glob:

brainreg
cellfinder-migration
cellfinder-core-and-plugin-merge
```
