import { exportVolume, FORMATS, saveText, sinkGzip } from "./export/export.js";
import { rawSize } from "./export/formats.js";
import { buildTree, hexToRgb, ITKSNAP_MAX_LABEL, toItkSnap, toSlicerCtbl, toStructuresJson } from "./export/ontology.js";
import { canStreamToDisk, openSink } from "./export/sink.js";
import { componentUrls, stateFileUrl, viewerUrl } from "./neuroglancer.js";
import { loadPreview } from "./slice.js";
import { buildSearchIndex, commonName, compareAtlases, facetCounts, formatResolution, minResolution, search } from "./search.js";

const app = document.getElementById("app");
const jobsEl = document.getElementById("jobs");

let INDEX = null;
let DOCS = null;
const BY_KEY = new Map(); // "allen_mouse_25um" -> latest atlas entry (one resolution)
const VERSIONS = new Map(); // "allen_mouse_25um" -> entries of every published version, newest first
const BY_NAME = new Map(); // "allen_mouse" -> {name, family, keys: [atlas entries, finest first]}
const TERM_CACHE = new Map();
const ADDED = new Map(); // "allen_mouse_25um" -> upload time of its first published version (ISO)
let FIRST_UPLOAD_DAY = ""; // day of the initial bulk upload; atlases from then predate the bucket

const state = {
  q: "",
  facets: { species: new Set(), resMin: null, resMax: null },
  expanded: new Set(),
};

// With no query the list is newest first; a query ranks by relevance.
const byRecency = () => !state.q.trim();

// ---------------------------------------------------------------------------
// utilities
// ---------------------------------------------------------------------------
const esc = (s) =>
  String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);

function h(html) {
  const t = document.createElement("template");
  t.innerHTML = html.trim();
  return t.content.firstElementChild;
}

function formatBytes(n) {
  if (!Number.isFinite(n)) return "?";
  const u = ["B", "KB", "MB", "GB", "TB"];
  let i = 0;
  while (n >= 1000 && i < u.length - 1) {
    n /= 1000;
    i++;
  }
  return `${n < 10 && i ? n.toFixed(1) : Math.round(n)} ${u[i]}`;
}

function linkify(text) {
  return esc(text).replace(/(https?:\/\/[^\s,;)]+)/g, '<a href="$1">$1</a>');
}

function highlight(text, terms) {
  let out = esc(text);
  for (const t of terms) {
    if (t.length < 2) continue;
    const re = new RegExp(`(${esc(t).replace(/[.*+?^${}()|[\]\\]/g, "\\$&")})`, "ig");
    out = out.replace(re, "<mark>$1</mark>");
  }
  return out;
}

function debounce(fn, ms = 120) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);
  };
}

let toastTimer;
function toast(msg) {
  let el = document.querySelector(".toast");
  if (!el) {
    el = h('<div class="toast" role="status"></div>');
    document.body.append(el);
  }
  el.textContent = msg;
  el.classList.add("show");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => el.classList.remove("show"), 2200);
}

async function copy(text, what = "Copied") {
  try {
    await navigator.clipboard.writeText(text);
    toast(`${what} to clipboard`);
  } catch {
    toast("Copy failed: the browser blocked clipboard access");
  }
}

function compareVersions(a, b) {
  const x = String(a).split(".").map(Number);
  const y = String(b).split(".").map(Number);
  for (let i = 0; i < Math.max(x.length, y.length); i++) if ((x[i] || 0) !== (y[i] || 0)) return (x[i] || 0) - (y[i] || 0);
  return 0;
}

const fmtDate = (iso) =>
  iso ? new Date(iso).toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric", timeZone: "UTC" }) : "";

function familyOf(a) {
  return a.docs?.title || a.name;
}

const pageHref = (name) => `#/atlas/${encodeURIComponent(name)}`;
/** Link to one resolution, pinned to its version or following the latest. */
const versionHref = (a, pinned) => (pinned ? `${pageHref(a.key)}/v${encodeURIComponent(a.version)}` : pageHref(a.key));

async function loadTerminology(atlas) {
  const t = INDEX.terminologies[atlas.terminology.location];
  if (!t) return null;
  if (!TERM_CACHE.has(t.file)) TERM_CACHE.set(t.file, fetch(`data/${t.file}`).then((r) => (r.ok ? r.json() : null)));
  return TERM_CACHE.get(t.file);
}

// ---------------------------------------------------------------------------
// theme (system / light / dark), as on brainglobe.info
// ---------------------------------------------------------------------------
function setupThemeToggle() {
  const btn = document.getElementById("theme-toggle");
  const order = ["system", "light", "dark"];
  const apply = (mode) => {
    if (mode === "system") delete document.documentElement.dataset.theme;
    else document.documentElement.dataset.theme = mode;
    btn.dataset.mode = mode;
    btn.title = `Theme: ${mode} (click to change)`;
    btn.setAttribute("aria-label", btn.title);
  };
  let saved = null;
  try {
    saved = localStorage.getItem("theme");
  } catch {}
  apply(saved || "system");
  btn.addEventListener("click", () => {
    const next = order[(order.indexOf(btn.dataset.mode) + 1) % order.length];
    try {
      if (next === "system") localStorage.removeItem("theme");
      else localStorage.setItem("theme", next);
    } catch {}
    apply(next);
  });
}

// ---------------------------------------------------------------------------
// routing
// ---------------------------------------------------------------------------
/**
 * Section id of a collection title on the former "atlas details" docs page
 * (docutils ids, after smart quotes removed the apostrophes).
 */
