# Reading the rules of evolution off the twelve step graphs

A note accompanying the Standard Model Epistemic Graph (GEN_HEP). The synthesis view of the page (Step 13) re-draws the whole graph at every step; this note reads the ten rules of evolution (paper, Section 4) off those twelve pictures. Counts are those of `data/statistics.json`. The page itself is unchanged; this is text only. Rich markup: <sup>sup</sup>, <sub>sub</sub>.

| Step | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 One-particle quantum mechanics |  |  |  |  |  |  |  |  |  |  |
| 2 Wigner's classification | ● |  |  |  |  |  |  | ● |  |  |
| 3 The particle-production anomaly |  | ○ |  |  |  |  |  |  |  |  |
| 4 Fields on Fock space |  | ● | ● |  |  |  |  |  |  |  |
| 5 The QED vertex |  | ● |  | ● |  |  |  |  | ● |  |
| 6 Fermi's contact term |  | ● |  | ● | ● |  |  |  | ● |  |
| 7 The muon and universality |  |  |  | ● | ● | ○ |  | ● | ● |  |
| 8 Parity violation and V−A |  | ● |  | ● |  | ● |  |  | ● |  |
| 9 W, Z and the gauge theory |  | ● |  | ● |  |  | ● | ● | ● |  |
| 10 The Higgs sector |  | ● |  | ● |  |  |  |  | ● |  |
| 11 The neutrino-mass frontier |  | ○ |  | ● |  |  |  | ○ |  |  |
| 12 The Standard Model as clusters |  |  |  | ● |  |  |  |  | ● | ● |

● the rule fires; ○ prepared or announced but not executed. R1 symmetry partition; R2 in-degree-zero drive; R3 Fock extension; R4 route composition; R5 effective status; R6 universality merge; R7 absorption; R8 sector refinement; R9 calibration; R10 clustering.

## Step 1: One-particle quantum mechanics

**The graph.** The schematic shows 1 state node, 3 model nodes and 5 observable chips joined by 9 edges: two state→model edges, the dashed back-edge of U(t) into the state column, one model→model edge (the Lagrangian generates the evolution), one solid prediction edge (Lagrangian → energy levels) and four dotted framework assignments (postulate → x̂, p̂, L̂, Ŝ). There are no routes. Two chips carry the badge A (energy levels, spin): they were measured before the model nodes existed.

**The rules in it.** No rule fires: this is the initial condition. What the picture fixes is the grammar the rules act on. The only arrow that points into the state column is a back-edge from the model column, which is the content of Rule 8 before any change has happened; the only solid edge to the observable column leaves the Lagrangian node, which is the content of Rule 9 before any parameter has been calibrated; and the absence of junctions shows that Rule 4 has nothing to act on, because no interaction term exists.

## Step 2: Wigner's classification

**The graph.** The one state node has become 9 representation classes, all marked +, two of them dashed (continuous spin, tachyonic: no instance). Two model nodes carry the rewrite mark ~ (U(t) → U(Λ, a); L → Klein–Gordon/Dirac) and the dashed back-edge now leaves the rewritten U(Λ, a) node. Two new chips with badge P (mass, spin) receive solid edges from U(Λ, a). Counts: 3 model nodes, 6 observables, 10 edges, no route, no red ring.

**The rules in it.** Rule 1 is the whole picture: a symmetry represented on the state layer partitions it, and the labels of the pieces become observables. The partition is drawn as the fan of nine boxes below one rewritten model node; the Casimir labels are the two new P chips. Rule 8 is visible negatively: no arrow runs from one state box to another, so the change came from the model column, as the rule requires.

## Step 3: The particle-production anomaly

**The graph.** The graph is that of Step 2 with one addition: a chip with a red dashed ring (particle production and decay) and no incoming arrow. Counts: 9 state nodes, 3 model nodes, 6 observables, 9 edges, 1 unexplained chip. The cycle shows only observe and deficit.

