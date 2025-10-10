"""
Interacting with cloud atlas data through Python
=====================

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
# - the annotation image is stored in a zipped [zarr](https://zarr.dev/) array.
# - the region metadata (e.g. each region's id, name, acronym and parent) are stored in a comma separated (csv) file
# - these files (and other atlas files, like the template) are stored on AWS
#
# To compute the volume of RSP we will therefore
#
# - download the structures file
# - determine the id of the RSP region and all its children from the structures file
# - download the annotation file
# - count how many pixels in the annotation file correspond to any of the ids
# - convert the pixels to cubic millimeters
#
# Now the conceptual part is covered, let's dive into the code:
# 
# We start by importing some Python libraries that we will need 

import pooch
import numpy as np
import zarr
from pathlib import Path


# %%
# Next, we download the structures file using `pooch` (TODO download from AWS instead)

atlas_url = "https://gin.g-node.org/BrainGlobe/atlases-v2/raw/master/annotations/allen_mouse_v1/"
structures_file = "structures.csv"

csv_path = pooch.retrieve(
    url=atlas_url+"/"+structures_file,
    known_hash="a04e9f6656c98bcd6d9d4c0ba2bd0ef927cf5cb97658ded9cda8237ad4575ff2",
    path=pooch.os_cache("brainglobe_atlases")
)

# %%
# By printing the rows, we can observe that the structures file contains one row per region, with the first column (index 0) containing the region acronym, and the second column (index 1) containing the region ID:

with open(csv_path) as file:
    for i, row in enumerate(file):
        if i >= 10:
            break
        print(row)


# %%
# We know that all child regions of RSP have a name starting with "RSP", which we can use to identify our IDs of interest
# and store them in a list called `rsp_ids`.

rsp_ids = []

with open(csv_path) as file:
    for row in file:
        entries = row.split(",")
        if entries[0].startswith("RSP"):
            rsp_ids.append(int(entries[1]))

# %%
# Equipped with this information, we can now download the annotations file for the atlas.
# Annotation files are stored in zipped zarr files in the cloud.

ZARR_ANNOTATIONS_FILENAME = "25um.zarr.zip"
zarr_path = pooch.retrieve(
    url=atlas_url+"/"+ZARR_ANNOTATIONS_FILENAME,
    known_hash=None,
    processor=pooch.Unzip(),
    path=pooch.os_cache("brainglobe_atlases")
)

print(zarr_path)

# %% 
# After downloading and unzipping, we can open the zarr folder, which contains a single zarr array.

zarr_array = zarr.open(Path(zarr_path[0]).parent, mode="r")

print(zarr_array)

# %%
# Combining the annotation data with our RSP IDs allows us to calculate the volume of the RSP,
# which we finally print. This reaches the goal of this tutorial.
num_pixels = np.isin(zarr_array[:], rsp_ids).sum()
pixel_volume = 25*25*25
cubic_microns_to_cubic_millimeters = 1.0/1000**3

print(f"RSP has volume of around {np.round(num_pixels*pixel_volume*cubic_microns_to_cubic_millimeters)} cubic millimeters")

# %%
# In conclusion, this tutorial shows how to programmatically access and process atlas data for 
# the specific purpose of calculating a region volume. More generally, it also constitutes an example for
# BrainGlobe atlas data being used independently of the BrainGlobe software tools.
