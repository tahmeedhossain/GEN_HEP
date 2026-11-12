#!/usr/bin/env python3
"""Connect the rules of evolution with the twelve step graphs of the synthesis view.

Writes paper/sec_rules_steps.tex, paper/tab_rulematrix.tex and notes/rules-and-step-graphs.md
from the per-step counts in data/statistics.json and the discussion below (hand-written, kept in
one place so that the paper section and the note cannot drift apart).
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
stats = {x['step']: x for x in json.load(open(os.path.join(ROOT, 'data', 'statistics.json')))['per_step']}

RULE_NAMES = {1: 'symmetry partition', 2: 'in-degree-zero drive', 3: 'Fock extension', 4: 'route composition', 5: 'effective status',
              6: 'universality merge', 7: 'absorption', 8: 'sector refinement', 9: 'calibration', 10: 'clustering'}
# which rules fire (●) or are prepared / announced (○) in each step
MATRIX = {1: {}, 2: {1: '●', 8: '●'}, 3: {2: '○'}, 4: {2: '●', 3: '●'}, 5: {2: '●', 4: '●', 9: '●'}, 6: {2: '●', 4: '●', 5: '●', 9: '●'},
          7: {4: '●', 5: '●', 6: '○', 8: '●', 9: '●'}, 8: {2: '●', 4: '●', 6: '●', 9: '●'}, 9: {2: '●', 4: '●', 7: '●', 8: '●', 9: '●'},
          10: {2: '●', 4: '●', 9: '●'}, 11: {2: '○', 4: '●', 8: '○'}, 12: {4: '●', 9: '●', 10: '●'}}

def C(k):
    x = stats[k]
    return dict(S=x['state_nodes'], M=x['model_nodes'], O=x['observable_nodes'], R=x['and_routes'], E=x['edges'], U=len(x['unexplained_observables']),
                eff=x['effective_nodes_active'], fund=x['fundamental_nodes'], absd=x['effective_nodes_absorbed'], cl=x['clusters'])

# Each entry: (title, graph-as-displayed, rules-visible). Rich markup ^{} _{} as on the page.
STEPS = [
(1, 'One-particle quantum mechanics',
 'The schematic shows {S} state node, {M} model nodes and {O} observable chips joined by {E} edges: two state→model edges, the dashed back-edge of U(t) into the state column, one model→model edge (the Lagrangian generates the evolution), one solid prediction edge (Lagrangian → energy levels) and four dotted framework assignments (postulate → x̂, p̂, L̂, Ŝ). There are no routes. Two chips carry the badge A (energy levels, spin): they were measured before the model nodes existed.',
 'No rule fires: this is the initial condition. What the picture fixes is the grammar the rules act on. The only arrow that points into the state column is a back-edge from the model column, which is the content of Rule 8 before any change has happened; the only solid edge to the observable column leaves the Lagrangian node, which is the content of Rule 9 before any parameter has been calibrated; and the absence of junctions shows that Rule 4 has nothing to act on, because no interaction term exists.'),
(2, 'Wigner\'s classification',
 'The one state node has become {S} representation classes, all marked +, two of them dashed (continuous spin, tachyonic: no instance). Two model nodes carry the rewrite mark ~ (U(t) → U(Λ, a); L → Klein–Gordon/Dirac) and the dashed back-edge now leaves the rewritten U(Λ, a) node. Two new chips with badge P (mass, spin) receive solid edges from U(Λ, a). Counts: {M} model nodes, {O} observables, {E} edges, no route, no red ring.',
 'Rule 1 is the whole picture: a symmetry represented on the state layer partitions it, and the labels of the pieces become observables. The partition is drawn as the fan of nine boxes below one rewritten model node; the Casimir labels are the two new P chips. Rule 8 is visible negatively: no arrow runs from one state box to another, so the change came from the model column, as the rule requires.'),
(3, 'The particle-production anomaly',
 'The graph is that of Step 2 with one addition: a chip with a red dashed ring (particle production and decay) and no incoming arrow. Counts: {S} state nodes, {M} model nodes, {O} observables, {E} edges, {U} unexplained chip. The cycle shows only observe and deficit.',
 'Rule 2 is announced, not yet executed: the red ring is the precondition, an observable with in-degree zero from the model layer. This is the only step in which the graph grows by an observable alone; neither the model nor the state column changes, which is why the counts of those two columns are those of Step 2.'),
(4, 'Fields on Fock space',
 'The nine classes have slid into {S} sectors (the four classes without an instance and the vacuum move into the sector that replaces them), and every sector box now shows four ladder dots. A new model node (+, the field) stands where the one-particle Lagrangian stood, which has merged into it; the observable postulate is rewritten (~) as the S-matrix. A second dashed back-edge leaves the field node. The observable column has {O} chips, two of them (Γ, σ) with red rings. Routes: {R}; edges: {E}.',
 'Rule 2 fires: a model node is added against the deficit of Step 3. Rule 3 is drawn twice, as the new back-edge and as the ladder dots that appear in every state box; its minimality clause is visible as the fact that the five boxes are exactly the Step-2 classes that have an instance, with nothing added. The two red rings show the limit of the free field: the deficit has moved from one chip (production in general) to two (which processes, at what rate), and the schematic says so by giving the new node no edge into the observable column.'),
(5, 'The QED vertex',
 'The first junction appears: two blue legs, from the e^{−} and γ boxes, meet at ∧ and enter a new solid (fundamental) model node. The observable column has {O} chips: four new ones with solid edges from the vertex (Compton, pair production, a_{e}, Lamb shift), one with a dashed calibration edge (α), and the β-decay chip, still ringed. Counts: {M} model nodes, {R} route, {E} edges, {U} unexplained chip.',
 'Rule 4 appears with the junction: the legs are the two fields of the term, and the route is drawn from the minimal occupation numbers e(1)∧γ(1). Rule 9 is visible as the one dashed edge against four solid ones: one parameter, four predictions. Rule 2 is visible as the ring that remains on β decay, the next to-do item of the model column. The badges show three A and one P: pair production is the first prediction-before-observation in the graph.'),
(6, 'Fermi\'s contact term',
 'A dashed model node (+) stands under the QED vertex, entered by a second junction with four legs (n, p, e, ν). Two new chips (τ_{n} with P, G_{F} with a dashed calibration edge); the ring on β decay is gone because its edge now comes from the new node. Counts: {M} model nodes ({eff} effective, {fund} fundamental), {R} routes, {E} edges, no unexplained chip.',
 'Rule 2 closes the deficit of Step 5. Rule 4 shows a route with four legs, one per field of the four-fermion term. Rule 5 is the dashed outline itself: the coupling G_{F} has mass dimension −2, so the node is drawn as temporary from the moment it is added. Rule 9 adds one more dashed edge. The count of unexplained chips returns to zero for the first time since Step 2.'),
(7, 'The muon and universality',
 'The state column grows from 5 to {S}: a μ box (+) and two neutrino boxes where there was one (ν_{e} keeps the old node, ν_{μ} is new). A second dashed model node (+) with its own four-leg junction. The observable column grows to {O} chips (τ_{μ} with A; Michel ρ and ν_{μ} ≠ ν_{e} with P); the dashed calibration edge to G_{F} now leaves the muon node. Counts: {M} model nodes ({eff} effective), {R} routes, {E} edges.',
 'Rule 8 fires in its split form: two ν boxes where there was one, caused by an observable (ν beams produce muons, not electrons), not by anything inside the state column. Rule 6 is prepared: two dashed nodes both send a dashed edge toward the same G_{F} chip, which is the picture of two nodes sharing one calibration; the operation log marks it as a signal. Rule 5 holds for both dashed nodes; this is the step at which the count of effective nodes peaks at {eff}.'),
(8, 'Parity violation and V−A',
 'The two dashed nodes slide into one (V−A, still dashed), which now has three junctions on its left (β decay, μ decay, μ capture) and a fan of edges on its right. Two new chips (parity asymmetries, ν helicity, both P). Counts: {M} model nodes ({eff} effective), {O} observables, {R} routes, {E} edges, no red ring.',
 'Rule 6 is the merge animation and its result: one node entered by the union of the routes, with one coupling. Rule 2 fires in the same step: the two new chips would be ringed under the parity-even nodes of Step 7, and the merged node reaches them (the log shows FLAG followed by MERGE). Rule 4 counts the routes as unified processes: three. The model column shrinks (6 → 5) while the observable column grows (9 → 11): the first reduction in the graph, and the first increase of predictive content without a new node.'),
(9, 'W, Z and the gauge theory',
 'The state column grows to {S}: W^{±} and Z^{0} appear (+), and the n and p boxes slide into u and d. The dashed V−A node slides into a solid charged-current node; two more solid nodes appear (neutral current, self-couplings); the QED node is rewritten (~). Routes go from 4 to {R}: three charged-current routes with a W leg each, one neutral-current route whose leg is a bracket over all fermion boxes, two self-coupling routes, one electromagnetic route with a bracket over the charged boxes. The observable column has {O} chips, five of them new and all five with badge P. Counts: {M} model nodes ({fund} fundamental, {eff} effective), {E} edges.',
 'Rule 7 is visible three times: the dashed node sliding into a solid one (absorption), the W leg added to each former four-leg route (the mediator sector enters every route), and the two solid nodes that no red ring asked for (the symmetry forces them) with their P-badged chips. Rule 8 fires in its replace form (u, d for n, p). Rule 2 fires in its theory-internal form: the model column changed without a red ring, because the dashed node could not be fundamental. Rule 9 adds sin^{2}θ_{W}. The count of effective nodes drops to zero and stays there; the count of fundamental nodes jumps from 1 to {fund}.'),
(10, 'The Higgs sector',
 'An H box (+) completes the state column at {S}. Three solid model nodes appear with four new junctions: H with W, H with Z, H with the bracket of massive fermions, and H alone (the self-coupling route H(3), the first with a single leg). The observable column has {O} chips: m_{H}, the Higgs rates, the fermion masses (dashed calibration edge) and λ_{HHH} with a blue dashed ring (predicted, untested). The M_{W} and M_{Z} chips now receive their edges from the Higgs–gauge node. Counts: {M} model nodes ({fund} fundamental), {R} routes, {E} edges.',
 'Rule 2 fires in its theory-internal form again: there is no red ring, the symmetry forbids explicit mass terms. Rule 4 shows a route with one leg, a self-interaction. Rule 9 is visible as two dashed edges (m_{f}, m_{H}) and as a reassignment: M_{W} is now predicted by a different node than in Step 9, which is a prediction being re-derived rather than a new one. The blue ring is a prediction waiting for its observable.'),
(11, 'The neutrino-mass frontier',
 'One new chip with a red ring (flavour oscillation) and one dotted model node with a dotted route (the ν bracket with H) and a dotted edge. Nothing else changes. Counts: {S} state nodes, {M} model nodes, {O} observables, {R} routes, {U} unexplained chip.',
 'Rule 2 is announced for the third time (the cycle shows observe, deficit, hypothesize), and this time the hypothesis is dotted: the literature offers two repairs and the data select neither. Rule 8 is due but not executed: the ν boxes would have to change (a right-handed state or a Majorana term), and the graph leaves them as they are. The ring is the current research target in the GEN sense.'),
(12, 'The Standard Model as clusters',
 'The model column is reorganized into {cl} outlined clusters; the three absorbed nodes sit, greyed and dashed, inside the first cluster with lineage arrows between them and into the charged-current node. Routes are re-attached to the clusters: {R} in all (5, 2, 2, 1, 1 and 1 candidate). The observable column has {O} chips; all have an edge except the oscillation chip. Counts: {M} model nodes ({fund} fundamental, {absd} absorbed, 1 candidate), {E} edges.',
 'Rule 10 is the picture: the number of outlined clusters equals the number of terms of the Lagrangian plus one candidate, and every absorbed node sits in the cluster whose member reproduces it. Rule 4 appears cumulatively: the number of routes into a cluster counts the sector combinations the term couples. Rule 9 is readable at a glance as four dashed edges (α, G_{F}, m_{f}, m_{H}) leaving three clusters against twelve solid ones. The lineage arrows are all that remains of Steps 6–8: Rule 7 leaves exactly this trace in the final form.'),
]

CUMULATIVE = [
 ('State column', 'The count runs 1 → 9 → 9 → 5 → 5 → 5 → 7 → 7 → 9 → 10 → 10 → 10. Every change has a cause outside the column: a symmetry (Step 2), a model node\'s back-edge (Step 4), an observable that distinguishes sectors (Step 7), an absorption with a new mediator (Step 9), and a theory-internal requirement (Step 10). No change is caused by a state node. That is Rule 8 read across the strip.'),
 ('Dashed model nodes', 'Effective nodes appear at Step 6, peak at Step 7 (two), merge at Step 8 (one) and vanish at Step 9; at Step 12 they reappear only as greyed chips inside a cluster. The strip shows the rise and fall that Rules 5–7 describe: temporary nodes that proliferate, merge when they share a calibration, and are absorbed by solid nodes.'),
 ('Solid model nodes', 'Fundamental nodes go 1 (Step 5) → 4 (Step 9) → 7 (Step 10) and never decrease. Two of the jumps are caused by red rings (Rule 2, anomaly form) and two by the symmetry (Rule 2, theory-internal form). The two forms are distinguishable in the strip: the first follows a ringed chip, the second does not.'),
 ('Red rings', 'Rings appear at Steps 3, 4, 5 and 11. The first is closed at Step 4 by being replaced with two, the two are closed at Steps 5 and 6, and the last is still open. Rule 2 is the engine: every closure is a new model node, and the open ring is the place where the next node will appear.'),
 ('Junctions', 'Routes are absent until Step 5, then grow by one per interaction node (Steps 5, 6, 7), by one at the merge (Step 8, three processes into one node), by three at the absorption (Step 9, each route gaining a W leg and the symmetry adding two more), by one per Higgs term, and are finally re-attached to clusters (Step 12). Rule 4 is visible as the one-to-one correspondence between legs and the fields of a term.'),
 ('Badges', 'A badges dominate Steps 1–8, P badges dominate Steps 9–10, and Step 11 opens with an A. This is the regime flip of the cycle: the first run of the loop is anomaly-first, its second half prediction-first, and the third run begins as the first did.'),
 ('Dashed calibration edges', 'One appears per new parameter: α (Step 5), G_{F} (Step 6, re-attached at Steps 7, 8, 9), sin^{2}θ_{W} (Step 9), m_{f} and m_{H} (Step 10). Rule 9 locates the predictive content of the final graph as the excess of solid over dashed edges leaving the clusters.'),
]

# ---------- renderers ----------
def tex_escape(s):
    return (s.replace('\\', r'\textbackslash{}').replace('&', r'\&').replace('%', r'\%').replace('#', r'\#').replace('$', r'\$').replace('~', r'\textasciitilde{}'))
def rich2tex(s):
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c in '^_' and i + 1 < len(s) and s[i+1] == '{':
            j = s.find('}', i + 2)
            out.append((r'\textsuperscript{' if c == '^' else r'\textsubscript{') + tex_escape(s[i+2:j]) + '}'); i = j + 1
        else:
            out.append(tex_escape(c) if c in '\\&%#$~' else ('\\_' if c == '_' else '\\^{}' if c == '^' else '\\{' if c == '{' else '\\}' if c == '}' else c)); i += 1
    return ''.join(out)
def md(s):
    return re.sub(r'\^\{([^}]*)\}', r'<sup>\1</sup>', re.sub(r'_\{([^}]*)\}', r'<sub>\1</sub>', s))
def fill(s, k):
    c = C(k)
    return re.sub(r'\{(S|M|O|R|E|U|eff|fund|absd|cl)\}', lambda m: str(c[m.group(1)]), s)

def write_tex():
    P = os.path.join(ROOT, 'paper')
    L = [r'\section{Reading the rules off the twelve step graphs}\label{sec:rulesteps}',
         r'The synthesis view of the page (Step~13) draws the whole graph small and re-lays it out at every step, so that the twelve graphs can be seen in sequence (Figure~\ref{fig:film}); the cycle diagram beside it shows which phases of the method are active (Figure~\ref{fig:cycles}). This section reads the rules of Section~\ref{sec:laws} off those twelve pictures, one step at a time, and then across the sequence. For each step the first paragraph describes the graph as displayed and the second says which rules are visible in it and how; Table~\ref{tab:rulematrix} summarizes the assignment. The counts quoted are those of \texttt{data/statistics.json}, which the page and this section share.',
         '',
         r'\begin{figure}[p]\centering\includegraphics[width=\linewidth]{filmstrip.png}\caption{The twelve graphs of the synthesis view, in order, each labelled with the rules visible in it. Blue junctions are AND routes; dashed violet nodes are effective; red dashed rings mark observables with no model edge; a $+$ marks a node added in the step and a $\sim$ a node rewritten.}\label{fig:film}\end{figure}',
         r'\begin{figure}[htbp]\centering\includegraphics[width=\linewidth]{cyclestrip.png}\caption{The method cycle at each of the twelve steps: filled phases are active. Steps 3 and 11 light observe and deficit; Steps 9 and 10 light hypothesize and predict before observe; Step 12 lights only reduce.}\label{fig:cycles}\end{figure}',
         '']
    for k, title, graph, rules in STEPS:
        L.append(r'\subsection*{Step %d: %s}' % (k, rich2tex(title)))
        L.append(r'\noindent\emph{The graph.} ' + rich2tex(fill(graph, k)))
        L.append('')
        L.append(r'\noindent\emph{The rules in it.} ' + rich2tex(fill(rules, k)))
        L.append('')
    L.append(r'\subsection*{Across the sequence}')
    L.append(r'Read down the filmstrip instead of across it, the twelve graphs give the rules a second time, as regularities of the whole sequence.')
    L.append(r'\begin{description}[style=nextline]')
    for h, t in CUMULATIVE:
        L.append(r'\item[%s.] %s' % (rich2tex(h), rich2tex(t)))
    L.append(r'\end{description}')
    L.append(r"""The reading is cumulative in a precise sense: no rule needs a later step to be recognized, but each later step narrows what a rule can mean. Rule~2 at Step~4 could be read as ``a deficit triggers a model node''; by Step~10 it must be read as ``a deficit \emph{or} a theory-internal inconsistency triggers a model node'', and by Step~11 as a rule that can be announced without being executed. Rule~8 at Step~2 is a statement about symmetry; by Step~9 it covers four distinct causes. The step graphs are therefore not illustrations of the rules but the evidence for them, and the only evidence this paper offers.""")
    L.append('')
    L.append(r'\input{tab_rulematrix.tex}')
    open(os.path.join(P, 'sec_rules_steps.tex'), 'w').write('\n'.join(L) + '\n')
    # matrix
    T = [r'\begin{table}[htbp]\centering\small', r'\caption{Rules visible in each step graph: $\bullet$ the rule fires, $\circ$ the rule is prepared or announced but not executed.}\label{tab:rulematrix}',
         r'\begin{tabular}{@{}l' + 'c' * 10 + r'@{}}\toprule', 'Step & ' + ' & '.join('R%d' % r for r in range(1, 11)) + r'\\\midrule']
    for k in range(1, 13):
        T.append('%d %s & ' % (k, rich2tex(STEPS[k-1][1])) + ' & '.join({'●': r'$\bullet$', '○': r'$\circ$'}.get(MATRIX[k].get(r, ''), '') for r in range(1, 11)) + r'\\')
    T.append(r'\bottomrule\end{tabular}')
    T.append(r'\par\smallskip\noindent\footnotesize ' + '; '.join('R%d %s' % (r, RULE_NAMES[r]) for r in range(1, 11)) + '.')
    T.append(r'\end{table}')
    open(os.path.join(P, 'tab_rulematrix.tex'), 'w').write('\n'.join(T) + '\n')

def write_md():
    os.makedirs(os.path.join(ROOT, 'notes'), exist_ok=True)
    L = ['# Reading the rules of evolution off the twelve step graphs', '',
         'A note accompanying the Standard Model Epistemic Graph (GEN_HEP). The synthesis view of the page (Step 13) re-draws the whole graph at every step; this note reads the ten rules of evolution (paper, Section 4) off those twelve pictures. Counts are those of `data/statistics.json`. The page itself is unchanged; this is text only. Rich markup: <sup>sup</sup>, <sub>sub</sub>.', '',
         '| Step | ' + ' | '.join('R%d' % r for r in range(1, 11)) + ' |', '|---|' + '---|' * 10]
    for k in range(1, 13):
        L.append('| %d %s | ' % (k, md(STEPS[k-1][1])) + ' | '.join(MATRIX[k].get(r, '') for r in range(1, 11)) + ' |')
    L.append('')
    L.append('● the rule fires; ○ prepared or announced but not executed. ' + '; '.join('R%d %s' % (r, RULE_NAMES[r]) for r in range(1, 11)) + '.')
    L.append('')
    for k, title, graph, rules in STEPS:
        L.append('## Step %d: %s' % (k, md(title)))
        L.append('')
        L.append('**The graph.** ' + md(fill(graph, k)))
        L.append('')
        L.append('**The rules in it.** ' + md(fill(rules, k)))
        L.append('')
    L.append('## Across the sequence')
    L.append('')
    for h, t in CUMULATIVE:
        L.append('- **%s.** %s' % (md(h), md(t)))
    L.append('')
    L.append('The reading is cumulative: no rule needs a later step to be recognized, but each later step narrows what a rule can mean. Rule 2 at Step 4 could be read as "a deficit triggers a model node"; by Step 10 it must be read as "a deficit *or* a theory-internal inconsistency triggers a model node", and by Step 11 as a rule that can be announced without being executed. Rule 8 at Step 2 is a statement about symmetry; by Step 9 it covers four distinct causes. The step graphs are the evidence for the rules, and the only evidence offered.')
    open(os.path.join(ROOT, 'notes', 'rules-and-step-graphs.md'), 'w').write('\n'.join(L) + '\n')

if __name__ == '__main__':
    write_tex(); write_md(); print('wrote paper/sec_rules_steps.tex, paper/tab_rulematrix.tex, notes/rules-and-step-graphs.md')
