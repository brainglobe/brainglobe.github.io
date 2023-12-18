---
blogpost: true
date: Dec 18, 2023
author: Alessandro Felder
location: Zurich, Switzerland
category: brainrender
language: English
---

# Now `brainrender` support has resumed, what are the plans for its future?

As some of you may have noticed, `brainrender` has undergone some much-needed and extensive maintenance work over the last few months. We are happy to report that, as a consequence, we have resumed supporting `brainrender` after a short hiatus. `brainrender` now works with [more recent versions of Python](../community/developers/conventions.md#dependency-support) and more recent versions of key dependencies (such as [vedo](https://vedo.embl.es/)). It should also be straightforward to [install on all operating systems](../documentation/brainrender/installation.md). We take this opportunity to set out the next steps for this tool.

In line [with our roadmap](../community/roadmaps/november-2023.md#v2-q2-2024), we plan to deprecate brainrender's graphical user interface (GUI) in the next few months, in favour of [`brainrender-napari`](../tutorials/visualise-atlas-napari.md). This will mean that users can use `brainrender` through the same GUI framework - [`napari`](https://napari.org/stable/) - as other BrainGlobe tools.

We plan to continue to support `brainrender` as a command line tool. Under the hood, we might move some functionality around so that it can be used both from `brainrender` and `brainrender-napari`.

## What do I need to do?

You may want to [install the updated `brainrender` into a fresh `conda` environment](../documentation/brainrender/installation.md), especially if you were experiencing issues with `brainrender`. If you use `brainrender` through its GUI, you may want to start experimenting [with `brainrender-napari`](../tutorials/visualise-atlas-napari.md) and [let us know](../contact.md) how it works for you - we always welcome your feedback.