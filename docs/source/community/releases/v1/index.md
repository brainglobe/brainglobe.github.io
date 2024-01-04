# BrainGlobe version 1 overview

BrainGlobe version 1 provides users with the `brainglobe` "meta"-package: a single package that will fetch all the tools in the BrainGlobe suite and install them onto your machine, ready for use.
It also provides the `brainglobe-workflows` package, which builds on top of `brainglobe` and provides some common analysis pipelines to users, as well as a benchmarking suite for developers working on code performance improvements.

## Updating to version 1

Our recommendation for updating to BrainGlobe version 1 is to follow the [installation instructions on the main documentation page](/documentation/index.md#installing-brainglobe) in a clean virtual environment, and delete or archive your old environment.
This will ensure that when you install `brainglobe`, the tools are fetched in a consistent manner and do not pick up any manually installed BrainGlobe tools that might be in your environment or python path.
Likewise, it also avoids potential issues when tools have been installed from both `conda-forge` and `PyPI`.

If you don't want to install the entire BrainGlobe suite and are happy to manage the tooling interdependencies yourself, you can still manually install the individual BrainGlobe tools that you wish to use.
If you choose to do so; as a general rule of thumb you should not mix `conda-forge` and `PyPI` installs, and avoid installing BrainGlobe tools of versions less than 1 in the same environment as those with version greater than 1 at all costs.

### Previous installs with conda

If you have previously installed any of our tools from conda, we strongly recommend that you create a new environment and follow the `pip` installation instructions provided on the [installation page](/documentation/index.md#installing-brainglobe).
The new "version 1" of BrainGlobe provides a PyPI package that comes with the complete suite of tools, and ensures that these are all consistent with one another.
These are fetched by `pip` and so may cause conflicts if they are already present in your environment, having been fetched from `conda-forge`.
Mixing `conda-forge` installed packages with the `brainglobe` package from PyPI will likely throw versioning issues as we can't guarantee that `conda` will resolve the tool dependencies correctly.

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
The cellfinder command-line tool has been replaced with `brainmapper` | [Further info](cellfinder-core-and-plugin-merge.md) |

## Complete index

```{toctree}
:maxdepth: 1
:glob:

brainreg
cellfinder-migration
cellfinder-core-and-plugin-merge
```
