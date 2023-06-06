# Setting up

## Installation and download
* First install the cellfinder command line tool, following the 
[Installation guide](/documentation/cellfinder/installation)
* Download the data from [here](https://gin.g-node.org/cellfinder/data/raw/master/test\_brain\_SK\_AA\_71\_3.zip) 
(it will take a long time to download). Thanks to [Sepiedeh Keshavarzi](https://www.keshavarzilab.com/) for sharing the data.
* Unzip the data to a directory of your choice (doesn't matter where). You should end up with a directory called 
`test_brain` with two directories, each containing 2800 images
* Open a terminal (Linux) or your command prompt (Windows)
* Navigate to the directory containing the `test_brain` directory (e.g. using `cd`)
* Activate your [conda environment ](/documentation/general/conda)

:::{hint}
The test data supplied is purposefully not the "best". It has a low SNR, and some artefacts such as fluorescent 
vasculature, and bright spots on the surface of the brain. In addition, the cell classification network was 
trained on different data, to give you an idea of "real world" performance.

The aim of this tutorial is not to show cellfinder performing perfectly, but to illustrate how it deals with 
less than perfect data, and how to improve the performance.

With all analysis methods, please test it out on your data to see if it works for you, and feel free 
[get in touch]](/contact).
:::

## Before you start

To run cellfinder, you need to know:

* Where your data is (in this case, it's the path to the `test_brain` directory)
* Which image is the primary signal channel (the one with the labelled cells) and which is the secondary 
autofluorescence channel. In this case, `test_brain/ch00` is the signal channel and `test_brain/ch01` is the 
autofluroescence channel
* Where you want to save the output data (we'll just save it into a directory called `cellfinder_output`in the 
same directory as the `test_brain`)
* The pixel sizes of your data in microns (see [Image definition](/documentation/general/image-definition) for details). 
In this case, our data is 2&#956;m per pixel in the coronal plane and the spacing of each plane is 5&#956;m
* The orientation of your data. For atlas registration (using [brainreg](/documentation/brainreg/index)) the 
software needs to know how you acquired your data (coronal, sagittal etc.). For this cellfinder uses 
[bg-space](/documentation/bg-space/index). Full details on how to enter your data orientation can also be 
found in the [Image definition](/documentation/general/image-definition) section. For this tutorial, the orientation 
is `psl`, which means that the data origin is the most **p**osterior, **s**uperior, **l**eft voxel.
* Which atlas you want to use (you can see which are available by running `brainglobe list`. In this 
case, we want to use a mouse atlas (as that's what our data is), and we'll use the 10&#956;m version of the 
[Allen Mouse Brain Atlas](https://mouse.brain-map.org/static/atlas)

Now you're ready to start [Running cellfinder](running-cellfinder).
