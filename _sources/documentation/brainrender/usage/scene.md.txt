# Scene

The `Scene` class is the focal point of any work using `brainrender`. It's used to add [actors](actors) to your 
visualization, to add brain regions meshes (by interacting with the `Atlas` class), to render your scene and use 
it to export images (using the `Render` class). Finally, the creation of a `Scene` is the first step towards the 
generation of [videos and animations](videos-animations-and-exporting-to-html) as well.

Given its integration with the [BrainGlobe Atlas API](/documentation/bg-atlasapi/index), `brainrender` can be used with 
any atlas supported by the API. The moment when you're creating your `Scene` is when you have a chance to specify 
which atlas you intend to use by passing `atlas_name='atlas to use'` to `Scene()`.


## Methods 

### Adding/removing actors

* `add` and `add_brain_regions`    __can be used to add `actors` to your scene or generate new `actors` to represent 
brain regions, respectively. To fetch brain regions data, `Scene` uses `brainrender.atlas.Atlas` behind the scenes. 
The atlas class has a few useful methods (e.g. `Atlas.hierarchy` can be used to visualize a list of all brain regions 
in the atlas being used), these can be accessed using `Scene.atlas.x`.
* `get_actors` can be used to get a handle on actors that are already part of the `Scene`.  You can look for actors 
using either their name  or br\_class \(e.g. streamlines, neurons...\).
* `remove`  can be used to remove any actor from your scene. 
* All actors that are currently in your scene can be found at `Scene.actors` and `Scene.content` can be used to print 
out an overview of the scene's content.

### Editing actors

* `add_label` and `add_silhouette` both take actors as inputs and can be used to add a label or a silhouette to your 
actors. The label is a piece of text that label's the actor's  mesh in your scene, the silhouette is a black outline 
around your actor which can be used to make it stand out in your visualization.
* `slice` is a special method which can be used to 'cut' the scene's content with a plane (e.g. imagine a plane going 
along the mid-line of the brain, this can be used to cut all meshes in half). Several parameters can be passed to 
`slice` for instance to only cut specific actors. When using `slice`, you can specify which plane to use for the 
cutting by either passing one of the supported plane names \(sagittal, frontal and horizontal\) or by creating a 
custom plane. This can be done using `Scene.atlas.get_plane` and specifying the position and normal of the plane.

### Rendering and exporting

All the code relative to the rendering of your scene is defined in `brainrender.render.Render`, however `Scene` uses
`Render` directly, and as such you can access methods like `Render.render` with `Scene.render`.

The central method is obviously `Scene.render`, this creates a window and generates the 3D interactive rendering. 
When calling `render` you can specify a camera position (see below) you wish to use. 

Additional methods include `screenshots` and `export` (for exporting .html files with your rendered scene).

## Working with cameras

The creation of an interactive rendering, or a video, involves the specification of the position and orientation of a 
"camera" representing your point of view.

`Brainrender` provides a number of pre-defined cameras that can be used (e.g. `sagittal` or `frontal`). If you wish 
to use any of these cameras just pass the corresponding name to `Scene.render` (e.g. `scene.render(camera='frontal')`). 
`render` also takes a `zoom` parameter which specifies the camera's zoom.

You can, however, create a **custom** camera for your needs by specifying a set of **camera parameters** and pass that 
(as a dictionary) to `scene.render`. To get the parameters you need, the simplest thing is to render your scene with 
any camera, move the scene to get the point of view you need and press `c` on your keyboard. This will print out 
the current camera parameters. You can then close your scene and copy-paste the camera parameters in your code. 
The next time you render your scene it will use your parameters.

The **parameters** used to specify a camera include:

* `pos`: a set of 3D coordinate specifying the position of the camera
* `viewup`: a 3d vector indicating the direction of "up" in your scene \(should always be `0, -1, 0`\).
* `clippingRange`: a set of a short and long distance, anything outside this range will not be rendered

Additional parameters (not generally needed):

* `focalPoint` specifies the 'focal point' of the camera
* `distance` the camera's distance.

