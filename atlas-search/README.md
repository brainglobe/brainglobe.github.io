# BrainGlobe Atlas Search

A static website for finding [BrainGlobe](https://brainglobe.info) atlases, viewing them in
[neuroglancer](https://github.com/google/neuroglancer), and downloading their components.

- **Search** across atlas name, species (latin or common name), category, description,
  citation, links, coordinate space, component names, and **brain-region names/acronyms**.
  Filter by species, and by resolution with a range slider showing how many atlases exist at each resolution.
- **One page per atlas** (e.g. `allen_mouse`). A single resolution dropdown at the top drives
  the downloads, code snippets and metadata, and shows the full atlas name
  (`allen_mouse_25um`) with a copy button. Atlases that belong to one collection (e.g. the eight
  ADMBA developmental stages) are switched with an atlas dropdown next to it.
- **View** any atlas in neuroglancer using the state file BrainGlobe publishes for it
  (`ng_state_files/<atlas>.json`), which streams every resolution level.
- **Download** the template, annotation, hemisphere map and ontology separately:

  | Component | Formats |
  |---|---|
  | Template, annotation, hemisphere map | TIFF, NIfTI (`.nii.gz`), NRRD, OME-Zarr (`.zip`, optionally with every pyramid level) |
  | Ontology (terminology) | CSV (original), JSON (`structures.json` style), ITK-SNAP label file, 3D Slicer colour table |

Everything runs in the browser. There is no backend: volumes are read chunk-by-chunk straight
from the public BrainGlobe S3 bucket (OME-Zarr v0.5 / zarr v3) and converted client-side. On
Chromium browsers (Chrome, Edge) exports are streamed directly to disk via the File System
Access API, so even multi-GB volumes (e.g. 10 µm annotations) work; other browsers assemble the
file in memory.

## How it works

```
collections.toml         atlas titles, categories and descriptions (edited by hand)
scripts/build_index.py   crawl s3://brainglobe/atlas -> public/data/index.json
                         (+ public/data/terminologies/*.json)
src/search.js            query parsing, ranking, facets
src/neuroglancer.js      neuroglancer links (published state files)
src/slice.js             coronal section previews
src/export/formats.js    TIFF/BigTIFF, NIfTI-1 and NRRD header writers
src/export/zip.js        streaming ZIP64 writer (for OME-Zarr)
src/export/export.js     stream zarr chunks -> planes -> file
src/export/sink.js       save to disk (File System Access) or Blob, optional gzip
src/export/ontology.js   terminology converters
src/main.js              UI
```

The index builder reads `atlases/last_versions.conf`, every atlas `manifest.json`, the OME-Zarr
metadata of each template/annotation/hemisphere store, every `terminology.csv`, and the
atlas collections in `collections.toml`. It also samples each template to set a sensible
neuroglancer contrast range. It needs only the Python standard library (3.11+, plus optional
`numpy` and `zstandard` for contrast ranges and previews).

### Adding an atlas

The bucket is crawled automatically, but the human-written information about each atlas lives
in [`collections.toml`](collections.toml). When a new atlas is released, add its key (e.g.
`allen_mouse_25um`) to the `atlases` list of an existing `[[collection]]`, or add a new
collection with a `title`, `group` (category), optional `link`, and `description`. The index
build prints a warning for every atlas in the bucket that is not listed there; such atlases still
appear on the site, under their manifest name and without a description.

Each atlas page shows a coronal section of the template and annotation. Because zarr chunks are
3D, reading even one plane means downloading every chunk it crosses (hundreds of MB for atlases
stored at a single resolution), so the builder reads each plane once and writes a small preview
(`public/data/previews/*.json`, ~20–120 KB: a contrast-scaled template plane and the annotation
labels). Previews are named after the store versions; existing ones are reused (CI takes them
from the last published build) and previews of replaced stores are deleted.

### Coordinate conventions

BrainGlobe arrays are `(z, y, x)` with an orientation string giving the origin of each axis
(e.g. `asr`: anterior, superior, right). Exports keep the voxel order unchanged:

- **TIFF**: multi-page stack, one page per `z` slice; ImageJ metadata (µm spacing) for
  8/16-bit and float data, `tifffile` shape metadata otherwise. `tifffile.imread` returns exactly
  the BrainGlobe array.
- **NIfTI / NRRD**: axes `(i, j, k) = (x, y, z)`, with a qform/sform (NIfTI) or space directions
  (NRRD) mapping voxels to RAS+ millimetres derived from the orientation string, so
  the volumes open correctly oriented in ITK-SNAP, 3D Slicer, FSL, ANTs, etc.
- **OME-Zarr**: the original store (chosen level, or all levels), zipped without recompression.

## Development

```bash
cd atlas-search
npm install
python scripts/build_index.py      # ~5–15 min; writes public/data/
npm run dev                        # http://localhost:5173
npm run build                      # static site in dist/
```

Tests (need Python with `numpy tifffile nibabel pynrrd zarr>=3`):

```bash
npm test          # format writers vs tifffile / nibabel / pynrrd / zipfile
npm run test:e2e  # export a real atlas from S3 with the site's code, compare to zarr-python
```

## Deployment

The site is part of [brainglobe.info](https://brainglobe.info) and is served at
`https://brainglobe.info/atlases/`.

1. `.github/workflows/atlas_search.yml` (at the root of this repository) builds the index,
   runs the tests and builds the site. On pull requests the built site is uploaded as the
   `atlas-search` workflow artifact. On `main` (pushes that touch `atlas-search/`, a nightly
   schedule that picks up new atlas versions in the bucket, and manual runs) it publishes `dist/`
   to the `atlas-search-dist` branch and, if anything changed, starts the docs workflow.
2. The docs build (`make html`) downloads the `atlas-search-dist` branch into
   `docs/source/_atlas_search/atlases/`, which Sphinx copies to `atlases/` in the output, so the
   regular docs deployment publishes it alongside the rest of the website.

The old atlas details page (`documentation/brainglobe-atlasapi/usage/atlas-details.html`)
redirects here, sending its section anchors (e.g. `#allen-adult-mouse-brain-atlas`) to
`#/details/<anchor>`, which opens the matching atlas.

The site uses relative paths, so it can also be hosted under any sub-path or on any static host.
Atlases open in the public neuroglancer instance at `https://neuroglancer-demo.appspot.com/`
(`DEFAULT_NEUROGLANCER` in `src/neuroglancer.js`).
