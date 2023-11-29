# Installing brainrender

## Basic installation

To install `brainrender`, we strongly recommend [creating a `conda` environment](/documentation/setting-up/conda) and a [supported version of Python](/community/developers/conventions).
Then, installing `brainrender` is as simple as:

```bash
pip install brainrender
```

:::{caution}
With newer versions of Python on Windows, you may need to run `conda install pyside2` before running `pip install`.
:::

:::{caution}
You might get some error messages reporting conflicting version requirements for the `allensdk` package and a couple of 
others. You can safely ignore these.
:::

:::{hint}
Note that some of `brainrender`'s more rarely used features may require the installation of additional packages. In particular, for exporting videos you will need to install [`ffmpeg`](https://ffmpeg.org/download.html).
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

