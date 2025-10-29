# Documentation

## Installing BrainGlobe

We always recommend that you install BrainGlobe tools into a virtual environment (managed by software such as `conda` or `venv`).
Your environment should run Python 3.10, 3.11 or 3.12. To specify the Python version for new conda environment, add it as a parameter on creation:

```bash
conda create -c conda-forge -n brainglobe-env python=3.12
```

Once you have created and activated your desired environment, you can install all BrainGlobe tools using `pip`:

```bash
pip install brainglobe
```

This will fetch all BrainGlobe tools, their Python APIs, and [`napari`](https://napari.org) plugins if they possess one.
It will also install `napari` into your environment so that you can make use of the plugins.

If you also want to install our analysis workflows (such as `brainmapper`, previously the `cellfinder` CLI), you will also need to install the `brainglobe-workflows` package.
This package builds on top of the `brainglobe` tools, and provides you with some commonly-used data analysis pipelines to save you from having to write your own scripts for standard workflows.
You can read about the workflows that are provided [on the documentation page](./brainglobe-workflows/index.md).
To install `brainglobe-workflows`, run

```bash
pip install brainglobe-workflows>=1.0.0
```

in your environment.
If you didn't previously install `brainglobe` into this environment, `brainglobe-workflows` will do so when you run the command above.
Otherwise, it will use the version of `brainglobe` that you already have installed.

### Updating

You can update your BrainGlobe tools by running

```bash
pip install brainglobe --upgrade
```

in your virtual environment.

### Installing Individual Tools

We recommend installing BrainGlobe in the manner detailed above, however each of the tools in the suite can be individually installed if you so wish.
This can be done by following the install instructions for the particular tool in question.

Please note that, if you choose to install the tools individually, we cannot guarantee that you will have a consistent and interoperable set of BrainGlobe tools - you may encounter version conflicts or dependency issues.
If you're not confident in resolving these yourself, we recommend installing BrainGlobe in the manner above, and updating your BrainGlobe tools by updating the overarching `brainglobe` package.

## Individual Tool Documentation

Once you have installed `brainglobe`, or [installed an individual tool](#installing-individual-tools) if you choose to go that route, you can lookup how to use it by following the links below.

```{toctree}
:maxdepth: 1
setting-up/index
brainglobe-atlasapi/index
brainglobe-space/index
brainglobe-utils/index
brainreg/index
brainglobe-segmentation/index
brainglobe-workflows/index
brainrender/index
brainglobe-heatmap/index
cellfinder/index
morphapi/index
```

Developers may also wish to review the documentation [for the `brainglobe` package](/community/developers/repositories/brainglobe-meta/index.md) itself.
