# brainglobe-workflows

`brainglobe-workflows` is simultaneously a package containing data analysis pipelines that utilise BrainGlobe tools, as well as a benchmarking suite for those tools.

Users are only expected to interact with the command-line entry points (or equivalent backend functions) that the package provides.
A successful package install does not ship the benchmarking suite by default - indeed, a full clone of the repository is required to allow local running of the benchmarks.

Developers can clone the repository and run a `dev` install (`pip install .[dev]`) to install the developer requirements, in particular [`AirSpeed Velocity (asv)`](https://asv.readthedocs.io/en/v0.6.1/).
This will allow for running the benchmark workflows locally, however if you don't have a suitably performant machine, they will likely take a long time to run!

## `cellfinder` file paths

All file paths should be defined in `brainglobe_workflows.cellfinder.tools.prep.Paths`.
Any intermediate file paths, (i.e., those which are not of interest to the typical end-user) should be prefixed with `tmp__`.
These should then be cleaned up as soon as possible after generation.
