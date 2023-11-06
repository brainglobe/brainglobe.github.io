# Use with docker

## Prerequisites

* Linux machine ([most common distributions are supported](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html))
* Recent NVIDIA GPU ([compute capability](https://en.wikipedia.org/wiki/CUDA) >=3)
* [NVIDIA driver](https://www.nvidia.co.uk/Download/index.aspx?lang=en-uk) >= 418.81.07
* [Docker version](https://docs.docker.com/engine/install/) >= 19.03

## Setup

**Install NVIDIA Container Toolkit**

Full instructions are [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

## Running cellfinder

To run with GPU support, and mount the current working directory at `/data`**:**

```bash
docker container run --mount type=bind,source=${PWD},target=/data --gpus all -it ghcr.io/brainglobe/cellfinder
```

This will open up a bash prompt, and you can use cellfinder (or brainreg etc.) to analyse your data (mounted at `/data`) as normal, e.g.:

```bash
cellfinder -s /data/brain1/channel0 -b /data/brain1/channel1 -v 5 2 2 --orientation psl -o /data/analysis/brain1 --trained-model /data/models/retrained.h5
```

To leave the docker container when done, just `exit`.The data will be saved onto the host system, at your current working directory (you can mount different directories, or multiple directories, see the [docker documentation](https://docs.docker.com/storage/bind-mounts/)).
