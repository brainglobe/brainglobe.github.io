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
