# `brainglobe-workflows`

## `cellfinder` file paths

All file paths should be defined in `brainglobe_workflows.cellfinder.tools.prep.Paths`.
Any intermediate file paths, (i.e., those which are not of interest to the typical end-user) should be prefixed with `tmp__`.
These should then be cleaned up as soon as possible after generation.
