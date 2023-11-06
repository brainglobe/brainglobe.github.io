# Speeding up cellfinder

## Introduction

Before trying to troubleshoot, **cellfinder can be slow**. Even on a very good desktop computer, a full analysis of a 
labelled mouse brain with many thousands of cells can take between 4-12 hours.

## Things to Try

### Use a better computer

Annoying advice, but a bigger, better computer will likely speed up cellfinder. In particular, we recommend:
* Multicore CPU (the more cores and the faster the better)
* A recent NVIDIA GPU (the more VRAM and CUDA cores the better).
* Plenty of RAM. If you want to register your images to an atlas, this can use up to 50GB of RAM (depending on the atlas)
* Fast local storage for your data (ideally SSD)


### Put your data on a fast hard drive

If your data is on a "normal" spinning hard drive, and you have a solid-state drive (SSD) available, putting 
your data on there will likely speed things up.

If your data is on a network drive (microscopy facility server, institutional file storage, etc.), 
consider moving it to your local machine first.

If you're using a compute cluster, there is likely to be a specific fast data storage area for this, 
maybe called `scratch`. Ask your sysadmins for help

## Specific Issues

### Cell classification or training the network is slow

:::{hint}
If you think that cellfinder is using the GPU properly, you can often increase the batch size used for training or 
inference. This will depend on your specific GPU, but for inference, batch sizes of up to 128 
often work well on modern GPUs with >8GB memory.
:::

These steps may be slow if cellfinder is not properly using the GPU. If you have followed the instructions in 
[setting up your GPU](/documentation/setting-up/gpu), you may need to check that everything is configured properly:

Open a terminal (or Anaconda Prompt):

:::{note}
As always, make sure your conda environment is activated
:::

Start Python

```bash
  python
```

Check that tensorflow can use the GPU

```python
import tensorflow as tf
tf.test.is_gpu_available()
```

If you see something like this, then all is well.

```bash
2019-06-26 10:51:34.697900: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX512F
2019-06-26 10:51:34.881183: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1432] Found device 0 with properties: 
name: TITAN RTX major: 7 minor: 5 memoryClockRate(GHz): 1.77
pciBusID: 0000:2d:00.0
totalMemory: 23.62GiB freeMemory: 504.25MiB
2019-06-26 10:51:34.881217: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1511] Adding visible gpu devices: 0
2019-06-26 10:51:35.251465: I tensorflow/core/common_runtime/gpu/gpu_device.cc:982] Device interconnect StreamExecutor with strength 1 edge matrix:
2019-06-26 10:51:35.251505: I tensorflow/core/common_runtime/gpu/gpu_device.cc:988]      0 
2019-06-26 10:51:35.251511: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1001] 0:   N 
2019-06-26 10:51:35.251729: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] Created TensorFlow device (/device:GPU:0 with 195 MB memory) -> physical GPU (device: 0, name: TITAN RTX, pci bus id: 0000:2d:00.0, compute capability: 7.5)
True
```

If you see something like this:

```bash
2020-05-11 12:02:11.891275: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-05-11 12:02:11.948022: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 1992000000 Hz
2020-05-11 12:02:11.949756: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x55ae9ffc5860 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-11 12:02:11.949823: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-05-11 12:02:11.954796: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory
2020-05-11 12:02:11.954847: E tensorflow/stream_executor/cuda/cuda_driver.cc:351] failed call to cuInit: UNKNOWN ERROR (303)
2020-05-11 12:02:11.954894: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (hostname): /proc/driver/nvidia/version does not exist
False
```

Then your GPU is not properly configured. If you have followed everything in 
[setting up your GPU](/documentation/setting-up/gpu), please go speak to whoever administers your machine. If you're 
still stuck [get in touch](/contact), but there is a limited amount we can do to help configure your system.

