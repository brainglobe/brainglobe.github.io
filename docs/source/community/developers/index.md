# Developer's guide

## Introduction

**Contributors to BrainGlobe are absolutely encouraged**, whether to fix a bug, develop a new feature, or add a new atlas.

There are many BrainGlobe repositories, so it may not be obvious where a new contribution should go.
If you're unsure about any part of the contributing process, please [get in touch](../../contact.md). 

The best place for questions about contributing is probably
the [BrainGlobe Zulip chat](https://brainglobe.zulipchat.com/).
You are furthermore welcome to join the bi-weekly developer meetings and contribute items to the agenda - check out the [developer-meeting stream on Zulip](https://brainglobe.zulipchat.com/#narrow/stream/414089-developer-meeting) (requires sign-up) for more information.

If for any reason, you'd rather not reach out in public, feel free to send a direct message on Zulip 
to [Adam Tyson](https://github.com/adamltyson), one of the core developers.

Some of our tools have additional information about how data files are organised, where user caches are placed, and similar.
You can view these repositories and the relevant information by heading to the [specific repository developer docs page](./specific_repos.md).

## To contribute a new atlas

To add a new BrainGlobe atlas, please see the guide [here](/documentation/brainglobe-atlasapi/adding-a-new-atlas).

## To contribute code

Before contributing code, it may be useful to familiarise yourself with the [introduction to the BrainGlobe code for developers](./intro_to_codebase.md) as well as the [testing](./testing.md), [developer tooling](./tooling.md) and [conventions](./conventions.md) sections. 

The core development team will support you in contributing code, irrespective of your experience.
To ensure BrainGlobe remains easy-to-maintain, they will help ensure all code contributions meet 
a high standard.


### Creating a development environment

It is recommended to use a recent version of `conda` to install a development environment for
BrainGlobe projects ([`conda` versions >=23.10.0](https://conda.org/blog/2023-11-06-conda-23-10-0-release/) 
will significantly speed up installation time). Once you have `conda` installed, the following commands
will create and activate a `conda` environment with the requirements needed
for a development environment:

```sh
conda create -n brainglobe-dev -c conda-forge python=3.11 napari
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

### Pull requests

In all cases, please submit code to the main repository via a pull request. The developers recommend, and adhere,
to the following conventions:

- Please submit _draft_ pull requests as early as possible (you can still push to the branch once submitted) to
  allow for discussion.
- One approval of a PR (by a repo owner) is enough for it to be merged.
- Unless someone approves the PR with optional comments, the PR is immediately merged by the approving reviewer.
- Please merge via "Squash and Merge" on GitHub to maintain a clean commit history.
- Ask for a review from someone specific if you think they would be a particularly suited reviewer (possibly noting
  why they are suited on the PR description)

## To improve the documentation

Documentation for BrainGlobe is **very important** because it is aimed at researchers who may not have much
computational experience. In particular:

- Installation, although simple via PyPI, assumes a lot (e.g. functional Python installation, CUDA installation etc.).
- There are a lot of parameters that can be changed, and their impact on the final results is not always obvious.
- It is not immediately obvious how to use the results of the pipeline to answer the particular biological question.

For these reasons (and others) every part of all software must be documented as well as possible,
and all new features must be fully documented.

### Editing the documentation

The documentation is hosted using [GitHub Pages](https://pages.github.com/), and the source can be found at
[GitHub](https://github.com/brainglobe/brainglobe.github.io). Most content is found under `docs/source`, where the
structure mostly mirrors the rendered website. To edit a page, please:

- Fork the repository
- Make edits to the relevant pages
- Create a pull request outlining the changes made

If you aren't sure where the changes should be made, please
[get in touch](https://brainglobe.info/contact.html#contributing).

## Further information

:::{toctree}
:maxdepth: 1
intro_to_codebase
tooling
conventions
testing
new_releases
specific_repos
Code of conduct <https://github.com/brainglobe/.github/blob/main/CODE_OF_CONDUCT.md>
:::
