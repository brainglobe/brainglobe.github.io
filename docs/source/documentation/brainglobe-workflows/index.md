# brainglobe-workflows

brainglobe-workflows is a collection of common data analysis pipelines that utilise a combination of BrainGlobe tools.
It currently provides:

- `cellfinder`: Whole-brain cell detection and classification. [Read more about the command line interface here](/documentation/cellfinder/user-guide/command-line/index.md).

## Installation

brainglobe-workflows can be installed into your Python environment using `pip`:

```bash
pip install brainglobe-workflows
```

Doing so will make all of the command-line tools that `brainglobe-workflows` provides visible whilst working inside your environment.

## Old `cellfinder` installations

If you have a version of the `cellfinder` package that is older than `v1.0.0`, we recommend that you uninstall your version of `cellfinder` and replace the command-line tool with the version provided by `brainglobe-workflows`.
See the [blog post](/blog/version1/cellfinder_migration_live.md) for more information.
