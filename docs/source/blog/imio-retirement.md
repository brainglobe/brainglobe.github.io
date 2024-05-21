---
blogpost: true
date: Feb 08, 2024
author: Will Graham
location: London, England
category: brainglobe
language: English
---

# `imio` will be merging into `brainglobe-utils`

The `imio` package will be absorbed into `brainglobe-utils` as a submodule, so will no longer be receiving standalone updates.
This decision was made because:

- `imio` only has `brainglobe-utils` as a direct dependency as it stands anyway, so users are already installing `brainglobe_utils` to get `imio` currently.
- There was [a circular dependency](https://github.com/brainglobe/BrainGlobe/issues/64) between the two packages. Whilst not a circular import, this behaviour is undesirable going forward.
- It reduces the number of repositories that have to be maintained.

`imio`'s functionality will be available under the new `brainglobe_utils.image_io` submodule, and can otherwise be interacted with in the same way as the old `imio` library.
In terms of your source code, the only necessary changes should be to:

- Pin `brainglobe_utils` to at least version 0.4.0, which provides the `image_io` submodule.
- Remove any dependencies on `imio`.
- Replace `from imio import X` with `from brainglobe_utils.image_io import X` everywhere in your source code.

## What do I need to do?

Users who installed BrainGlobe through it's single ("meta") package install with `pip install brainglobe` will just need to update the package by running

```bash
pip install brainglobe --upgrade
```

in your environment, which will fetch the new version of all the affected packages.
You can use `pip show brainglobe` to check your version has updated - you should find you now have `brainglobe` version as 1.0.2 or higher.

If you are manually managing your BrainGlobe tools, you will need to uninstall `imio` and update `brainglobe-utils` to at least version 0.4.0, through

```bash
pip uninstall imio
pip install --upgrade brainglobe-utils
```

You'll also need to update the following packages, which now depend on at least `brainglobe-utils` version 0.4.0 instead of `imio`:

- `brainglobe-segment`, version 1.2.2 or newer.
- `brainreg`, version 1.0.5 or newer.
