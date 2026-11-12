# GEN_HEP — Standard Model Epistemic Graph

Particle physics as a state / model / observable concept graph that grows step by step, from one-particle quantum mechanics (1925) to the electroweak Standard Model with its Higgs sector (2012), clustered at the end into the terms of the Standard-Model Lagrangian.

- **Live page:** https://tahmeedhossain.github.io/GEN_HEP/ (landing page with all versions; `latest/` opens the newest)
- **Paper:** [paper/main.pdf](paper/main.pdf) — the graph, a pedagogical walk through the history, ten rules of evolution read off the graph, the clustered final graph, and a reader's guide with annotated screenshots
- **Data:** [data/v1.1_sm_epistemic_graph.json](data/v1.1_sm_epistemic_graph.json), [data/statistics.json](data/statistics.json), [catalog.md](catalog.md)

Part of the **Great Epistemic Network** (GEN) project, whose aims are to generate research ideas automatically (an edge the literature should contain but the graph lacks is a research target), to make reviewing a field easy (a field becomes a graph one can step through), and to see a field through its review (the graph is drawn, not only listed).

## The graph in one paragraph

Three layers. **States**: what the theory says can exist — the one-particle Hilbert space, then Wigner's irreducible representations, then one Fock sector per field with its occupation ladder |0⟩…|N⟩. **Models**: framework nodes (unitary evolution, observable postulate, field construction) and interaction nodes, i.e. Lagrangian terms, marked effective (dimensionful coupling), fundamental, or candidate. **Observables**: spectra, then widths, cross sections, masses and couplings, each badged A (observed before explained), P (predicted before observed) or F (calibration). Interaction nodes are entered by **AND routes** from the occupation-number nodes of several sectors (e.g. n(1)∧p(1)∧e(1)∧ν̄(1) into Fermi's term); edges to observables leave only from model nodes; back-edges from the evolution and the field node partition and build the state layer. An observable with no model edge (red dashed ring) is the to-do item that drives the next model node.

## Steps

| # | Step | Years |
|---|---|---|
| 1 | One-particle quantum mechanics | 1925–1932 |
| 2 | Poincaré symmetry: Wigner's classification (state layer partitioned into UIRs) | 1926–1939 |
| 3 | An observable with no model edge: particle creation and destruction | 1914–1934 |
| 4 | Model response: quantum fields on Fock space (UIRs become sectors with ladders) | 1927–1940 |
| 5 | First interaction node: the QED vertex, route e(1)∧γ(1) | 1927–1949 |
| 6 | Second interaction node: Fermi's contact term (effective) | 1934 |
| 7 | Universality: the muon and a second contact node; ν splits into ν_e, ν_μ | 1937–1962 |
| 8 | Parity violation: the two contact nodes merge into V−A | 1956–1958 |
| 9 | Fundamental nodes: W, Z and SU(2)_L×U(1)_Y; (n,p) → (u,d) | 1954–1983 |
| 10 | Mass: the Higgs sector | 1964–2012 |
| 11 | Frontier: neutrino oscillation, an unexplained observable again | 1998– |
| 12 | Final form: the Standard Model as clusters of its Lagrangian terms | (view) |
| 13 | Synthesis: counts per step and the epistemic pattern | |

Scope: QED and the electroweak sector (ν_e, e, ν_μ, μ, u, d, γ, W±, Z⁰, H). The strong sector is left for a later version.

## Versions

Every version is kept at its own address.

| Version | Folder | What changed |
|---|---|---|
| v1.1 (latest) | `v1.1/` (= `latest/`) | Adds Step 12, the clustered final view (effective nodes absorbed inside the SM Lagrangian terms, lineage arrows); fixes the synthesis charts |
| v1.0 | `v1.0/` | First release: 11 graph steps + synthesis |

`versions.json` is the manifest. The GitHub Pages site is published from the `gh-pages` branch, which the workflow in `.github/workflows/publish-pages.yml` copies from `main` on every push.

## Repository layout

```
index.html            landing page (versions, how to read, aims, paper/data links)
v1.0/ v1.1/ latest/   the interactive pages (self-contained HTML; data embedded)
data/                 graph JSON per version, statistics.json
catalog.md            nodes, edges and routes of every step (generated)
paper/                main.tex + sections, figures/, generated tables, main.pdf (XeLaTeX)
tools/build_derived.py  regenerates statistics.json, catalog.md and the paper tables from the JSON
assets/               images used by the landing page
```

## Regenerating

```
python3 tools/build_derived.py            # statistics, catalogue, paper tables (latest version)
cd paper && latexmk -xelatex main.tex     # paper (needs the FreeSerif/FreeSans/DejaVu Sans Mono fonts)
```

## Extending the graph

Add a node to the `NODES` dictionary of the page (or the JSON), list it in a step's `S`, `M` or `O`, add the edges (with their mathematical relation) and the AND routes (with their legs), run the build script, and keep the previous page in its version folder. The GEN rule for edges applies: a relation the literature establishes must be an edge, so two nodes stay unconnected only when no edge can be made from the literature.

## Disclosure

Graph data, pages, scripts and paper were generated with an AI assistant (Claude, Anthropic) under the author's direction, who specified the layers, the edge conventions, the historical order, the clustering rule and the scope, and reviewed the output. Citations were written from the assistant's knowledge and should be verified against the sources before formal use; two are flagged in the data (`[verify page numbers]`). Open to community review, modification and addition.

## Citation

See `CITATION.cff`.
