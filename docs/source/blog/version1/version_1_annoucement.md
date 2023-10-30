---
blogpost: true
date: Oct 30, 2023
author: Will Graham
location: London, England
category: BrainGlobe-v1
language: English
---

# BrainGlobe version 1 is coming

BrainGlobe provides and maintains a number of open-source tools, each of which are provided as Python-based software packages.
A number of these tools also come with a user-interface provided by a [napari plugin](https://napari.org/) that can be installed on top of the basic tool package.
Whilst there is an advantage to the modularity provided by maintaining separate tools, the same modularity can present challenges and unnecessary difficulties when running an analysis that relies on multiple BrainGlobe tools.
Particular pinch points include:

- Needing to manually install each tool (and its napari plugin in some cases) that needs to be used one-at-a-time.
- Propagation of legacy naming conventions, as tools have evolved and their purpose has been redefined.
- Complex dependency trees, further complicated by optional dependencies.

To address these issues, we are pleased to announce that development on "BrainGlobe version 1" is underway.
The key features of this "version 1" will be:

- Allowing for all tools to be installed in a single command, `pip install brainglobe`.
- A reorganisation of the functionality offered by some tools (notably `cellfinder` and `brainreg`).
- To provide a stable, citable release of all existing BrainGlobe tools that can be found in a single place.

The individual tools (and the packages that provide them) will be remaining separate, so users can continue to manage and install individual tools if they so choose.

## What is changing?

One of our priorities with version 1 is that users should have to change as little as possible when they update.
Whilst the majority of changes are happening "under the hood", the way users interact with them through napari or the package API will change minimally and should be limited to the renaming certain tools or functions.
However we will be releasing changelogs for the individual tools as they are updated, as well as a final changelog with a complete listing of what tools have moved/changed and where to find them or their replacement.

Changes will be happening in a modular fashion, before the all-in-one `brainglobe` package is then released at the end.
This means that tools like `brainreg`, then `cellfinder`, etc will receive separate version updates as they are ready.
There should be no ill affects from updating the tools as they are released, however once the all-in-ine `brainglobe` package is ready we recommend you make a clean install anyway, just so that there's no funny business.

## Under the hood?

Under-the-hood, we are taking this opportunity to create an easily-citable and stable version of each of our tools, as well as perform some much needed housekeeping on how we organise the tools themselves.
This includes merging napari plugins with their corresponding "backend" tool; so to use `brainreg` with napari, users won't need to install `brainreg` and then also install `brainreg-napari`, for example.
It also includes a renaming of a few tools that have since grown out of their original purpose; the workflow methods currently in `cellfinder` will move into a dedicated tool for running analysis, and `cellfinder-core` and `cellfinder-napari` will now be incorporated into the `cellfinder` package itself rather than being standalone.
Finally, this will also simplify the number of inter-dependencies that we need to manage between our tools, and prevents issues surrounding modular installations from affecting users.
We are not *removing* the option of manual installation of individual tools from the users that want to do this, however at the same time we are taking away this concern from users who want to jump right into using BrainGlobe's features without worrying if they have the right tool installed or setup correctly.

## How can I stay updated?

The blog will be updated as the modular updates progress, as well as with the final announcement when everything is ready.
You can also [join us on Zulip](https://brainglobe.zulipchat.com/) and head over to the development stream to see live updates as development progresses.
