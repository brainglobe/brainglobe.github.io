---
blogpost: true
date: Nov 1, 2023
author: Will Graham
location: London, England
category: BrainGlobe-v1
language: English
---

# `cellfinder` has moved: version 1 of `brainglobe-workflows` released

Continuing the [restructuring of BrainGlobe](./version_1_announcement.md), the `cellfinder` command-line tool has moved to a new home, `brainglobe-workflows`.
Please note that we will no longer be providing Docker images for `cellfinder`'s command-line functionality either - if you were previously using the Docker image, please see the advice in the [full changelog](#full-changelog).

Our vision for this new `brainglobe-workflows` package is to provide one package that bundles together several data-analysis pipelines that are run frequently in neuroscience.
By providing a package which knits together the relevant BrainGlobe tools into a single command or Python function, we can reduce the amount of manual work that users have to do to setup and run their own analyses.
No longer will it be necessary to manually install or import 3 different BrainGlobe tools to do your analysis - if it's provided by the `workflows` package, we will take care of this setup behind the scenes so you can focus on obtaining the results.

For now, `cellfinder` will retain it's name, but it will soon be renamed to bring it in line with the convention for additional workflows we will be providing.

From a developer and sustainability perspective, it also provides us with a natural series of workflows to benchmark the BrainGlobe tools against - to help speed up run times, catch any bugs, and check for compatibility breakages before we push future updates.
It also frees up the name "cellfinder" for the backend code that is currently stored in `cellfinder-core` and `cellfinder-napari`.
Much like the changes to [`brainreg`](./brainreg_update_live.md), we are looking to combine `cellfinder-core` and `cellfinder-napari` into a single package, then bundle it with the `BrainGlobe` version 1 release.
Migrating the `cellfinder` command-line tool to `brainglobe-workflows` is the first step to ensure that the analysis workflow it provides remains available to users, in a manner which can still be updated and receive bug reports.

## What do I need to do?

If you were previously using the `cellfinder` command-line tool; you don't need to do anything right now if you want to wait for the full release of BrainGlobe version 1, which will take care of these dependencies for you.
Be aware however, that the `cellfinder` tool that you have installed will no longer be receiving updates.

If you would like to update to the `cellfinder` command-line tool provided by `brainglobe-workflows`, we recommend you take a look at the instructions in the [full changelog](#full-changelog).

## Full changelog

You can find the [full changelog on the releases page](../../community/releases/v1/cellfinder-migration.md).
