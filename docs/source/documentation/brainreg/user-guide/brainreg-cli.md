# Command line tool

## Basic usage

```bash
brainreg /path/to/raw/data /path/to/output/directory -v 5 2 2 --orientation osl
```

:::{hint}
Full command-line arguments are available with `brainreg -h`
:::

:::{caution}
If you have any spaces in your file-path, please enclose it in quotation marks, otherwise brainreg will interpret it as two inputs, separated by a space.
**i.e. `"/path/to/my data"` not `path/to/my data`.**
:::

## Arguments

### Mandatory

* Path to the directory of the images. (Can also be a text file pointing to the files)
* Output directory for all intermediate and final results

:::{hint}
You must also specify the orientation and voxel size of your data, see [Image definition](/documentation/setting-up/image-definition).
:::

### Additional options

* `-a` or `--additional` Paths to N additional channels to also register to the same coordinate space.
* `--sort-input-file` If set to true, the input text file will be sorted using natural sorting. This means that the 
file paths will be sorted as would be expected by a human and not purely alphabetically

#### Misc options

* `--n-free-cpus` The number of CPU cores on the machine to leave unused by the program to spare resources.
* `--debug` Debug mode - will increase verbosity of logging and save all intermediate files for diagnosis of software issues.
* `--save-original-orientation` Option to save the registered atlas with the same orientation as the input data.
* `--brain_geometry` To allow brain sub-volumes to be processed. Currently, the options are `full` 
(default, whole brain), `hemisphere_l` (only the left hemisphere) and `hemisphere_r` (only the right hemisphere).
* `--pre-processing` To specify the preprocessing method used before registration. Currently, the only options 
are `default` or `skip`. Use `skip` to ensure no preprocessing is performed.

### Atlas

By default, brainreg will use the 25&mu;m version of the [Allen Mouse Brain Atlas](https://mouse.brain-map.org/). To 
use another atlas (e.g. for another species, or another resolution), you must use the `--atlas` flag, followed by 
the string describing the atlas, e.g.:

```bash
--atlas allen_mouse_50um
```

:::{hint}
To find out which atlases are available, once brainreg is installed, please run `brainglobe list`. The name of the 
resulting atlases is the string to pass with the `--atlas` flag.
:::

### Registration backend

To change the registration algorithm used, use the `--backend` flag. The default is `niftyreg` as that is 
currently the only option.

### Registration options

To change how the actual registration performs, see [Registration parameters](parameters)
