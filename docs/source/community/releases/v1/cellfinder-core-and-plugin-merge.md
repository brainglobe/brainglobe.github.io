# Version 1: changes to the cellfinder backend and plugin

The `cellfinder-core` package and `cellfinder-napari` plugin have now been migrated to a [package called cellfinder](https://github.com/brainglobe/cellfinder).
Please note that this is enacting the [future warning from the earlier `cellfinder` (CLI) migration](./cellfinder-migration.md#future-warning).
If you wish to continue using both the `cellfinder` command-line interface *and* the backend Python API, you will need to install the latest version of `brainglobe-workflows`, which will automatically fetch the new version of the `cellfinder` package.
See the [updating section](#updating) for more details.

## `cellfinder-core`

If you were previously using the Python API to `cellfinder-core`, you will need to uninstall `cellfinder-core` from your environment and install `cellfinder` version `1.0.0` or later.

The internal package structure has not changed in this move, but it is now a submodule of the new cellfinder package.
So if you were using the Python API in your scripts, you will need to change any `from cellfinder_core import X` statements to `from cellfinder.core import X`.
Once you make this change, everything should work as it was before.

## `cellfinder-napari`

If you were previously using the napari plugin for visualising output data, you will need to uninstall `cellfinder-napari` and install `cellfinder[napari]`, making sure to fetch the optional napari dependency.

The plugin itself has not undergone any interface changes, but is now just called "cellfinder" rather than "cellfinder-napari" when viewed from the napari widget panel.

## `brainglobe-workflows`

Now ships with the new version of cellfinder, containing `cellfinder.core` and `cellfinder.napari` submodules.
`brainglobe-workflows` is now the *only* package that provides the cellfinder command-line interface.

## Updating

The update steps that you will need to perform vary depending on how you currently use cellfinder (CLI) and whether you upgraded to `brainglobe-workflows` previously.
Regardless, before you begin the process of updating we recommend you uninstall `cellfinder-core` and `cellfinder-napari` from your environment 

```bash
pip uninstall cellfinder-core cellfinder-napari
```

Alternatively; you can create a new, clean environment to install into.

### I previously updated to `brainglobe-workflows`

If you previously updated from the old cellfinder package to `brainglobe-workflows`, then you should be able to simply update to the latest version of `brainglobe-workflows`, with

```bash
pip install --upgrade brainglobe-workflows
```

This will fetch the new cellfinder package containing the merged `cellfinder.core` and `cellfinder.napari` modules.
You can then continue using the cellfinder CLI as you were before, and will also have the updated backend and plugins ready to go.

### I have not updated to `brainglobe-workflows`, but I don't use the cellfinder CLI

If you don't use the `cellfinder` CLI, then you can just upgrade your version of the cellfinder package to version `1.0.0` or later:

```bash
pip install --upgrade cellfinder
```

### I have not updated to `brainglobe-workflows`, and I use the cellfinder CLI

In this case, we strongly recommend you either create a new Python environment to install into (and delete your old one), or remove `cellfinder`, `cellfinder-core`, and `cellfinder-napari` from your current environment with

```bash
pip uninstall cellfinder cellfinder-core cellfinder-napari
```

You may also wish to use `pip` to uninstall `tensorflow` to make sure that the new install does not encounter potential version conflicts.

Once you have cleaned your environment, you will need to install the latest version of `brainglobe-workflows`:

```bash
pip install brainglobe-workflows
```

You will now have access to the cellfinder CLI from within your environment, as you did previously - but now it is [supplied by the `brainglobe-workflows` package](blog/version1/cellfinder_migration_live.md).
You will also have the latest version of the cellfinder package (`1.0.0` or later) installed;

- `cellfinder-core` is included as a submodule, `cellfinder.core`.
- `cellfinder-napari` is included as a submodule, and the plugin has been renamed to just "cellfinder" when viewed in napari.
