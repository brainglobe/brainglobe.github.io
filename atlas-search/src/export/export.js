// Stream BrainGlobe OME-Zarr volumes from S3 into downloadable files.

import * as zarr from "zarrita";
import { niftiHeader, nrrdHeader, rawSize, tiffHeader } from "./formats.js";
import { gzipSink, openSink } from "./sink.js";
import { ZipWriter } from "./zip.js";

const CONCURRENCY = 8;

async function mapLimit(items, limit, fn) {
  const out = new Array(items.length);
  let next = 0;
  const workers = Array.from({ length: Math.min(limit, items.length) }, async () => {
    while (next < items.length) {
      const i = next++;
      out[i] = await fn(items[i], i);
    }
  });
  await Promise.all(workers);
  return out;
}

// `native`: the format BrainGlobe stores the volumes in; the others are
// converted in the browser.
export const FORMATS = {
  "ome-zarr": { label: "OME-Zarr", ext: ".ome.zarr.zip", note: "zipped zarr v3 store", native: true },
  tiff: { label: "TIFF", ext: ".tiff", note: "multi-page stack (tifffile / Fiji)" },
  nifti: { label: "NIfTI", ext: ".nii.gz", note: "gzip-compressed, RAS affine" },
  nrrd: { label: "NRRD", ext: ".nrrd", note: "gzip-encoded, RAS space directions" },
};

/** Whether the output sink itself must be gzip-wrapped for a format. */
export function sinkGzip(format) {
  return format === "nifti"; // .nii.gz; NRRD gzips only its payload
}

/**
 * Stream a 3D zarr array plane by plane (z), in C order.
 * Holds one row of chunks (along z) in memory at a time.
 */
async function streamPlanes(arrayUrl, onPlane, { signal, onChunk } = {}) {
  const store = new zarr.FetchStore(arrayUrl);
  const arr = await zarr.open.v3(store, { kind: "array" });
  const [Z, Y, X] = arr.shape;
  const [cz, cy, cx] = arr.chunks;
  const nj = Math.ceil(Y / cy);
  const nk = Math.ceil(X / cx);
  const coords = [];
  for (let j = 0; j < nj; j++) for (let k = 0; k < nk; k++) coords.push([j, k]);

  let plane = null;
  for (let i = 0; i * cz < Z; i++) {
    if (signal?.aborted) throw new DOMException("Export cancelled", "AbortError");
    const chunks = await mapLimit(coords, CONCURRENCY, async ([j, k]) => {
      const c = await arr.getChunk([i, j, k], { signal });
      onChunk?.();
      return { j, k, c };
    });
    const dz = Math.min(cz, Z - i * cz);
    if (!plane) plane = new chunks[0].c.data.constructor(Y * X);
    for (let z = 0; z < dz; z++) {
      for (const { j, k, c } of chunks) {
        const [sz, sy, sx] = c.stride;
        const y0 = j * cy;
        const x0 = k * cx;
        const h = Math.min(cy, Y - y0);
        const w = Math.min(cx, X - x0);
        for (let y = 0; y < h; y++) {
          const src = z * sz + y * sy;
          if (sx === 1) {
            plane.set(c.data.subarray(src, src + w), (y0 + y) * X + x0);
          } else {
            for (let x = 0; x < w; x++) plane[(y0 + y) * X + x0 + x] = c.data[src + x * sx];
          }
        }
      }
      await onPlane(plane, i * cz + z);
    }
  }
}

/**
 * Export one atlas component to a file.
 * @param {object} p
 * @param {string} p.zarrUrl  URL of the OME-Zarr group (…/template.ome.zarr)
 * @param {object} p.level    level info from the index ({path, shape, scale, dtype, chunks, separator})
 * @param {object[]} p.levels all levels in the group (for OME-Zarr "all levels")
 * @param {"tiff"|"nifti"|"nrrd"|"ome-zarr"} p.format
 * @param {string} p.orientation BrainGlobe orientation string
 * @param {string} p.filename
 * @param {boolean} [p.allLevels] OME-Zarr only: include every pyramid level
 * @param {string} [p.description]
 * @param {(done: number, total: number) => void} [p.onProgress]
 * @param {AbortSignal} [p.signal]
 * @param {Promise} [p.sinkPromise] sink opened from the click handler
 */
