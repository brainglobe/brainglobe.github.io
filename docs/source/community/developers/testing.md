# Testing

* We use [pytest](https://docs.pytest.org/en/latest/) for testing. Please try to ensure that all functions
are tested, including both unit and integration tests. We aim for 100% coverage where possible.
* We use [codecov](https://about.codecov.io/) as the coverage reporting tool. This is free for open-source
  projects and integrates with GitHub actions.

## Local testing with pytest and coverage
### pytest
We recommend to start unit testing locally through your project's terminal with the activated environment. 
You can also use VS Code or PyCharm for unit testing.
```bash
#activate python environment
pytest -vs tests/
```

Sometimes, you may need to run a single test or specific modules. You can do so using the following examples.
Make sure to check the paths, filenames, and test names.
```
pytest -vs tests/atlasapi/test_cli.py
pytest -vs tests/atlasapi/test_cli.py::test_config_cli
```

## Continuous integration
A GitHub actions workflow (`.github/workflows/test_and_deploy.yml`) has been set up to run (on each commit/PR):
* Linting checks (pre-commit).
* Testing (only if linting checks pass)
* Release to PyPI (only if a git tag is present and if tests pass). Requires `TWINE_API_KEY` 
from PyPI to be set in repository secrets.
* Sometimes additional, cross-repository, tests are run such as testing `brainmapper` with a development version of
`cellfinder`

Many of these workflows use actions from 
[neuroinformatics-unit/actions](https://github.com/neuroinformatics-unit/actions). Feel free to raise a PR to that 
repository!

## Test data

Data used by the tests should be kept on [GIN](https://gin.g-node.org/BrainGlobe/) and fetched using `pooch`.
Test data should not live on GitHub.
To avoid local tests running checks on user data interfering with separate user data on the same machine, tests should mock test-user data by mocking `Path.home()` - an example of how to achieve this can [be viewed in `brainrender-napari`](https://github.com/brainglobe/brainrender-napari/blob/014f5c5908065ddaa5d6b05ecdf90493383cfa2f/tests/conftest.py). 

