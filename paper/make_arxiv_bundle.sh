#!/bin/sh
# Build the arXiv source bundle: main.tex, every \input file, figures and the subset fonts.
# The paper compiles with XeLaTeX (fontspec); the fonts are shipped in fonts/, so no system fonts are needed.
set -e
cd "$(dirname "$0")"
python3 ../tools/build_derived.py >/dev/null
python3 ../tools/rules_steps.py >/dev/null
python3 ../tools/make_fonts.py >/dev/null 2>&1 || echo "fonts not regenerated (fontTools missing?); using the committed fonts/"
rm -f main.aux main.toc main.out main.fls main.fdb_latexmk main.xdv
latexmk -xelatex -interaction=nonstopmode main.tex >/dev/null
cat > README_ARXIV.txt <<'TXT'
Standard Model Epistemic Graph -- arXiv source
Compile with XeLaTeX (fontspec is used; the fonts are included in fonts/):
    latexmk -xelatex main.tex
Files: main.tex (top level), sec_*.tex, tab_*.tex, numbers.tex, refs_generated.tex (bibliography,
no BibTeX needed), figures/*.png, fonts/*.ttf (subsets of GNU FreeFont and DejaVu Sans Mono;
licences permit redistribution). All tables and numbers are generated from the graph data in the
GitHub repository https://github.com/tahmeedhossain/GEN_HEP.
TXT
rm -f arxiv_source.tar.gz
tar czf arxiv_source.tar.gz README_ARXIV.txt main.tex sec_laws.tex sec_guide.tex sec_rules_steps.tex numbers.tex tab_*.tex refs_generated.tex figures/*.png fonts/*.ttf
echo "wrote paper/arxiv_source.tar.gz ($(du -h arxiv_source.tar.gz | cut -f1))"