function legacyAnchor(title) {
  return title
    .replace(/['"]/g, "")
    .normalize("NFKD")
    .replace(/[^\x00-\x7f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^[^a-z]+/, "")
    .replace(/-+$/, "");
}

function route() {
  // Old links to …/atlas-details.html#<section> are redirected to #/details/<section>.
  const legacy = /^#\/details\/([^/]+)$/.exec(location.hash);
  if (legacy) {
    const id = decodeURIComponent(legacy[1]);
    const names = [...BY_NAME.values()]
      .filter((p) => p.keys.some((a) => a.docs?.title && legacyAnchor(a.docs.title) === id))
      .map((p) => p.name)
      .sort(byNameNumeric);
    history.replaceState(null, "", names.length ? pageHref(names[0]) : "#/");
  }
  const m = /^#\/atlas\/([^/]+)(?:\/v([^/]+))?$/.exec(location.hash);
  if (m) {
    const id = decodeURIComponent(m[1]);
    if (BY_NAME.has(id)) return renderDetail(BY_NAME.get(id));
    // a resolution-specific atlas name selects that resolution on the atlas
    // page, and /v<version> selects a version of it
    const atlas = BY_KEY.get(id);
    if (atlas) {
      const version = m[2] && VERSIONS.get(id).find((a) => a.version === decodeURIComponent(m[2]));
      return renderDetail(BY_NAME.get(atlas.name), version || atlas, Boolean(version));
    }
  }
  renderSearch();
}

window.addEventListener("hashchange", () => {
  route();
  window.scrollTo(0, 0);
});

// ---------------------------------------------------------------------------
// search view
// ---------------------------------------------------------------------------
const SYNTAX = [
  ["allen mouse", "atlases matching every word"],
  ['"light sheet"', "exact phrase"],
  ["region:CA1", "atlases whose ontology contains a region (name or acronym)"],
  ["res:<=25, res:10-50", "available at a resolution, in µm"],
  ["species:rattus", "field filter; also name, citation, orientation"],
  ["sym:no", "asymmetric atlases only"],
];

let searchView = null;

function renderSearch() {
  document.title = "Atlas search · BrainGlobe";
  if (!searchView) {
    searchView = h(`
      <div class="with-sidebar">
        <aside class="sidebar" id="facets" aria-label="Filters"></aside>
        <div class="content">
          <h1>Atlas search</h1>
          <p>Search the ${BY_NAME.size} atlases, in ${new Set([...BY_NAME.values()].map((p) => p.family)).size} collections, available through the
            <a href="../documentation/brainglobe-atlasapi/index.html">BrainGlobe Atlas API</a>
            by name, species, resolution, publication or brain region. Each atlas can be viewed in neuroglancer,
            and its template, annotation, hemisphere map and ontology downloaded separately.</p>
          <div class="searchbar">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
            <input id="q" type="search" autocomplete="off" spellcheck="false"
              placeholder="Search atlases" aria-label="Search atlases" />
          </div>
          <details class="syntax"><summary>Search syntax</summary>
            <table>${SYNTAX.map(([q, d]) => `<tr><td><code>${esc(q)}</code></td><td>${esc(d)}</td></tr>`).join("")}</table>
          </details>
          <p class="result-meta" id="result-meta"></p>
          <div id="results"></div>
        </div>
      </div>`);
    setupFacets();
    const input = searchView.querySelector("#q");
    input.value = state.q;
    input.addEventListener(
      "input",
      debounce(() => {
        state.q = input.value;
        syncUrl();
        updateResults();
      }),
    );
  }
  app.replaceChildren(searchView);
  updateResults();
  const input = searchView.querySelector("#q");
  if (document.activeElement === document.body) input.focus({ preventScroll: true });
}

function syncUrl() {
  const u = new URL(location.href);
  if (state.q) u.searchParams.set("q", state.q);
  else u.searchParams.delete("q");
  history.replaceState(null, "", u);
}

/** Collapse per-resolution results into one result per atlas name. */
function byName(results) {
  const out = new Map();
  for (const r of results) {
    const n = r.atlas.name;
    const e = out.get(n);
    if (!e) out.set(n, { ...r, atlas: BY_NAME.get(n).keys[0], regionMatches: [...r.regionMatches] });
    else for (const x of r.regionMatches) if (!e.regionMatches.includes(x)) e.regionMatches.push(x);
  }
  return [...out.values()];
}

/** When an atlas name was first added: the earliest upload of any of its resolutions. */
function addedOf(name) {
  let first = "";
  for (const a of BY_NAME.get(name).keys) {
    const t = ADDED.get(a.key) || "";
    if (t && (!first || t < first)) first = t;
  }
  return first;
}

function updateResults() {
  const results = byName(search(DOCS, state.q, state.facets));
  if (byRecency()) {
    // newest first; stable, so ties keep the relevance / default order
    for (const r of results) r.added = addedOf(r.atlas.name);
    results.sort((x, y) => (y.added > x.added) - (y.added < x.added));
  }
  updateFacets();

  // group atlases by documentation family, preserving the rank of the best member
  const families = new Map();
  for (const r of results) {
    const fam = familyOf(r.atlas);
    if (!families.has(fam)) families.set(fam, { name: fam, items: [], regionMatches: new Set() });
    const f = families.get(fam);
    f.items.push(r);
    if ((r.added || "") > (f.added || "")) f.added = r.added;
    r.regionMatches.forEach((x) => f.regionMatches.add(x));
  }
  const n = results.length;
  const c = families.size;
  searchView.querySelector("#result-meta").textContent =
    `${n} atlas${n === 1 ? "" : "es"} in ${c} collection${c === 1 ? "" : "s"}${byRecency() ? ", newest first" : ""}`;

  const terms = (state.q.match(/"[^"]+"|\S+/g) || []).filter((t) => !t.includes(":")).map((t) => t.replace(/"/g, ""));
  const list = searchView.querySelector("#results");
  if (!n) {
    list.innerHTML = `<p class="muted">No atlases match. Try fewer words or clear the filters.</p>`;
    return;
  }
  const frag = document.createDocumentFragment();
  for (const fam of families.values()) frag.append(familyEntry(fam, terms));
  list.replaceChildren(frag);
}

const byNameNumeric = (a, b) => a.localeCompare(b, undefined, { numeric: true });

function resolutionsText(page) {
  return page.keys.map((a) => formatResolution(a).replace(" µm", "")).join(", ") + " µm";
}

function familyEntry(fam, terms) {
  const first = fam.items[0].atlas;
  const d = first.docs || {};
  const names = fam.items.map((r) => r.atlas.name).sort(byNameNumeric);
  const LIMIT = 12;
  const expanded = state.expanded.has(fam.name);
  const shown = expanded ? names : names.slice(0, LIMIT);
  const regions = [...fam.regionMatches].slice(0, 6);
  const common = commonName(first.species);
  const summary = d.description ? d.description.split("\n\n")[0] : first.citation || "";
  const single = names.length === 1 ? BY_NAME.get(names[0]) : null;
  const addedDay = fam.added?.slice(0, 10);
  const added = byRecency() && addedDay && addedDay !== FIRST_UPLOAD_DAY ? fmtDate(fam.added) : "";
  const el = h(`
    <article class="result">
      <h2><a href="${pageHref(names[0])}">${highlight(fam.name, terms)}</a></h2>
      <p class="species">${common ? `${esc(common)} · ` : ""}<em>${highlight(first.species || "", terms)}</em>
        ${single ? ` · ${esc(resolutionsText(single))}` : ""}
        ${added ? ` · <span class="added">Added ${esc(added)}</span>` : ""}</p>
      <p class="summary">${highlight(summary, terms)}</p>
      ${single ? "" : `<p class="keys">${shown
        .map((nm) => `<a href="${pageHref(nm)}"><code>${highlight(nm, terms)}</code></a>`)
        .join(" ")}
        ${names.length > LIMIT ? `<button class="link-button" type="button">${expanded ? "show fewer" : `${names.length - LIMIT} more`}</button>` : ""}</p>`}
      ${regions.length ? `<p class="regions-hit">Matching regions: ${regions.map((r) => {
        const [acr, name] = r.split("\t");
        return `${highlight(name, terms)} (<code>${esc(acr)}</code>)`;
      }).join(", ")}</p>` : ""}
    </article>`);
  el.querySelector(".link-button")?.addEventListener("click", () => {
    if (expanded) state.expanded.delete(fam.name);
    else state.expanded.add(fam.name);
    updateResults();
  });
  return el;
}

// Distinct resolutions (finest axis, µm) across all atlases; the stops of the resolution slider.
let RES_VALUES = [];
let SPECIES_ORDER = []; // all species, most atlases first
const KEY_RES_INDEX = new Map(); // atlas key -> index into RES_VALUES

function buildResolutionStops() {
  const vals = [...new Set(INDEX.atlases.map((a) => minResolution(a)))].sort((a, b) => a - b);
  RES_VALUES = vals.filter((v, i) => i === 0 || v - vals[i - 1] > 1e-6);
  const perSpecies = facetCounts([...BY_NAME.values()].map((p) => ({ atlas: p.keys[0] }))).species;
  SPECIES_ORDER = [...perSpecies.keys()].sort((a, b) => perSpecies.get(b) - perSpecies.get(a) || a.localeCompare(b));
  for (const a of INDEX.atlases) {
    const r = minResolution(a);
    KEY_RES_INDEX.set(a.key, RES_VALUES.findIndex((v) => Math.abs(v - r) <= 1e-6));
  }
}

const fmtRes = (v) => `${Number(v.toFixed(3))} µm`;

let resSlider = null;

/** Dual-handle resolution slider with a histogram of available atlases per resolution. */
function createResSlider(onChange) {
  const n = RES_VALUES.length;
  const el = h(`
    <div class="res-slider" style="--steps:${Math.max(1, n - 1)}">
      <div class="histogram" aria-hidden="true">${RES_VALUES.map(() => "<span></span>").join("")}</div>
      <div class="range">
        <div class="track"></div><div class="fill"></div>
        <input type="range" class="lo" min="0" max="${n - 1}" step="1" value="0" aria-label="Finest resolution" />
        <input type="range" class="hi" min="0" max="${n - 1}" step="1" value="${n - 1}" aria-label="Coarsest resolution" />
      </div>
      <div class="range-values"><output class="lo-val"></output><output class="hi-val"></output></div>
    </div>`);
  const lo = el.querySelector(".lo");
  const hi = el.querySelector(".hi");
  const fill = el.querySelector(".fill");
  const bars = [...el.querySelectorAll(".histogram span")];
  const sync = () => {
    const a = +lo.value;
    const b = +hi.value;
    fill.style.setProperty("--lo", a);
    fill.style.setProperty("--hi", b);
    // let the lower handle be grabbed when both sit at the top end
    lo.style.zIndex = a > (n - 1) / 2 ? 3 : 1;
    lo.setAttribute("aria-valuetext", fmtRes(RES_VALUES[a]));
    hi.setAttribute("aria-valuetext", fmtRes(RES_VALUES[b]));
    el.querySelector(".lo-val").textContent = fmtRes(RES_VALUES[a]);
    el.querySelector(".hi-val").textContent = fmtRes(RES_VALUES[b]);
    bars.forEach((s, i) => s.classList.toggle("in", i >= a && i <= b));
  };
  // handles can't cross; null means "no limit" at either end
  const onInput = (moved, other) => () => {
    if (moved === lo ? +lo.value > +hi.value : +hi.value < +lo.value) moved.value = other.value;
    sync();
    onChange(+lo.value === 0 ? null : RES_VALUES[+lo.value], +hi.value === n - 1 ? null : RES_VALUES[+hi.value]);
  };
  lo.addEventListener("input", onInput(lo, hi));
  hi.addEventListener("input", onInput(hi, lo));
  sync();
  return {
    el,
    /** counts[i] = number of atlases available at RES_VALUES[i] */
    setCounts(counts) {
      const max = Math.max(1, ...counts);
      bars.forEach((s, i) => {
        // square-root scale so single atlases stay visible next to the 20/25 µm peaks
        s.style.height = counts[i] ? `${Math.max(6, Math.sqrt(counts[i] / max) * 100)}%` : "0";
        s.title = `${fmtRes(RES_VALUES[i])}: ${counts[i]} atlas${counts[i] === 1 ? "" : "es"}`;
      });
    },
    set(min, max) {
      lo.value = min == null ? 0 : Math.max(0, RES_VALUES.findIndex((v) => v >= min - 1e-6));
      const j = max == null ? n - 1 : RES_VALUES.findLastIndex((v) => v <= max + 1e-6);
      hi.value = j < 0 ? n - 1 : j;
      sync();
    },
  };
}

function setupFacets() {
  const box = searchView.querySelector("#facets");
  box.innerHTML = `
    <h2>Species</h2>
    <div class="facet-list" id="species-list"></div>
    <h2>Resolution</h2>
    <div id="res-slot"></div>
    <button class="link-button clear-facets" type="button" hidden>Clear filters</button>`;
  const f = state.facets;
  resSlider = createResSlider((min, max) => {
    f.resMin = min;
    f.resMax = max;
    updateResults();
  });
  box.querySelector("#res-slot").replaceWith(resSlider.el);
  box.querySelector("#species-list").addEventListener("change", (e) => {
    const cb = e.target;
    if (cb.checked) f.species.add(cb.value);
    else f.species.delete(cb.value);
    updateResults();
  });
  box.querySelector(".clear-facets").addEventListener("click", () => {
    Object.assign(f, { species: new Set(), resMin: null, resMax: null });
    resSlider.set(null, null);
    updateResults();
  });
}

/** Facet counts follow the other filters, not their own (as on booking sites). */
function updateFacets() {
  const f = state.facets;
  const box = searchView.querySelector("#facets");

  // every species stays listed in a fixed order so rows don't jump while the slider moves
  const speciesCounts = facetCounts(byName(search(DOCS, state.q, { resMin: f.resMin, resMax: f.resMax }))).species;
  box.querySelector("#species-list").innerHTML = SPECIES_ORDER.map((v) => {
    const n = speciesCounts.get(v) || 0;
    const on = f.species.has(v);
    const common = commonName(v);
    return `<label class="facet-item${n ? "" : " empty"}" title="${esc(v)}"><input type="checkbox" value="${esc(v)}" ${on ? "checked" : ""} ${n || on ? "" : "disabled"}/>
      <span>${common ? esc(common) : `<em>${esc(v)}</em>`}</span><span class="count">${n}</span></label>`;
  }).join("");

  // atlases (names) available at each resolution, given the query and species filter
  const sets = RES_VALUES.map(() => new Set());
  for (const r of search(DOCS, state.q, { species: f.species })) sets[KEY_RES_INDEX.get(r.atlas.key)]?.add(r.atlas.name);
  resSlider.setCounts(sets.map((s) => s.size));

  box.querySelector(".clear-facets").hidden = !(f.species.size || f.resMin != null || f.resMax != null);
}


// ---------------------------------------------------------------------------
// atlas page (one per atlas name, covering all its resolutions)
// ---------------------------------------------------------------------------
const COMPONENTS = [
  { id: "template", label: "Template", help: "reference image" },
  { id: "annotation", label: "Annotation", help: "region label volume" },
  { id: "hemispheres", label: "Hemisphere map", help: "left/right label volume" },
];

/** Multiscale store of one component for one atlas entry: {url, levels, level} or null. */
function componentStore(atlas, comp) {
  const url = componentUrls(INDEX, atlas)[comp.id];
  if (comp.id === "template") {
    const t = INDEX.templates[atlas.template.location];
    return t && { url, levels: t.levels, level: atlas.template.level };
  }
  const g = INDEX.annotation_sets[atlas.annotation_set.location]?.[comp.id];
  const { level, hemispheres_level } = atlas.annotation_set;
  return g && { url, levels: g.levels, level: comp.id === "annotation" ? level : hemispheres_level };
}

const levelText = (lv) => `${lv.shape.join(" × ")} · ${lv.dtype} · ${formatBytes(rawSize(lv.shape, lv.dtype))}`;

let allLevels = true; // "include all resolution levels" in OME-Zarr downloads (default on), kept across pages

/**
 * One page per atlas name. `selected` is the atlas entry (resolution) that the
 * single resolution dropdown at the top of the page selects; everything on the
 * page (downloads, code, metadata) follows it.
 */
function renderDetail(page, selected = null, pinned = false) {
  const atlas = selected && page.keys.some((a) => a.key === selected.key) ? selected : page.keys[0];
  const versions = VERSIONS.get(atlas.key);
  const newest = versions[0];
  // Unless a version is picked, the page follows the latest version and links
  // the unversioned neuroglancer state, which BrainGlobe keeps on the latest.
  if (atlas.latest === false) pinned = true;
  const d = atlas.docs || {};
  const title = familyOf(atlas);
  const ann = INDEX.annotation_sets[atlas.annotation_set.location] || {};
  const term = INDEX.terminologies[atlas.terminology.location];
  const urls = componentUrls(INDEX, atlas);
  const stateUrl = stateFileUrl(INDEX, atlas.name, pinned ? atlas.version : null);
  document.title = `${atlas.key}${atlas.latest ? "" : ` v${atlas.version}`} · BrainGlobe atlas search`;
  const common = commonName(atlas.species);
  const variants = [...BY_NAME.values()].filter((p) => p.family === page.family).sort((a, b) => byNameNumeric(a.name, b.name));
  const sections = [
    ["about", "About"],
    ["download", "Download"],
    ["regions", "Brain regions"],
    ["code", "Use from code"],
    ["metadata", "Metadata"],
  ];
  const row = (k, v) => `<tr><th scope="row">${k}</th><td>${v}</td></tr>`;

  const view = h(`
    <div class="with-sidebar detail">
      <div class="content">
        <nav class="breadcrumb" aria-label="Breadcrumb"><a href="#/">Atlas search</a><span aria-hidden="true">›</span><span>${esc(title)}</span></nav>
        <h1>${esc(title)}</h1>
        <p class="atlas-line"><span>${common ? `${esc(common)}, ` : ""}<em>${esc(atlas.species)}</em></span>
          ${variants.length > 1 ? `<span>one of ${variants.length} atlases in this collection</span>` : ""}</p>

        <div class="atlas-picker">
          ${variants.length > 1 ? `
            <label for="variant">Atlas</label>
            <select id="variant">${variants
              .map((p) => `<option value="${esc(p.name)}" ${p.name === page.name ? "selected" : ""}>${esc(p.name)}</option>`)
              .join("")}</select>` : ""}
          <label for="resolution">Resolution</label>
          ${page.keys.length > 1
            ? `<select id="resolution">${page.keys
                .map((a) => `<option value="${esc(a.key)}" ${a.key === atlas.key ? "selected" : ""}>${esc(formatResolution(a))}</option>`)
                .join("")}</select>`
            : `<span id="resolution" class="static">${esc(formatResolution(atlas))}</span>`}
          <label for="version">Version</label>
          <select id="version">
            <option value="" ${pinned ? "" : "selected"}>Latest (${esc(newest.version)})</option>
            ${versions.map((a) => `<option value="${esc(a.version)}" ${pinned && a === atlas ? "selected" : ""}>${esc(a.version)}</option>`).join("")}
          </select>
          <span class="label" id="key-label">Atlas name</span>
          <div class="copy-field" role="group" aria-labelledby="key-label">
            <code>${esc(atlas.key)}</code>
            <button class="btn small" type="button" data-copy="${esc(atlas.key)}">Copy</button>
          </div>
        </div>

        ${atlas.latest ? "" : `<p class="notice">This is version ${esc(atlas.version)}, uploaded ${esc(fmtDate(atlas.uploaded))}.
          The latest version is <a href="${esc(versionHref(newest, false))}">${esc(newest.version)}</a>; everything on this page refers to ${esc(atlas.version)}.</p>`}

        <div class="actions">
          <a class="btn primary" id="ng-open" href="#" target="_blank" rel="noopener">Open in neuroglancer</a>
          <button class="btn" id="ng-copy" type="button">Copy neuroglancer link</button>
        </div>

        <section id="about"><h2>About</h2>
          <figure class="slice-figure" id="slice-figure">
            <div class="slice-panels">
              <div class="slice-panel"><canvas id="slice-template" aria-label="Coronal section of the template"></canvas></div>
              <div class="slice-panel"><canvas id="slice-annotation" aria-label="Coronal section of the annotation"></canvas></div>
            </div>
            <figcaption id="slice-caption" class="muted">Loading coronal section…</figcaption>
          </figure>
          ${d.description ? d.description.split("\n\n").map((p) => `<p>${linkify(p)}</p>`).join("") : ""}</section>

        <section id="download">
          <h2>Download</h2>
          <table class="dl-table">
            <thead><tr><th>Component</th><th>Size at ${esc(formatResolution(atlas))}</th><th>Format</th></tr></thead>
            <tbody id="dl-body"></tbody>
          </table>
          <label class="option"><input type="checkbox" id="opt-all-levels" ${allLevels ? "checked" : ""}/> Include all resolution levels in OME-Zarr downloads</label>
          <p class="note" id="itk-note" hidden></p>
          <p class="note">BrainGlobe stores volumes as OME-Zarr and ontologies as CSV; these downloads contain the data as published.
            The other formats are converted in your browser: volumes are read chunk by chunk from the public OME-Zarr stores and rewritten.
            TIFF files are multi-page stacks in (z, y, x) order. NIfTI and NRRD files carry a RAS affine derived from
            the atlas orientation (<code>${esc(atlas.orientation)}</code>).
            ${canStreamToDisk
              ? "Files are written straight to disk as they download."
              : "This browser cannot stream to disk, so files are assembled in memory; for large volumes use Chrome or Edge, a lower resolution, or the Python API."}</p>
        </section>

        <section id="regions">
          <h2>Brain regions${term ? ` <span class="count">${term.count}</span>` : ""}</h2>
          <div class="region-filter"><input class="text-input" id="region-q" type="search" placeholder="Filter by name or acronym" aria-label="Filter regions" />
            <span class="muted" id="region-status" aria-live="polite"></span></div>
          <div class="tree" id="tree"><p class="muted">Loading…</p></div>
        </section>

        <section id="code">
          <h2>Use from code</h2>
          <h3>Python</h3>
          ${snippet(`from brainglobe_atlasapi import BrainGlobeAtlas\n\natlas = BrainGlobeAtlas("${atlas.key}"${pinned ? `, version="${atlas.version}"` : ""})\ntemplate = atlas.template        # numpy array (z, y, x)\nannotation = atlas.annotation\nhemispheres = atlas.hemispheres\nprint(atlas.lookup_df)           # brain regions`)}
          <h3>Command line</h3>
          ${atlas.latest
            ? snippet(`brainglobe install -a ${atlas.key}`)
            : `<p class="note">The <code>brainglobe install</code> command only installs the latest version (${esc(newest.version)}).
                Use the Python API above to get version ${esc(atlas.version)}.</p>`}
        </section>

        <section id="metadata">
          <h2>Metadata</h2>
          <table class="meta">
            ${row("Atlas name", `<code>${esc(atlas.key)}</code>`)}
            ${row("Species", `<em>${esc(atlas.species)}</em>`)}
            ${row("Version", `${esc(atlas.version)}${atlas.latest ? " (latest)" : ""}`)}
            ${atlas.uploaded ? row("Uploaded", esc(fmtDate(atlas.uploaded))) : ""}
            ${row("Resolution", `${esc(atlas.resolution.join(" × "))} µm`)}
            ${row("Shape", `${esc(atlas.shape.join(" × "))} (z, y, x)`)}
            ${row("Orientation", `<code>${esc(atlas.orientation)}</code>`)}
            ${row("Symmetric", atlas.symmetric ? "yes" : "no")}
            ${row("Citation", linkify(atlas.citation))}
            ${row("Atlas link", linkify(atlas.atlas_link))}
            ${atlas.additional_references.length
              ? row(
                  "Additional templates",
                  atlas.additional_references
                    .map((r) => (typeof r === "string" ? linkify(r) : `<code>${esc(r.name)}</code>${r.version ? ` v${esc(r.version)}` : ""}`))
                    .join("<br>"),
                )
              : ""}
            ${atlas.atlas_packager ? row("Packager", linkify(atlas.atlas_packager)) : ""}
            ${row("Coordinate space", `<code>${esc(atlas.coordinate_space)}</code>`)}
            ${row("Template", `<code>${esc(atlas.template.name)}</code> v${esc(atlas.template.version)}`)}
            ${row("Annotation set", `<code>${esc(atlas.annotation_set.name)}</code> v${esc(atlas.annotation_set.version)}`)}
            ${row("Terminology", `<code>${esc(atlas.terminology.name)}</code> v${esc(atlas.terminology.version)}`)}
            ${row("Meshes", ann.meshes ? "yes" : "no")}
            ${row("Manifest", `<a href="${esc(urls.manifest)}">manifest.json</a>`)}
            ${row("Neuroglancer state", `<a href="${esc(stateUrl)}">${esc(decodeURIComponent(stateUrl.split("/").pop()))}</a>`)}
          </table>
        </section>

      </div>

      <aside class="toc" aria-label="On this page">
        <h2>On this page</h2>
        <ul>${sections.map(([id, label]) => `<li><a href="#${id}" data-jump="${id}">${label}</a></li>`).join("")}</ul>
      </aside>
    </div>`);

  view.addEventListener("click", (e) => {
    const b = e.target.closest("[data-copy]");
    if (b) copy(b.dataset.copy);
  });
  // in-page links: scroll without touching the hash router
  view.querySelectorAll("[data-jump]").forEach((a) =>
    a.addEventListener("click", (e) => {
      e.preventDefault();
      view.querySelector(`#${a.dataset.jump}`)?.scrollIntoView({ behavior: "smooth" });
    }),
  );
  view.querySelector("#variant")?.addEventListener("change", (e) => {
    location.hash = pageHref(e.target.value);
  });
  // the URL names the selected resolution and version, so links keep them
  const select = (entry, pin, focus) => {
    history.replaceState(null, "", versionHref(entry, pin));
    renderDetail(page, entry, pin);
    app.querySelector(focus)?.focus();
  };
  view.querySelector("select#resolution")?.addEventListener("change", (e) => {
    // keep the selected version if the new resolution has it
    const vs = VERSIONS.get(e.target.value);
    const same = pinned && vs.find((a) => a.version === atlas.version);
    select(same || vs[0], Boolean(same), "#resolution");
  });
  view.querySelector("select#version")?.addEventListener("change", (e) => {
    const v = e.target.value;
    select(v ? versions.find((a) => a.version === v) : newest, Boolean(v), "#version");
  });
  view.querySelector("#opt-all-levels").addEventListener("change", (e) => (allLevels = e.target.checked));
  app.replaceChildren(view);

  renderDownloads(view, page, atlas);

  const ngLink = viewerUrl(stateUrl);
  view.querySelector("#ng-open").href = ngLink;
  view.querySelector("#ng-copy").addEventListener("click", () => copy(ngLink, "Neuroglancer link copied"));

  renderSlice(view, atlas);

  loadTerminology(atlas).then((rows) => {
    if (!view.isConnected) return;
    renderTree(view, rows);
    const over = rows ? rows.filter((r) => r.value > ITKSNAP_MAX_LABEL).length : 0;
    if (over) {
      const note = view.querySelector("#itk-note");
      note.textContent = `${over} of ${rows.length} regions have annotation values above ${ITKSNAP_MAX_LABEL}, which ITK-SNAP cannot represent; they are commented out in the ITK-SNAP label file.`;
      note.hidden = false;
    }
    renderOntologyRow(view, atlas, rows, urls);
  });
}

