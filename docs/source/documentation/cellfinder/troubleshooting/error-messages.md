# Debugging common error messages

## Error messages
### OSError: [Errno 24] Too many open files

```bash
OSError: [Errno 24] Too many open files
```

This is likely because your default limits are set too low. To fix this, follow the instructions 
[here](https://easyengine.io/tutorials/linux/increase-open-files-limit/). If for any reason you don't want to or 
can't change the system-wide limits, running `ulimit -n 60000` before running cellfinder should work. This setting 
will persist for the present shell session, but will have to be repeated if you open a new terminal.

### error: unrecognized arguments:

```bash
main.py: error: unrecognized arguments: data/dataset1
```

If what comes after `urecognised arguements` looks to be the part of the filepath you entered, after a space, 
then you should enclose the full path in quotation marks. (**i.e. `"/path/to/my data"` not `path/to/my data`**) . 
Otherwise cellfinder will interpret the path as two inputs, separated by a space.\)

### CommandLineInputError: File path: cannot be found.

```bash
imlib.general.exceptions.CommandLineInputError: File path: '/media/adam/Storage/cellfinder/data/dataset1' cannot be found.
```

If you see an error like this, there could be a few possible reasons, e.g.:

* The filepath that you've passed to cellfinder does not exist, maybe it's misspelled, or on a drive that isn't mounted?
* If the filepath that cannot be found looks to be the part of the filepath you entered, after a space, then you 
should enclose the full path in quotation marks. (**i.e. `"/path/to/my data"` not `path/to/my data`**) . Otherwise 
cellfinder will interpret the path as two inputs, separated by a space.)

### INFO:tensorflow:Error reported to Coordinator: Failed to get convolution algorithm

```bash
INFO:tensorflow:global_step/sec: 0
2019-05-17 13:04:53.550306: E tensorflow/stream_executor/cuda/cuda_dnn.cc:334] Could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR
2019-05-17 13:04:53.565467: E tensorflow/stream_executor/cuda/cuda_dnn.cc:334] Could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR
INFO:tensorflow:Error reported to Coordinator: Failed to get convolution algorithm. This is probably because cuDNN failed to initialize, so try looking to see if a warning log message was printed above.
```

If you see an error like this, it's likely to be one of two things, either your GPU memory is full, or an issue with 
your CUDA and cuDNN version.

Your GPU memory may be full if it is still being used by another process. To test this, run `nvidia-smi`, and you will 
see something like this:

```text
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.56       Driver Version: 418.56       CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  TITAN RTX           On   | 00000000:2D:00.0  On |                  N/A |
| 41%   38C    P2    55W / 280W |  23408MiB / 24187MiB |      4%      Default |
+-------------------------------+----------------------+----------------------+
```

The bit to look for is the memory use (`23408MiB / 24187MiB`), is this is nearly full (like the example) then 
find the culprit:

```text
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0     37793      C   ...miniconda3/envs/cellfinder/bin/python 23408MiB   |
+-----------------------------------------------------------------------------+
```

In this case, a previous run of cellfinder hasn't completed. Either wait for it to run, or cancel it with CTRL+C 
(in the terminal).

Alternatively, your version of CUDA and cuDNN may be not compatible with TensorFlow. You can update them by 
following the instructions [here](/documentation/setting-up/gpu).

### ImportError: DLL load failed: The specified module could not be found.

```bash
ImportError: DLL load failed: The specified module could not be found.
```

If this occurs on Windows, it is likely that you need to install "Microsoft Visual C++ Redistributable for Visual 
Studio 2015, 2017 and 2019", available from Microsoft's website 
[here](https://learn.microsoft.com/en-GB/cpp/windows/latest-supported-vc-redist?view=msvc-170).

### SyntaxError: invalid syntax \(logging\)

```bash
  File "/home/adam/projects/cellfinder/cellfinder/tools/tools.py", line 444
    logging.debug(f"Free memory is: {free_mem} bytes.")
                                                     ^
SyntaxError: invalid syntax
```

### Can't find /usr/local/opt/libpng/lib/libpng16.16.dylib

```
Can't find /usr/local/opt/libpng/lib/libpng16.16.dylib
```

This sometimes happens when running registration on macOS. You may need to install `libpng`. The first thing to 
do is to [install homebrew](https://brew.sh/) and then run:

```
brew install libpng
```

## Things that look like errors, but aren't:

Most things that are actually errors will interrupt cellfinder, and the program won't run. Other things will get 
logged with an `ERROR` or a `WARNING` flag and will get printed to the console in addition to the log file.

A number of third party modules may raise their own errors. As long as you understand what they mean, they can 
usually be safely ignored.

### Can't find openCV

```
CRITICAL:tensorflow:Optional Python module cv2 not found, please install cv2 and retry if the application fails.
```

Tensorflow thinks this is critical, it's not.

### CPU instruction sets

```
tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary 
was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
```

Unless you built tensorflow from source, something like this will come up. It'll still work fine

