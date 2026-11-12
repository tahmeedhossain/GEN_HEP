#!/usr/bin/env python3
"""Subset the fonts used by the paper to the characters it contains and write them to paper/fonts/,
so that the arXiv source is self-contained (no system fonts). Needs fontTools (pip install fonttools)."""
import glob, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, 'paper'); F = os.path.join(P, 'fonts'); os.makedirs(F, exist_ok=True)
chars = set(chr(c) for c in range(32, 127))
for f in glob.glob(os.path.join(P, '*.tex')):
    chars |= set(open(f, encoding='utf-8').read())
chars |= set('–—‘’“”…·×−≤≥≈≠→←↔∞∂∑∏√∫∧∨∝⟨⟩⊂⊃⊕⊗αβγδεζηθικλμνξοπρστυφχψωΓΔΘΛΞΠΣΦΨΩ°±½¼¾ħ')
ranges = ['U+0020-007E', 'U+00A0-00FF', 'U+0100-017F', 'U+0300-036F', 'U+0370-03FF', 'U+1E00-1EFF', 'U+2000-206F', 'U+2070-209F', 'U+20A0-20AC', 'U+2100-214F', 'U+2190-21FF', 'U+2200-22FF', 'U+2300-231F', 'U+25A0-25FF', 'U+27E6-27EF', 'U+2A00-2AFF']
unis = ','.join(ranges + ['U+%04X' % ord(c) for c in sorted(chars) if ord(c) >= 32])
SRC = {'/usr/share/fonts/truetype/freefont/': ['FreeSerif', 'FreeSerifBold', 'FreeSerifItalic', 'FreeSerifBoldItalic', 'FreeSans', 'FreeSansBold', 'FreeSansOblique', 'FreeSansBoldOblique'],
       '/usr/share/fonts/truetype/dejavu/': ['DejaVuSansMono', 'DejaVuSansMono-Bold', 'DejaVuSansMono-Oblique', 'DejaVuSansMono-BoldOblique']}
for d, names in SRC.items():
    for n in names:
        src = os.path.join(d, n + '.ttf'); dst = os.path.join(F, n + '.ttf')
        subprocess.run([sys.executable, '-m', 'fontTools.subset', src, '--unicodes=' + unis, '--layout-features=*', '--name-IDs=*', '--notdef-outline', '--glyph-names', '--output-file=' + dst], check=True)
        print(n, os.path.getsize(dst) // 1024, 'KB')
