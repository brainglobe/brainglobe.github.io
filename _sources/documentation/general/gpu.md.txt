# Setting up your GPU

## Introduction
Some BrainGlobe software will run faster if you have an NVIDIA GPU, and the appropriate software installed.

### Requirements

The requirements are the same as those for [tensorflow GPU support](https://www.tensorflow.org/install/gpu), but essentially you need:

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

### Installing CUDA and cuDNN

BrainGlobe uses [TensorFlow](https://www.tensorflow.org/) which relies upon [CUDA](https://en.wikipedia.org/wiki/CUDA) 
and [cuDNN](https://developer.nvidia.com/cudnn). BrainGlobe requires **CUDA** and **cuDNN.**

CUDA and cuDNN are not too hard to install, but sometimes other software on your machine relies on different versions. 
It is possible to switch between the two, and it is easier if you are [using conda](gpu) 
(see [here](https://blog.kovalevskyi.com/multiple-version-of-cuda-libraries-on-the-same-machine-b9502d50ae77)).

However, we recommend that you install CUDA 11.2 and cuDNN 8.1 via conda if possible:

```
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
```

This method is easier and also doesn't require any admin rights (useful on a cluster or shared machine).

if this does not work for any reason, or you wish to have a system-wide installation of CUDA and cuDNN, then CUDA can 
be downloaded [here](https://developer.nvidia.com/cuda-toolkit-archive) and cuDNN from 
[here](https://developer.nvidia.com/cudnn). N.B. you will need to sign up for a (free) account to download cuDNN.
