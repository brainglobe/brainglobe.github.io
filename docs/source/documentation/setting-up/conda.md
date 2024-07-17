# Using conda
Managing your Python environments with conda

:::{note}
You don't have to use conda, but we recommended it.
:::

## Introduction

Conda is a package and environment management system that allows you to:

* Install the correct version of Python to run your software
* Install software without admin rights (useful for shared machines and compute clusters).
* Install software without affecting anyone else's software installation (e.g., on a shared machine).
* Install software without potentially messing up any important software on your machine.
* Install multiple (potentially conflicting) versions of software at the same time, and allow you to switch between the 
two. This is very useful if you want to keep using a specific version of software for one experiment, but try out 
some new features of the latest release for another.

:::{hint}
If you know what you're doing with virtual environments, feel free to ignore this, but conda does make 
[CUDA and cuDNN installation easier](gpu).
:::

## Installation

**N.B. If you already have** [**Anaconda**](https://www.anaconda.com/) **or** 
[**miniconda**](https://docs.conda.io/en/latest/miniconda.html) **you can skip this section.**

### Download miniconda

Download the correct version of miniconda from [here](https://docs.conda.io/en/latest/miniconda.html). You should download:

* The correct version for your operating system (Linux/Windows/macOS etc.)
* The **Python 3.x** version (i.e. not the Python 2.7 version)
* The 64-bit version (in the unlikely event that you have a 32-bit machine, cellfinder probably won't work anyway).

You can download [Anaconda](https://www.anaconda.com/) instead, but we recommend miniconda.

### Install miniconda

Follow the miniconda instructions for 
[Windows](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html), 
[Linux](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html) or 
[macOS](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html).

### Check that conda is installed

N.B. conda is the program we are using, and is installed by both miniconda or Anaconda.

Open a new terminal window. On Linux and macOS, this is just called "Terminal", and on Windows, 
it will be called "Anaconda Prompt".

You should see a small screen with a prompt like:

```bash
(base) me@my-computer:~$
```

The `(base)` is the bit that tells you that conda is set up

## Setup your conda environment

### Create the environment

Open a terminal (or Anaconda Prompt) and type:

```bash
conda create --name ENV_NAME python=3.12
```

This will:

* Create a new conda environment (a kind of walled-off area on your computer that shouldn't affect other parts)
* Call it something, so you can reference it later (replace `ENV_NAME` with something useful)
* Install python version 3.12 into it



### Activate the environment

```bash
conda activate ENV_NAME
```

Replace `ENV_NAME` with whatever you called your environment

Your prompt should change to show the change from `(base)` to `(ENV_ANME)`:

```bash
(ENV_NAME) me@my-computer:~$
```

:::{caution}
**You must run `conda activate ENV_NAME` whenever you open a new terminal window** to use your software. If you don't 
see the `(ENV_NAME)` part of the prompt, the environment isn't activated
:::

## Further details

The reason why we use conda environments (other methods other than conda are available) is to have separate Python 
installations. This way, anything we do in the environment shouldn't affect any of the other environments.

If anything goes wrong, and your software stops working (and can't be fixed), you can simply make a new environment, 
and start again. If you have any troubles though, please [get in touch](../../contact.md).
