---
blogpost: true
date: May 15, 2026
author: Harry Carey
location: London, England
category: brainglobe
language: English
---

# The Systematic Atlas Packaging Project

The purpose of the BrainGlobe Atlas API is to standardise atlases and provide them to researchers via a common, easy to use, interface. As part of this initiative we have integrated atlases of all kinds, including atlases of mice, rats, bees, cuttlefish, and more. The logical endpoint of all of this would be integrate _all_ existing 3D atlases into BrainGlobe. 

While this may be a long process we have decided to get started. First by creating a comprehensive list of all published non-human brain atlases which have available data. It is available [here](https://github.com/brainglobe/brainglobe-atlasapi/issues?q=is%3Aissue%20state%3Aopen%20label%3Anew-atlas).  This list is a work in progress and if you find an atlas which is not mentioned please open an issue on the brainglobe-atlasapi repository and we will be sure to add it. 

The second step is to actually integrate the atlases on this list into the API. To this end [Jung Woo Kim](https://github.com/kjungwoo5) and [Amirreza Bahramani](https://github.com/bahramani) have joined the BrainGlobe team. They have already begun integrating several atlases (expect to see a Macaque atlas soon!). 

In total our review found 221 3D atlases across approximately 89 species of which we could find shared data for 121. 

<div style="max-height: 400px; overflow-y: auto; border: 1px solid #ddd; border-radius: 4px; margin: 1em 0;">
  <table style="width: 100%; border-collapse: collapse; font-size: 0.9em;">
    <thead style="position: sticky; top: 0; background: #f5f5f5; z-index: 1;">
      <tr>
        <th style="padding: 8px 12px; text-align: left; border-bottom: 2px solid #ccc;">Species</th>
        <th style="padding: 8px 12px; text-align: center; border-bottom: 2px solid #ccc; min-width: 140px;">Number of Atlases</th>
      </tr>
    </thead>
    <tbody>
    <tr><td>Mouse</td><td style="text-align:center">54</td></tr>
    <tr><td>Rat</td><td style="text-align:center">21</td></tr>
    <tr><td>Rhesus macaque</td><td style="text-align:center">16</td></tr>
    <tr><td>Marmoset</td><td style="text-align:center">9</td></tr>
    <tr><td>Drosophilia</td><td style="text-align:center">9</td></tr>
    <tr><td>Dog</td><td style="text-align:center">8</td></tr>
    <tr><td>Macaque</td><td style="text-align:center">6</td></tr>
    <tr><td>Chimpanzee</td><td style="text-align:center">5</td></tr>
    <tr><td>Moth</td><td style="text-align:center">5</td></tr>
    <tr><td>Zebrafish</td><td style="text-align:center">4</td></tr>
    <tr><td>Bee</td><td style="text-align:center">4</td></tr>
    <tr><td>Sheep</td><td style="text-align:center">3</td></tr>
    <tr><td>Vervet monkey</td><td style="text-align:center">3</td></tr>
    <tr><td>Mouse lemur</td><td style="text-align:center">3</td></tr>
    <tr><td>Squirrel monkey</td><td style="text-align:center">3</td></tr>
    <tr><td>Cynomolgus macaque</td><td style="text-align:center">3</td></tr>
    <tr><td>Spider</td><td style="text-align:center">3</td></tr>
    <tr><td>Rabbit</td><td style="text-align:center">2</td></tr>
    <tr><td>Ferret</td><td style="text-align:center">2</td></tr>
    <tr><td>Ant</td><td style="text-align:center">2</td></tr>
    <tr><td>Red flour beetle</td><td style="text-align:center">2</td></tr>
    <tr><td>Tree shrew</td><td style="text-align:center">2</td></tr>
    <tr><td>Dung beetle</td><td style="text-align:center">2</td></tr>
    <tr><td>Cat</td><td style="text-align:center">2</td></tr>
    <tr><td>Locust</td><td style="text-align:center">2</td></tr>
    <tr><td>Baboon</td><td style="text-align:center">2</td></tr>
    <tr><td>Wasp</td><td style="text-align:center">1</td></tr>
    <tr><td>Squirrel</td><td style="text-align:center">1</td></tr>
    <tr><td>Starling</td><td style="text-align:center">1</td></tr>
    <tr><td>Tawny dragon</td><td style="text-align:center">1</td></tr>
    <tr><td>Teleost fish</td><td style="text-align:center">1</td></tr>
    <tr><td>Sea lion</td><td style="text-align:center">1</td></tr>
    <tr><td>Zebrafinch</td><td style="text-align:center">1</td></tr>
    <tr><td>Monarch butterfly</td><td style="text-align:center">1</td></tr>
    <tr><td>Sea spider</td><td style="text-align:center">1</td></tr>
    <tr><td>Minpig</td><td style="text-align:center">1</td></tr>
    <tr><td>California sea lion</td><td style="text-align:center">1</td></tr>
    <tr><td>Cockroach</td><td style="text-align:center">1</td></tr>
    <tr><td>Cynomolgus macaques</td><td style="text-align:center">1</td></tr>
    <tr><td>Octopus</td><td style="text-align:center">1</td></tr>
    <tr><td>Hagfish</td><td style="text-align:center">1</td></tr>
    <tr><td>Killer whale</td><td style="text-align:center">1</td></tr>
    <tr><td>Sea turtle</td><td style="text-align:center">1</td></tr>
    <tr><td>Mozambique tilapia</td><td style="text-align:center">1</td></tr>
    <tr><td>Prairie vole</td><td style="text-align:center">1</td></tr>
    <tr><td>Pigeon</td><td style="text-align:center">1</td></tr>
    <tr><td>Common degu</td><td style="text-align:center">1</td></tr>
    <tr><td>Pygmy squid</td><td style="text-align:center">1</td></tr>
    <tr><td>Squid</td><td style="text-align:center">1</td></tr>
    <tr><td>Australian tawny dragon</td><td style="text-align:center">1</td></tr>
    <tr><td>Axolotl</td><td style="text-align:center">1</td></tr>
    <tr><td>Bearded dragon</td><td style="text-align:center">1</td></tr>
    <tr><td>Blackcap</td><td style="text-align:center">1</td></tr>
    <tr><td>Canary</td><td style="text-align:center">1</td></tr>
    <tr><td>Canine</td><td style="text-align:center">1</td></tr>
    <tr><td>Cavefish</td><td style="text-align:center">1</td></tr>
    <tr><td>Common shrew</td><td style="text-align:center">1</td></tr>
    <tr><td>Crocodile</td><td style="text-align:center">1</td></tr>
    <tr><td>Cuttlefish</td><td style="text-align:center">1</td></tr>
    <tr><td>Degu</td><td style="text-align:center">1</td></tr>
    <tr><td>Domestic pig</td><td style="text-align:center">1</td></tr>
    <tr><td>Fly</td><td style="text-align:center">1</td></tr>
    <tr><td>Horse</td><td style="text-align:center">1</td></tr>
    <tr><td>Japanese quail</td><td style="text-align:center">1</td></tr>
    <tr><td>Lemur</td><td style="text-align:center">1</td></tr>
    <tr><td>Lungfish</td><td style="text-align:center">1</td></tr>
    <tr><td>Mole rat</td><td style="text-align:center">1</td></tr>
    <tr><td>Moustached bat</td><td style="text-align:center">1</td></tr>
    <tr><td>African elephant</td><td style="text-align:center">1</td></tr>
    <tr><td>Opossum</td><td style="text-align:center">1</td></tr>
    <tr><td>Pig</td><td style="text-align:center">1</td></tr>
    <tr><td>Coyote</td><td style="text-align:center">1</td></tr>
    </tbody>
  </table>
</div>


As always, if you would like to get involved with this project just get in touch with us! There are several ways to contribute including adding missing atlases to the list, helping with data standardisation, or contributing to integration and validation. [Reach out to us](https://brainglobe.info/contact.html) if you would like to get involved. 

