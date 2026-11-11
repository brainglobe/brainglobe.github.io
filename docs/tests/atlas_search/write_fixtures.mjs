// Writes small test volumes in every export format to the directory given
// as argv[2]; verify_fixtures.py checks them with tifffile/nibabel/pynrrd.
import { writeFileSync, mkdirSync } from "node:fs";
import { gzipSync } from "node:zlib";
import { niftiHeader, nrrdHeader, tiffHeader } from "../../source/_static/atlas-search/export/formats.js";
import { ZipWriter } from "../../source/_static/atlas-search/export/zip.js";

const out = process.argv[2];
mkdirSync(out, { recursive: true });
const shape = [5, 6, 7]; // z, y, x
const spacing = [0.025, 0.05, 0.01]; // mm
const n = shape[0] * shape[1] * shape[2];

const arrays = {
  uint8: Uint8Array, uint16: Uint16Array, uint32: Uint32Array, float32: Float32Array,
};
for (const [dtype, Ctor] of Object.entries(arrays)) {
  const data = new Ctor(n);
  for (let i = 0; i < n; i++) data[i] = (i * 7) % 251 + (dtype === "uint32" ? 100000 : 0);
  const bytes = new Uint8Array(data.buffer);
  const cat = (h, b) => { const o = new Uint8Array(h.length + b.length); o.set(h); o.set(b, h.length); return o; };
  writeFileSync(`${out}/${dtype}.tiff`, cat(tiffHeader({ shape, dtype, spacing }), bytes));
  writeFileSync(`${out}/${dtype}.big.tiff`, cat(tiffHeader({ shape, dtype, spacing, forceBigTiff: true }), bytes));
  for (const o of ["asr", "lpi", "pir"]) {
    writeFileSync(`${out}/${dtype}.${o}.nii.gz`, gzipSync(cat(niftiHeader({ shape, dtype, spacing, orientation: o }), bytes)));
    writeFileSync(`${out}/${dtype}.${o}.nrrd`, cat(nrrdHeader({ shape, dtype, spacing, orientation: o, gzip: true }), gzipSync(bytes)));
  }
}
const parts = [];
const zip = new ZipWriter(async (u8) => parts.push(Buffer.from(u8)));
await zip.add("a.ome.zarr/zarr.json", new TextEncoder().encode('{"zarr_format":3}'));
await zip.add("a.ome.zarr/s0/c/0/0/0", new Uint8Array([1, 2, 3, 4]));
await zip.add("a.ome.zarr/empty", new Uint8Array(0));
await zip.close();
writeFileSync(`${out}/test.zip`, Buffer.concat(parts));
console.log("fixtures written to", out);
