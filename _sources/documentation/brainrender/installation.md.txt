# Installing brainrender

## Environment

To install `brainrender`, you need a python environment with a Python 3.8. This may be a different version than you are 
using for other software. Using [conda](/documentation/general/conda) this can be created with:

```bash
conda create --name brainrender python=3.8 -y
```

## Basic installation

Installing `brainrender` is as simple as:

```bash
pip install brainrender
```

:::{attention}
Make sure to have your conda environment active when running `pip install`
:::

:::{caution}
You might get some error messages reporting conflicting version requirements for the `allensdk` package and a couple of 
others. You can safely ignore these.
:::

:::{hint}
Note that some of `brainrender`'s more rarely used features may require the installation of additional packages.
:::

Once you have installed brainrender, dive right in with this 
[getting started example notebook!](https://github.com/brainglobe/brainrender/blob/master/getting_started.ipynb)

## Advanced installation

If you want the most recent version of `brainrender`'s code, perhaps to help developing it, you can either 
clone the [GitHub repository](https://github.com/brainglobe/brainrender) or you can get install it directly from 
GitHub with:

```text
pip install -U git+https://github.com/brainglobe/brainrender.git
```

