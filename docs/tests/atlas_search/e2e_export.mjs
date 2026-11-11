// End-to-end: export a real (small) atlas from S3 with the same code the
// website uses, writing to argv[2]. Verified by e2e_verify.py.
import { createWriteStream, mkdirSync } from "node:fs";
import { createGzip } from "node:zlib";
import { writeFileSync } from "node:fs";
import { exportVolume, sinkGzip } from "../../source/_static/atlas-search/export/export.js";
import { toItkSnap } from "../../source/_static/atlas-search/export/ontology.js";

const out = process.argv[2];
mkdirSync(out, { recursive: true });
const ROOT = "https://brainglobe.s3.us-west-2.amazonaws.com/atlas";
const ANN = `${ROOT}/annotation-sets/allen_mouse-annotation/3_1/annotations_compressed.ome.zarr`;
const TPL = `${ROOT}/templates/allen_mouse-template/3_1/template.ome.zarr`;
const HEMI = `${ROOT}/annotation-sets/allen_mouse-annotation/3_1/hemispheres.ome.zarr`;

async function levels(url) {
  const g = await (await fetch(`${url}/zarr.json`)).json();
  const ds = g.attributes.ome.multiscales[0].datasets;
  return Promise.all(ds.map(async (d) => {
    const a = await (await fetch(`${url}/${d.path}/zarr.json`)).json();
    return { path: d.path, scale: d.coordinateTransformations[0].scale, shape: a.shape,
      chunks: a.chunk_grid.configuration.chunk_shape, dtype: a.data_type, separator: "/" };
  }));
}

function fileSink(path, gzip) {
  const ws = createWriteStream(path);
  const target = gzip ? createGzip() : ws;
  if (gzip) target.pipe(ws);
  const write = (u8) => new Promise((res, rej) => target.write(Buffer.from(u8), (e) => (e ? rej(e) : res())));
  return {
    write,
    close: () => new Promise((res) => { ws.on("finish", res); target.end(); }),
    abort: async () => target.destroy(),
  };
}

// terminology rows in the same shape the index builder produces
const csv = await (await fetch(`${ROOT}/terminologies/allen_mouse-terminology/3_1/terminology.csv`)).text();
const rows = csv.trim().split("\n").slice(1).map((line) => {
  const f = line.match(/("[^"]*"|[^,]*)(,|$)/g).map((x) => x.replace(/,$/, "").replace(/^"|"$/g, ""));
  return { id: +f[0], parent: f[1] ? +f[1] : null, value: +f[2], name: f[3], acronym: f[4], color: f[5], path: [] };
});
writeFileSync(`${out}/allen_itksnap.txt`, toItkSnap(rows));
writeFileSync(`${out}/allen_terminology.csv`, csv);

const jobs = [
  [ANN, "s3", "tiff", "annotation_100um.tiff"],
  [ANN, "s3", "nifti", "annotation_100um.nii.gz"],
  [TPL, "s2", "nrrd", "template_50um.nrrd"],
  [HEMI, "s3", "nifti", "hemispheres_100um.nii.gz"],
  [ANN, "s3", "ome-zarr", "annotation_100um.ome.zarr.zip"],
];
for (const [url, path, format, name] of jobs) {
  const lv = await levels(url);
  const level = lv.find((l) => l.path === path);
  const t = performance.now();
  await exportVolume({
    zarrUrl: url, level, levels: lv, format, orientation: "asr", filename: name,
    sinkPromise: Promise.resolve(fileSink(`${out}/${name}`, sinkGzip(format))),
  });
  console.log(`exported ${name} in ${((performance.now() - t) / 1000).toFixed(1)} s`);
}
