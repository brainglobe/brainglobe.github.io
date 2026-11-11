// Neuroglancer links for BrainGlobe atlases.
//
// BrainGlobe publishes one viewer state per atlas version at
// <bucket>/ng_state_files/<atlas name>_v<version>.json (and the latest version
// again at <atlas name>.json). Each references the multiscale
// OME-Zarr template and annotation (all resolution levels), plus segment
// names and meshes from the precomputed layer, so there is one state per atlas
// rather than one per resolution. Neuroglancer loads a state from a URL given
// as the fragment: <instance>#!https://.../state.json

export const DEFAULT_NEUROGLANCER = "https://neuroglancer-demo.appspot.com/";

/** URLs of an atlas's stores, for the atlas entry of one resolution. */
export function componentUrls(index, atlas) {
  const root = index.root;
  const a = `${root}${atlas.annotation_set.location}`;
  return {
    template: `${root}${atlas.template.location}/template.ome.zarr`,
    annotation: `${a}/annotations_compressed.ome.zarr`,
    hemispheres: `${a}/hemispheres.ome.zarr`,
    precomputed: `${a}/annotations.precomputed`,
    terminology: `${root}${atlas.terminology.location}/terminology.csv`,
    manifest: `${root}${atlas.manifest}`,
  };
}

/**
 * URL of BrainGlobe's neuroglancer state for an atlas name: pinned to a version
 * (<name>_v<version>.json) or, without one, the latest version (<name>.json).
 */
export function stateFileUrl(index, name, version = null) {
  const file = version ? `${name}_v${version}.json` : `${name}.json`;
  return `${index.root.replace(/\/atlas\/?$/, "")}/ng_state_files/${encodeURIComponent(file)}`;
}

/** Link that opens a state file in a neuroglancer instance. */
export function viewerUrl(stateUrl, base = DEFAULT_NEUROGLANCER) {
  return `${(base || DEFAULT_NEUROGLANCER).replace(/#.*$/, "")}#!${stateUrl}`;
}
