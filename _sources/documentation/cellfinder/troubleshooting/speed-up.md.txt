# Speeding up cellfinder

## Introduction

Before trying to troubleshoot, **cellfinder can be slow**.
Even on a very good desktop computer, a full analysis of a labelled mouse brain with many thousands of cells can take between 4-12 hours.

## Things to Try

### Use a better computer

Annoying advice, but a bigger, better computer will likely speed up cellfinder.
In particular, we recommend:

* Multicore CPU (the more cores and the faster the better)
* A recent NVIDIA GPU (the more VRAM and CUDA cores the better)
* Plenty of RAM (ideally >32GB)
* Fast local storage for your data (ideally SSD)

### Put your data on a fast hard drive

If your data is on a "normal" spinning hard drive, and you have a solid-state drive (SSD) available, putting your data on there will likely speed things up.

If your data is on a network drive (microscopy facility server, institutional file storage, etc.), consider moving it to your local machine first.

If you're using a compute cluster, there is likely to be a specific fast data storage area for this, maybe called `scratch`. Ask your sysadmins for help

## Specific Issues

### Cell classification or training the network is slow

:::{hint}
If you think that cellfinder is using the GPU properly, you can often increase the batch size used for training or inference.
This will depend on your specific GPU, but for inference, batch sizes of up to 128 often work well on modern GPUs with >8GB memory.
:::

These steps may be slow if cellfinder is not properly using the GPU.
If you have followed the instructions in [setting up your GPU](/documentation/setting-up/gpu), you may need to check that everything is configured properly.

:::{note}
As always, make sure your conda environment is activated
:::

Open a terminal (or Anaconda Prompt), start Python,

```bash
  python
```

and check that PyTorch can use the GPU,

```python
import torch
print(torch.cuda.is_available())
print([(i, torch.cuda.get_device_properties(i)) for i in range(torch.cuda.device_count())])
```

If you see something like the output below, then all is well.

```bash
True
[(0, _CudaDeviceProperties(name='NVIDIA GeForce RTX 4080', major=8, minor=9, total_memory=16049MB, multi_processor_count=76))]
```

If you see something like this:

```bash
False
[]
```

Then your GPU is not properly configured.
If you have followed everything in [setting up your GPU](/documentation/setting-up/gpu), please go speak to whoever administers your machine.
If you're still stuck [get in touch](/contact), but there is a limited amount we can do to help configure your system.
