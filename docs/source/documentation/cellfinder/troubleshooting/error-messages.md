# Debugging common error messages

## Error messages

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

