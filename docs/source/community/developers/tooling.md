# Tooling


## Pre-commit hooks
It is important that all BrainGlobe is consistently formatted for readability, and for clean git diffs. For this 
reason, we use [pre-commit](https://pre-commit.com/). Running `pre-commit install` will set up 
[pre-commit hooks](https://pre-commit.com/) to ensure the code is formatted correctly. Currently, these are:
* [black](https://black.readthedocs.io/en/stable/) for code structure formatting (maximum line length set to 79)
* [mypy](https://mypy.readthedocs.io/en/stable/index.html) a static type checker
* [ruff](https://github.com/astral-sh/ruff) does a number of jobs, including enforcing PEP8 and sorting imports

These will prevent code from being committed if any of these hooks fail. To run them individually:
```bash
ruff .
black ./
mypy -p name_of_package
```

You can also execute all the hooks using `pre-commit run`. The best time to run this is after you have staged 
your changes, but before you commit them.

In the case you see `mypy` failing with an error like `Library stubs not installed for this-package`, you have 
to edit the `.pre-commit-config.yaml` file by adding the additional dependency to `mypy`:
```
- id: mypy
	additional_dependencies:
		- types-setuptools
		- types-this-package
```

## Versioning
We use [semantic versioning](https://semver.org/), which uses a `MAJOR`.`MINOR`.`PATCH` versiong number where these mean:

* PATCH = small bugfix
* MINOR = new feature
* MAJOR = breaking change

### Automated versioning
[`setuptools_scm`](https://github.com/pypa/setuptools_scm) can be used to automatically version each package. It has 
been pre-configured in the `pyproject.toml` file. 
`setuptools_scm` will automatically infer the version using git. To manually set a new semantic version, create a tag 
and make sure the tag is pushed to GitHub. Make sure you commit any changes you wish to be included in this version. 
E.g., to bump the version to `1.0.0`:

```bash
git add .
git commit -m "Add new changes"
git tag -a v1.0.0 -m "Bump to version 1.0.0"
git push --follow-tags
```



