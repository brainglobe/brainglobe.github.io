# Using cellfinder at the SWC

N.B. Before starting to use cellfinder on the SWC. It is recommended to familarise yourself with the job scheduler system
([SLURM](https://slurm.schedmd.com/documentation.html)).

:::{hint}
This information refers to using cellfinder for cell detection and registration, but any of the BrainGlobe 
command-line tools (e.g. training cellfinder, or running only registration with brainreg) can be used similarly.
:::

## Interactive use

On the SWC cluster, no software needs to be installed, as cellfinder can be loaded with `module load brainglobe`.

Cellfinder can be used interactively, by starting an interactive job:

```bash
srun -p gpu --gres=gpu:1 -n 20 -t 0-24:00 --pty --mem=120G bash -i
```

Loading cellfinder:

```bash
module load brainglobe
```

And then running cellfinder as per the [User guide](index).

## Batch processing

It is recommended to use cellfinder by using the batch submission system. This has many advantages:

Your analysis is reproducible \(you have a script showing exactly what you did\)
* You don't need to wait for computing resources to become available \(once submitted, the job will wait until it can be run\)
* If for any reason the analysis is interrupted, you can easily restart
* You don't need to keep a connection to the cluster open
* You can easily receive email updates when the job starts and finishes.

An example batch script is given below, but it is recommended to familarise yourself with the batch submission system before trying to optimise cellfinder.

```bash
#!/bin/bash

#SBATCH -p gpu # partition (queue)
#SBATCH -N 1   # number of nodes
#SBATCH --mem 120G # memory pool for all cores
#SBATCH --gres=gpu:1
#SBATCH -n 10
#SBATCH -t 1-0:0 # time (D-HH:MM)
#SBATCH -o cellfinder.out
#SBATCH -e cellfinder.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=youremail@domain.com

cell_file='/path/to/signal/channel'
background_file='path/to/background/channel'
output_dir='/path/to/output/directory'

echo "Loading brainglobe environment"
module load brainglobe

echo "Running cellfinder"
# Just an example. See the user guide for the specific parameters
cellfinder -s $cell_file -b $background_file -o $output_dir -v 5 2 2 --orientation psl
```



