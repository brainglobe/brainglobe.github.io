## A digital three-dimensional brain atlas for the blackcap (Sylvia atricapilla)

## Introduction
BrainGlobe provides a 
[consistent interface to existing anatomical atlases from many species](/documentation/brainglobe-atlasapi). However, 
digital 3D atlases do not exist for the majority of species. 

The Eurasian blackcap (*Sylvia atricapilla*) is a songbird known to navigate by the Earth's magnetic field, making it 
a very interesting animal model. However, the lack of a high quality reference atlas hinders computational neuroanatomy 
research in this species. Anatomical atlases define a standard coordinate system for an organ, and allow data from 
multiple sources to be aligned and then visualised and analysed together. This makes it easier to integrate results 
different sources, and facilitates data sharing and collaboration.

For this reason, we collaborated with [Simon Weiler](https://sites.google.com/view/neuroweiler) from the 
[Sainsbury Wellcome Centre](https://www.sainsburywellcome.org), and the lab of 
[Henrik Mouritsen](https://uol.de/en/ibu/animal-navigation) at the 
[Carl von Ossietzky University of Oldenburg](https://uol.de/en) to build a high-quality digital reference atlas 
of the blackcap brain.

## Process
Full details of the atlas generation process are available in the [preprint](), however it is briefly as follows:
1. Acquire high-resolution whole-brain images using the
[Sainsbury Wellcome Centre Advanced Microscopy Facility serial-section two-photon microscopy platform](https://swc-advanced-microscopy.github.io/facility_webpage/)
2. Crop images to generate individual hemisphere images without damage (we used 18 hemispheres from 10 birds).
3. Iteratively generate a high signal-to-noise average template image from all the individual images using 
[ANTs](http://stnava.github.io/ANTs/) via an [optimised script](https://github.com/CoBrALab/optimized_antsMultivariateTemplateConstruction) 
from the [CoBra lab](https://www.cobralab.ca/). 
4. Manually annotate brain regions using [ITK-SNAP](http://www.itksnap.org/pmwiki/pmwiki.php)
5. Package the template and annotations image [into the BrainGlobe format](https://brainglobe.info/documentation/brainglobe-atlasapi/adding-a-new-atlas.html).