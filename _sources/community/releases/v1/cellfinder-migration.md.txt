# Version 1: Cellfinder migration and `brainglobe-workflows`

## Disambiguation

Due to some historical naming decisions, there are some unfortunate clashes of language between packages, workflows, and tools.
We disambiguate these terms before proceeding with the changelog:

- "workflow" refers to an analysis pipeline - a sequence of data analysis steps to process data and produce an output, using a combination of BrainGlobe tools.
- `brainglobe-workflows` refers to the new package released with this update. [Source code on GitHub](https://github.com/brainglobe/brainglobe-workflows).
- cellfinder (package) refers to the [package named cellfinder on PyPI](https://pypi.org/project/cellfinder/0.8.0/). Specifically, to any versions `<1.0.0` of this package.
- cellfinder (repository) refers to the [source code on GitHub](https://github.com/brainglobe/cellfinder).
- `cellfinder` (CLI) refers to the `cellfinder` command-line tool. This is provided by both cellfinder (package) and `brainglobe-workflows`.
- cellfinder (Docker image) refers to the [Docker image](https://hub.docker.com/r/adamltyson/cellfinder) that allows users to mount their data and run `cellfinder` (CLI).

## Python version support

With this update, we are dropping `cellfinder` (CLI) support for Python 3.8.
Whilst the workflow should still run on Python 3.8 in the immediate future, the oldest supported version is now Python 3.9.

## cellfinder (package)

This package should now be considered deprecated to users.
Consequently, the `cellfinder` (CLI) tool provided by this package will no longer receive updates.
If you want to keep the `cellfinder` (CLI) up to date, you will need to [install `brainglobe-workflows`](#updating-to-the-new-cellfinder-cli-tool) and use the `cellfinder` (CLI) provided there.

### Future-warning

For development purposes, cellfinder (package) **will later become** the new name for the combined `cellfinder-core` and `cellfinder-napari` package.
This release of the package will be tagged with version `>=1.0.0`, to indicate that a breaking change has occurred, and there will be a corresponding blog post published.

If you have not moved to using `cellfinder` (CLI) provided by `brainglobe-workflows`, this change will break your analysis pipelines if you try to update.
You will need to install either `brainglobe-workflows` or BrainGlobe version 1, or prevent your package manager from attempting to update cellfinder (package).

## cellfinder (repository)

For development purposes, the cellfinder repository will be recycled to include the backend code that is currently stored in `cellfinder-core` and `cellfinder-napari`.
Similarly to `brainreg`, we will be combining the functionality of the backend code and visualisation tool into a single package.

## cellfinder (Docker image)

We will no longer be providing Docker images for `cellfinder` (CLI).
We recommend that you install `brainglobe-workflows`, or BrainGlobe version 1 when it is release, into a clean virtual environment as an alternative.

## brainglobe-workflows

This package now provides the `cellfinder` (CLI) tool, and is the recommended way to run the analysis pipeline.
It can be installed via pip - [see the instructions below](#updating-to-the-new-cellfinder-cli-tool).

This package will continue to grow to include additional analysis pipelines and workflows for data analysis in neuroscience.

## Updating to the new `cellfinder` (CLI) tool

In order to update to the new `cellfinder` (CLI) tool provided by `brainglobe-workflows`, follow the steps below:

1. Uninstall cellfinder (package) from your Python environment. This should be a case of running `pip uninstall cellfinder` on the command line, with the environment activated.
1. (Optional) verify that the `cellfinder` (CLI) tool has been removed. If the output of `which cellfinder` is nothing, then the old tool has been successfully removed.
1. Install `brainglobe-workflows` into your environment. Again, we recommend installing via pip: `pip install brainglobe-workflows`.
1. (Optional) verify that the (new) `cellfinder` (CLI) tool has been installed. The output of `which cellfinder` should display a path to your activated environment, which ends inside the `brainglobe-workflows` package.

If you are making a clean install into a fresh environment, there is no need to run the first two (uninstall) steps.
Simply `pip install brainglobe-workflows` into your new environment.

As mentioned in the main blog post, `cellfinder` (CLI) will also be getting a new name in the near future, as additional workflow tools are added.
It's name isn't changing right now, but keep an eye on this space.

### Delaying updating

We **strongly recommend** you move to using `brainglobe-workflows` if you wish to continue using the `cellfinder` (CLI) tool.

If you really want to keep using the old cellfinder (package), you will need to prevent further updates to it.
The `cellfinder` (CLI) provided by cellfinder (package) will continue to work so long as you do not update, however you should consider any versions of `cellfinder` (CLI) provided by cellfinder (package) unmaintained.
You will eventually run into the [name conflicts](#cellfinder-repository) listed above, as BrainGlobe version 1 starts to roll out.
