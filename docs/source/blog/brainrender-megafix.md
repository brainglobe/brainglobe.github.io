---
blogpost: true
date: Dec 18, 2023
author: Alessandro Felder
location: Zurich, Switzerland
category: brainrender
language: English
---

# Plans for `brainrender`

Recent maintenance work means `brainrender` now works with [more recent versions of Python](../community/developers/conventions.md#dependency-support) and more recent versions of key dependencies (such as [vedo](https://vedo.embl.es/)). It should also be straightforward to [install on all operating systems](../documentation/brainrender/installation.md). We take this opportunity to set out the next steps for this tool.

In line [with our roadmap](../community/roadmaps/november-2023.md#v2-q2-2024), we plan to deprecate brainrender's graphical user interface (GUI) in the next few months, in favour of [`brainrender-napari`](../tutorials/visualise-atlas-napari.md). This new tool will mean that users can visualise neuroanatomical data registered to a BrainGlobe atlas through the same GUI framework - [`napari`](https://napari.org/stable/) - as other BrainGlobe tools. This will allow you to perform the BrainGlobe analysis pipeline flexibly in the same application, without resorting to the command line.

We also plan to continue to support using `brainrender` through a command line interface (CLI). Note that `brainrender` CLI and `brainrender-napari` will be two equivalent, but independent ways to visualise neuroanatomical data in a common coordinate space (the former through `vedo`, the latter through the `napari` canvas) rather than co-existing in a frontend-backend relationship like other brainglobe tools (e.g. `cellfinder.napari` and `cellfinder.core`). Under the hood, we might move some functionality around so that it can be used both from `brainrender` and `brainrender-napari`.

## What do I need to do?

You may want to [install the updated `brainrender` into a fresh `conda` environment](../documentation/brainrender/installation.md), especially if you were experiencing issues with `brainrender`. If you use `brainrender` through its GUI, you may want to start experimenting [with `brainrender-napari`](../tutorials/visualise-atlas-napari.md) and [let us know](../contact.md) how it works for you - we always welcome your feedback.