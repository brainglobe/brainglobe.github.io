// Client-side search over the atlas index.
//
// Query syntax
//   free text            every word must match some field (AND), ranked by field weight
//   "quoted phrase"      exact phrase
//   species:mus          field filters: key, name, species, group, region, citation, orientation
//   res:25  res:<=25  res:10-50   resolution in µm (finest axis)
//   sym:yes / sym:no     symmetric atlases
//   region:CA1           atlases whose terminology contains a matching region

const FIELD_WEIGHTS = {
  key: 10,
  title: 8,
  name: 6,
  species: 6,
  group: 4,
  aliases: 4,
  coordinate_space: 3,
  components: 2,
  description: 1.5,
  citation: 1.5,
  links: 1,
  orientation: 0.5,
};

// Common names so "mouse", "zebrafish" etc. match the latin species name.
const SPECIES_ALIASES = {
  "mus musculus": "mouse",
  "rattus norvegicus": "rat",
  "danio rerio": "zebrafish fish",
  "homo sapiens": "human primate",
  "microtus ochrogaster": "prairie vole rodent",
  "felis catus": "cat",
  "ambystoma mexicanum": "axolotl amphibian salamander",
  "astyanax mexicanus": "mexican cavefish fish",
  "microcebus murinus": "mouse lemur primate",
  "sepia bandensis": "cuttlefish cephalopod",
  "bombus impatiens": "bumblebee bee insect",
  "drosophila melanogaster": "fruit fly insect",
  "ctenophorus decresii": "tawny dragon lizard reptile",
  "sylvia atricapilla": "eurasian blackcap bird",
  "heterocephalus glaber": "naked mole-rat mole rat rodent",
  "fukomys anselli": "mole-rat mole rat rodent",
  "danionella cerebrum": "danionella fish",
};

// Display names for the species filter.
const COMMON_NAMES = {
  "mus musculus": "Mouse",
  "rattus norvegicus": "Rat",
  "danio rerio": "Zebrafish",
  "homo sapiens": "Human",
  "macaca mulatta": "Rhesus macaque",
  "microtus ochrogaster": "Prairie vole",
  "felis catus": "Cat",
  "ambystoma mexicanum": "Axolotl",
  "astyanax mexicanus": "Mexican cavefish",
  "microcebus murinus": "Grey mouse lemur",
  "sepia bandensis": "Dwarf cuttlefish",
  "bombus impatiens": "Common eastern bumblebee",
  "drosophila melanogaster": "Fruit fly",
  "ctenophorus decresii": "Tawny dragon",
  "sylvia atricapilla": "Eurasian blackcap",
  "heterocephalus glaber": "Naked mole-rat",
  "fukomys anselli": "Ansell's mole-rat",
  "danionella cerebrum": "Danionella",
};

export function commonName(species = "") {
  return COMMON_NAMES[species.toLowerCase()] || "";
}

// Imaging-modality and common-term synonyms; any alternative may match.
const SYNONYMS = {
  lightsheet: ["light-sheet", "light sheet", "lsfm"],
  "light-sheet": ["lightsheet", "light sheet", "lsfm"],
  lsfm: ["light-sheet", "lightsheet", "light sheet"],
  stpt: ["two-photon", "serial two-photon", "serial section two-photon"],
  "two-photon": ["stpt"],
  mri: ["magnetic resonance", "mr "],
  developmental: ["development", "developing", "embryo", "postnatal"],
  development: ["developmental", "developing"],
  developing: ["developmental", "development"],
  embryonic: ["embryo", "e11", "e13", "e15", "e18"],
  primate: ["macaque", "monkey", "lemur", "human"],
  monkey: ["macaque", "primate"],
  fish: ["zebrafish", "cavefish", "danionella"],
  fly: ["drosophila"],
  drosophila: ["fly"],
};

