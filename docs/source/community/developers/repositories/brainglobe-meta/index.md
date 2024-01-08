# brainglobe-meta

`pip install brainglobe` is doing what you expect - installing a package from PyPI called `brainglobe`.
This package, colloquially referred to as _the_ "meta"-package, `brainglobe`, and/or `brainglobe-meta`, doesn't actually contain any functionality beyond providing a version and some author information.
Instead, it's primary purpose is to (explicitly) depend on the other BrainGlobe tools that we want users to be able to install in a single command, through this package.
You can find the source for this package in the [`brainglobe-meta` repository](https://github.com/brainglobe/brainglobe-meta) on GitHub.

## Installation

The meta-package should always be installable in one line, and preferably should be installed for the first time in a clean environment.

### From `PyPI`, via `pip`

`brainglobe` can be installed from PyPI via

```bash
pip install brainglobe
```

or

```bash
python -m pip install brainglobe
```

Pass the `-U` or `--update` flag to `pip` to force an update on an existing install.

## Conventions

### Versioning

The rule of thumb for versioning and releasing the meta-package (creating a "new version of `brainglobe`"):

> Any `brainglobe` vX.0.0 release is a set of stable, compatible tools that interoperate with each other consistently.
> A `brainglobe` vX.Y.0 or vX.Y.Z release should be used when there have been several minor or patch updates to the BrainGlobe tool suite, that we want to encourage the user-base to adopt.

As such, we typically envision major version releases of the meta-package taking place when one or more BrainGlobe tools undergo major updates.
An example would be the release of `brainglobe` version 1; which saw the various `brainreg` packages merged, the `cellfinder` package was repurposed in order to merge `cellfinder-core` and `cellfinder-napari`, and the `brainmapper` tool replace the (old) cellfinder command-line interface.
The resulting `brainglobe` version 1.0.0 release prevents users from installing incompatible versions of `brainreg` and `cellfinder`, for example, both by removing the need for users to install these tools manually and by pinning minimum versions for each.

Minor or patch updates to `brainglobe` we envision to be cases where multiple tools have undergone performance improvements, minor patches, or under-the-hood code refactoring that we feel benefits the user experience, but does not require a change in how the user interacts with these tools.
A typical example of this might be when a function appears in both `brainglobe-tool-A` and `brainglobe-tool-B`, so we decide to refactor it into `brainglobe-utils` which is a common dependency.
In this case; each of `brainglobe-tool-A`, `brainglobe-tool-B`, and `brainglobe-utils` would get new releases, and furthermore both `brainglobe-tool-A` and `brainglobe-tool-B` would now depend on the new version of `brainglobe-utils`.
We would then decide to release a minor version of the meta-package, which updates the minimum version of these three packages - from the user perspective, this will come in a single update.

### Dependency Pinning

With the above conventions on versioning in mind, meta-package dependencies are always **pinned from below, and from above by the next major version**.
As such, all BrainGlobe dependencies in the meta-package `pyproject.toml` will have the form:

```toml
dependencies = [
    "brainglobe-tool-1>=X.Y.Z,<(X+1)",
]
```

for example,

```toml
dependencies = [
    "cellfinder>=1.1.0,<2",
    "brainrender>=2.1.3,<3",
]
```

This ensures that:

- Minor and patch updates to BrainGlobe tools should be picked up automatically by package installer when updating the metapackage. For example, if `cellfinder` bumps from `1.1.3` to `1.2.0`, updating the meta-package will result in `cellfinder` being updated to `1.2.0`.
- Major or breaking changes to BrainGlobe tools are **not** automatically picked up on update!
- We can force certain (combinations of) minor/patch updates to tools on users by simply releasing minor/patch updates to `brainglobe`. Changing `cellfinder>=1.1.0,<2` to `cellfinder>=1.1.4,<2` and `brainrender>=2.1.3,<3"` to `brainrender>=2.2.1,<3"`, then creating a new `brainglobe` minor/patch release, allows the user to update both of these packages with an update to `brainglobe`, not having to worry about the individual packages themselves.

## Dependency Tree

BrainGlobe comprises a number of tools, spread across a number of repositories.
These tools are all interlinked and interdependent, but the meta-package allows us to abstract this complexity away from the user.

To ensure we retain explicit control over what `brainglobe` provides to users, it is important that the meta-package explicitly depends on all BrainGlobe tools that it wants to provide, including "redundant dependencies".
For example, if the meta-package is providing `brainglobe-tool-A`, which itself depends on `brainglobe-tool-B`, then the dependency list of the meta-package should include **both** `brainglobe-tool-A` and `brainglobe-tool-B`.
Both packages should also have minimum versions pinned as per the [dependency pinning guidelines](#dependency-pinning) above.

The dependency tree of BrainGlobe tools provided by the meta-package is provided below, and should be updated periodically as new tools are added, or new versions of `brainglobe` are released.
Whilst it is not necessary for developers to remember the dependency structure, it is a useful reference guide for discerning how updates to one BrainGlobe tool might have knock-on effects on others.
The dependency tree reads top-to-bottom; that is, arrows are drawn **out** of dependencies **into** the tools that depend on them.
The tree does not include non-BrainGlobe dependencies.
Coloured arrows are only present to allow for line-tracing when arrows cross.

![Dependency tree for tools provided by the meta-package.](./brainglobe-dependencies.svg)

### Regenerating the Dependency Tree

The image file containing the dependency tree is saved under `<repo_root>/docs/source/community/developers/repositories/brainglobe-meta/brainglobe-dependencies.svg`.
It can be edited with any software that can open and manipulate `.svg` files, however the recommended tool is [`drawio`](https://app.diagrams.net/) which provides a GUI for editing `.svg`s.
Simply upload the current version of the file to the website, edit the flowchart as you see fit, then hit `File > Export As... > SVG`, which will open a further dialogue box with export options.
In this box, be sure to select "`Text Settings: Convert Labels to SVG`" to ensure that the exported flowchart's text is encoded correctly.
You can then export the file and save the new version to the repository.

As a general rule of thumb when editing the dependency chart, packages/tools should be organised into levels from the top down, with arrows pointing _out of dependencies_ **into** _the dependent packages_.

Packages on the top level depend on no other BrainGlobe tools.
Packages on the level below depend on at least one package from the level above, and any number of packages from the level(s) further up than that.
This illustrates both how BrainGlobe tools build on each other, as well as which tools can be considered ambivalent to new releases of others.
