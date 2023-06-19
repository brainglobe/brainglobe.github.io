# Testing

We use [pytest](https://docs.pytest.org/en/latest/) for testing. Please try to ensure that all functions
are tested, including both unit and integration tests.

## Long running tests
Some tests may take a long time, e.g. those requiring `TensorFlow` if you don't have a GPU. These tests should be
marked with `@pytest.mark.slow`, e.g.:

```python
import pytest
@pytest.mark.slow
def test_something_slow() -> None:
    slow_result = run_slow_processes()
    assert slow_result == expected_slow_thing, "some useful error message"
```

During development, these "slow" tests can be skipped by running `pytest -m "not slow"`.

## Continuous integration
A GitHub actions workflow (`.github/workflows/test_and_deploy.yml`) has been set up to run (on each commit/PR):
* Linting checks (pre-commit).
* Testing (only if linting checks pass)
* Release to PyPI (only if a git tag is present and if tests pass). Requires `TWINE_API_KEY` 
from PyPI to be set in repository secrets.

Many of these workflows use actions from 
[neuroinformatics-unit/actions](https://github.com/neuroinformatics-unit/actions). Feel free to raise a PR to that 
repository!
