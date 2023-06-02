# Requirements
The hardware requirements for brainreg depend on the atlas (and in particular, the resolution) you want to use. 
Most machines (including laptops) will be able to use most of the atlases, but some atlases 
(such as the 10&mu;m mouse atlases) may need up to 50GB of RAM.

# Installation
There are two ways to run the registration using brainreg.
If you're just getting started, we recommend the [napari](https://napari.org/stable) plugin.
This provides a graphical user interface, and makes it easier to tweak parameters.

If you need to run brainreg on many samples, or on a remote machine
(e.g., using an institutional high-performance computing system), there is a command-line interface.

Whichever interface you use, the results will be identical.

:::{admonition} Installing the napari plugin
:class: dropdown
* [Make sure you have napari installed](https://napari.org/stable/tutorials/fundamentals/installation.html)
* Install the brainreg-napari plugin from within napari (`Plugins` -> `Install/Uninstall Package(s)`, choosing `brainreg-napari`).)

:::{note}
If you are using macOS, you will need to install the plugin using the
command line (`conda install -c conda-forge brainreg-napari`)
:::

:::{admonition} Installing the command line tool
:class: dropdown

```{hint}
If you know what you're doing just run `conda install -c conda-forge brainreg`
```

## Installing Python

brainreg is written in Python, and so needs a functional Python installation. Your machine may already have Python 
installed, but **we recommend installing miniconda**.

**See** [**Using conda**](/documentation/general/conda) **for details.**

```{caution}
brainreg should run on any type of Python installation, but if you don't use conda, 
we may be limited in the support we can offer.
```


## Installing brainreg
```{hint}
Remember to activate your conda environment before doing anything
```

### Using conda (recommended)

```bash
conda install -c conda-forge brainreg
```

###  Using pip 
```bash
pip install brainreg[napari]
```

To only install the command line tool with no GUI (e.g., to run brainreg on an HPC cluster), just run:

```
pip install brainreg
```

```{note}
If you are using macOS then please also run `conda install -c conda-forge niftyreg`
```

:::

## Download atlas (optional)

When brainreg runs, the appropriate reference atlas will be downloaded (if not previously
done so). To install download BrainGlobe atlases in advance, please see the guide to
[the BrainGlobe Atlas API command-line interface](/documentation/bg-atlasapi/usage/command-line-interface) for details.