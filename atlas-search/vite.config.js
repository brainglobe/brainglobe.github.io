import { defineConfig } from "vite";

// `base` is relative so the built site works from any sub-path
// (e.g. GitHub Pages at https://<org>.github.io/brainglobe-search/).
export default defineConfig({
  base: "./",
  build: {
    target: "es2022",
    // zstd/blosc WASM codecs are large but lazy-loaded only when exporting
    chunkSizeWarningLimit: 1000,
  },
});
