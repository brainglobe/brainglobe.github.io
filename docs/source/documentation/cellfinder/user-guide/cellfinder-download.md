# Downloading the pre-trained model in advance

`cellfinder` will download the pre-trained model when it's needed. However, you may want to download this model in 
advance to save time later, or if you know your internet connection will be disrupted. For this reason, cellfinder 
comes with a command-line tool (`cellfinder_download`) to download a pre-trained model.

To download the recommended model, just run `cellfinder_download`. However, you can also use the following options:

* `--install-path` Use this flag to choose where you would like to download the model to, and also update the 
cellfinder config file (at `~/.brainglobe/cellfinder/cellfinder.conf.custom`) to point to this location. 
By default, models are saved in your home directory at `~/.brainglobe/cellfinder/models`.
* `--model` Use this flag to specify a specific model. The default model is `restnet50_tv`, which is (currently) the 
only recommended model to use. 
* `--no-amend-config` Use this flag to ensure the cellfinder config file is not updated (useful if you just want to 
download the trained model)