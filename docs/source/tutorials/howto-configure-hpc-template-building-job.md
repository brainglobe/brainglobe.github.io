
# Configuring a template-building run on the HPC

:::{caution}
This tutorial uses `brainglobe-template-builder` which is still in early development. This means features are missing and things may change a lot. We welcome your feedback on how this works for you - please get [in touch](/contact)!
:::

This how-to guide documents how to run a configure a Slurm job to make a template. 

## Before you start

:::{note}
You will need access to a high-performance computing (HPC) platform to build a template. On the HPC, you will need to have ANTs and the optimizedANTs scripts installed and available on your path. See our [installation guide](https://github.com/brainglobe/brainglobe-template-builder/blob/main/README.md#installation) for more details. In our case, we have this as [an `Lmod` module](https://lmod.readthedocs.io/en/latest/) that we can access by calling `module load template-builder`.


You will also require, in an otherwise empty "template folder":
* A `brain_paths.txt` file, containing absolute paths to each `.nii.gz` image file to include in your template
* A `mask_paths.txt` file, containing absolute paths to each `.nii.gz` mask file, matching your image files
* Initial familiarity with `bash`, and ideally Slurm.

These can be obtained (for example) following our ["How to prepare input images for template building" guide](./howto-process-for-template-building.md).
:::

## Configure the Slurm script

Save the script below as `configure_slurm.sh` and adapt it for your purposes:

```bash
#!/bin/bash

#SBATCH -J <job_name> # job name
#SBATCH -p cpu # partition
#SBATCH -N 1   # number of nodes
#SBATCH --mem 64G # memory pool for all cores
#SBATCH -n 10 # number of cores
#SBATCH -t 0-01:00 # time (D-HH:MM)
#SBATCH -o std_slurm/slurm.%x.%N.%j.out # write STDOUT
#SBATCH -e std_slurm/slurm.%x.%N.%j.err # write STDERR
#SBATCH --mail-type=ALL
#SBATCH --mail-user=<user@email.com>

# Load the required module
module load template-builder

# Set up QBATCH variables to configure parallel jobs that will be spawned by modelbuild.sh
export QBATCH_PPJ=1
export QBATCH_CHUNKSIZE=1
export QBATCH_CORES=24
export QBATCH_SYSTEM="slurm"
export QBATCH_QUEUE="cpu"
export QBATCH_MEM="128G"
export QBATCH_OPTIONS="--mail-type=ALL --mail-user=<user@email.com> --mem 128G"

# Define atlas-forge directory, species and template names, and average type
TEMPLATE_DIR="<template_folder>"
AVE_TYPE="efficient_trimean"

if [ ! -d "${TEMPLATE_DIR}" ]; then
  mkdir $TEMPLATE_DIR
  echo "Created new template directory ${TEMPLATE_DIR}"
else
  echo "Continuing work on existing template in ${TEMPLATE_DIR}"
fi

# (optional) point to initial target.
# if not using an initial target, delete the related lines
INITIAL_TARGET="${template_dir}/<initial_target.nii.gz>" 

if [ ! -f "${INITIAL_TARGET}" ]; then
  echo "Error: Initial target not found"
  exit 1
fi

# Path to the bash script that builds the template
# This can be obtained from github.com/brainglobe/brainglobe-template-builder/blob/main/scripts/build_template_with_slurm.sh
BUILD_SCRIPT="</path/to/build_template_with_slurm.sh>"

if [ ! -f $BUILD_SCRIPT ]; then
  echo "Error: ${BUILD_SCRIPT} does not exist."
  exit 1
fi

# Run the script to build the template
bash $BUILD_SCRIPT --template-dir $TEMPLATE_DIR \
  --average-type $AVE_TYPE \
  --toggle-dry-run "--no-dry-run" \
  --walltime-short "10:00:00" \
  --walltime-linear "20:00:00" \
  --walltime-nonlinear "240:00:00" \
  --initial_target $INITIAL_TARGET # if not using an initial target, pass "--initial_target first" instead
```

You will at least need to set
* the slurm job name (`<job_name>`): you can choose this, make it expressive
* your email (`<user@email.com>`, twice): slurm will send notification emails here
* the template folder path (`<template_folder>`): the absolute path to the folder with your input text files, where your template will be made.
* the build script path (`<path/to/build_template_with_slurm.sh>`): the absolute path to a local version of the build script.
* the initial target path (`<path/to/initial_target.nii.gz`), if using. F

You may also want to customise with
* the [slurm job variables](https://slurm.schedmd.com/heterogeneous_jobs.html)
* the [`qbatch` environmental variables](https://github.com/CoBrALab/qbatch/blob/master/README.md), in particular `QBATCH_QUEUE` should match the name of a partition on your HPC, otherwise parallelisation will not work.

If you want to [customise `modelbuild.sh` in more detail](https://github.com/CoBrALab/optimized_antsMultivariateTemplateConstruction/blob/master/modelbuild.sh)(beyond the option shown in our example configuration script), you will have to adapt the build script instead of the configuration script.

### Launch the Slurm job

In a terminal connected to your HPC, navigate to your configuration script.
```bash
cd </path/to/template/folder>
```
and submit your script to the Slurm queue
```bash
sbatch configure_slurm.sh
```
The configuration job will spawn a number of parallel jobs (depending on how you have set up [your `qbatch` environmental variables](https://github.com/CoBrALab/qbatch/blob/master/README.md) in the configuration script).

### Monitor Slurm job

TODO
For troubleshooting, you can check the various logs for an indication of where things went wrong.
* explain structure of outputs
* point to which logs are where
