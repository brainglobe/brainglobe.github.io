# Developer's guide

## Introduction

**Contributors to BrainGlobe are absolutely encouraged**, whether to fix a bug, develop a new feature, or add a new atlas.

There are many BrainGlobe repositories, so it may not be obvious where a new contribution should go.
If you're unsure about any part of the contributing process, please [get in touch](../contact.md). The best place is to start a new discussion on
the [image.sc forum](https://forum.image.sc/tag/brainglobe). If you tag your post with `brainglobe` (and optionally a
specific tool, e.g. `cellfinder`) we will see your question and respond as soon as we can.

If you have a query about contributing to a specific tool, please do raise an issue on the relevant GitHub page.
If it's not the correct repository (e.g. `cellfinder` vs `cellfinder-core`), don't worry, we can move it to the 
relevant repository later. If for any reason, you'd rather not reach out in public, feel free to
[email](mailto:code@adamltyson.com?subject=brainglobe-contribution) [Adam Tyson](https://github.com/adamltyson), one
of the core developers.

## To contribute a new atlas

To add a new BrainGlobe atlas, please see the guide [here](/documentation/bg-atlasapi/adding-a-new-atlas).

## To improve the documentation

Documentation for BrainGlobe is **very important** because it is aimed at researchers who may not have much
computational experience. In particular:

- Installation, although simple via PyPI, assumes a lot (functional Python installation, CUDA installation etc.).
- Although most software can be run through a single command, there are a lot of steps, and so a lot to understand.
- There are a lot of parameters that can be changed, and their impact on the final results is not always obvious.
- It is not immediately obvious how to use the results of the pipeline to answer the particular biological question.

For these reasons (and others) every part of all software must be documented as well as possible,
and all new features must be fully documented.

### Editing the documentation

TBC

## To contribute code

### Creating a development environment

It is recommended to use `conda` to install a development environment for
BrainGlobe projects. Once you have `conda` installed, the following commands
will create and activate a `conda` environment with the requirements needed
for a development environment:

```sh
conda create -n brainglobe-dev -c conda-forge python=3.10 napari
conda activate brainglobe-dev
```

This installs packages that often can't be installed via `pip`, including
`pyqt`. The specific version of `Python` is chosen to allow `TensorFlow` to be
installed on macOS arm64 machines.

To install a specific BrainGlobe project for development, clone the
GitHub repository, and then run

```sh
pip install -e .[dev]
```

Or if using `zsh`:

```sh
pip install -e '.[dev]'
```

from inside the repository. This will install the package, its dependencies,
and its development dependencies.

## Pull requests

In all cases, please submit code to the main repository via a pull request. The developers recommend, and adhere,
to the following conventions:

- Please submit _draft_ pull requests as early as possible (you can still push to the branch once submitted) to
  allow for discussion.
- One approval of a PR (by a repo owner) is enough for it to be merged.
- Unless someone approves the PR with optional comments, the PR is immediately merged by the approving reviewer.
- Please merge via "Squash and Merge" on GitHub to maintain a clean commit history.
- Ask for a review from someone specific if you think they would be a particularly suited reviewer (possibly noting
  why they are suited on the PR description)


## Further information
:::{toctree}
:maxdepth: 1
tooling
conventions
testing
new_releases
Code of conduct <https://github.com/brainglobe/.github/blob/main/CODE_OF_CONDUCT.md>
:::

## Specific repository information
:::{toctree}
:maxdepth: 1
repositories/cellfinder-core/index
repositories/cellfinder/index
:::