# Exploring the numerical results

In the `test_brain/output/analysis` directory is a `summary.csv` file which you can open in Microsoft Excel (or similar) to view a summary of the results.
This file lists (for each brain area); the number of cells detected, the volume of the brain area, and the density of cells (in cells per mm<sup>3</sup>).
This is the file you'll most likely use for statistical analysis.
It will look something like this (but with an entry for each brain area):

| structure\_name | left\_cell\_count | right\_cell\_count | total\_cells | left\_volume\_mm3 | right\_volume\_mm3 | total\_volume\_mm3 | left\_cells\_per\_mm3 | right\_cells\_per\_mm3 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Retrosplenial area, ventral part, layer 5 | 1853 | 814 | 2667 | 0.952479 | 0.966508 | 1.918987 | 1945.44971595174 | 842.207203665153 |
| Lateral dorsal nucleus of thalamus | 1541 | 0 | 1541 | 0.597768 | 0.534717 | 1.132485 | 2577.92320766585 | 0 |
| Retrosplenial area, ventral part, layer 2/3 | 163 | 686 | 849 | 0.57638 | 0.614387 | 1.190767 | 282.79954196884 | 1116.56008346531 |
| Retrosplenial area, dorsal part, layer 5 | 561 | 82 | 643 | 0.611487 | 0.644904 | 1.256391 | 917.435693645163 | 127.150707702232 |
| Retrosplenial area, dorsal part, layer 2/3 | 194 | 245 | 439 | 0.460668 | 0.492384 | 0.953052 | 421.127579949117 | 497.579125235589 |
| Ventral anterior-lateral complex of the thalamus | 412 | 0 | 412 | 0.397422 | 0.365181 | 0.762603 | 1036.6814116984 | 0 |

These data allow you to compare data from multiple samples.
To visualise data from different samples in the same coordinate space, take a look at [Visualising your data in brainrender](visualising-your-data-in-brainrender).
