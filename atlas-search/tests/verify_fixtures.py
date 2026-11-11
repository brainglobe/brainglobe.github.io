"""Verify files from tests/write_fixtures.mjs with standard Python readers."""
import sys
import zipfile
from pathlib import Path

import nibabel as nib
import nrrd
import numpy as np
import tifffile

d = Path(sys.argv[1])
shape = (5, 6, 7)
spacing = np.array([0.025, 0.05, 0.01])
DIR = {"a": [0, -1, 0], "p": [0, 1, 0], "s": [0, 0, -1], "i": [0, 0, 1], "r": [-1, 0, 0], "l": [1, 0, 0]}


def expected(dtype):
    n = np.prod(shape)
    v = (np.arange(n) * 7) % 251 + (100000 if dtype == "uint32" else 0)
    return v.astype(dtype).reshape(shape)


def expected_affine(o):
    A = np.eye(4)
    for col, ax in enumerate([2, 1, 0]):
        A[:3, col] = np.array(DIR[o[ax]]) * spacing[ax]
    return A


fails = 0
for dtype in ["uint8", "uint16", "uint32", "float32"]:
    exp = expected(dtype)
    for name in [f"{dtype}.tiff", f"{dtype}.big.tiff"]:
        with tifffile.TiffFile(d / name) as tf:
            arr = tf.asarray()
            ok = arr.shape == shape and arr.dtype == exp.dtype and np.array_equal(arr, exp)
            if dtype in ("uint8", "uint16", "float32"):
                ij = tf.imagej_metadata
                ok &= abs(ij["spacing"] - 25.0) < 1e-6
            print(("OK  " if ok else "FAIL"), name, arr.shape, arr.dtype, "bigtiff" if tf.is_bigtiff else "")
            fails += not ok
    for o in ["asr", "lpi", "pir"]:
        img = nib.load(d / f"{dtype}.{o}.nii.gz")
        arr = np.asarray(img.dataobj)
        ok_data = np.array_equal(arr, exp.transpose(2, 1, 0)) and arr.dtype == exp.dtype
        ok_s = np.allclose(img.get_sform(), expected_affine(o), atol=1e-6)
        ok_q = np.allclose(img.get_qform(), expected_affine(o), atol=1e-5)
        ok = ok_data and ok_s and ok_q
        print(("OK  " if ok else "FAIL"), f"{dtype}.{o}.nii.gz", "data", ok_data, "sform", ok_s, "qform", ok_q,
              nib.aff2axcodes(img.affine))
        fails += not ok
        data, hdr = nrrd.read(str(d / f"{dtype}.{o}.nrrd"))
        ok_data = np.array_equal(data, exp.transpose(2, 1, 0))
        ok_dir = np.allclose(hdr["space directions"], expected_affine(o)[:3, :3].T)
        ok = ok_data and ok_dir
        print(("OK  " if ok else "FAIL"), f"{dtype}.{o}.nrrd", "data", ok_data, "dirs", ok_dir)
        fails += not ok

with zipfile.ZipFile(d / "test.zip") as z:
    ok = z.testzip() is None and z.read("a.ome.zarr/s0/c/0/0/0") == bytes([1, 2, 3, 4])
    print(("OK  " if ok else "FAIL"), "test.zip", z.namelist())
    fails += not ok
print("FAILURES:", fails)
sys.exit(1 if fails else 0)