const WORD_BOUNDARY = /[\s_\-(,./:;"'[\]]/;

/**
 * Score how well `t` occurs in `text`: 1 for a word-start match, 0.5 for an
 * infix match (only for terms of 4+ characters, so "rat" doesn't match
 * "integrated"), 0 otherwise.
 */
export function termMatch(text, t) {
  let idx = text.indexOf(t);
  let best = 0;
  while (idx >= 0) {
    if (idx === 0 || WORD_BOUNDARY.test(text[idx - 1])) return 1;
    if (t.length >= 4) best = 0.5;
    idx = text.indexOf(t, idx + 1);
  }
  return best;
}

function alternatives(t) {
  return [t, ...(SYNONYMS[t] || [])];
}

export function speciesAlias(species = "") {
  return SPECIES_ALIASES[species.toLowerCase()] || "";
}

export function minResolution(a) {
  return a.resolution?.length ? Math.min(...a.resolution) : Infinity;
}

export function formatResolution(a) {
  const r = a.resolution || [];
  if (!r.length) return "?";
  const fmt = (x) => (Number.isInteger(x) ? String(x) : String(Number(x.toFixed(3))));
  return r.every((x) => x === r[0]) ? `${fmt(r[0])} µm` : `${r.map(fmt).join(" × ")} µm`;
}

/** Precompute lowercase search fields for every atlas. */
export function buildSearchIndex(index) {
  return index.atlases.map((a) => {
    const d = a.docs || {};
    const term = index.terminologies[a.terminology.location];
    const fields = {
      key: a.key.toLowerCase(),
      title: (d.title || "").toLowerCase(),
      name: (a.name || "").toLowerCase(),
      species: (a.species || "").toLowerCase(),
      aliases: speciesAlias(a.species),
      group: (d.group || "").toLowerCase(),
      coordinate_space: (a.coordinate_space || "").toLowerCase(),
      components: [a.template.name, a.annotation_set.name, a.terminology.name].join(" ").toLowerCase(),
      description: (d.description || "").toLowerCase(),
      citation: (a.citation || "").toLowerCase(),
      links: [a.atlas_link, d.link, ...(a.additional_references || [])].join(" ").toLowerCase(),
      orientation: (a.orientation || "").toLowerCase(),
    };
    return {
      atlas: a,
      fields,
      regions: term?.regions || [],
      regionsLower: (term?.regions || []).map((r) => r.toLowerCase()),
      res: minResolution(a),
    };
  });
}

/** Split a query into terms and field filters. */
export function parseQuery(q) {
  const terms = [];
  const filters = [];
  const re = /(\w+):(?:"([^"]*)"|(\S+))|"([^"]*)"|(\S+)/g;
  let m;
  while ((m = re.exec(q || ""))) {
    if (m[1]) filters.push({ field: m[1].toLowerCase(), value: (m[2] ?? m[3]).toLowerCase() });
    else if (m[4] != null) m[4].trim() && terms.push(m[4].toLowerCase());
    else terms.push(m[5].toLowerCase());
  }
  return { terms, filters };
}

function resMatches(value, res) {
  let m;
  if ((m = /^(<=|>=|<|>)?(\d+(?:\.\d+)?)$/.exec(value))) {
    const v = parseFloat(m[2]);
    switch (m[1]) {
      case "<=": return res <= v + 1e-9;
      case ">=": return res >= v - 1e-9;
      case "<": return res < v;
      case ">": return res > v;
      default: return Math.abs(res - v) < 1e-6;
    }
  }
  if ((m = /^(\d+(?:\.\d+)?)-(\d+(?:\.\d+)?)$/.exec(value))) {
    return res >= parseFloat(m[1]) - 1e-9 && res <= parseFloat(m[2]) + 1e-9;
  }
  return true;
}

function regionHits(doc, needle, max = 5) {
  const hits = [];
  for (let i = 0; i < doc.regionsLower.length; i++) {
    if (termMatch(doc.regionsLower[i], needle)) {
      hits.push(doc.regions[i]);
      if (hits.length >= max) break;
    }
  }
  return hits;
}

function countRegionHits(doc, needle) {
  let n = 0;
  for (const r of doc.regionsLower) if (termMatch(r, needle)) n++;
  return n;
}

/** Exact acronym match is a strong signal, e.g. "CA1", "VISp". */
function acronymExact(doc, needle) {
  for (const r of doc.regionsLower) {
    if (r.slice(0, r.indexOf("\t")) === needle) return true;
  }
  return false;
}

/**
 * Run a query. Returns [{atlas, score, regionMatches: string[]}] sorted by score.
 * `facets` restricts results: {species:Set, resMin, resMax}
 */
export function search(docs, query, facets = {}) {
  const { terms, filters } = parseQuery(query);
  const results = [];
  outer: for (const doc of docs) {
    const a = doc.atlas;
    // facet filters
    if (facets.species?.size && !facets.species.has(a.species)) continue;
    if (facets.resMin != null && doc.res < facets.resMin) continue;
    if (facets.resMax != null && doc.res > facets.resMax) continue;

    let score = 0;
    const regionMatches = [];
    for (const f of filters) {
      const v = f.value;
      switch (f.field) {
        case "res":
        case "resolution":
          if (!resMatches(v, doc.res)) continue outer;
          break;
        case "sym":
        case "symmetric": {
          const want = ["yes", "true", "1", "y"].includes(v);
          if (Boolean(a.symmetric) !== want) continue outer;
          break;
        }
        case "region":
        case "structure": {
          const hits = regionHits(doc, v);
          if (!hits.length) continue outer;
          regionMatches.push(...hits);
          score += 2;
          break;
        }
        case "species":
          if (!doc.fields.species.includes(v) && !doc.fields.aliases.includes(v)) continue outer;
          break;
        default: {
          const field = doc.fields[f.field];
          if (field == null || !field.includes(v)) continue outer;
        }
      }
    }
    for (const t of terms) {
      let s = 0;
      for (const [name, w] of Object.entries(FIELD_WEIGHTS)) {
        const text = doc.fields[name];
        if (!text) continue;
        let m = 0;
        for (const alt of alternatives(t)) m = Math.max(m, termMatch(text, alt) * (alt === t ? 1 : 0.8));
        if (!m) continue;
        s += w * m * (text === t ? 2 : 1);
      }
      if (s === 0) {
        // fall back to brain-region names / acronyms
        const exact = acronymExact(doc, t);
        const n = exact ? 1 : countRegionHits(doc, t);
        if (!n) continue outer;
        s = exact ? 3 : 1 + Math.min(1, n / 20);
        regionMatches.push(...regionHits(doc, t, 3));
      }
      score += s;
    }
    results.push({ atlas: a, score, regionMatches: [...new Set(regionMatches)] });
  }
  if (terms.length || filters.length) {
    results.sort((x, y) => y.score - x.score || compareAtlases(x.atlas, y.atlas));
  } else {
    results.sort((x, y) => compareAtlases(x.atlas, y.atlas));
  }
  return results;
}

const GROUP_ORDER = ["Mouse", "Rat", "Other rodent", "Fish", "Lizard", "Amphibian", "Human and non-human primate", "Other mammal", "Bird", "Invertebrate"];

export function compareAtlases(a, b) {
  const ga = GROUP_ORDER.indexOf(a.docs?.group ?? "");
  const gb = GROUP_ORDER.indexOf(b.docs?.group ?? "");
  const oa = ga < 0 ? 99 : ga;
  const ob = gb < 0 ? 99 : gb;
  if (oa !== ob) return oa - ob;
  const ta = a.docs?.title || a.name || "";
  const tb = b.docs?.title || b.name || "";
  if (ta !== tb) return ta.localeCompare(tb);
  return minResolution(a) - minResolution(b) || a.key.localeCompare(b.key, undefined, { numeric: true });
}

/** Count values for facet UI given the current result set. */
export function facetCounts(results) {
  const species = new Map();
  for (const { atlas: a } of results) species.set(a.species, (species.get(a.species) || 0) + 1);
  return { species };
}
