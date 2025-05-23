# Software built by the community

Tools like the [BrainGlobe Atlas API](/documentation/brainglobe-atlasapi/index) were developed to help establish a community of 
developers creating interoperable tools. The BrainGlobe core developers have created a number of such tools
([cellfinder](/documentation/cellfinder/index), [brainreg](/documentation/brainreg/index), 
[brainrender](/documentation/brainrender/index) etc.). More recently, members of the community have built their own 
software that leverages the BrainGlobe ecosystem in some way:

## Aligning Big Brains & Atlases
Aligning Big Brains & Atlases (ABBA) is a FIJI plugin for the registration of 2D brain sections to an atlas. Using 
the [Python version](https://github.com/BIOP/abba_python) allows users to register their data to any BrainGlobe Atlas. 
- [Website](https://biop.github.io/ijp-imagetoatlas/registration.html)
- [GitHub repository](https://github.com/BIOP/ijp-imagetoatlas)
- [ABBA Python](https://github.com/BIOP/abba_python)

## Brainways
Brainways is a user-friendly tool for mapping single sections to an atlas using deep learning. 

- [Preprint](https://www.biorxiv.org/content/10.1101/2023.05.25.542252v1)
- [GitHub repository](https://github.com/bkntr/brainways)
- [Napari plugin](https://github.com/bkntr/napari-brainways)

## MagellanMapper
MagellanMapper is a graphical tool for 3D reconstruction and automated analysis of whole specimens using BrainGlobe 
atlases for registration. 
- [GitHub repository](https://github.com/sanderslab/magellanmapper)
- [Documentation](https://magellanmapper.readthedocs.io/en/latest/)


## Braintracer
Braintracer is an extension of BrainGlobe providing further analysis tools that build upon brainreg and cellfinder.
- [GitHub repository](https://github.com/samclothier/braintracer)

## pAPRica
pAPRica is a package for analysis of large microscopy datasets that incorporates registration using brainreg.
- [Preprint](https://www.biorxiv.org/content/10.1101/2023.01.27.525687v1)
- [GitHub repository](https://github.com/WyssCenter/pAPRica)
- [Documentation](https://wysscenter.github.io/pAPRica/index.html)

## BrainAtlas
BrainAtlas wraps the BrainGlobe Atlas API into a package for easy use with the Unity video game engine.
- [GitHub repository](https://github.com/VirtualBrainLab/BrainAtlas/)
- [Documentation](https://virtualbrainlab.org/misc/brain_atlas.html)

## ClearFinder
ClearFinder is a graphical user interface that allows users without programming experience to use cellfinder and ClearMap for cell counting and reference atlas annotation of the whole volume of adult tissue-cleared mouse brains. Basic statistics and visualization round up the analysis.
- [GitHub repository](https://github.com/stegiopast/ClearFinder)
- [Preprint](https://www.biorxiv.org/content/10.1101/2024.06.21.599877v1)

## vvasp
vvasp (pronounced wasp) is a python library for 3D viewing of spatially defined neuroscience data (histology, probe trajectories, neuron locations, etc.).  It uses the default PyVista plotter and is fully interoperable with PyVista functionality.
- [GitHub repository](https://github.com/spkware/vvasp)

## cuisto
cuisto is a Python package for histological quantification of objects in reference atlas regions.
cuisto uses data exported from QuPath used with ABBA to pool data and derive, average and display metrics.
- [GitHub repository](https://github.com/TeamNCMC/cuisto)
- [Documentation](https://teamncmc.github.io/cuisto)

## BlenderBrain
BlenderBrain allows the user to visualise atlas data from the BrainGlobe Atlas API in Blender.
- [GitHub repository](https://github.com/ArtemKirsanov/BlenderBrain)

## DMC-BrainMap
DMC-BrainMap is a napari-based tool for the analysis of 2D brain sections, including feature segmentation and atlas registration. 
- [GitHub repository](https://github.com/hejDMC/napari-dmc-brainmap)

## CoperniFUS
CoperniFUS is a flexible GUI for stereotaxic Focused UltraSound (FUS) experiment planning.
- [GitHub repository](https://github.com/Tomaubier/CoperniFUS)
- [Documentation](https://copernifus.readthedocs.io/en/latest/index.html)

:::{hint}
if you have developed any software using BrainGlobe tools, please [let us know](../contact) and we can advertise it here. 
:::
