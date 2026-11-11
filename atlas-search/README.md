# BrainGlobe Atlas Search

A static website, served at <https://brainglobe.info/atlases/>, for finding
[BrainGlobe](https://brainglobe.info) atlases, viewing them in
[neuroglancer](https://github.com/google/neuroglancer) and downloading their components.

- **Search** by name, species (Latin or common), category, description, citation, links,
  coordinate space, component names and **brain-region names/acronyms**; filter by species and
  resolution.
- **One page per atlas** (e.g. `allen_mouse`), with resolution, version and (for collections such
  as the ADMBA stages) atlas pickers.
- **View** each atlas in neuroglancer via the state file BrainGlobe publishes for it.
- **Download** the template, annotation and hemisphere map as OME-Zarr (as published, every
  pyramid level by default) or converted to TIFF, NIfTI or NRRD, and the ontology as CSV (as
  published), `structures.json`, an ITK-SNAP label file or a 3D Slicer colour table.

There is no backend: volumes are read chunk by chunk from the public BrainGlobe bucket
(OME-Zarr v0.5) and converted in the browser. Chrome and Edge stream exports straight to disk, so
multi-GB volumes work; other browsers assemble the file in memory.

## Adding an atlas

The bucket is crawled automatically; the human-written information about each atlas lives in
[`collections.toml`](collections.toml). For a new atlas, add its name (e.g. `allen_mouse`, which
covers every resolution) to an existing `[[collection]]`, or add a collection with a `title`,
`group` (category), optional `link` and `description`. The index build warns about atlases that
are not listed; they still appear on the site, without a description.

## How it works

```
collections.toml         atlas titles, categories and descriptions (edited by hand)
scripts/build_index.py   bucket -> public/data/ (index.json, terminologies, previews)
src/main.js              UI
src/search.js            query parsing and ranking
src/neuroglancer.js      neuroglancer links
src/slice.js             coronal section previews
src/export/              TIFF/BigTIFF, NIfTI, NRRD and ZIP64 writers, streaming to disk
```

The index builder reads `last_versions.conf`, every atlas manifest, the OME-Zarr metadata of each
store, every `terminology.csv` and `collections.toml`. It needs only the Python standard library
(3.11+); with `numpy` and `zstandard` it also writes a coronal preview per atlas
(`public/data/previews/`), since reading one plane of a 3D-chunked store in the browser can mean
downloading hundreds of MB. Previews are named after the store versions and reused between builds.

Exports keep BrainGlobe's `(z, y, x)` voxel order. TIFF is a multi-page stack (`tifffile.imread`
returns the BrainGlobe array); NIfTI and NRRD carry a RAS+ affine derived from the orientation
string (e.g. `asr`), so they open correctly oriented in ITK-SNAP, 3D Slicer, FSL, ANTs, etc.

## Development

```bash
cd atlas-search
npm install
python scripts/build_index.py      # ~5–15 min; writes public/data/
npm run dev                        # http://localhost:5173
npm run build                      # static site in dist/
npm test                           # format writers vs tifffile / nibabel / pynrrd / zipfile
npm run test:e2e                   # export a real atlas from S3, compare to zarr-python
```

Tests need Python with `numpy tifffile nibabel pynrrd zarr>=3`.

## Deployment

`.github/workflows/atlas_search.yml` builds the index and site and runs the tests (on pull
requests the site is uploaded as the `atlas-search` artifact). On `main`, on pushes to
`atlas-search/`, nightly and on manual runs, it publishes the site to the `atlas-search-dist`
branch and, if anything changed, starts the docs workflow. `make html` copies that branch into
the docs build, which serves it at `atlases/`.

The old atlas details page redirects here; its section anchors (e.g.
`#allen-adult-mouse-brain-atlas`) open the matching atlas via `#/details/<anchor>`.