**The rules in it.** Rule 2 is announced, not yet executed: the red ring is the precondition, an observable with in-degree zero from the model layer. This is the only step in which the graph grows by an observable alone; neither the model nor the state column changes, which is why the counts of those two columns are those of Step 2.

## Step 4: Fields on Fock space

**The graph.** The nine classes have slid into 5 sectors (the four classes without an instance and the vacuum move into the sector that replaces them), and every sector box now shows four ladder dots. A new model node (+, the field) stands where the one-particle Lagrangian stood, which has merged into it; the observable postulate is rewritten (~) as the S-matrix. A second dashed back-edge leaves the field node. The observable column has 4 chips, two of them (Γ, σ) with red rings. Routes: 0; edges: 9.

**The rules in it.** Rule 2 fires: a model node is added against the deficit of Step 3. Rule 3 is drawn twice, as the new back-edge and as the ladder dots that appear in every state box; its minimality clause is visible as the fact that the five boxes are exactly the Step-2 classes that have an instance, with nothing added. The two red rings show the limit of the free field: the deficit has moved from one chip (production in general) to two (which processes, at what rate), and the schematic says so by giving the new node no edge into the observable column.

## Step 5: The QED vertex

**The graph.** The first junction appears: two blue legs, from the e<sup>−</sup> and γ boxes, meet at ∧ and enter a new solid (fundamental) model node. The observable column has 6 chips: four new ones with solid edges from the vertex (Compton, pair production, a<sub>e</sub>, Lamb shift), one with a dashed calibration edge (α), and the β-decay chip, still ringed. Counts: 4 model nodes, 1 route, 10 edges, 1 unexplained chip.

**The rules in it.** Rule 4 appears with the junction: the legs are the two fields of the term, and the route is drawn from the minimal occupation numbers e(1)∧γ(1). Rule 9 is visible as the one dashed edge against four solid ones: one parameter, four predictions. Rule 2 is visible as the ring that remains on β decay, the next to-do item of the model column. The badges show three A and one P: pair production is the first prediction-before-observation in the graph.

## Step 6: Fermi's contact term

**The graph.** A dashed model node (+) stands under the QED vertex, entered by a second junction with four legs (n, p, e, ν). Two new chips (τ<sub>n</sub> with P, G<sub>F</sub> with a dashed calibration edge); the ring on β decay is gone because its edge now comes from the new node. Counts: 5 model nodes (1 effective, 1 fundamental), 2 routes, 11 edges, no unexplained chip.

**The rules in it.** Rule 2 closes the deficit of Step 5. Rule 4 shows a route with four legs, one per field of the four-fermion term. Rule 5 is the dashed outline itself: the coupling G<sub>F</sub> has mass dimension −2, so the node is drawn as temporary from the moment it is added. Rule 9 adds one more dashed edge. The count of unexplained chips returns to zero for the first time since Step 2.

## Step 7: The muon and universality

**The graph.** The state column grows from 5 to 7: a μ box (+) and two neutrino boxes where there was one (ν<sub>e</sub> keeps the old node, ν<sub>μ</sub> is new). A second dashed model node (+) with its own four-leg junction. The observable column grows to 9 chips (τ<sub>μ</sub> with A; Michel ρ and ν<sub>μ</sub> ≠ ν<sub>e</sub> with P); the dashed calibration edge to G<sub>F</sub> now leaves the muon node. Counts: 6 model nodes (2 effective), 3 routes, 14 edges.

**The rules in it.** Rule 8 fires in its split form: two ν boxes where there was one, caused by an observable (ν beams produce muons, not electrons), not by anything inside the state column. Rule 6 is prepared: two dashed nodes both send a dashed edge toward the same G<sub>F</sub> chip, which is the picture of two nodes sharing one calibration; the operation log marks it as a signal. Rule 5 holds for both dashed nodes; this is the step at which the count of effective nodes peaks at 2.

