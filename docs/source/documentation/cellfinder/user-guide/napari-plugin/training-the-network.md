# Retraining the network for new data


Once napari, and the cellfinder plugin is installed, open napari, and load the plugin 
(`Plugins` -> Train network).

:::{hint}
Make sure your GPU is set up to speed up the training. See 
[Setting up your GPU](/documentation/setting-up/gpu).
:::

## Set parameters

### **Mandatory**

* **YAML files** - choose at least one YAML file containing paths to training data
* **Output directory** - Choose (or create new) directory to save the trained models to

### **Optional**

**Network**&#x20;

* **Trained model** - Path to a trained model to continue training from
* **Model weights** - Path to existing model weights to continue training
* **Model depth** - Resnet depth (based on [He et al. (2015)](https://arxiv.org/abs/1512.03385)). 
Choose from 18, 34, 50, 101 or 152. In theory, a deeper network should classify better, at the expense 
of a larger model, and longer training time. **Default: 50**
* **Pretrained model** - Choose an existing model supplied with the software to continue training from.

When training your network, you can either train the network from scratch (not recommended), or 
select the **Continue training** box to retrain an existing network. Depending on how you want to 
train your network, different data or options must be supplied:

* If you are training a new network from scratch (i.e. **Continue training** is not selected), 
then you only need to select a **Model depth**.
* If you are continuing training from a default, pretrained model, only **Pretrained model** needs to be chosen.
* If you are continuing training from your own model, then only **Trained model** needs to be set.
* If you are continuing training from your own model weights (i.e. not the full model, 
saved when **Save weights** is checked).

**Training**

* **Continue Training** - Continue training from an existing trained model. If no model or 
model weights are specified, this will continue from the included model.
* **Augment** - Use data augmentation to synthetically increase the amount of training data
* **Tensorboard** - Log to `output_directory/tensorboard`. Use 
`tensorboard --logdir outputdirectory/tensorboard` to view.
* **Save weights** - Only store the model weights, and not the full model. Useful to save storage space.
* **Save checkpoints** - Save the model after each training epoch. Each model file can be large, and if you don't 
have much training data, they can be generated quickly. Deselect if you are training for many epochs, and you are 
happy to wait for the chosen number of epochs to complete.
* **Save progress** - Save training progress to a .csv file (`output_directory/training.csv`
* **Epochs** - How many times to use each sample for training. **Default: 100**
* **Learning rate** - Learning rate for training the model
* **Batch size** - Batch size for training (how many cell candidates to process at once). **Default: 16**
* **Test fraction** - What fraction of data to keep for validation. **Default: 0.1**

**Misc options**

* To ensure that cellfinder doesn't use all the CPU cores on a machine, the 
**Number of free cpus** can be set. **Default: 2**

:::{hint}
Parameter values will be saved between sessions. The values can be reset by clicking the **Reset defaults** button.
:::

## Run training

Click the **Run** button.&#x20;

The plugin will then run (this may take a while if you have lots of training data, 
or you have set many epochs). Trained models (`.h5` files) will be saved into your 
output directory, to be used for cell detection.
