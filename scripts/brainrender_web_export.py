from brainrender import Scene
from brainrender.actors import Points
import pandas as pd
from myterial import salmon

scene = Scene()

# Load and add cells
coords = pd.read_hdf("./data/cell-detect-paper-cells.h5")
cells = scene.add(
    Points(coords[["x", "y", "z"]].values, radius=30, colors=salmon)
)
scene.add_silhouette(cells, lw=1)

# add brain regions
rsp = scene.add_brain_region(
    "RSP",
    alpha=0.5,
    silhouette=True,
)
scene.add_brain_region(
    "TH",
    alpha=0.15,
    color=[0.6, 0.6, 0.6],
    silhouette=True,
)
# cut and render
scene.render()
scene.close()
scene.export("brainrender.html")