## Step 8: Parity violation and V−A

**The graph.** The two dashed nodes slide into one (V−A, still dashed), which now has three junctions on its left (β decay, μ decay, μ capture) and a fan of edges on its right. Two new chips (parity asymmetries, ν helicity, both P). Counts: 5 model nodes (1 effective), 11 observables, 4 routes, 16 edges, no red ring.

**The rules in it.** Rule 6 is the merge animation and its result: one node entered by the union of the routes, with one coupling. Rule 2 fires in the same step: the two new chips would be ringed under the parity-even nodes of Step 7, and the merged node reaches them (the log shows FLAG followed by MERGE). Rule 4 counts the routes as unified processes: three. The model column shrinks (6 → 5) while the observable column grows (9 → 11): the first reduction in the graph, and the first increase of predictive content without a new node.

## Step 9: W, Z and the gauge theory

**The graph.** The state column grows to 9: W<sup>±</sup> and Z<sup>0</sup> appear (+), and the n and p boxes slide into u and d. The dashed V−A node slides into a solid charged-current node; two more solid nodes appear (neutral current, self-couplings); the QED node is rewritten (~). Routes go from 4 to 7: three charged-current routes with a W leg each, one neutral-current route whose leg is a bracket over all fermion boxes, two self-coupling routes, one electromagnetic route with a bracket over the charged boxes. The observable column has 12 chips, five of them new and all five with badge P. Counts: 7 model nodes (4 fundamental, 0 effective), 17 edges.

**The rules in it.** Rule 7 is visible three times: the dashed node sliding into a solid one (absorption), the W leg added to each former four-leg route (the mediator sector enters every route), and the two solid nodes that no red ring asked for (the symmetry forces them) with their P-badged chips. Rule 8 fires in its replace form (u, d for n, p). Rule 2 fires in its theory-internal form: the model column changed without a red ring, because the dashed node could not be fundamental. Rule 9 adds sin<sup>2</sup>θ<sub>W</sub>. The count of effective nodes drops to zero and stays there; the count of fundamental nodes jumps from 1 to 4.

## Step 10: The Higgs sector

**The graph.** An H box (+) completes the state column at 10. Three solid model nodes appear with four new junctions: H with W, H with Z, H with the bracket of massive fermions, and H alone (the self-coupling route H(3), the first with a single leg). The observable column has 13 chips: m<sub>H</sub>, the Higgs rates, the fermion masses (dashed calibration edge) and λ<sub>HHH</sub> with a blue dashed ring (predicted, untested). The M<sub>W</sub> and M<sub>Z</sub> chips now receive their edges from the Higgs–gauge node. Counts: 10 model nodes (7 fundamental), 8 routes, 19 edges.

**The rules in it.** Rule 2 fires in its theory-internal form again: there is no red ring, the symmetry forbids explicit mass terms. Rule 4 shows a route with one leg, a self-interaction. Rule 9 is visible as two dashed edges (m<sub>f</sub>, m<sub>H</sub>) and as a reassignment: M<sub>W</sub> is now predicted by a different node than in Step 9, which is a prediction being re-derived rather than a new one. The blue ring is a prediction waiting for its observable.

## Step 11: The neutrino-mass frontier

**The graph.** One new chip with a red ring (flavour oscillation) and one dotted model node with a dotted route (the ν bracket with H) and a dotted edge. Nothing else changes. Counts: 10 state nodes, 11 model nodes, 12 observables, 9 routes, 1 unexplained chip.

**The rules in it.** Rule 2 is announced for the third time (the cycle shows observe, deficit, hypothesize), and this time the hypothesis is dotted: the literature offers two repairs and the data select neither. Rule 8 is due but not executed: the ν boxes would have to change (a right-handed state or a Majorana term), and the graph leaves them as they are. The ring is the current research target in the GEN sense.

## Step 12: The Standard Model as clusters

