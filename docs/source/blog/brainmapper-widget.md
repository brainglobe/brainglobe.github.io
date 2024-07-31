---
blogpost: true
date: July 31, 2024
author: Adam Tyson
location: London, England
category: brainglobe
language: English
---

# New brainmapper napari widget released

One common use of BrainGlobe tools is to analyse the distribution of cells in a whole brain image. This process 
involves first detecting cells using [`cellfinder`](/documentation/cellfinder/index) and then registering (aligning) the 
data to a BrainGlobe atlas using [`brainreg`](/documentation/brainreg/index). The detected cell positions must then be 
transformed from the coordinate space of the raw data to the coordinate space of the atlas for analysis.

This workflow has previously been implemented with the [`brainmapper`](/documentation/brainglobe-workflows/brainmapper/index) 
command line tool, which runs brainreg, then cellfinder and then analyses the distribution of cells throughout 
the brain. This tool is excellent for automated analyses, but using a command-line tool isn't very intuitive for many 
users, and it is difficult to optimise parameters for a new application.

`brainreg` and `cellfinder` both have napari plugins. This allows use within a graphical user interface, and to 
make it easier to iteratively optimise parameters. However, to assign cells to a brain region, users had to use the 
`brainmapper` command line tool. 

To fix this **we have released a new `brainmapper` napari widget**. This allows users to combine the results of 
`brainreg` and `cellfinder` to analyse the distribution of cells across the brain.

## What does it do?

The plugin takes as input cell coordinates (from `cellfinder` or another tool) and a `brainreg` output directory. It 
then transforms cells to the atlas space. A summary of the cellular distribution (i.e. cells per brain region) is 
then displayed.

| structure\_name | left\_cell\_count | right\_cell\_count |
| :--- | :--- | :--- |
| Retrosplenial area, ventral part, layer 5 | 1853 | 814 |
| Lateral dorsal nucleus of thalamus | 1541 | 0 |
| Retrosplenial area, ventral part, layer 2/3 | 163 | 686 | 
| Retrosplenial area, dorsal part, layer 5 | 561 | 82 | 
| Retrosplenial area, dorsal part, layer 2/3 | 194 | 245 |
| Ventral anterior-lateral complex of the thalamus | 412 | 0 |

**Example of the results displayed within napari after running the widget**

Full analysis results (coordinates of every cell, and numbers of cells for every brain region) can be
saved alongside the transformed cell coordinates.

## How do I install it?
The widget is part of the `brainglobe-utils` package. However, the easiest way to install it is to upgrade the 
`brainglobe` package:

```bash
pip install brainglobe --upgrade
```

It can also be installed from the 
[napari plugin manager](https://napari.org/stable/plugins/start_using_plugins/finding_and_installing_plugins.html#find-and-install-plugins) 
by searching for "brainglobe-utils".

## How do I use it?
Please see the [documentation](/documentation/brainglobe-utils/transform-widget) and the
[analysing brainwide distribution of cells tutorial](/tutorials/transform-cells-atlas).

