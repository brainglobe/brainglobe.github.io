# Running cellfinder

cellfinder runs with a single command, with various arguments that are detailed in 
[Command line options](/documentation/cellfinder/user-guide/command-line/cli). To analyse the example data, the flags 
we need are:

* `-s` The primary **s**ignal channel: `test_brain/ch00`
* `-b` The secondary autofluorescence channel \(or **b**ackground\): `test_brain/ch01`
* `-o` The **o**utput directory :  `test_brain/output`
* `--orientation` The data orientation: `psl`
* `-v` The **v**oxel spacing in the same order as the data orientation \(`psl`\): `5 2 2` 
* `--atlas` The atlas we want to use: `allen_mouse_10um`

:::{hint}
If your machine has less than 32GB of RAM, you should use the `allen_mouse_25um` atlas either way, 
as registration with the high-resolution atlas requires about 30GB for this image.
:::

Putting this all together into a single command gives:

```text
cellfinder -s test_brain/ch00 -b test_brain/ch01 -o test_brain/output -v 5 2 2 --orientation psl --atlas allen_mouse_10um
```

This command will take quite a long time (anywhere from 2-10 hours) to run, depending on:

* The speed of the disk the data is stored on
* The CPU speed and number of cores
* The GPU you have

:::{hint}
You'll know cellfinder has finished when you see something like this:  
`2020-10-14 00:07:20 AM - INFO - MainProcess main.py:86 - Finished. Total time taken: 3:22:42`
:::

If you just want to check that everything is working, we can speed everything up by:

* Only analysing part of the brain using the flags: `--start-plane 1500 --end-plane 1550`
* Using a lower-resolution atlas, using the flag: `--atlas allen_mouse_25um`

```text
cellfinder -s test_brain/ch00 -b test_brain/ch01 -o test_brain/output -v 5 2 2 --orientation psl --atlas allen_mouse_25um --start-plane 1500 --end-plane 1550
```

:::{hint}
If the cell classification step takes a (very) long time, it may not be using the GPU. If you have an NVIDIA GPU, 
see [Speeding up cellfinder](/documentation/cellfinder/troubleshooting/speed-up) to make sure that your GPU is set up properly.
:::

Once cellfinder has run, you can go onto [Visualising the results](visualising-the-results)