/** Middle coronal section (pre-rendered by the index builder), template beside annotation. */
async function renderSlice(view, atlas) {
  const fig = view.querySelector("#slice-figure");
  const caption = view.querySelector("#slice-caption");
  const selLevel = INDEX.templates[atlas.template.location]?.levels.find((l) => l.path === atlas.template.level);
  if (!atlas.preview || !selLevel) {
    fig.remove();
    return;
  }
  try {
    const rows = await loadTerminology(atlas);
    const colours = new Map((rows || []).map((r) => [r.value, hexToRgb(r.color)]));
    const img = await loadPreview(`data/${atlas.preview}`, colours);
    if (!view.isConnected) return;

    // the slice index in the selected resolution, from the preview's physical position
    const ap = img.ap_axis;
    const n = selLevel.shape[ap];
    const res = selLevel.scale[ap];
    const index = Math.min(n - 1, Math.max(0, Math.round((img.position_mm - selLevel.translation[ap]) / res)));
    const fromAnterior = (img.ap_from === "a" ? index : n - 1 - index) * res;

    const draw = (canvas, data) => {
      canvas.width = img.width;
      canvas.height = img.height;
      canvas.getContext("2d").putImageData(data, 0, 0);
      canvas.style.aspectRatio = String(img.aspect);
      canvas.style.setProperty("--aspect", String(img.aspect));
      canvas.parentElement.dataset.left = img.left;
      canvas.parentElement.dataset.right = img.right;
    };
    const tc = view.querySelector("#slice-template");
    const ac = view.querySelector("#slice-annotation");
    draw(tc, img.template);
    if (img.labels) draw(ac, img.overlay);
    else ac.parentElement.remove();

    const shownUm = +(img.level.scale[ap] * 1000).toPrecision(4);
    caption.classList.remove("muted");
    caption.innerHTML = `<strong>Coronal section ${index} of ${n}</strong> of <code>${esc(atlas.key)}</code> version ${esc(atlas.version)}
      (0-based index along the anterior–posterior axis, ${fromAnterior.toFixed(2)} mm from the anterior edge).
      Left: template.${img.labels ? " Right: annotation in the atlas colours over the template." : ""}
      Shown at ${esc(String(shownUm))} µm, viewed from the front, with the
      ${img.left === "L" ? "left" : "right"} hemisphere on the left of the image.
      ${Object.keys(img.corrupt_chunks || {}).length
        ? `<span class="slice-warning">Black rectangles are missing data: ${Object.entries(img.corrupt_chunks)
            .map(([k, v]) => `${v.length} corrupt chunk${v.length === 1 ? "" : "s"} in the published ${k} (${v.map((c) => `<code>${esc(c)}</code>`).join(", ")})`)
            .join("; ")}.</span>`
        : ""}
      ${img.labels ? `<span class="slice-hover" id="slice-hover">Hover over the annotation to name a region.</span>` : ""}`;

    if (img.labels) {
      const byValue = new Map((rows || []).map((r) => [r.value, r]));
      const hover = view.querySelector("#slice-hover");
      const idle = "Hover over the annotation to name a region.";
      ac.addEventListener("mousemove", (e) => {
        const r = ac.getBoundingClientRect();
        const x = Math.min(img.width - 1, Math.floor(((e.clientX - r.left) / r.width) * img.width));
        const y = Math.min(img.height - 1, Math.floor(((e.clientY - r.top) / r.height) * img.height));
        const v = img.labels[y * img.width + x];
        const row = byValue.get(v);
        hover.textContent = v ? (row ? `${row.name} (${row.acronym})` : `Label ${v}`) : "Outside the annotated regions.";
      });
      ac.addEventListener("mouseleave", () => (hover.textContent = idle));
    }
  } catch (e) {
    console.error(e);
    if (view.isConnected) fig.remove();
  }
}

