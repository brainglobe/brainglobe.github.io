# Retraining the pre-trained network


Retraining the classification network is often the key step to ensure high-performance of cellfinder.
We recommend that the presupplied network is retrained for each new application
(e.g. microscope, labelling strategy etc.). The design of the cellfinder software means that this is 
different, but often simpler than other deep-learning-based analysis tools you may have used.

:::{hint}
It may be useful to consult the [original PLOS Computational Biology paper](https://doi.org/10.1371/journal.pcbi.1009074) 
to get a better idea of the ideas behind the software.
:::

## Pre-trained network
cellfinder is supplied with a network that was trained on approximately 100,000 manually annotated cell candidates 
(with a roughly 50/50 split between cells and non-cells). These came from serial-section two-photon data with 
whole-cell labelling. This is likely to be different from your data in some ways, e.g.:
- Microscopy technique
- Fluorescent label
- Labelled brain regions
- Labelled cell types

However, we usually find that this network is a good starting point in a new analysis. 

## Workflow
The typical workflow for using cellfinder on new data is:
1. Run cellfinder using the pre-trained network (or a network you or a collaborator has already trained)
2. Assess the performance of the network
3. Generate training data to "correct" the network in areas it has performed poorly
4. Retrain the network
5. Run cellfinder with the new network
6. Repeat steps 2 to 5

Considering generating training data requires the input of a skilled human, but the other steps can be run automatically,
we suggest that only small amounts of training data are generated at a time. Training data can be pooled from separate  
batches of annotations, so the network can be iteratively improved step by step. 

## Training data generation strategy
There is no "correct" way to create training data, but it is usually best to target the areas in which the current 
network performs worse. Typically, we recommend generating 1000-5000 cell candidates with a roughly even split between 
- Correctly classified cells
- Correctly classified artefacts
- Incorrectly classified cells
- Incorrectly classified artefacts

This process would usually take 2-4 hours (with practice it usually becomes much quicker!).

Once the network is retrained, the process can be repeated until performance is satisfactory for the application. 

:::{caution}
Make sure you save all your training data, you can re-use it later (or share it with others).
:::