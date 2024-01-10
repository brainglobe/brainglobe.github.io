# brainglobe-workflows

brainglobe-workflows is a collection of common data analysis pipelines that utilise a combination of BrainGlobe tools.
It currently provides:

- `brainmapper`: Whole-brain cell detection and classification. [Read more about the command line interface here](brainmapper/index.md). This workflow was [previously called `cellfinder`](/blog/version1/core_and_napari_merge.md).

You can find more information on each of these tools by visiting the links below:

```{toctree}
:maxdepth: 1
brainmapper/index
```

## Installation

brainglobe-workflows can be installed into your Python environment using `pip`:

```bash
pip install brainglobe-workflows
```

Doing so will make all of the command-line tools that `brainglobe-workflows` provides visible whilst working inside your environment.

## Installing with `cellfinder` versions older than `v1.0.0`

The `cellfinder` package, command-line tool, and workflow have undergone significant changes in the move to version 1.
You can find a case-by-case breakdown of what you will need to do if you want to upgrade/install `brainglobe-workflows` whilst retaining the functionality of old `cellfinder` installs (and the command-line tool) [in the corresponding changelog](/community/releases/v1/cellfinder-migration.md).

However, the simplest option is to create a fresh Python environment and install `brainglobe-workflows`:

```bash
pip install brainglobe-workflows
```
This will fetch the latest version of `brainglobe-workflows`, providing you with the `brainmapper` command-line tool / workflow which is functionally equivalent to the old "cellfinder" command-line tool.
It will also provide you with the updated `cellfinder` package (at least `v1.0.0`) whose API and package structure matches that described in the documentation.