function snippet(code) {
  return `<div class="snippet-wrap"><pre class="snippet"><code>${esc(code)}</code></pre><button class="btn small" type="button" data-copy="${esc(code)}">Copy</button></div>`;
}

/** Download buttons split into the format BrainGlobe stores and in-browser conversions. */
function fmtGroups(buttons) {
  const group = (native) => {
    const items = buttons.filter((b) => !!b.native === native);
    if (!items.length) return "";
    return `<div class="fmt-group"><span class="fmt-kind">${native ? "BrainGlobe format" : "Converted in browser"}</span>
      <div class="fmt-buttons">${items
        .map((b) => `<button class="btn small${native ? " native" : ""}" type="button" ${b.attr} title="${esc(b.title)}">${b.label}</button>`)
        .join("")}</div></div>`;
  };
  return `<div class="fmt-groups">${group(true)}${group(false)}</div>`;
}

function renderDownloads(view, page, atlas) {
  const body = view.querySelector("#dl-body");
  const formatButtons = fmtGroups(Object.entries(FORMATS).map(([k, f]) => ({ native: f.native, attr: `data-fmt="${k}"`, title: f.note, label: f.label })));
  for (const comp of COMPONENTS) {
    const what = `<td class="what">${comp.label}<small>${comp.help}</small></td>`;
    const store = componentStore(atlas, comp);
    const level = store?.levels.find((l) => l.path === store.level);
    if (!level) {
      body.append(h(`<tr>${what}<td colspan="2" class="muted">Not available for this atlas</td></tr>`));
      continue;
    }
    const row = h(`
      <tr>
        ${what}
        <td class="size">${esc(levelText(level))}</td>
        <td>${formatButtons}</td>
      </tr>`);
    row.addEventListener("click", (e) => {
      const fmt = e.target.closest("[data-fmt]")?.dataset.fmt;
      if (!fmt) return;
      const all = fmt === "ome-zarr" && allLevels;
      const filename = `${all ? `${page.name}_multiscale` : atlas.key}_v${atlas.version}_${comp.id}${FORMATS[fmt].ext}`;
      startJob(filename, { gzip: sinkGzip(fmt) }, (onProgress, signal, sinkPromise) =>
        exportVolume({
          zarrUrl: store.url,
          level,
          levels: store.levels,
          allLevels: all,
          format: fmt,
          orientation: atlas.orientation,
          filename,
          description: `BrainGlobe ${atlas.key} v${atlas.version} ${comp.id}`,
          onProgress,
          signal,
          sinkPromise,
        }),
      );
    });
    body.append(row);
  }
  body.append(h(`<tr id="ontology-row"><td class="what">Ontology<small>region terminology</small></td><td class="muted">${esc(atlas.terminology.name)}</td><td class="muted">Loading…</td></tr>`));
}


