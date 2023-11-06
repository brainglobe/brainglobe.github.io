# Requirements

cellfinder should run on most machines, but for routine use on large datasets, you will need a fairly high-powered
computer (see the guide to [Speeding up cellfinder](/documentation/cellfinder/troubleshooting/speed-up) for details).

Using an NVIDIA GPU will speed up cell classification considerably. See [setting up your GPU](/documentation/setting-up/gpu) 
for details.

cellfinder uses brainreg for atlas registration, and the hardware requirements for brainreg depend on the atlas 
(and in particular, the resolution) you want to use.
Most machines (including laptops) will be able to use most of the atlases, but some atlases
(such as the 10&mu;m mouse atlases) may need up to 50GB of RAM.

# Installation
:::{admonition} Installing the napari plugin
:class: dropdown
* [Make sure you have napari installed](https://napari.org/stable/tutorials/fundamentals/installation.html)
* Install the cellfinder-napari plugin from within napari 
* (`Plugins` -> `Install/Uninstall Package(s)`, choosing `cellfinder-napari`).)
:::

:::{admonition} Installing the cellfinder-core Python package
:class: dropdown


## Installing Python
Your machine may already have Python
installed, but we recommend installing miniconda. See [Using conda](/documentation/setting-up/conda) for details.

## Installing cellfinder
```{hint}
Remember to activate your conda environment before doing anything
```

```bash
pip install cellfinder-core
```
:::

:::{admonition} Installing the command line tool
:class: dropdown

```{hint}
If you know what you're doing (and [your GPU is set up](/documentation/setting-up/gpu)), just run `pip install cellfinder`
```


## Installing Python

cellfinder is written in Python, and so needs a functional Python installation. Your machine may already have Python
installed, but we recommend installing miniconda. See [Using conda](/documentation/setting-up/conda) for details.

```{caution}
cellfinder should run on any type of Python installation, but if you don't use conda, 
we may be limited in the support we can offer.
```


## Installing cellfinder
```{hint}
Remember to activate your conda environment before doing anything
```

###  Using pip
```bash
pip install cellfinder[napari]
```

To only install the command line tool with no GUI (e.g., to run cellfinder on an HPC cluster), just run:

```
pip install cellfinder
```
:::

:::{admonition} Installing the command line tool using docker
:class: dropdown

Please see the [guide to using cellfinder with docker](user-guide/command-line/docker.md)
:::

To install download BrainGlobe atlases in advance, please see the guide to
[the BrainGlobe Atlas API command-line interface](/documentation/bg-atlasapi/usage/command-line-interface) for details.