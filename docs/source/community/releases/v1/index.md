# BrainGlobe version 1 overview

BrainGlobe version 1 provides users with the `brainglobe` "meta"-package: a single package that will fetch all the tools in the BrainGlobe suite and install them onto your machine, ready for use.
It also provides the `brainglobe-workflows` package, which builds on top of `brainglobe` and provides some common analysis pipelines to users, as well as a benchmarking suite for developers working on code performance improvements.

If you want to know more about the under-the-hood workings of the `brainglobe` "meta"-package, you can head to the [developer documentation](/docs/source/community/developers/repositories/brainglobe-meta/index.md).

## Updating to version 1

Our recommendation for updating to BrainGlobe version 1 is to follow the [installation instructions on the main documentation page](/documentation/index.md#installing-brainglobe) in a clean virtual environment, and delete or archive your old environment.
This will ensure that when you install `brainglobe`, the tools are fetched in a consistent manner and do not pick up any manually installed BrainGlobe tools that might be in your environment or python path.
Likewise, it also avoids potential issues when tools have been installed from both `conda-forge` and `PyPI`.

If you don't want to install the entire BrainGlobe suite and are happy to manage the tooling interdependencies yourself, you can still manually install the individual BrainGlobe tools that you wish to use.

### Can I install from `conda-forge`?

We are working on providing a `conda-forge` install for BrainGlobe version 1, as an alternative to the `pip install brainglobe` command that we currently recommend.
However for the time being, there is no one-line installation possible using `conda`.

There are no problems with `pip install brainglobe`-ing into a `conda` environment, we just need some time to setup all of the individual BrainGlobe tools on `conda-forge` before we can provide an all-in-one install through `conda`!

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
`brainrender` and `brainrender-napari` are now available through the `brainglobe` meta-package | [Further info](/blog/version1/version_1_released.md)

```{toctree}
:maxdepth: 1
:glob:

brainreg
cellfinder-migration
cellfinder-core-and-plugin-merge
```

## Full Changelog

- Recommended BrainGlobe install is via pip, into a clean environment.
  - `pip install brainglobe` to install BrainGlobe tools. Recommended even if you only want to use one or two tools.
  - `pip install brainglobe-workflows` if you also want to use the example analysis workflows that we provide.
- `brainreg-napari` is now shipped with `brainreg`
  - `brainreg` functionality is now available in a submodule, `brainreg.core`. If you previously used the Python API provided in `brainreg`, you will need to change your `from brainreg import X` statements to `from brainreg.core import X`.
  - The `brainreg-napari` plugin is now just called `brainreg` when using `napari`. The plugin's backend is in the submodule `brainreg.napari` rather than `brainreg-napari`.
  - The new `brainreg.core` and `brainreg.napari` submodules retain the old internal structure of the respective deprecated packages.
- `brainreg-segment` has been renamed `brainglobe-segmentation`.
  - Beyond the name change, package internals have not changed.
- `cellfinder` command-line-interface (CLI) has been renamed and moved.
  - The command-line interface is now provided by `brainglobe-workflows`.
  - The command-line tool is now called `brainmapper`.
  - The name "cellfinder" is now reserved for the merged `cellfinder-core` and `cellfinder-napari` packages.
- `cellfinder-core` and `cellfinder-napari` have been merged into a single package, called `cellfinder`.
  - The `cellfinder` package should not be confused with the old cellfinder command-line tool, described above. Going forward, "cellfinder" will refer exclusively to this new, merged package created from `cellfinder-core` and `cellfinder-napari` which only performs cell detection. The command-line tool with use the name `brainmapper`.
  - The `core` and `napari` features are now available as submodules of the `cellfinder` package. If you previously used `from cellfinder_core import X`, you'll have to use `from cellfinder.core import X` instead.
  - Internal function names and locations have otherwise not changed, beyond their conversion into the `core` and `napari` submodules.
  - The napari plugin is now referred to as the `cellfinder` plugin, and shows up with the name `cellfinder` when viewed in napari (as opposed to the old `cellfinder-napari` name it used to have).
- `brainglobe-workflows` has been released.
  - This package provides some exemplar data analysis workflows for users to modify or customise to suit their needs.
  - It will also provide command-line interfaces for particularly common workflows. Currently it provides `brainmapper`, the successor to the _old_ cellfinder command-line tool.
- `pip install brainglobe` is now the recommended way to install all BrainGlobe tools.
  - This will fetch the `brainglobe` meta-package, which includes the latest stable versions of all BrainGlobe tools and napari plugins.
  - All tools will be accessible in the install environment as if they had been pip-installed directly.
  - If you are updating to `brainglobe` version 1 having previously installed BrainGlobe tools individually, we [recommend you create](#updating-to-version-1) a clean Python environment and install `brainglobe` into this fresh environment to avoid potential package conflicts.
  - `brainglobe` package now ships the fixed `brainrender`, as well as `brainrender-napari` which we plan to transition to in the future.