export async function exportVolume(p) {
  const sink = await (p.sinkPromise ?? openSink(p.filename, { gzip: sinkGzip(p.format) }));
  try {
    if (p.format === "ome-zarr") await writeOmeZarrZip(sink, p);
    else await writeRaster(sink, p);
    await sink.close();
  } catch (e) {
    await sink.abort();
    throw e;
  }
}

async function writeRaster(sink, { zarrUrl, level, format, orientation, description, onProgress, signal }) {
  const { shape, dtype } = level;
  const spacing = level.scale.slice(-3); // mm
  let header;
  if (format === "tiff") header = tiffHeader({ shape, dtype, spacing });
  else if (format === "nifti") header = niftiHeader({ shape, dtype, spacing, orientation, description });
  else if (format === "nrrd") header = nrrdHeader({ shape, dtype, spacing, orientation, gzip: true, description });
  else throw new Error(`Unknown format ${format}`);
  await sink.write(header);
  const out = format === "nrrd" ? gzipSink(sink, { closeInner: false }) : sink;
  const total = rawSize(shape, dtype);
  let done = 0;
  onProgress?.(0, total);
  await streamPlanes(
    `${zarrUrl}/${level.path}`,
    async (plane) => {
      const bytes = new Uint8Array(plane.buffer, plane.byteOffset, plane.byteLength);
      await out.write(bytes);
      done += bytes.length;
      onProgress?.(done, total);
    },
    { signal },
  );
  if (out !== sink) await out.close();
}

async function fetchBytes(url, signal) {
  const r = await fetch(url, { signal });
  if (r.status === 404 || r.status === 403) return null;
  if (!r.ok) throw new Error(`HTTP ${r.status} fetching ${url}`);
  return new Uint8Array(await r.arrayBuffer());
}

async function writeOmeZarrZip(sink, { zarrUrl, level, levels, allLevels, filename, onProgress, signal }) {
  const zip = new ZipWriter((u8) => sink.write(u8));
  const root = filename.replace(/\.zip$/, "");
  const chosen = allLevels ? levels : [level];

  // Root group metadata, restricted to the exported levels.
  const groupMeta = JSON.parse(new TextDecoder().decode(await fetchBytes(`${zarrUrl}/zarr.json`, signal)));
  const ome = groupMeta.attributes?.ome ?? groupMeta.attributes;
  const keep = new Set(chosen.map((l) => l.path));
  for (const ms of ome.multiscales) ms.datasets = ms.datasets.filter((d) => keep.has(d.path));
  await zip.add(`${root}/zarr.json`, new TextEncoder().encode(JSON.stringify(groupMeta, null, 2)));

  const jobs = [];
  for (const lv of chosen) {
    jobs.push({ key: `${lv.path}/zarr.json` });
    const n = lv.shape.map((s, d) => Math.ceil(s / lv.chunks[d]));
    const sep = lv.separator || "/";
    for (let i = 0; i < n[0]; i++)
      for (let j = 0; j < n[1]; j++)
        for (let k = 0; k < n[2]; k++) jobs.push({ key: `${lv.path}/${["c", i, j, k].join(sep)}` });
  }
  let done = 0;
  onProgress?.(0, jobs.length, "files");
  // Fetch in parallel batches, write in order.
  for (let b = 0; b < jobs.length; b += CONCURRENCY * 4) {
    if (signal?.aborted) throw new DOMException("Export cancelled", "AbortError");
    const batch = jobs.slice(b, b + CONCURRENCY * 4);
    const data = await mapLimit(batch, CONCURRENCY, (job) => fetchBytes(`${zarrUrl}/${job.key}`, signal));
    for (let x = 0; x < batch.length; x++) {
      if (data[x]) await zip.add(`${root}/${batch[x].key}`, data[x]);
      done++;
    }
    onProgress?.(done, jobs.length, "files");
  }
  await zip.close();
}

/** Save a small text/bytes payload. */
export async function saveText(filename, text, mimeType = "text/plain", sinkPromise) {
  const sink = await (sinkPromise ?? openSink(filename, { mimeType }));
  await sink.write(typeof text === "string" ? new TextEncoder().encode(text) : text);
  await sink.close();
}
