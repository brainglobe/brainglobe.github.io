# Troubleshooting

brainreg uses [NiftyReg](http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg) "under the hood" to perform the 
registration. For this reason, some of the error messages are not very easy to understand, because they come from 
NiftyReg, and not directly from brainreg. 

## Common problems
If brainreg fails to run (rather than runs, but the registration is poor) there are many potential causes. However, 
the majority of the time, this is due to incorrect parameters passed to brainreg, particularly the [image 
orientation and the voxel sizes](/documentation/setting-up/image-definition). Please check these values against your image metadata before running brainreg. 

## Improving registration performance
There are many ways to improve registration performance, but this will depend on your data. Some options to try include:
* [Changing registration parameters](user-guide/parameters)
* Registration to a [different resolution atlas](/documentation/bg-atlasapi/usage/atlas-details) (if available)
* Improving data quality. brainreg relies on high-contrast data. Poorly cleared tissue, or tissue with limited 
autofluorescence may not register well

## Error messages
### Segmentation fault

```bash
Process failed:
 Segmentation fault (core dumped)
```

This error could be caused by many things, but it is usually due to incorrect [definition of the image orientation or 
voxel sizes](/documentation/setting-up/image-definition). Please double-check the values entered are correct. 