function renderOntologyRow(view, atlas, rows, urls) {
  const row = view.querySelector("#ontology-row");
  if (!row) return;
  const cell = row.lastElementChild;
  if (!rows) {
    cell.textContent = "Not available";
    return;
  }
  cell.classList.remove("muted");
  cell.innerHTML = fmtGroups([
    { native: true, attr: `data-o="csv"`, title: "Original BrainGlobe terminology.csv", label: "CSV" },
    { attr: `data-o="json"`, title: "BrainGlobe structures.json (list of structures)", label: "JSON" },
    { attr: `data-o="itk"`, title: "ITK-SNAP label description file (labels above 65535 are commented out)", label: "ITK-SNAP" },
    { attr: `data-o="ctbl"`, title: "3D Slicer colour table", label: "Slicer" },
  ]);
  const base = `${atlas.terminology.name}_v${atlas.terminology.version}`;
  const outputs = {
    csv: [`${base}.csv`, "text/csv", async () => new Uint8Array(await (await fetch(urls.terminology)).arrayBuffer())],
    json: [`${base}_structures.json`, "application/json", () => toStructuresJson(rows)],
    itk: [`${base}_itksnap.txt`, "text/plain", () => toItkSnap(rows)],
    ctbl: [`${base}.ctbl`, "text/plain", () => toSlicerCtbl(rows)],
  };
  cell.addEventListener("click", (e) => {
    const o = e.target.closest("[data-o]")?.dataset.o;
    if (!o) return;
    const [name, mimeType, make] = outputs[o];
    startJob(name, { mimeType }, async (onProgress, signal, sinkPromise) => saveText(name, await make(), mimeType, sinkPromise));
  });
}

