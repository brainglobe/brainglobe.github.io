# Publishing new releases

BrianGlobe packages hosted on GitHub have CI workflows setup that are used to automatically upload and publish new version releases when they are made available.
This is the preferred method for publishing new versions to `PyPI` (and where appropriate, the linked `conda` feedstocks) - avoid manual uploads where possible.

Maintainers can trigger a new release by pushing a new tag, in the format `vX.Y.Z`, to the main branch of a package repository.
The `v` prefix **is necessary** as the workflow will only attempt to upload to `PyPI` if the tag matches the format previously provided.
The `X`, `Y`, and `Z` values should be integers corresponding to the new version number.

## Triggering a new release

The steps for triggering a new release are:

1. Head to the "releases" UI on GitHub for the package you want to release a new version for, and select "draft a new release".
2. In the "choose a tag" box, opt to create a new tag in the format described above. Ensure that the target is `main` (or the desired commit on `main` if the current `HEAD` is not the desired release state).
3. Choose the release title. Typically this is the same as the tag that will be created.
4. In the "write" box, you should have the option to select the "previous tag". Choose the tag of the previous release, then select "generate release notes".
5. Check the "set as latest release" box.
6. Then hit "publish release".

This will trigger a tag-push event to the `main` branch, which will set the [deployment workflow](#workflow-for-publishing-new-releases) in motion.
You can now relax whilst the workflow uploads the new package version to `PyPI`; however you will need to look out for [`conda-forge` feedstock updates](#conda-forge-feedstocks) in the next couple of days, or pre-empt this by making your own.
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
Each package available in this way has a feedstock repository, usually under the name

```
conda-forge/<package-name>-feedstock
```

on GitHub.

These feedstocks are linked to their `PyPI` counterparts - when a new version comes available on `PyPI`, the `conda-forge` admin bot should open a PR in the feedstock repository which will update the version of the package available through `conda`.
These PRs must be approved by one of the feedstock maintainers before they are merged in.

- Feedstock maintainers and package maintainers may be different
- New versions of packages will **NOT** be available through `conda` until these PRs are merged in.

If the new version changes are extensive or non-trivial; a manual update to the `meta.yaml` "recipe" file might be needed, as the admin bot is unable to resolve complex edits.
Examples of such changes are; changing package dependencies, introducing new submodules, and/or editing command-line entry-points.
You will need to use the `conda-forge` CI to debug the builds when manually updating in this way.

## Workflow for publishing new releases

BrainGlobe repositories hosted on GitHub each possess a `test_and_deploy.yaml` workflow.
The basic functionality of these workflows use the [neuroinformatics-unit](https://github.com/neuroinformatics-unit/actions) actions to;

1. Lint the source code
1. Check the package manifest
1. Run the package tests

These checks are run against _all_ PRs opened against the repository, and on the `main` branch when they are merged in.
When a tag in the `vX.Y.Z` format is pushed to `main`, these checks are run again and _if they are successful_ the workflow will build the source distribution and upload this to `PyPI`.