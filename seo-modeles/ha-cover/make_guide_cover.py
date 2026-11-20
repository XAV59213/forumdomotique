#!/usr/bin/env python3
"""Génère une couverture 1200x630 de guide / intégration, style « Actualité Home Assistant ».
Usage : python3 make_guide_cover.py "Guide" "Sauvegarde|Home Assistant" "Sous-titre" "Accroche (ou vide)" "icone:couleur,..." sortie.png
"""
import json, os, subprocess, sys, urllib.parse
here = os.path.dirname(os.path.abspath(__file__))
label, title, sub, tagline, icons, out = sys.argv[1:7]
cp = json.load(open(os.path.join(here, 'mdi-codepoints.json')))
names = [s.split(':')[0] for s in icons.split(',') if s]
missing = [n for n in names if n not in cp]
if missing:
    sys.exit('Icônes MDI inconnues : ' + ', '.join(missing))
q = urllib.parse.urlencode({'l': label, 'h': title, 'm': sub, 't': tagline, 'i': icons,
                            'cp': json.dumps([cp[n] for n in names])})
url = 'file://' + os.path.join(here, 'guide-cover.html') + '?' + q
png = os.path.abspath(out)
# Capture via le protocole DevTools (shot.py) : plus fiable que --screenshot.
subprocess.run([sys.executable, os.path.join(here, 'shot.py'), url, png, '1200', '630'],
               check=True, stdout=subprocess.DEVNULL, timeout=120)
print(png)
