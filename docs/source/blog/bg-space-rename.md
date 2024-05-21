---
blogpost: true
date: Jan 24, 2024
author: Will Graham
location: London, England
category: brainglobe
language: English
---

# `bg-space` has been renamed

The "bg" prefix that a number of BrainGlobe tools carry is not very distinctive nor informative, so we are rolling out minor name changes to a lot of our packages that contain this prefix.
We are also taking this opportunity to bring these tools into line with our developer guidelines for automatic deployment, tooling, and testing.

The first on our list is `bg-space`, which will be changing name to the more explicit `brainglobe-space`.
Beyond this name change, there will be no functionality changes to the package, but several other tools will switch to depending on `brainglobe-space` from now on, and `bg-space` will be archived and not receive any future updates.

## What do I need to do?

Users who installed BrainGlobe through it's single ("meta") package install with `pip install brainglobe` will just need to update the package by running

```bash
pip install brainglobe --upgrade
```

in your environment, which will fetch the new version of all the affected packages.
You can use `pip show brainglobe` to check your version has updated - you should find you now have `brainglobe` version as 1.0.1 or higher.

If you are manually managing your BrainGlobe tools, you will need to uninstall `bg-space` and install `brainglobe-space` in its place.
You'll also need to update the following packages, which have dropped their `bg-space` dependency and now depend on `brainglobe-space`:

- `bg-atlasapi`, version 1.0.3 or newer.
- `brainglobe-napari-io`, version 0.3.3 or newer.
- `morphapi`, version 0.2.2 or newer.
- `brainrender`, version 2.1.5 or newer.
- `brainreg`, version 1.0.4 or newer.
