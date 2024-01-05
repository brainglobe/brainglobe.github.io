---
blogpost: true
date: Jan 8th, 2024
author: Will Graham
location: London, England
category: BrainGlobe-v1
language: English
---

# BrainGlobe version 1 is here! :partying_face:

Following our series of incremental updates to a number of BrainGlobe tools, we are pleased to announce that BrainGlobe version 1 has been released today!
Users can now enjoy:

- A one-line installation of _all_ BrainGlobe tools, automatically handling dependency inconsistencies and providing the _entire_ BrainGlobe tool suite. Individual tools no longer need to be manually installed as-and-when they're needed, and users do not need to worry about the behind-the-scenes organisation of the packages providing the tools.
- A clearer and more consistent naming convention for the tools that are provided.
- Access to example analysis workflows, installable on top of the BrainGlobe tool suite.

BrainGlobe version 1 is hallmarked by the release of (version 1 of) the [`brainglobe` package on PyPI](https://pypi.org/project/brainglobe/), and the new [`brainglobe-workflows` package](https://pypi.org/project/brainglobe-workflows/).

## Users: what you need to know

The version 1 release of `brainglobe` on PyPI will provide you with the entire BrainGlobe tool suite and ensure that the tools are consistent with one another.
You will no longer need to worry about manually installing individual BrainGlobe tools and checking how they interface with other tools.
You can also easily install the complete BrainGlobe suite of tools on a new machine or into a fresh environment in a single `pip` command:

```bash
pip install brainglobe>=1.0.0
```

The `brainglobe` package, or "meta-package" as we like to refer to it, ensures that the BrainGlobe tools installed onto your machine are stable and consistent with each other.
Key packages provided include:

- `bg-atlasapi`
- `brainreg`
- `brainrender` and `brainrender-napari` (new with version 1)
- `brainglobe-napari-io`
- `brainglobe-segmentation`
- `cellfinder`

The individual tools that you have been using are still available, and are largely still using the same name (with the exception of the old `cellfinder` command-line-tool, see below).
Regardless of how many of our tools you use in your analysis, we recommend that you create a new environment and (re)install any BrainGlobe tools you have been using following the instructions on the installation page.

For the most part, the effects of moving to version 1 should be limited to the cases where a tool has been merged with its napari plugin, or the relocation of the (old) cellfinder command-line tool.
The previous blog posts in this series outline these changes:

- [Blog post](./brainreg_update_live.md) | `brainreg`, `brainreg-napari` have been merged, whilst the somewhat unrelated `brainreg-segment` package has been renamed to distinguish it.
- [Blog post](./cellfinder_migration_live.md) | The old command-line tool (which confusingly was called "cellfinder" despite being a combination of several BrainGlobe tools) has been moved to `brainmapper` in the `brainglobe-workflows` package.
- [Blog post](./core_and_napari_merge.md) | `cellfinder-core` and `cellfinder-napari` have been merged into just "`cellfinder`".

Our vision for the new `brainglobe-workflows` package is to take this one step further and provide a selection of pre-written data analysis pipelines for neuroscientific data.
Currently the `brainglobe-workflows` package contains the successor to the old cellfinder command-line tool, now called `brainmapper`, but additional workflows will be added in the future.

## Developers: what you need to know

The `brainglobe` package allows us to ensure that tools cannot be installed in a manner which is inconsistent with each other.
If tool `A` necessitates a change in tool `B`, it was possible to update `A` without knowing about the knock-on effect on `B`, which would cause bugs further down the line.
Now the `brainglobe` package can be re-released in a manner which pins consistent versions of `A` and `B`, preventing this from happening.

The `brainglobe-workflows` package allows us to do two further things:

- It provides a distinct location for workflows that utilise BrainGlobe tools, so these workflows are not bundled together with their backends.
- It provides us with a set of analysis pipelines that we expect users to frequently run, which we can use to benchmark our tools and identify areas for improvement in terms of performance or speed.
- It builds on top of the `brainglobe` package, rather than having packages be interdependent on each other due to a workflow utilising multiple tools but being provided with its backend.

## Full Changelog

The full changelog is [available here](/community/releases/v1/index.md).
