# Downloading data

## Allen Morphology

The `AllenMorphology` class is used to download data for this dataset. It can be used to specify neurons from a given species and brain regions, like in the example below:

```python
from morphapi.api.allenmorphology import AllenMorphology


am = AllenMorphology()


# Select mouse neurons in the primary visual cortex
neurons = am.neurons.loc[
    (am.neurons.species == "Mus musculus")
    & (am.neurons.structure_area_abbrev == "VISp")
]

# Download some of these neurons
neurons = am.download_neurons(neurons[:5].id.values)
```

## Neuromorpho

Neuromorpho.org is a vast online repository of morphological data. The `NeuroMorpOrgAPI` class can be used to download data from it. Note that given the size of this huge dataset, it is not possible to download all metadata matching specific criteria at once.

```python
from morphapi.api.neuromorphorg import NeuroMorpOrgAPI

api = NeuroMorpOrgAPI()

# ---------------------------- Downloading metadata --------------------------- #
# Get metadata for pyramidal neurons from the mouse cortex.
metadata, _ = api.get_neurons_metadata(
    size=10,  # Can get the metadata for up to 500 neurons at the time
    species="mouse",
    cell_type="pyramidal",
    brain_region="neocortex",
)

# To get a list of available query fields: print(api.fields)
# To get a list of valid values for a field: print(api.get_fields_values(field))
print("Neurons metadata:")
print(metadata[0])

# ---------------------------- Download morphology --------------------------- #
neurons = api.download_neurons(metadata[5])

```



## MouseLight

To download neurons morphologies from Janelia Campus' MouseLight project, you can use the `MouseLightAPI` class. 

```python
from morphapi.api.mouselight import MouseLightAPI


# ---------------------------- Downloading neurons --------------------------- #
mlapi = MouseLightAPI()

# Fetch metadata for neurons with soma in the secondary motor cortex
neurons_metadata = mlapi.fetch_neurons_metadata(
    filterby="soma", filter_regions=["MOs"]
)

# Then we can download the files
neurons = mlapi.download_neurons(neurons_metadata[0])

```



## Mpin Zebrafish

To download neurons registered to a zebrafish atlas, you can use the `MpinMorphologyAPI` class.

```python
from morphapi.api.mpin_celldb import MpinMorphologyAPI


api = MpinMorphologyAPI()

# ----------------------------- Download dataset ----------------------------- #
"""
    If it's the first time using this API, you'll have to download the dataset
    with all of the neurons' data.
"""
api.download_dataset()
# You can then inspect metadata about all neurons:
print(api.neurons_df.head())


# Get neurons for a given brain structure
neurons_ids = api.get_neurons_by_structure(837)


# and load the selected neurons
neurons = api.load_neurons(neurons_ids)

```



