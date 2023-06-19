# Using Notebooks

`brainrender` can be used with Jupyter notebooks in two ways:

1. you can **embed** a window with your rendered scene
2. you can have your scene be rendered in a **pop-up** window.

For an example of how to use `brainrender` with `jupyter` have a look 
[here](https://github.com/brainglobe/brainrender/blob/master/examples/notebook_workflow.ipynb).

## Rendering your scene in a separate window

If you want to have your scene be rendered in a new window, then you just need to set this option before your create your `scene`.

```python
from vedo import embedWindow
embedWindow(None) 
```

After this everything will work exactly the same as usual, and you will have access to all of `brainrender`'s features!

## Embedding renderings in Jupyter notebooks

:::{hint}
When embedding renderings in Jupyter Notebook not all of `brainrender`'s functionality will work! 
If you want to support all of `brainrender`'s features you should **not embed** renderings in the notebooks.

Note that this is due to the backend \(`k3d`\) used to embed the renderings not because of `brainrender`.
:::

If you want to embed your scene anyway, you can do that as either a `k3d` panel or a with `itkwidgets` by setting:

```python
embedWindow('k3d') # or 'itkwidgets' 
```

If you chose `k3d` then to rendered your scene:

```python
from vedo import show

# scene.render now will prepare the scene for rendering, 
# but it won't render anything yet
scene.render()

# to actually display the scene we use `vedo`'s `show` 
# method to show the scene's actors
show(scene.actors)
```

and with `itkwidgets`:

```python
from ipywidgets import VBox, Button
VBox([show(scene.actors)])
```



