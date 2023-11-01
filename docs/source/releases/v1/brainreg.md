# Version 1: changes to registration and segmentation tools

## `brainreg` and `brainreg-napari`

The previously separate packages `brainreg` and `brainreg-napari` have now been combined into a single package that keeps the `brainreg` name.
This (new) `brainreg` package contains two submodules; `brainreg.core` whose contents are equivalent to the (old) `brainreg` package, and `brainreg.napari` that handles the napari widget.
The `brainreg.napari` module is optional and needs to be specified at install if you are not intending to install it via the BrainGlobe version 1 package.

If you were previously using brainreg in your scripts and have updated to version 1, you will now need to use `brainreg.core` instead of `brainreg`.
However, the internal structure of the `core` submodule has been retained, so updating your scripts should be a case of replacing "`brainreg`" with "`brainreg.core`" across your codebase.
Similarly, if you were ever importing `brainreg_napari` into your Python scripts, you will need to replace all occurrences of this with `brainreg.napari`.

If you are installing `brainreg` as part of the brainglobe version 1 package, the napari plugin will be automatically included and you won't need to do anything else to install the plugin.
Otherwise, to install the napari plugin, you will need to install `brainreg` with it's optional napari dependency via pip (recommended)

```bash
python -m pip install brainreg[napari]
```

or alternatively via conda

```bash
conda install brainreg
```

After updating, you may want to remove the now deprecated `brainreg-napari` package from your environment if it still persists;

```bash
pip uninstall brainreg-napari # If you originally installed via pip
conda remove brainreg-napari # If you originally installed via conda
```

## Command-line executable

The command-line executable has retained the name `brainreg` and has undergone no usability changes.

## napari plugin

When loading the plugin in napari, you will now find it listed under the plugins menu as "`Atlas Registration (brainreg)`" rather than "`Atlas Registration (brainreg-napari)`".
If you have external scripts that reply on the internal name of the plugin, you will need to update these to `brainreg` (from `brainreg-napari`) accordingly.

## `brainreg-segment`

This package has been renamed `brainglobe-segmentation`.
Beyond this renaming, there have been no internal changes to the package, so you may continue to use it as previously.
However, you will need to switch all occurrences of `brainglobe_segment` to `brainglobe_segmentation` in your Python scripts.

If you want to install the package standalone (without using BrainGlobe version 1 or through installing `brainreg`) then we recommend you `pip install` the package into your environment:

```bash
pip install brainglobe-segmentation
```

If you have `brainreg-segment` in your environment, you may wish to remove it as it will no longer be needed by `brainreg`:

```bash
pip uninstall brainreg-segment
```

however, `brainreg-segment` is still required by [`cellfinder`](../../documentation/cellfinder/index.md) versions `<=v1.0.0`.
