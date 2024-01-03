# Using Notebooks

`brainrender` can be used with Jupyter notebooks in two ways:

1. you can **embed** a window with your rendered scene
2. you can have your scene be rendered in a **pop-up** window.


## Rendering your scene in a separate window

If you want your scene to be rendered in a new window, then set this option before you create 
your `Scene`.

```python
import vedo
vedo.settings.default_backend= 'vtk'
```

After this everything will work exactly the same as usual, and you will have access to all of `brainrender`'s features.
E.g. to visualise primary visual cortex in the Allen Adult Mouse Brain Atlas:

```python
import vedo
vedo.settings.default_backend= 'vtk'

from brainrender import Scene
popup_scene = Scene(atlas_name='allen_mouse_50um', title='popup')

popup_scene.add_brain_region('VISp')

popup_scene.render()  # press 'Esc' to close
```
## Embedding renderings in Jupyter notebooks

:::{hint}
When embedding renderings in Jupyter Notebook not all of `brainrender`'s functionality will work! 
If you want to support all of `brainrender`'s features you should **not embed** renderings in the notebooks.

Note that this is due to the backend \(`k3d`\) used to embed the renderings not because of `brainrender`.
:::

If you still need to embed your `Scene` then `brainrender` works slightly differently. E.g. to visualise the 
tectum in the larval zebrafish atlas:

```python
# Set the backend
import vedo
vedo.settings.default_backend= 'k3d'

# Create a brainrender scene
from brainrender import Scene
scene = Scene(atlas_name='mpin_zfish_1um', title='Embedded')  # note the title will not actually display
scene.add_brain_region('tectum')

# Make sure it gets embedded in the window
scene.jupyter = True

# scene.render now will prepare the scene for rendering, but it won't render anything yet
scene.render()

# To display the scene we use `vedo`'s `show` method to show the scene's actors
from vedo import Plotter  # <- this will be used to render an embedded scene 
plt = Plotter()
plt.show(*scene.renderables)  # same as vedo.show(*scene.renderables)
```

:::{hint}
As with all BrainGlobe tools, if you do not have these atlases locally, the first time you run the commands 
it may be slow as the data is downloaded.
:::