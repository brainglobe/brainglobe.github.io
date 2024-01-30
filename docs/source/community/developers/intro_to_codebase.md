# Introduction to the BrainGlobe codebase for developers

This is an introduction to the high-level organisation of the BrainGlobe codebase for developers. It serves as an introduction for new contributors and as a reference for all contributors.

It will cover BrainGlobe's guiding principles for development and the default software architecture for BrainGlobe repositories. Note that this high-level organisation is (at least partially) aspirational, and implementing it is work-in-progress (see [the current roadmap](/community/roadmaps/index.md) and the [Core Development Project Board](https://github.com/orgs/brainglobe/projects/2))


## Guiding principles for development

The first guiding principle is that BrainGlobe should be easy-to-use by everyone. In practice, this means that BrainGlobe code should be independent of species of interest or image modality, and should be installable and runnable by anyone with a reasonably modern laptop within minutes. Users should not require programming expertise.

As a secondary guiding principle, we additionally aim to make the codebase easy-to-maintain, and easy-to-contribute-to, where this doesn't interfere with the first principle.

Choices around the software architecture and technology stack (detailed below) are taken with these principles in mind.


### Examples of guiding principles in practice

* ease of installation: through the metapackage, we provide a one-line command to install all BrainGlobe tools at once. None of the packages depend on anything other than Python (we've removed historical compiled code), and are therefore easy to install cross-platform.
* accessibility: we aim to provide a Graphical User Interface (GUI) for all BrainGlobe tools. By asking users for feedback, we ensure that the GUI provides an nice user experience.
* ease of use through Python/interoperability: we aim to provide a well-documented Python API for all BrainGlobe tools.
* performance: By running weekly benchmarks comparing the latest release with the development version, we guarantee that performance will not deteriorate as BrainGlobe evolves.
* Species/modality independent: none of the code makes any assumptions about the imaging modality or the species of the model organism of interest. We provide atlases for a variety of model organisms.
* useability: we sacrifice the code simplicity provided by `magicgui` in exchange for fine-grained control of the user experience by writing brainglobe widgets in `qtpy`. This is an example where the first guiding principle takes priority over the second.
* easy-to-maintain: we move functionality used by more than one independent BrainGlobe tool to `brainglobe-utils` to reduce code duplication and make maintenance easier.


## BrainGlobe Tools

Code providing functionality related to a specific analysis or visualisation step is referred to as a BrainGlobe "tool". Each BrainGlobe tool has its own Github repository on the BrainGlobe organisation. 

Currently stable tools are:
- `brainglobe-atlasapi`
- `brainglobe-heatmap`
- `brainglobe-segmentation`
- `brainreg`
- `brainrender`
- `cellfinder`
- `morphapi`

Tools currently in development are
- `brainglobe-registration`
- `brainrender-napari`

The BrainGlobe Github organisation also hosts the [`brainglobe` (meta-)package](./repositories/brainglobe-meta/index.md) and the [`brainglobe-workflows` collection](./repositories/brainglobe-workflows/index.md) in separate repositories (which are not tools in themselves), as well as the utility packages `brainglobe-utils` and `brainglobe-space`.

As can be seen from the package names, we follow a **loose** naming convention for packages following a pattern of {brain(globe) || cell}-{noun describing what the tool does}. The most important criterion is the expressiveness of the name. The `bg-` prefix for BrainGlobe tools has been discontinued.

### Default architecture for BrainGlobe Tools

By default, each brainglobe tool should be organised into three distinct submodules: `core`, `qt`, and `napari`. These submodules should live in the same GitHub repository and are packaged together on PyPI. It is acceptable to deviate from the default where there is a reason to.

* `core` contains the central logic to use this tool and exposes it through a Python API
* `qt` contains user-friendly widgets and related Qt code that is implemented using `qtpy` . Each of these widgets provides an intuitive graphical user interface for one part (or few related parts) of the Python API defined in `core`. 
The widgets additionally emit Qt signals that any frontend (e.g. the code in `napari`) can connect to.
* `napari` contains at least one Napari plugin that connects to signals in `qt` and implements a napari-specific response (e.g. adding a Napari layer) to them.

The architecture has a number of advantages
- the modularity ensure each of submodule can (and should be) tested individually in the first instance
- widgets can be re-used outside of napari
- integration tests in the same repo to avoid messy CI dependencies

Additionally, keeping the architecture consistent across BrainGlobe tools should make it easier to contribute to several tools once someone has contributed to one tool, due to the familiar codebase organisation.