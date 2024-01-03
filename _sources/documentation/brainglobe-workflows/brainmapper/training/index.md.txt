# Training the network

Cellfinder includes a pretrained network for cell candidate classification. This will likely need to be retrained for 
different applications. Rather than generate training data blindly, the aim is to reduce the amount of hands-on 
time by only generating training data where cellfinder classified a cell candidate incorrectly.

:::{hint}
If you don't have any data yet, and want to try out the training see [Using supplied training data](using-supplied-data)
:::

## Generate training data

To generate training data, you will need:

* The cellfinder output file, `cell_classification.xml` (it's in the `points` subdirectory).
* The raw data used initially for cellfinder

To generate training data for a single brain, use the 
[napari plugin](/documentation/cellfinder/user-guide/napari-plugin/training-data-generation).

## Start training

You can then use these yaml files for training, either using the
[napari plugin](/documentation/cellfinder/user-guide/napari-plugin/training-the-network), or the following 
command-line tool.

:::{caution}
If you have any yaml files from previous versions of cellfinder, they will continue to work, but are not documented 
here. Just use them as you would the files from the napari plugin._&#x20;
:::

:::{hint}
If you would like to use the data that was originally used to train the supplied network, 
please see [Using supplied training data](using-supplied-data)
:::

```bash
cellfinder_train -y yaml_1.yml  yaml_2.yml -o /path/to/output/directory/
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