**The graph.** The model column is reorganized into 6 outlined clusters; the three absorbed nodes sit, greyed and dashed, inside the first cluster with lineage arrows between them and into the charged-current node. Routes are re-attached to the clusters: 12 in all (5, 2, 2, 1, 1 and 1 candidate). The observable column has 16 chips; all have an edge except the oscillation chip. Counts: 14 model nodes (7 fundamental, 3 absorbed, 1 candidate), 22 edges.

**The rules in it.** Rule 10 is the picture: the number of outlined clusters equals the number of terms of the Lagrangian plus one candidate, and every absorbed node sits in the cluster whose member reproduces it. Rule 4 appears cumulatively: the number of routes into a cluster counts the sector combinations the term couples. Rule 9 is readable at a glance as four dashed edges (α, G<sub>F</sub>, m<sub>f</sub>, m<sub>H</sub>) leaving three clusters against twelve solid ones. The lineage arrows are all that remains of Steps 6–8: Rule 7 leaves exactly this trace in the final form.

## Across the sequence

- **State column.** The count runs 1 → 9 → 9 → 5 → 5 → 5 → 7 → 7 → 9 → 10 → 10 → 10. Every change has a cause outside the column: a symmetry (Step 2), a model node's back-edge (Step 4), an observable that distinguishes sectors (Step 7), an absorption with a new mediator (Step 9), and a theory-internal requirement (Step 10). No change is caused by a state node. That is Rule 8 read across the strip.
- **Dashed model nodes.** Effective nodes appear at Step 6, peak at Step 7 (two), merge at Step 8 (one) and vanish at Step 9; at Step 12 they reappear only as greyed chips inside a cluster. The strip shows the rise and fall that Rules 5–7 describe: temporary nodes that proliferate, merge when they share a calibration, and are absorbed by solid nodes.
- **Solid model nodes.** Fundamental nodes go 1 (Step 5) → 4 (Step 9) → 7 (Step 10) and never decrease. Two of the jumps are caused by red rings (Rule 2, anomaly form) and two by the symmetry (Rule 2, theory-internal form). The two forms are distinguishable in the strip: the first follows a ringed chip, the second does not.
- **Red rings.** Rings appear at Steps 3, 4, 5 and 11. The first is closed at Step 4 by being replaced with two, the two are closed at Steps 5 and 6, and the last is still open. Rule 2 is the engine: every closure is a new model node, and the open ring is the place where the next node will appear.
- **Junctions.** Routes are absent until Step 5, then grow by one per interaction node (Steps 5, 6, 7), by one at the merge (Step 8, three processes into one node), by three at the absorption (Step 9, each route gaining a W leg and the symmetry adding two more), by one per Higgs term, and are finally re-attached to clusters (Step 12). Rule 4 is visible as the one-to-one correspondence between legs and the fields of a term.
- **Badges.** A badges dominate Steps 1–8, P badges dominate Steps 9–10, and Step 11 opens with an A. This is the regime flip of the cycle: the first run of the loop is anomaly-first, its second half prediction-first, and the third run begins as the first did.
- **Dashed calibration edges.** One appears per new parameter: α (Step 5), G<sub>F</sub> (Step 6, re-attached at Steps 7, 8, 9), sin<sup>2</sup>θ<sub>W</sub> (Step 9), m<sub>f</sub> and m<sub>H</sub> (Step 10). Rule 9 locates the predictive content of the final graph as the excess of solid over dashed edges leaving the clusters.

The reading is cumulative: no rule needs a later step to be recognized, but each later step narrows what a rule can mean. Rule 2 at Step 4 could be read as "a deficit triggers a model node"; by Step 10 it must be read as "a deficit *or* a theory-internal inconsistency triggers a model node", and by Step 11 as a rule that can be announced without being executed. Rule 8 at Step 2 is a statement about symmetry; by Step 9 it covers four distinct causes. The step graphs are the evidence for the rules, and the only evidence offered.
