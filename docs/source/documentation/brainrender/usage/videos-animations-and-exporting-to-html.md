# Videos, animations and exporting to html

A key goal for `brainrender` was to facilitate the dissemination of neuroanatomical data. To do so, creating
spectacular renderings is not enough, you need to have a way to export them into a format that you can easily share.
For this reason we've put a lot of effort into allowing you to do just that by creating screenshots, animated videos
and interactive online visualizations with your renderings.

You can find examples about how to do all of this at the
[GitHub repository](https://github.com/brainglobe/brainrender/tree/master/examples).

## Screenshots

The `Scene` class has a `screenshot` method that allows you to save a `.png`, `.jpg`, `.svg`, `.pdf`, or `.eps` image showing the current view of the
rendering.  By default, the screenshots are saved in the current directory, but you can use `screenshots_folder` to
pass a path to the folder where you want them to be saved when you're creating an instance of Scene.

Note -- when saving a `.svg` or `.eps` file the output will be compressed as a `.gz` and will need to be extracted
before it can be viewed.

You can take a screenshot while viewing and interacting with a rendered scene by pressing the `s` key in your keyboard.
Using `Scene.screenshot` however gives you the freedom to specify a name for the image file to be saved.

By default `brainrender` is set up to ignore the background when saving the screenshots. That means that you will have
all of your rendered objects in your image, but the background will be transparent. If you want to include the
background in your image, include these two lines before creating the screenshot:

```python
import brainrender
brainrender.SCREENSHOT_TRANSPARENT_BACKGROUND = False
```

:::{hint}
You can also quickly take a screenshot by pressing the "s" key on your keyboard while interacting with the scene!
:::



## Videos

The beauty of creating 3d renderings is that you can look at your data from multiple points of view. A 2d picture can't
convey the same information, but a video showing the brain moving across frames may.

For this reason `brainrender` supports the creating videos where at each frame it shows the current view of the scene
and in-between frames it lets you move the scene around.

The easiest way to create a video is with the `VideoMaker` class. This takes a populate `scene` as argument and allows
you to create a video by specifying how the camera should move at each frame in the video. The basic `VideoMaker` class
only allows for rotations in the three principal directions, however you can use a custom function to specify what
should happen at each frame.

If you need to make more sophisticated animation (e.g. with actors being added, removed or edited in the video), you
might prefer to use the `Animation` class. This allows you to specify the video's content by defining a few keyframes.
At each keyframe you can specify a few parameters (e.g. camera position) and a function to be called when that point
of the video is reached: you can then have your function perform the actions that you need (e.g. add a new actor). The
video is then created by interpolating the parameter across keyframes and calling the specified functions when
necessary.



## Exporting to html

Videos are an improvement over screenshots in that they let the viewer see the scene from multiple points of view.
Ideally though you would need a way to let the viewer explore the scene at their own will, moving the camera around,
zooming etc., the same way you do when you create your renderings. `brainrender` also lets you
export your scene to an `.html` file which you can send to your colleagues (so that they can open it in their web
browser) or embed in a website [such as this one](https://brainglobe.info/_static/brainrender_web.html).

:::{caution}
Warning: for large and complex scenes the resulting html file might be fairly large (>100MB) and loading the
interactive scene in your web browser might take a few minutes.
:::

Exporting to `html` is simple, all you need to do is create a `Scene`, add elements to it and once you're happy
with it use the `export` method of `Scene` to create the `.html`. e.g.:

```python
from pathlib import Path

from myterial import orange
from rich import print

from brainrender import Scene

print(f"[{orange}]Running example: {Path(__file__).name}")

# Create a brainrender scene
scene = Scene(title="brainrender web export")

# Add brain regions
scene.add_brain_region("MOs", "CA1", alpha=0.2, color="green")

# Render!
scene.render()

# Export to web
scene.export("brain_regions.html")
```

:::{important}
Not all of `brainrender's` features can be included into your web export (because of limitations with the
`k3d` package.  For instance the appearance of your exported scene might be different from the one you
saw in `brainrender.`
:::
