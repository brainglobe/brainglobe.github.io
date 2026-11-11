"""Compare files from tests/e2e_export.mjs with arrays read by zarr-python."""
import sys
import zipfile
from pathlib import Path

import nibabel as nib
import nrrd
import numpy as np
import tifffile
import zarr

d = Path(sys.argv[1])
ROOT = "https://brainglobe.s3.us-west-2.amazonaws.com/atlas"
ANN = f"{ROOT}/annotation-sets/allen_mouse-annotation/3_1/annotations_compressed.ome.zarr"
TPL = f"{ROOT}/templates/allen_mouse-template/3_1/template.ome.zarr"
HEMI = f"{ROOT}/annotation-sets/allen_mouse-annotation/3_1/hemispheres.ome.zarr"


def ref(url, path):
    return zarr.open_array(f"{url}/{path}", mode="r")[:]


fails = 0
def check(name, ok, extra=""):
    global fails
    print("OK  " if ok else "FAIL", name, extra)
    fails += not ok

ann = ref(ANN, "s3")
check("tiff", np.array_equal(tifffile.imread(d / "annotation_100um.tiff"), ann), ann.shape)
img = nib.load(d / "annotation_100um.nii.gz")
check("nifti", np.array_equal(np.asarray(img.dataobj), ann.transpose(2, 1, 0)), nib.aff2axcodes(img.affine))
check("nifti zooms", np.allclose(img.header.get_zooms(), (0.1, 0.1, 0.1)))
tpl = ref(TPL, "s2")
data, hdr = nrrd.read(str(d / "template_50um.nrrd"))
check("nrrd", np.array_equal(data, tpl.transpose(2, 1, 0)), tpl.shape)
hemi = ref(HEMI, "s3")
check("hemispheres nifti", np.array_equal(np.asarray(nib.load(d / "hemispheres_100um.nii.gz").dataobj), hemi.transpose(2, 1, 0)), np.unique(hemi))
zpath = d / "annotation_100um.ome.zarr.zip"
with zipfile.ZipFile(zpath) as z:
    check("zip integrity", z.testzip() is None, f"{len(z.namelist())} entries")
store = zarr.storage.ZipStore(zpath, mode="r")
g = zarr.open_group(store, path="annotation_100um.ome.zarr", mode="r")
check("ome-zarr zip", np.array_equal(g["s3"][:], ann), list(g.array_keys()))
check("ome-zarr multiscales", [x["path"] for x in g.attrs["ome"]["multiscales"][0]["datasets"]] == ["s3"])
# ITK-SNAP: values must be the original annotation values; labels above
# 65535 (ITK-SNAP's limit) must be commented out, everything else active.
import csv
import re
term = {int(r["annotation_value"]): r["name"] for r in csv.DictReader(open(d / "allen_terminology.csv"))}
active, commented, ok = {}, {}, True
for line in (d / "allen_itksnap.txt").read_text().splitlines():
    m = re.match(r'^(#?)\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+([\d.]+)\s+([01])\s+([01])\s+"([^"]*)"$', line)
    if not m:
        ok &= line.startswith("#")  # header comments
        continue
    (commented if m.group(1) else active)[int(m.group(2))] = m.group(9)
check("itksnap lines parse", ok)
check("itksnap active <= 65535", max(active) <= 65535, f"{len(active)} active, max {max(active)}")
check("itksnap commented == values > 65535", set(commented) == {v for v in term if v > 65535}, f"{len(commented)} commented")
check("itksnap values unchanged", (set(active) | set(commented)) - {0} == set(term) - {0})
check("itksnap names match", all(active[v].startswith(term[v].replace('"', "'")) for v in active if v))
print("FAILURES:", fails)
sys.exit(1 if fails else 0)
