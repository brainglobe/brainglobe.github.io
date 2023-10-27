# Version 1: changes to registration and segmentation tools

Prior to the release of brainglobe version 1, there were three tools with the prefix brainreg ("brain registration") that were split across three packages.

- brainreg was the core Python package that contained the functional code for performing registration of an atlas to a sample image (sequence).
- brainreg-napari provided a plugin to perform the registration steps interactively through napari. It depended on brainreg for the core functionality.
- brainreg-segment was a companion to brainreg that allowed for manual segmentation of regions/objects within the brain. However it was not necessarily involved with the registration process itself.

With the release of brainglobe version 1 and the development of brainglobe-registration, the decision was made to disambiguate the role of the segmentation functionality and combine the napari plugin with the core functionality.
As a result; brainreg-segment has changed name to brainglobe-segmentation to emphasise that the segmentation methods are separate from the registration process, and brainreg and brainreg-napari have been merged.
See below for more details.

## brainreg and brainreg-napari

The previously separate packages brainreg and brainreg-napari have now been combined into a single package that keeps the brainreg name.
This (new) brainreg package contains two submodules; `brainreg.core` whose contents are equivalent to the (old) brainreg package, and `brainreg.napari` that handles the napari widget.
The `brainreg.napari` module is optional and needs to be specified at install if you are not intending to install it via the brainglobe version 1 package.

If you were previously using brainreg in your scripts and have updated to version 1, you will now need to use `brainreg.core` instead of `brainreg`.
However, the internal structure of the `core` submodule has been retained, so updating your scripts should be a case of replacing "`brainreg`" with "`brainreg.core`" across your codebase.
Similarly, if you were ever importing `brainreg_napari` into your Python scripts, you will need to replace all occurrences of this with `brainreg.napari`.

If you are installing brainreg as part of the brainglobe version 1 package, the napari plugin will be automatically included and you won't need to do anything else to install the plugin.
Otherwise, to install the napari plugin, you will need to install brainreg with it's optional napari dependency via pip (recommended)

```bash
python -m pip install brainreg[napari]
```

or alternatively via conda

```bash
conda install brainreg
```

## Command-line executable

The command-line executable has retained the name `brainreg` and has undergone no usability changes.

## napari plugin

When loading the plugin in napari, you will now find it listed under the plugins menu as "`Atlas Registration (brainreg)`" rather than "`Atlas Registration (brainreg-napari)`".
If you have external scripts that reply on the internal name of the plugin, you will need to update these to `brainreg` (from `brainreg-napari`) accordingly.

## brainreg-segment

This package has been renamed brainglobe-segmentation.

Beyond this renaming, there have been no internal changes to the package, so you may continue to use it as previously.
However, you will need to switch all occurrences of `brainglobe_segment` to `brainglobe_segmentation` in your Python scripts.
