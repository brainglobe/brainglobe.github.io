# About

## Introduction
The BrainGlobe Initiative (BGI) was established by researchers at the
[Sainsbury Wellcome Centre](https://www.sainsburywellcome.org/web/) and the 
[Technical University of Munich](https://www.tum.de/en/). 

The core goal of BrainGlobe is to develop a suite of Python-based software tools for computational neuroanatomy. 
We have developed several software packages to access, analyze and visualize anatomical data. By ensuring the 
interoperability of all of BrainGlobe's software, we aim to streamline the development of analysis pipelines and facilitate the process of going from raw data to publication-ready content. By producing a set of high-quality 
open-source Python packages, we aim to accelerate the development of sophisticated analysis tools in python.

## Accessing data

Recent developments in high-resolution 3D electronic atlases for many model species and in high-throughput experimental 
techniques have enabled the production of a wealth of anatomical data and the creation of vast neuroanatomical datasets. 
However, accessing, downloading and using these data remains a challenging task which requires significant 
programming skills.

We aim to facilitate the access to available datasets, and have developed several tools to support this. For example, we developed 
[morphapi](/documentation/morphapi/index) which can be used to download neuronal morphological data, and
[brainrender](/documentation/brainrender/index) which provides functionality to 
download gene expression and mesoscale connectomics data for the mouse brain from the Allen institute.

A core step towards facilitating the usage of atlas data was also taken by developing the 
[BrainGlobe AtlasAPI](/documentation/bg-atlasapi/index). This tool provides a 
simple and unified interface for downloading and using data from a number of available atlases. Additionally, new atlases 
can easily be added to the API. With this tool we address a major obstacle when developing software for neuroanatomy:
few of the available atlases provide programmatic access to their data, and the APIs used to access the data vary 
across atlases. This obstacle resulted in most of the available software being dedicated to individual atlases or 
even datasets, requiring that additional and often duplicated effort be spent in adapting existing software to new 
atlases. By providing a unified API, we aim to facilitate the development of software capable of working 
across atlases. The AtlasAPI is used by other BrainGlobe software tools like [cellfinder](/documentation/cellfinder/index) 
and [brainrender](/documentation/brainrender/index), ensuring that they can effortlessly work in different model species.

## Analyzing data

The registration of anatomical data to a reference image (from an atlas) is a crucial step in the analysis of anatomical
data. Registering the data enables the comparison of data across individuals and experimental modalities and facilitates
the dissemination of anatomical data. It is also indispensable to easily compare user-generated data with data from 
publicly available datasets.

Registering 3D image data to a reference atlas is a technically demanding task. For this reason, we developed
[brainreg](/documentation/brainreg/index), a Python-based software tool for the 3D registration of anatomical data

[cellfinder](/documentation/cellfinder/index) uses a deep learning algorithm to identify the location of 
labelled cells (e.g. expressing a fluorescent protein) across an entire brain. It thus provides a fast, reliable 
and reproducible approach to the quantification of data from many experiments (e.g. viral tracing). 


## Visualizing data

In addition to downloading and analyzing data, visualization is a core step in any analysis pipeline. The creation 
of images and videos from data is crucial for both inspecting the results of analysis steps and for communicating one's 
findings. We developed [brainrender](/documentation/brainrender/index) to facilitate the creation of high-quality 3D interactive renderings of 
anatomical data. The necessity to visually explore increasingly large and rich datasets in 3D is clear in neuroanatomy: given the complicated 3D structures of many types of data (e.g. neuronal morphologies), 
2D alternatives are a poor substitute for 3D renderings. However, the creation of high-quality renderings remained a 
challenging technical problem. With [brainrender](/documentation/brainrender/index), we provide a user-friendly interface and a 
powerful and flexible rendering tool 
to ensure that any scientist can create rich and beautiful renderings of their anatomical data.


# Future
In addition to developing our own software, we are working to build a community of neuroscientists and
developers to leverage the vast data analysis ecosystem in Python for the analysis of neuroanatomical data.
To catalyse this, we aim to “fill the gaps” where tools do not exist, and
develop frameworks to facilitate collaboration. Our key future aims are:
* To enable the use of BGI tools across neuroscience by supporting all available high-quality neuroanatomical
  atlases
* To reduce barriers of entry and make sure BGI tools are accessible to all
* To ensure BGI tools and atlases can be incorporated into varied workflows to leverage the open-source
  image analysis community

# More details

```{toctree}
:maxdepth: 1
people
contact
publications
media
funders
```


