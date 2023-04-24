# Rendering data

Once you've [downloaded](downloading-data.md) some neuronal morphological reconstructions from your dataset of choice, you can use `morphapi` to create 3d meshes which you can use to visualize your data \(e.g. in `brainrender`\).

The functions to load neurons from the various APIs return instances of `morphapi`'s `Neuron` class which can be used to create meshes for your neurons morphologies:

```python
neuron.create_mesh()
```

This will return two items:

* A `vedo` actor with the entire neuron's morphology
* A `dict` of `vedo` actors. One for `soma`, one for the `axons` and one for the `dendrites`. This can be useful when these different parts are to be colored differently or if not the entire neuron is to be visualized. 

By default `Neuron` caches the results of `create_mesh` to speed up subsequent visualizations of the same neuron. You can override this behaviour in with `create_mesh(use_cache=False)` but keep in mind that this is done automatically when rendering parameters are changed \(e.g. if `soma_radius` is changed\).

