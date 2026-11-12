// Atlas search: filters the atlas cards that _ext/atlas_search renders on the
// search page (atlases/index), and the brain-region tree on each atlas page.
// Everything is already in the HTML; without this script all of it is shown.
(() => {
  const debounce = (fn, ms = 120) => {
    let t;
    return (...a) => {
      clearTimeout(t);
      t = setTimeout(() => fn(...a), ms);
    };
  };
  // Words that should also find their synonyms, e.g. "lightsheet" finds "LSFM".
  const SYNONYMS = {
    lightsheet: ["light-sheet", "light sheet", "lsfm"],
    "light-sheet": ["lightsheet", "light sheet", "lsfm"],
    lsfm: ["light-sheet", "lightsheet", "light sheet"],
    stpt: ["two-photon", "serial two-photon"],
    "two-photon": ["stpt"],
    mri: ["magnetic resonance"],
    developmental: ["development", "developing", "embryo", "postnatal"],
    embryonic: ["embryo", "e11", "e13", "e15", "e18"],
    primate: ["macaque", "monkey", "lemur", "human"],
    fly: ["drosophila"],
  };
  // 1 for a match at the start of a word, 0.5 inside a word (4+ letters, so "rat" misses "integrated").
  const termMatch = (text, t) => {
    let best = 0;
    for (let i = text.indexOf(t); i >= 0; i = text.indexOf(t, i + 1)) {
      if (i === 0 || /[\s_\-(,./:;"'[\]]/.test(text[i - 1])) return 1;
      if (t.length >= 4) best = 0.5;
    }
    return best;
  };

  function setupSearch(root) {
    const input = root.querySelector(".atlas-searchbar input");
    const facets = root.querySelector(".atlas-facets");
    const [resMin, resMax] = [facets.querySelector(".res-min"), facets.querySelector(".res-max")];
    const clear = facets.querySelector(".clear-facets");
    const meta = root.querySelector(".result-meta");
    const none = root.querySelector(".no-results");
    const list = meta.parentElement;
    const cards = [...root.querySelectorAll(".atlas-card")].map((el, i) => ({
      el,
      i,
      text: el.dataset.text,
      title: el.querySelector("h2").textContent.toLowerCase(),
      species: el.dataset.species,
      names: el.dataset.names.split(" "),
      speciesText: `${el.dataset.species} ${el.querySelector(".species").textContent}`.toLowerCase(),
      res: el.dataset.res.split(" ").map(Number),
      sym: el.dataset.sym === "1",
      terms: el.dataset.terms.split(" ").filter(Boolean),
      count: el.querySelectorAll(".keys a").length || 1,
      hits: el.querySelector(".regions-hit"),
    }));
    for (const el of [facets, root.querySelector(".atlas-searchbar"), root.querySelector(".atlas-syntax")]) el.hidden = false;

    let regions = null; // terminology location -> [["acronym\tname", lowercase], ...], loaded on the first query
    let loading = null;
    const loadRegions = () =>
      (loading ??= fetch("regions.json")
        .then((r) => r.json())
        .then((data) => (regions = Object.fromEntries(Object.entries(data).map(([k, v]) => [k, v.map((s) => [s, s.toLowerCase()])]))))
        .catch(() => (regions = {})));
    const regionHits = (card, t, max = 6) => {
      const out = [];
      for (const loc of card.terms)
        for (const [orig, low] of regions?.[loc] || []) {
          const [acr, name] = low.split("\t");
          if ((acr === t || termMatch(name, t) || termMatch(acr, t)) && !out.includes(orig)) out.push(orig);
          if (out.length >= max) return out;
        }
      return out;
    };
    const resOk = (card, test) => card.res.some(test);
    const resFilter = (v) => {
      let m = /^(<=|>=|<|>)?(\d+(?:\.\d+)?)$/.exec(v);
      if (m) {
        const x = +m[2];
        return { "<=": (r) => r <= x, ">=": (r) => r >= x, "<": (r) => r < x, ">": (r) => r > x }[m[1]] || ((r) => Math.abs(r - x) < 1e-6);
      }
      m = /^(\d+(?:\.\d+)?)-(\d+(?:\.\d+)?)$/.exec(v);
      return m ? (r) => r >= +m[1] && r <= +m[2] : () => true;
    };

    /** Score a card for the query (null = no match) and collect matching regions. */
    function score(card, terms, filters) {
      let s = 0;
      const hits = [];
      for (const [field, v] of filters) {
        if (field === "res" || field === "resolution") {
          if (!resOk(card, resFilter(v))) return null;
        } else if (field === "sym" || field === "symmetric") {
          if (card.sym !== ["yes", "true", "1", "y"].includes(v)) return null;
        } else if (field === "region") {
          const h = regionHits(card, v);
          if (!h.length) return null;
          hits.push(...h);
        } else if (field === "species") {
          if (!card.speciesText.includes(v)) return null;
        } else if (!card.text.includes(v)) return null;
      }
      for (const t of terms) {
        const alts = [t, ...(SYNONYMS[t] || [])];
        const m = Math.max(...alts.map((a) => 3 * termMatch(card.title, a) + termMatch(card.text, a)));
        if (m) s += m;
        else {
          const h = regionHits(card, t, 3); // plain words also search brain regions
          if (!h.length) return null;
          hits.push(...h);
          s += 0.5;
        }
      }
      if (terms.length && card.names.some((n) => n === terms.join("_"))) s += 10; // "allen mouse" -> allen_mouse
      return { s, hits: [...new Set(hits)].slice(0, 6) };
    }

    async function update() {
      const q = input.value.trim().toLowerCase();
      const terms = [];
      const filters = [];
      for (const m of q.matchAll(/(\w+):(?:"([^"]*)"|(\S+))|"([^"]*)"|(\S+)/g)) {
        if (m[1]) filters.push([m[1], m[2] ?? m[3]]);
        else if ((m[4] ?? m[5]).trim()) terms.push(m[4] ?? m[5]);
      }
      if (terms.length || filters.some(([f]) => f === "region")) await loadRegions();
      if (q !== input.value.trim().toLowerCase()) return; // a newer query is running

      const species = new Set([...facets.querySelectorAll(".facet-list input:checked")].map((c) => c.value));
      const [lo, hi] = [resMin.value ? +resMin.value : -Infinity, resMax.value ? +resMax.value : Infinity];
      const counts = new Map();
      const shown = [];
      for (const card of cards) {
        const r = resOk(card, (x) => x >= lo - 1e-9 && x <= hi + 1e-9) ? score(card, terms, filters) : null;
        if (r) counts.set(card.species, (counts.get(card.species) || 0) + 1); // species counts ignore the species filter
        card.match = r && (!species.size || species.has(card.species)) ? r : null;
        if (card.match) shown.push(card);
      }
      if (q) shown.sort((a, b) => b.match.s - a.match.s || a.i - b.i);
      for (const card of cards) card.el.hidden = !card.match;
      for (const card of shown) {
        list.insertBefore(card.el, none);
        card.hits.hidden = !card.match.hits.length;
        card.hits.textContent = card.match.hits.length
          ? `Matching regions: ${card.match.hits.map((h) => h.split("\t")).map(([a, n]) => `${n} (${a})`).join(", ")}`
          : "";
      }
      if (!q) for (const card of [...cards].sort((a, b) => a.i - b.i)) list.insertBefore(card.el, none);
      for (const label of facets.querySelectorAll(".facet-item")) {
        const n = counts.get(label.querySelector("input").value) || 0;
        label.querySelector(".count").textContent = n;
        label.classList.toggle("empty", !n);
      }
      const n = shown.reduce((a, c) => a + c.count, 0);
      meta.textContent = `${n} atlas${n === 1 ? "" : "es"} in ${shown.length} collection${shown.length === 1 ? "" : "s"}${q ? "" : ", newest first"}`;
      none.hidden = shown.length > 0;
      clear.hidden = !(species.size || resMin.value || resMax.value);
      const url = new URL(location.href);
      if (q) url.searchParams.set("search", input.value.trim());
      else url.searchParams.delete("search"); // not ?q=, which Sphinx's own search uses
      history.replaceState(null, "", url);
    }

    input.value = new URLSearchParams(location.search).get("search") || "";
    input.addEventListener("input", debounce(update));
    facets.addEventListener("change", update);
    clear.addEventListener("click", () => {
      facets.querySelectorAll(".facet-list input").forEach((c) => (c.checked = false));
      resMin.value = resMax.value = "";
      update();
    });
    update();
  }

  function setupRegionFilter(tree) {
    const box = document.querySelector(".region-filter");
    const input = box.querySelector("input");
    const status = box.querySelector(".region-status");
    const items = [...tree.querySelectorAll("li")].reverse(); // children before parents
    const label = (li) => (li.querySelector(":scope > details > summary") || li).textContent.toLowerCase();
    const initial = new Map([...tree.querySelectorAll("details")].map((d) => [d, d.open]));
    box.hidden = false;
    input.addEventListener(
      "input",
      debounce(() => {
        const q = input.value.trim().toLowerCase();
        let n = 0;
        const visible = new Set();
        for (const li of items) {
          const self = q && label(li).includes(q);
          const below = [...li.querySelectorAll(":scope > details > ul > li")].some((c) => visible.has(c));
          if (!q || self || below) visible.add(li);
          li.hidden = !visible.has(li);
          li.classList.toggle("hit", Boolean(self));
          const d = li.querySelector(":scope > details");
          if (d) d.open = q ? below : initial.get(d);
          if (self) {
            n++;
            li.querySelectorAll("li").forEach((c) => (c.hidden = false)); // a matching region keeps its sub-regions
          }
        }
        status.textContent = q ? `${n} matching region${n === 1 ? "" : "s"}` : "";
      }),
    );
  }

  const search = document.querySelector(".atlas-search");
  if (search) setupSearch(search);
  const tree = document.querySelector(".region-tree");
  if (tree) setupRegionFilter(tree);
})();
