# Analyze and visualize tracing experiments
Analysis and visualiztion of tracing data (e.g., Anterograde or retrograde) in brains imaged post-hoc in a standard coordinate space

## Introduction

The primary objective of tracing experiments in neuroscience is to elucidate the pathway specificity and establish connection relationships between neurons and various brain areas. By comprehending these intricate connections, we can gain a deeper understanding of how the brain generates behavior. Therefore, it becomes imperative to quantify the bulk-labeled axonal projections in images, as this process serves as a fundamental step in unraveling the intricate web of neuronal connectivity and its corresponding functionality.

Here we present a tool for the analysis of tracing axonal projections in post-hoc brain imaging data, all conveniently located within a standard coordinate space. This tool is seamlessly integrated into brainreg, within the suite of computational neuroanatomy tools known as BrainGlobe. Leveraging the segmentation plugins available in napari, our tool effortlessly imports and integrates these segmentation results into brainreg-segment, allowing for comprehensive analysis of bulk axonal projections within the context of the atlas.

## **Before tracing bulk axonal tracks**

Tracing Compound Selection: Choose an appropriate tracing compound (or multiple ones if you plan to use different color) based on the specific requirements of your experiment. 

Injection: Carefully inject the tracing compound into the target region of the brain. The compound should be injected in a controlled manner to ensure accurate delivery and minimize damage to surrounding tissue.

Incubation: Allow sufficient time for the tracing compound to be taken up by neurons and transported along the axonal projections. The duration of the incubation period can vary depending on the specific compound and experimental requirements.

Tissue Processing: Sacrifice the animal and extract the brain for further processing. The animal is anaesthetised and perfused with PFA 4% following standard perfusion protocols. The brain is carefully extracted and left in PFA 4% overnight.

![Figure 1.](./images/brainreg-segment-fig1.webp)
**Figure 1.**

:::{note}
To ensure high quality image registration, it is essential that the brain is properly perfused in order to decrease 
the autofluorescence of blood vessels. It is also important that the brain is extracted from the skull carefully in 
order to avoid tissue damage.
:::

The brain is then thoroughly washed with 100mM PBS and imaged (e.g. by 
[Serial 2-Photon Tomography](https://sainsburywellcomecentre.github.io/OpenSerialSection/acquisition/); **Fig. 1**, 
right). Image channels as needed according to number of tracing compounds (and extra channel is acquired as the background fluorescence only).


## **Brain registration to an atlas**

To track the bulk axonal projections into the standard space, the brain must first be registered to an atlas using brainreg.

Before registration, brainreg needs to be installed, please follow the instructions 
[here](/documentation/brainreg/installation). Once installed, we can proceed to register the imaged brain.

:::{note}
Make sure you activate your conda environment before starting
:::

You will need:

1. The path where the brain image stack (signal channels) is/are located
2. The path where the brain stack (background fluorescence channel) is located.&#x20;
3. The path where you want the registration result to be saved
4. The resolution at which the brain was imaged 

**To register your brain to an atlas, please follow the instructions for brainreg 
[here](/documentation/brainreg/user-guide/brainreg-napari)**.


A new output directory has been created, which contains the registered brain. We are now ready to use external pluggins to find a mask that covers the axonal projections.


## **Bulk axonal track detection**

Before we can proceed to register the axonal tracks in the imaged brain we need to install aditional Napari pluggins.

:::{caution}
Installation of external pluggins from the Napari hub are required.
* Make sure your conda environment is still activated!
* please follow the instructions for installing the  
[here](/documentation/brainreg/user-guide/brainreg-napari)**.
* Once installed we proceed to generate the layers that will contain our regions of interest
:::

## **Bulk axonal track tracing**

To open the graphical user interface, open napari and then load the `brainreg-segment` plugin (see 
[User guide](/documentation/brainreg-segment/user-guide/index)).

The `brainreg-segment`graphical user interface opens and shows a set of tools.You can then load your brainreg output 
directory, and follow the main brainreg-segment instructions [here](/documentation/brainreg-segment/user-guide/segmenting-1d-tracks) for 
segmenting external layers. Setting `Spline points` will determine how many times along the length of the track that 
the brain region is sampled at. This can be used to determine the brain region for each recording site on your probe.

**Instructions by** [**Sara Mederos**]
