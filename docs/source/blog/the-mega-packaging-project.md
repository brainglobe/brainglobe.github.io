---
blogpost: true
date: April 28, 2026
author: Harry Carey
location: London, England
category: brainglobe
language: English
---

# The mega packaging project 

The purpose of the BrainGlobe atlas api has always been to standardise atlases and provide them to researchers via a common, easy to use, interface. As part of this initiative we have integrated atlases of all kinds, including atlases of bees, cuttlefish, mice, and more. The logical endpoint of all of this would be integrate _all_ existing 3D atlases into BrainGlobe. 

While this may be a long process we have decided to start. First by creating a comprehensive list of all published non-human brain atlases which is available [here](https://docs.google.com/spreadsheets/d/18_ow4llQQVuwKu5WWM3PsZ1SjmeNYAhi6eENzhQRc40/edit?usp=sharing). This list is a work in progress and if you find an atlas which is not mentioned please open an issue on the [brainglobe-atlasapi](https://github.com/brainglobe/brainglobe-atlasapi/issues?q=sort%3Aupdated-desc+is%3Aissue+is%3Aopen) repository and we will be sure to add it. 

The second step is to actually integrate the atlases on this list into the API. To this end we have hired [Jung Woo Kim](https://github.com/kjungwoo5) and [Amirreza Bahramani](https://github.com/bahramani). They have already begun integrating several atlases (expect to see a Macaque atlas soon!). 

In total our review found 221 3D atlases across approximately 89 species of which we could find shared data for 121. 

```{raw} html
<iframe 
  src="../_static/species_bubbles.html" 
  width="100%" 
  height="840" 
  frameborder="0" 
  style="border:none; overflow:hidden;">
</iframe>
```

As always, if you would like to get involved with this project just get in touch with us! There are several ways to contribute  including adding missing atlases to the list, helping with data standardisation, or contributing to integration and validationWe are available via GitHub issues and [zulip](https://brainglobe.zulipchat.com). 