function renderTree(view, rows) {
  const box = view.querySelector("#tree");
  const input = view.querySelector("#region-q");
  const status = view.querySelector("#region-status");
  if (!rows) {
    box.innerHTML = `<p class="muted">No terminology available.</p>`;
    input.hidden = true;
    return;
  }
  const roots = buildTree(rows);
  const swatch = (c) => `<span class="swatch" style="background:${esc(c || "#ccc")}"></span>`;
  const mark = (text, q) => {
    const i = q ? text.toLowerCase().indexOf(q) : -1;
    return i < 0 ? esc(text) : `${esc(text.slice(0, i))}<mark>${esc(text.slice(i, i + q.length))}</mark>${esc(text.slice(i + q.length))}`;
  };
  const label = (n, q = "") =>
    `${swatch(n.color)}${mark(n.name, q)}<span class="acr">${mark(n.acronym, q)}</span><span class="val">${esc(n.value)}</span>`;

  // whole subtree; only the top level open unless `open` says otherwise
  const renderNode = (n, depth) =>
    n.children.length
      ? `<li><details ${depth < 1 ? "open" : ""}><summary>${label(n)}</summary><ul>${n.children.map((c) => renderNode(c, depth + 1)).join("")}</ul></details></li>`
      : `<li class="leaf">${label(n)}</li>`;
  const full = `<ul>${roots.map((r) => renderNode(r, 0)).join("")}</ul>`;
  box.innerHTML = full;
  status.textContent = "";

  const matches = (n, q) => n.name.toLowerCase().includes(q) || n.acronym.toLowerCase().includes(q);

  /**
   * Filtered tree: matching regions with their ancestors expanded down to them.
   * A matching region keeps all its children (collapsed, so they can be opened);
   * branches containing further matches are expanded.
   */
  const renderFiltered = (q) => {
    const hasMatch = new Map(); // node -> subtree contains a match
    const flag = (n) => {
      let any = matches(n, q);
      for (const c of n.children) any = flag(c) || any;
      hasMatch.set(n, any);
      return any;
    };
    roots.forEach(flag);
    let count = 0;
    const render = (n) => {
      const self = matches(n, q);
      if (self) count++;
      const kids = n.children.filter((c) => hasMatch.get(c));
      if (!self) {
        // ancestor of a match: show only the branches leading to matches, expanded
        return `<li><details open><summary>${label(n)}</summary><ul>${kids.map(render).join("")}</ul></details></li>`;
      }
      if (!n.children.length) return `<li class="leaf hit">${label(n, q)}</li>`;
      const children = n.children.map((c) => (hasMatch.get(c) ? render(c) : renderNode(c, 1))).join("");
      return `<li class="hit"><details ${kids.length ? "open" : ""}><summary>${label(n, q)}</summary><ul>${children}</ul></details></li>`;
    };
    const html = roots.filter((r) => hasMatch.get(r)).map(render).join("");
    return { html: html ? `<ul>${html}</ul>` : "", count };
  };

  input.addEventListener(
    "input",
    debounce(() => {
      const q = input.value.trim().toLowerCase();
      const { html, count } = q ? renderFiltered(q) : { html: full, count: 0 };
      box.innerHTML = html || `<p class="muted">No matching regions.</p>`;
      status.textContent = count ? `${count} matching region${count === 1 ? "" : "s"}` : "";
    }),
  );
}

