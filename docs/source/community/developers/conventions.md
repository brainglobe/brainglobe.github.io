# Conventions

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

For arrays representing spatial data, we follow `zyx` axis ordering in the same way as `numpy` and `napari`. The origin is the upper left corner when you show the first element `stack[0, :, :]`. The first dimension is the one that you are slicing, the second is the height of the image, and the third is the width of the image. The [`brainglobe-space`](/documentation/) provides an interface to manipulate data following different conventions to adhere to this standard.
