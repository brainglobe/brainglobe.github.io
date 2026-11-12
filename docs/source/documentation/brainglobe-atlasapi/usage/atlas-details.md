# Atlas details

The details of every atlas in the BrainGlobe Atlas API (its description, resolutions, versions, brain regions,
downloads and a preview) are on its page in the {ref}`atlas search <target-atlas-search>`, which also lets you
search atlases by name, species, resolution or brain region.

Sometimes choosing the most appropriate atlas for a specific question is easy, but in some cases (e.g. adult mouse
brains) there are many options. The annotations included with an atlas may dictate the choice: if the brain region
you are studying is not included in an atlas, it is not much use! In other cases the reference image will be
important. If you have imaged your sample with lightsheet microscopy (LSFM) it may be useful to use an atlas that also
uses this modality. An atlas using a different modality (such as serial section two-photon, STP) may produce inferior
registration results.

In most software you can choose the atlas from a list, but if using a command line tool, or the API directly, the
unique name (e.g. `example_mouse_100um`) must be used.

## Available atlases

```{atlas-collections}
```
