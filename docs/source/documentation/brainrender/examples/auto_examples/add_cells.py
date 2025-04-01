"""
add_cells.py

This script demonstrates how to generate and visualize random labeled cells in a specific brain region using brainrender.

Example:
    Run this script to see labeled cells rendered in 3D space.

Functions:
    - main(): Executes the visualization process.
"""

import random
from pathlib import Path

import numpy as np
from myterial import orange
from rich import print

from brainrender import Scene
from brainrender.actors import Points

print(f"[{orange}]Running example: {Path(__file__).name}")


def get_n_random_points_in_region(region, N):
    """
    Gets N random points inside (or on the surface) of a mes
    """

    region_bounds = region.mesh.bounds()
    X = np.random.randint(region_bounds[0], region_bounds[1], size=10000)
    Y = np.random.randint(region_bounds[2], region_bounds[3], size=10000)
    Z = np.random.randint(region_bounds[4], region_bounds[5], size=10000)
    pts = [[x, y, z] for x, y, z in zip(X, Y, Z)]

    ipts = region.mesh.inside_points(pts).coordinates
    return np.vstack(random.choices(ipts, k=N))


scene = Scene(title="Labelled cells")

# Get a numpy array with (fake) coordinates of some labelled cells
mos = scene.add_brain_region("MOs", alpha=0.15)
coordinates = get_n_random_points_in_region(mos, 2000)

# Add to scene
scene.add(Points(coordinates, name="CELLS", colors="steelblue"))

# render
scene.content
scene.render()