// ---------------------------------------------------------------------------
// download jobs
// ---------------------------------------------------------------------------
let jobCount = 0;

/**
 * Run a download with a progress entry in the downloads panel. The save
 * dialog is opened here, synchronously within the click that started it;
 * `run(onProgress, signal, sinkPromise)` writes the file.
 */
function startJob(name, sinkOptions, run) {
  const sinkPromise = openSink(name, sinkOptions);
  const id = ++jobCount;
  const ctrl = new AbortController();
  jobsEl.hidden = false;
  if (!jobsEl.querySelector("h3")) {
    jobsEl.append(h(`<h3>Downloads <button class="link-button" type="button">Hide</button></h3>`));
    jobsEl.querySelector("h3 button").addEventListener("click", () => {
      jobsEl.hidden = true;
      jobsEl.querySelectorAll(".job.done, .job.error").forEach((j) => j.remove());
    });
  }
  const el = h(`<div class="job" id="job-${id}">
      <div class="name">${esc(name)}</div>
      <progress max="1" value="0"></progress>
      <div class="status"><span class="msg">Waiting for save location…</span><button class="link-button" type="button">Cancel</button></div>
    </div>`);
  jobsEl.append(el);
  const msg = el.querySelector(".msg");
  const bar = el.querySelector("progress");
  const cancel = el.querySelector("button");
  cancel.addEventListener("click", () => ctrl.abort());
  const t0 = performance.now();
  const onProgress = (done, total, unit) => {
    bar.max = total || 1;
    bar.value = done;
    const pct = total ? Math.round((100 * done) / total) : 0;
    const elapsed = (performance.now() - t0) / 1000;
    const label = unit === "files" ? `${done}/${total} files` : `${formatBytes(done)} / ${formatBytes(total)}`;
    const eta = done && total && elapsed > 2 ? ` · ~${Math.max(1, Math.round((elapsed * (total - done)) / done))} s left` : "";
    msg.textContent = `${pct}% · ${label}${eta}`;
  };
  (async () => {
    try {
      await sinkPromise; // wait for the save dialog
      msg.textContent = "Starting…";
      await run(onProgress, ctrl.signal, sinkPromise);
      el.classList.add("done");
      bar.value = bar.max;
      msg.textContent = `Done in ${Math.round((performance.now() - t0) / 100) / 10} s`;
      cancel.remove();
    } catch (e) {
      if (e?.name === "AbortError") {
        el.remove();
        if (!jobsEl.querySelector(".job")) jobsEl.hidden = true;
        return;
      }
      console.error(e);
      el.classList.add("error");
      msg.textContent = `Failed: ${e?.message || e}`;
      cancel.remove();
    }
  })();
}

