# Command line interface

Although the atlases will be downloaded when you need them, we provide a command line interface to view which atlases are available, and update them if necessary.

To see the list of atlases available, run `brainglobe list` 

To download an atlas, use `brainglobe install` , the `-a` flag, followed by the name of the atlas, e.g.:

```bash
brainglobe install -a allen_mouse_25um
```

To update an atlas to a newer version, use `brainglobe update`, e.g.:

```bash
brainglobe update -a allen_mouse_25um
```

Further instructions can be found by running `brainglobe --help`.

We also provide a [graphical user interface](/tutorials/manage-atlases-in-GUI) to download and update atlases, as part of the `brainrender-napari` package.

