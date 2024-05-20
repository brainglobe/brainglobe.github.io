# Publishing new releases

BrainGlobe packages hosted on GitHub have CI workflows setup that are used to automatically upload and publish new version releases when they are made available.
This is the preferred method for publishing new versions to `PyPI` (and where appropriate, the linked `conda` feedstocks) - avoid manual uploads where possible.

Maintainers can trigger a new release by pushing a new tag, in the format `vX.Y.Z`, to the main branch of a package repository.
The `v` prefix **is necessary** as the workflow will only attempt to upload to `PyPI` if the tag matches the format previously provided.
The `X`, `Y`, and `Z` values should be integers corresponding to the new version number.

## Coordinating releases with the documentation and the metapackage

Releases will be made ad-hoc as bug-fixes and new features become available.
When releasing a new version of a BrainGlobe repository, we also need to update the website, the metapackage, and any other tools that depend on that repository accordingly.
This means we will typically create at least three dependent PRs;

- One in the repository itself (containing the bugfix or new feature we'd like to release)
- One in the [website repository](https://github.com/brainglobe/brainglobe.github.io) (to update documentation if necessary)
- One for each repository that depends on the updated tool, to bump the dependency version
- One in the [metapackage repository](https://github.com/brainglobe/brainglobe-meta), which pins the new versions of all affected tools at once

We should cross-link the latter to the website update, and release all affected packages to PyPI (and conda if appropriate) once they are all merged into `main`.
Ideally, updates and releases should be made in an order that [follows the dependency tree](<project:repositories/brainglobe-meta/index.md#dependency-tree>) - starting with our lower level tools, than their dependents, then dependents of those dependents, and so on.
The meta-package itself will always be the last by this convention.

### Example, highlighting pinning from below

It should be noted that our convention is to pin all our dependencies from below.
This allows us to minimise the number of new releases we have to make when updating one of our tools that several others depend on.
As such, when a package has a new release, only tools that depend on that package *that rely on the new features / structure* need to receive their own version bump (and thus a PR in the chain described above).

For example, suppose we have package `BG-A` at version `v1.0.0` which provides three features; `F1.foo`, `F1.bar`, and `F2`.
Then we have packages:

- `BG-B`, version `v1.2.0`, that uses `F1.foo`,
- `BG-C`, version `v1.5.0`, that uses `F1.bar`,
- `BG-D`, version `v1.7.0`, that uses `F2`.

Let's pretend that update `v1.1.0` to `BG-A` is going to re-write `F1.foo` to be more efficient (but keep the name), move `F1.bar` to `F2.bar`, and not change `F2`.
In this case, the PR chain would consist of:

- `BG-B` needs a new version (say `v1.2.1`), with the `BG-A` dependency pinned to `>=1.1.0`. This is so that the new `F1.foo` is used when `BG-A` is fetched by pip/conda.
- `BG-C` needs a new version (say `v1.6.0`), with the `BG-A` dependency pinned to `>=1.1.0` too. This is because version `v1.1.0` of `BG-A` is incompatible with `v1.0.0`. If we don't release a new `BG-C` version with this change, a user could `pip install BG-C`, have `BG-A` `v1.1.0` fetched as part of the dependency resolution, then would encounter an error whenever they tried to use `BG-C` since `F1.bar` would be unavailable (it's now `F2.bar`).
- `BG-D` doesn't need any new releases, since `F2` has not been affected by the `v1.1.0` update to `BG-A`.
- The metapackage then needs a new version which pins:
  - `BG-A >= v1.1.0`
  - `BG-B >= v1.2.1`
  - `BG-C >= v1.6.0`
  - `BG-D >= v1.7.0` (no change)

## Triggering a new release

The steps for triggering a new release are:

1. Head to the "releases" UI on GitHub for the package you want to release a new version for, and select "draft a new release".
2. In the "choose a tag" box, opt to create a new tag in the format described above. Ensure that the target is `main` (or the desired commit on `main` if the current `HEAD` is not the desired release state).
3. Choose the release title. Typically, this is the same as the tag that will be created.
4. In the "write" box, you should have the option to select the "previous tag". Choose the tag of the previous release, then select "generate release notes".
5. Check the "set as latest release" box.
6. Then hit "publish release".

This will trigger a tag-push event to the `main` branch, which will set the [deployment workflow](#workflow-for-publishing-new-releases) in motion.
You can now relax whilst the workflow uploads the new package version to `PyPI`; however you will need to look out for [`conda-forge` feedstock updates](#conda-forge-feedstocks) in the next couple of days, or preempt this by making your own.
See the section on feedstocks for more information.

### On the command line

If you have an up-to-date clone of the package repository, you can create a release tag on the command line with

```sh
git tag vX.Y.Z 
```

or one of

```sh
git tag -a vX.Y.Z
git tag -a vX.Y.Z -m "Tag annotation message"
```

if you want to annotate the tag; which is useful for tagging single-commit hotfixes or patches that might come after a release.

Once you have created the tag, you can `git push --tags` back to the main repository to trigger the release workflow.
**However** you still need to create release notes using the GitHub UI as described in [the section above](#triggering-a-new-release).
You will need to select the tag you just pushed, rather than creating a new tag, when you start drafting the release notes.

### Failed workflows

In the event that the release workflows fails after publishing a release, you will need to:

- Delete the tag from the repository from the GitHub tags UI
- Delete the release notes and release from the GitHub releases UI
- Debug the build failure and the commits with the fix are merged into `main`
- Begin the process over again.

### `conda-forge` feedstocks

A number of BrainGlobe packages are also available through `conda-forge`, providing an alternative installation method to `pip`.
Each package available in this way has a feedstock repository, usually at the GitHub repository:

```sh
conda-forge/<package-name>-feedstock
```

These feedstocks are linked to their `PyPI` counterparts - when a new version comes available on `PyPI`, the `conda-forge` admin bot should open a PR in the feedstock repository which will update the version of the package available through `conda`.
These PRs must be approved by one of the feedstock maintainers before they are merged in.

- Feedstock maintainers and package maintainers may be different
- New versions of packages will **NOT** be available through `conda` until these PRs are merged in.

If the new version changes are extensive or non-trivial; a manual update to the `meta.yaml` "recipe" file might be needed, as the admin bot is unable to resolve complex edits.
Examples of such changes are; changing package dependencies, introducing new submodules, and/or editing command-line entry-points.
You will need to use the `conda-forge` CI to debug the builds when manually updating in this way.

## Workflow for publishing new releases

BrainGlobe repositories hosted on GitHub each possess a `test_and_deploy.yaml` workflow.
The basic functionality of these workflows use the [neuroinformatics-unit](https://github.com/neuroinformatics-unit/actions) actions to:

1. Lint the source code
1. Check the package manifest
1. Run the package tests

These checks are run against *all* PRs opened against the repository, and on the `main` branch when they are merged in.
When a tag in the `vX.Y.Z` format is pushed to `main`, these checks are run again and *if they are successful* the workflow will build the source distribution and upload this to `PyPI`.
