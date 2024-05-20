# Setting up your GPU

## Introduction
Some BrainGlobe software will run faster if you have an NVIDIA GPU, and the appropriate software installed.

### Requirements

The requirements are the same as those for [PyTorch GPU support](https://pytorch.org/get-started/locally/), 
but essentially you need:

* A relatively modern **Windows or Linux based machine** (unfortunately, CUDA acceleration on macOS is not supported).
* An **NVIDIA GPU** with CUDA Compute Capability of 3.5 or higher (see the list
[here](https://en.wikipedia.org/wiki/CUDA)) with at least 8GB memory. Basically any relatively expensive NVIDIA GPU 
released in the last 5 years should be OK.
* Someone who has the admin password to install things.

## Installation

These instructions will vary somewhat between operating systems and on how your machine is set up (and how much control 
your institute will let you have).

### Installing NVIDIA drivers

The first thing you definitely need is the drivers for your GPU, which can be downloaded 
[here](https://www.nvidia.com/download/index.aspx?lang=en-us). Hopefully, these will have been installed when your 
machine was set up, but for GPU support in BrainGlobe, you will need version **450.x or greater**.

### Installing PyTorch with GPU support

BrainGlobe uses [PyTorch](https://pytorch.org/) which relies upon [CUDA](https://en.wikipedia.org/wiki/CUDA) 
and [cuDNN](https://developer.nvidia.com/cudnn). PyTorch will install the correct versions of CUDA and cuDNN
for you based on the choices you make when [installing PyTorch](https://pytorch.org/get-started/locally/).

We recommend using the `conda` installation method. Ensure you have the
`cellfinder` conda environment activated before running the command provided
by [PyTorch](https://pytorch.org/get-started/locally/).
