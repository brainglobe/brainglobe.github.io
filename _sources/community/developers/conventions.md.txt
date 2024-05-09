# Conventions

## Documentation
* We use [Sphinx](https://www.sphinx-doc.org/en/master/) to generate documentation (hosted on this website), built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html).
* Docstrings should be written in [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) format.
* Documentation structure should be informed by the [diataxis](https://diataxis.fr) framework.

## Dependency support
Packages have to choose which versions of dependencies they officially support,
with minimum supported versions of each dependency used in continuous
integration testing. BrainGlobe projects should follow
[NEP 29 — Recommend Python and NumPy version support as a community policy
standard](https://numpy.org/neps/nep-0029-deprecation_policy.html) to
determine the **minimum** set of supported package versions:

- The last 42 months of Python releases
- The last 24 months of NumPy releases

In addition to this, the last 24 months of other dependencies should also be
supported.

## Axis ordering in spatial arrays
For arrays representing spatial data, we follow `zyx` axis ordering in the same way as `numpy` and `napari`. 
The origin is the upper left corner when you show the first element `stack[0, :, :]`. The first dimension is the one 
that you are slicing, the second is the height of the image, and the third is the width of the image. 
The [`brainglobe-space` package](/documentation/brainglobe-space/index.md) provides an interface to manipulate data following different conventions 
to adhere to this standard.
