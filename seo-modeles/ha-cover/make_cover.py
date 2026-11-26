#!/usr/bin/env python3
"""Génère une couverture 1200x630 « Actualité Home Assistant ».
Usage : python3 make_cover.py [--dev] 2026.5 "Mai 2026" "Accroche" "radio-tower:e53935,battery-heart:43a047,..." sortie.png
"""
import json, os, subprocess, sys, urllib.parse
here = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1:]
dev = args[:1] == ['--dev']   # variante « Actualité HA développement » (orange, badge bêta)
if dev: args = args[1:]
v, month, tagline, icons, out = args[:5]
cp = json.load(open(os.path.join(here, 'mdi-codepoints.json')))
names = [s.split(':')[0] for s in icons.split(',') if s]
missing = [n for n in names if n not in cp]
if missing:
    sys.exit('Icônes MDI inconnues : ' + ', '.join(missing))
q = urllib.parse.urlencode({'v': v, 'm': month, 't': tagline, 'i': icons,
                            'cp': json.dumps([cp[n] for n in names])})
url = 'file://' + os.path.join(here, 'cover-dev.html' if dev else 'cover.html') + '?' + q
png = os.path.abspath(out)
# Capture via le protocole DevTools (shot.py) : plus fiable que --screenshot.
subprocess.run([sys.executable, os.path.join(here, 'shot.py'), url, png, '1200', '630'],
               check=True, stdout=subprocess.DEVNULL, timeout=120)
print(png)