window.addEventListener("beforeunload", (e) => {
  if (jobsEl.querySelector(".job:not(.done):not(.error)")) {
    e.preventDefault();
  }
});

// ---------------------------------------------------------------------------
// boot
// ---------------------------------------------------------------------------
async function boot() {
  setupThemeToggle();
  try {
    const r = await fetch("data/index.json");
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    INDEX = await r.json();
  } catch (e) {
    app.innerHTML = `<p class="muted">Could not load the atlas index (data/index.json): ${esc(e.message)}.<br>
      Run <code>python scripts/build_index.py</code> to generate it.</p>`;
    return;
  }
  // Search and the resolution list cover the latest version of every atlas;
  // older versions are reached from the version dropdown on its page.
  const all = INDEX.atlases;
  INDEX.atlases = all.filter((a) => a.latest !== false);
  for (const a of all) {
    if (!VERSIONS.has(a.key)) VERSIONS.set(a.key, []);
    VERSIONS.get(a.key).push(a);
  }
  for (const v of VERSIONS.values()) v.sort((x, y) => compareVersions(y.version, x.version));
  for (const [key, v] of VERSIONS) {
    const times = v.map((a) => a.uploaded).filter(Boolean).sort();
    if (times.length) ADDED.set(key, times[0]);
  }
  FIRST_UPLOAD_DAY = [...ADDED.values()].sort()[0]?.slice(0, 10) || "";
  for (const a of INDEX.atlases) {
    BY_KEY.set(a.key, a);
    if (!BY_NAME.has(a.name)) BY_NAME.set(a.name, { name: a.name, family: familyOf(a), keys: [] });
    BY_NAME.get(a.name).keys.push(a);
  }
  for (const p of BY_NAME.values()) p.keys.sort((x, y) => minResolution(x) - minResolution(y) || compareAtlases(x, y));
  DOCS = buildSearchIndex(INDEX);
  buildResolutionStops();
  const params = new URL(location.href).searchParams;
  state.q = params.get("q") || "";
  const dateEl = document.getElementById("index-date");
  if (INDEX.generated) dateEl.textContent = `Index built ${INDEX.generated.slice(0, 10)}.`;
  route();
}

boot();
