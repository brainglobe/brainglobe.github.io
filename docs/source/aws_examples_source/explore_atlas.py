"""
Interacting with cloud atlas data through Python
================================================

This example demonstrates how to calculate the volume of the retrosplenial area in the
Allen mouse brain atlas at 25um resolution. It does so avoiding use of BrainGlobe tools,
and using minimal other dependencies. It is intended to showcase the use of atlas data
directly.
"""

# %%
# This tutorial will guide through the steps needed to extract the volume of the retrosplenial area (RSP)
# in the Allen Mouse Brain Atlas, programmatically - but without using BrainGlobe. To do this, we 
# need some preliminary knowledge about how BrainGlobe atlases such as this are structured under the hood:
#
# - the annotation image is stored as an OME-Zarr <https://ngff.openmicroscopy.org/#next-generation-file-formats-ngff-ome-zarr>.
# - the region metadata (e.g. each region's id, name, acronym and parent) are stored in a comma separated (csv) file
# - these files (and other atlas files, like the template) are stored on AWS
#
# To compute the volume of RSP we will therefore
#
# - access the terminologies file
# - determine the id of the RSP region and all its children from the terminologies file
# - access the annotation file
# - count how many pixels in the annotation file correspond to any of the ids
# - convert the pixels to cubic millimeters
#
# Now the conceptual part is covered, let's dive into the code:
# 
# We start by importing some Python libraries that we will need 

import dask.array as da
import ngff_zarr as nz
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import colormaps as cm



# %%
# Next, we download the structures file using `pooch`

s3_bucket_stub = "s3://brainglobe/atlas/{}"
annotation_url = s3_bucket_stub.format("annotation-sets/allen-adult-mouse-annotation/2017/annotation.ome.zarr")
structures_file = s3_bucket_stub.format("terminologies/allen-adult-mouse-terminology/2017/terminology.csv")

terminologies_df = pd.read_csv(structures_file, storage_options={"anon": True})

# %%
# By printing the dataframe, we can observe that the structures file contains one row per region, with the first column (index 0) containing the region abbreviation, and the second column (index 1) containing the region ID:

terminologies_df.head()


# %%
# We know that all child regions of RSP have an abbreviation starting with "RSP", which we can use to identify our IDs of interest
# and store them in a list called `rsp_ids`.

terminologies_filtered = terminologies_df[terminologies_df["abbreviation"].str.startswith("RSP")]

rsp_ids = terminologies_filtered["annotation_value"].tolist()

# %%
# Equipped with this information, we can now access the annotations file for the atlas.
# Annotation files are stored in an OME-zarr file in the cloud.

annotations = nz.from_ngff_zarr(annotation_url, storage_options={"anon": True})

print(annotations.metadata)

# %% 
# We can see from the metadata that the zarr contains multiple resolution levels (a pyramid).
# For this tutorial, we will use the highest resolution level (level 0).

annotation_array = annotations.images[0].data

print(annotation_array)

# %%
# By plotting a slice of the array contents, we can see the various regions encoded by integer values:

# Get the middle section and plot
middle_section = annotation_array.shape[0] // 2

# Create a cyclic colormap due to the high values in the Allen atlas
N = 512
colors = cm.get_cmap('tab20').resampled(N)
lut = colors(np.arange(N))

# Map label image to lookup table and plot
plt.imshow(lut[annotation_array[middle_section,:,:] % N])

# %%
# Combining the annotation data with our RSP IDs allows us to calculate the volume of the RSP,
# which we finally print. This reaches the goal of this tutorial.
print(annotations.images[0].scale)
print(annotations.images[0].axes_units)

num_pixels = da.isin(annotation_array[:], rsp_ids).sum().compute()
pixel_size_list = annotations.images[0].scale.values()
pixel_volume = pixel_size_list[0] * pixel_size_list[1] * pixel_size_list[2]  # in cubic millimeters

print(f"RSP has volume of around {np.round(num_pixels*pixel_volume)} cubic millimeters")

# %%
# In conclusion, this tutorial shows how to programmatically access and process atlas data for 
# the specific purpose of calculating a region volume. More generally, it also constitutes an example for
# BrainGlobe atlas data being used independently of the BrainGlobe software tools.
