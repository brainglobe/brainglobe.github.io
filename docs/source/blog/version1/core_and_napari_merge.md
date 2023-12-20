---
blogpost: true
date: Jan 2, 2024
author: Will Graham
location: London, England
category: BrainGlobe-v1
language: English
---

# `cellfinder-core` and `cellfinder-napari` have merged

[BrainGlobe version 1](./version_1_announcement.md) is almost ready, and the next stage of its release journey is the merging of the "backend" `cellfinder-core` and `cellfinder-napari` packages into one.
We had previously [migrated the `cellfinder` data analysis workflow](./cellfinder_migration_live.md) into the new `brainglobe-workflows` package, as part of our efforts to separate "backend" BrainGlobe tools from common analysis pipelines.
This means that there is no longer any need to keep the "backend" package (`cellfinder-core`) and nor the visualisation plugin (`cellfinder-napari`) stored in separate, lower-level packages.
As such;

- [`cellfinder-core`](https://github.com/brainglobe/cellfinder-core) and [`cellfinder-napari`](https://github.com/brainglobe/cellfinder-napari) will be deprecated.
- [A _package_ called `cellfinder`](https://github.com/brainglobe/cellfinder) will become available as a replacement for this functionality. Note that this will re-use the old "cellfinder" name that the command-line-interface had, [prior to its migration](./cellfinder_migration_live.md).
- The `cellfinder-napari` plugin is now simply called "cellfinder" internally, and when loaded up in napari.
- The "cellfinder" name for the whole-brain registration and analysis workflow provided by [`brainglobe-workflows`](documentation/brainglobe-workflows/index) will be deprecated to avoid confusion. This workflow will now be available as "`brainmapper`".

From a user perspective, this is just a restructuring and reorganisation of existing functionality, and the renaming of the cellfinder command-line tool to `brainmapper`.
If you were using the `cellfinder-core` backend, or the `cellfinder-napari` plugins, you'll need to uninstall those packages and install version `1.0.0` (or later) of the [`cellfinder` _package_](https://pypi.org/project/cellfinder/).
By merging two packages together, we hope to reduce the complexity of a BrainGlobe install and make the API to the tools more intuitive.
For developers, this merge again reduces the number of repositories that we have to maintain.
It also ensures we continue to distinguish between BrainGlobe tools and workflows.
And finally, we also address a long-standing historical naming issue with the old "cellfinder" (now `brainmapper`) workflow being confused with the corresponding backend packages.

## What do I need to do?

If you were previously using `cellfinder-core` in your scripts, you will need to uninstall it and install `cellfinder` version `1.0.0` or greater.
Once you've done this, it should just be a case of changing each of your `from cellfinder_core import X` statements to `from cellfinder.core import X`.

If you were previously using `cellfinder-napari`, you'll need to uninstall it and install `cellfinder[napari]`, which will fetch `cellfinder` and its optional napari dependency.
Any references you have made to the `cellfinder_napari` plugin in your analysis will need to change to the "`cellfinder` plugin" instead.

If you were using the cellfinder command-line tool that was provided by `brainglobe-workflows`, you will need to update your version of `brainglobe-workflows`.
If you were still using the cellfinder command-line tool provided by the `cellfinder` _package_, with version less than `1.0.0`, you will need to take slightly more involved action - we recommand you look at the instructions on the [full changelog](#full-changelog) for details.

You can take a look at the instructions in the [full changelog](#full-changelog) for more details about updating to the new package.

## Full changelog

You can find the [full changelog on the releases page](../../community/releases/v1/cellfinder-core-and-plugin-merge.md).
