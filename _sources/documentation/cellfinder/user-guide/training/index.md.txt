# Retraining the pre-trained network

Retraining the classification network is often the key step to ensure high-performance of cellfinder.
We recommend that the presupplied network is retrained for each new application (e.g. microscope, labelling strategy etc.).
The design of the cellfinder software means that this is different, but often simpler than other deep-learning-based analysis tools you may have used.


## Theory
:::{hint}
It may be useful to consult the [original PLOS Computational Biology paper](https://doi.org/10.1371/journal.pcbi.1009074)
to get a better idea of the ideas behind the software.
:::

### Pre-trained network

cellfinder is supplied with a network that was trained on approximately 100,000 manually annotated cell candidates (with a roughly 50/50 split between cells and non-cells).
These came from serial-section two-photon data with whole-cell labelling.
This is likely to be different from your data in some ways, e.g.:

- Microscopy technique
- Fluorescent label
- Labelled brain regions
- Labelled cell types

However, we usually find that this network is a good starting point in a new analysis.

### Workflow

The typical workflow for using cellfinder on new data is:

1. Run cellfinder using the pre-trained network (or a network you or a collaborator has already trained)
2. Assess the performance of the network
3. Generate training data to "correct" the network in areas it has performed poorly
4. Retrain the network
5. Run cellfinder with the new network
6. Repeat steps 2 to 5

Considering generating training data requires the input of a skilled human, but the other steps can be run automatically, we suggest that only small amounts of training data are generated at a time.
Training data can be pooled from separate batches of annotations, so the network can be iteratively improved step by step.

### Training data generation strategy

There is no "correct" way to create training data, but it is usually best to target the areas in which the current network performs worse.
Typically, we recommend generating 1000-5000 cell candidates with a roughly even split between;

- Correctly classified cells
- Correctly classified artefacts
- Incorrectly classified cells
- Incorrectly classified artefacts

This process would usually take 2-4 hours (with practice it usually becomes much quicker!).
Once the network is retrained, the process can be repeated until performance is satisfactory for the application.

:::{caution}
Make sure you save all your training data, you can reuse it later (or share it with others).
:::

## Training the network

### Generate training data

To generate training data, you will need:

* The cellfinder output file, `cell_classification.xml` as saved using either the napari plugin
or the Python API (it's automatically saved in the `brainmapper` `points` subdirectory).
* The raw data used initially for cellfinder

To generate training data for a single brain, use the 
[napari plugin](/documentation/cellfinder/user-guide/napari-plugin/training-data-generation).

### Start training

You can then use these yaml files for training, either using the
[napari plugin](/documentation/cellfinder/user-guide/napari-plugin/training-the-network), or the following 
command-line tool.

:::{hint}
If you would like to use the data that was originally used to train the supplied network, 
please see [Using supplied training data](using-supplied-data)
:::

```bash
cellfinder_train -y yaml_1.yaml  yaml_2.yaml -o /path/to/output/directory/
```

### Arguments

* `-y` or `--yaml` The path to the yaml files defining training data
*   `-o` or `--output` Output directory for the trained model (or model weights)


**Optional**

* `--continue-training` Continue training from an existing trained model. If no model or model weights are 
specified, this will continue from the included model.
* `--trained-model` Path to a trained model to continue training
* `--model-weights` Path to existing model weights to continue training
*   `--network-depth` Resnet depth (based on [He et al. (2015)](https://arxiv.org/abs/1512.03385)). Choose from

    (18, 34, 50, 101 or 152). In theory, a deeper network should classify better,

    at the expense of a larger model, and longer training time. **Default: 50**
* `--batch-size` Batch size for training (how many cell candidates to process at once). Default: 16
* `--epochs` How many times to use each sample for training. **Default: 1000**
* `--test-fraction` What fraction of data to keep for validation. **Default: 0.1**
* `--learning-rate` Learning rate for training the model
* `--no-augment` Do not use data augmentation
* `--save-weights` Only store the model weights, and not the full model. Useful to save storage space.
* `--no-save-checkpoints` Do not save the model after each training epoch. Useful to save storage space 
if you are happy to wait for the chosen number of epochs to complete. Each model file can be large, and if 
you don't have much training data, they can be generated quickly.
* `--tensorboard` Log to `output_directory/tensorboard`. Use `tensorboard --logdir outputdirectory/tensorboard` to view.
* `--save-progress` Save training progress to a .csv file (`output_directory/training.csv`).

### Further help

All `cellfinder_train` options can be found by running:

```bash
cellfinder_train -h
```


```{toctree}
:maxdepth: 1
:hidden:
using-supplied-data
```
