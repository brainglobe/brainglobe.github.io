(target-brainglobe-atlasapi)=
# BrainGlobe Atlas API (brainglobe-atlasapi)

Many excellent brain atlases exist for different species. Some of them have an API (application programming interface)
to allow users to interact with the data programmatically (e.g. the excellent
[Allen Mouse Brain Atlas](https://portal.brain-map.org)), but many do not, and there is no consistent way to process
data from multiple sources.

The brainglobe atlas API deals with this problem by providing a common interface for programmers to download and process data from multiple sources.

## Atlases available

All atlases available through the API, with their descriptions, resolutions and brain regions, are listed in the
{ref}`BrainGlobe atlas search <target-atlas-search>`. From there, each atlas can be viewed in neuroglancer, and its template,
annotation, hemisphere map and ontology downloaded in a range of formats.

## Installation

BrainGlobe AtlasAPI works with Python >=3.10, and can be installed from PyPI with:

```bash
pip install brainglobe-atlasapi
```

## Usage
:::{note}
For a tutorial on how to use the basic features of the API, please see the [BrainGlobe Atlas API tutorial](../../api_examples/brainglobe_atlasapi).
:::

```{toctree}
:maxdepth: 2
usage/command-line-interface

```

## More details

```{toctree}
:maxdepth: 1
adding-a-new-atlas
```

## Citation

If you find the BrainGlobe Atlas API useful, please cite the paper in your work:

>Claudi, F., Petrucco, L., Tyson, A. L., Branco, T., Margrie, T. W. and Portugues, R. (2020). BrainGlobe Atlas API: a common interface for neuroanatomical atlases. Journal of Open Source Software, 5(54), 2668, <https://doi.org/10.21105/joss.02668>

**Don't forget to cite the developers of the atlas that you used!**


## API Reference

```{toctree}
:maxdepth: 1
api
```
