#!/usr/bin/env python3
"""Bannières 1200x630 des intégrations, style « Freebox Homexa » (fond sombre dégradé, badge, titre bicolore, puces, visuels à droite).
Usage : python3 make_banner.py <id> <sortie.png>     (les bannières sont décrites dans BANNERS ci-dessous)
Images à droite : icônes/logos tirés des dépôts GitHub XAV59213/<repo> (dossier assets/), cartes dessinées en HTML.
"""
import json, os, subprocess, sys
here = os.path.dirname(os.path.abspath(__file__))
cp = json.load(open(os.path.join(here, '..', 'ha-cover', 'mdi-codepoints.json')))
def mdi(n, col='#fff', size=30):
    return f'<i class="mdi" style="color:{col};font-size:{size}px">&#x{cp[n]};</i>'

CSS = """
@font-face{font-family:Figtree;src:url(figtree-latin.woff2) format('woff2');font-weight:300 900;}
@font-face{font-family:MDI;src:url(materialdesignicons-webfont.woff2) format('woff2');}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1200px;height:630px;overflow:hidden;font-family:Figtree,sans-serif;color:#fff}
body{background:radial-gradient(ellipse at 0% 0%,var(--g1) 0,rgba(0,0,0,0) 55%),radial-gradient(ellipse at 100% 100%,var(--g2) 0,rgba(0,0,0,0) 60%),linear-gradient(135deg,#1a1424 0%,#121829 55%,#14213f 100%);position:relative}
.mdi{font-family:MDI;font-style:normal;line-height:1}
.left{position:absolute;left:60px;top:58px;width:610px}
.badge{display:inline-flex;align-items:center;gap:8px;background:var(--badge);color:#0d1b2a;font-weight:800;font-size:23px;letter-spacing:.5px;padding:9px 22px;border-radius:999px}
h1{margin-top:34px;font-size:84px;line-height:.98;font-weight:900;letter-spacing:-1px}
h1 .a{color:var(--accent);display:block}
.sub{margin-top:22px;font-size:29px;color:#dfe6f3;font-weight:500}
.ver{margin-top:10px;font-size:24px;color:var(--ver);font-weight:800}
.chips{margin-top:26px;display:flex;flex-wrap:wrap;gap:12px;max-width:600px}
.chip{border:2px solid rgba(255,255,255,.35);background:rgba(255,255,255,.07);border-radius:999px;padding:7px 16px;font-size:20px;font-weight:700}
.foot{position:absolute;left:60px;bottom:20px;font-size:17px;color:rgba(255,255,255,.6)}
.right{position:absolute;left:690px;top:0;width:510px;height:630px}
.card{position:absolute;background:#fff;color:#1b2430;border-radius:22px;box-shadow:0 20px 50px rgba(0,0,0,.45),0 0 0 6px rgba(255,255,255,.08);padding:18px 20px}
.card h4{font-size:17px;color:#55606e;font-weight:700;display:flex;align-items:center;gap:8px;margin-bottom:8px}
.card .big{font-size:27px;font-weight:800}
.card .small{font-size:16px;color:#6a7480;margin-top:4px}
.row{display:flex;align-items:center;gap:12px;padding:7px 0;border-top:1px solid #eef0f3;font-size:17px}
.row:first-of-type{border-top:0}
.pill{margin-left:auto;font-size:13px;font-weight:800;padding:3px 10px;border-radius:999px}
.glow{position:absolute;border-radius:50%;filter:blur(40px);opacity:.55}
img.art{position:absolute;border-radius:28px;box-shadow:0 18px 50px rgba(0,0,0,.5)}
"""

BANNERS = {
 'jourferier': dict(vars='--g1:rgba(0,85,164,.55);--g2:rgba(239,65,53,.35);--accent:#ef4135;--badge:#5ec8f8;--ver:#7cc7ff',
   badge='✓ HACS OFFICIEL', t1='Jour', t2='Férié', sub='Les jours fériés français dans Home Assistant', ver='Version 1.3.1',
   chips=['Aujourd’hui &amp; demain férié','Prochain pont','Calendrier','Alsace-Moselle'], foot='github.com/XAV59213/jourferier',
   right=lambda: f"""
<div class="glow" style="left:120px;top:140px;width:300px;height:300px;background:#0055a4"></div>
<img class="art" src="assets/jourferier-icon.png" style="left:250px;top:40px;width:230px;height:230px">
<div class="card" style="left:20px;top:70px;width:250px">
 <h4>{mdi('calendar-today','#0055a4',22)} Aujourd’hui</h4><div class="big">Jour normal</div><div class="small">binary_sensor.est_ferie : off</div></div>
<div class="card" style="left:60px;top:300px;width:420px">
 <h4>{mdi('calendar-star','#ef4135',22)} Prochain jour férié</h4>
 <div class="big">Noël · vendredi 25 décembre</div><div class="small">avec le nombre de jours restants</div>
 <div style="margin-top:12px">
 <div class="row">{mdi('church','#6d4c41',22)} Saint-Étienne · 26 décembre <span class="pill" style="background:#e3f0ff;color:#0055a4">Alsace-Moselle</span></div>
 <div class="row">{mdi('bridge','#fb8c00',22)} Pont : vendredi 7 mai 2027 <span class="pill" style="background:#fff1e0;color:#c25e00">Ascension</span></div>
 </div></div>"""),
 'freesmsxa': dict(vars='--g1:rgba(205,30,37,.55);--g2:rgba(90,40,160,.35);--accent:#ff4d57;--badge:#5ec8f8;--ver:#7cc7ff',
   badge='✓ HACS OFFICIEL', t1='Free Mobile', t2='SMS XA', sub='Les alertes de la maison par SMS, gratuitement', ver='Version 6.12.14',
   chips=['Multi-utilisateurs','Suivi du quota','Historique des 50 SMS','Carte « Envoyer un SMS »'], foot='github.com/XAV59213/freesmsxa · projet indépendant, non affilié à Free',
   right=lambda: f"""
<div class="glow" style="left:150px;top:160px;width:280px;height:280px;background:#cd1e25"></div>
<div class="card" style="left:110px;top:40px;width:330px;height:550px;border-radius:40px;padding:26px 20px;background:#f4f6f9">
 <div style="text-align:center;font-weight:800;font-size:18px;color:#333;margin-bottom:6px">Maison</div>
 <div style="text-align:center;font-size:13px;color:#888;margin-bottom:16px">SMS · aujourd’hui</div>
 <div style="background:#e9ecf1;border-radius:18px 18px 18px 4px;padding:12px 14px;font-size:17px;margin-bottom:12px">🚪 Porte d’entrée ouverte alors que l’alarme est activée.</div>
 <div style="background:#e9ecf1;border-radius:18px 18px 18px 4px;padding:12px 14px;font-size:17px;margin-bottom:12px">🌡️ Congélateur du garage : −8 °C, vérifiez la porte.</div>
 <div style="background:#e9ecf1;border-radius:18px 18px 18px 4px;padding:12px 14px;font-size:17px;margin-bottom:12px">💧 Fuite d’eau détectée sous l’évier de la cuisine.</div>
 <div style="background:#e9ecf1;border-radius:18px 18px 18px 4px;padding:12px 14px;font-size:17px">✅ Test SMS Home Assistant : tout fonctionne.</div>
</div>
<img class="art" src="assets/freesmsxa-icon.png" style="left:20px;top:380px;width:150px;height:150px;border-radius:30px">"""),
 'saintdujour': dict(vars='--g1:rgba(176,137,58,.5);--g2:rgba(60,80,160,.35);--accent:#e7c06a;--badge:#e7c06a;--ver:#f3d996',
   badge='✓ HACS OFFICIEL', t1='Saints', t2='du Jour', sub='Le calendrier des saints dans Home Assistant', ver='Version 1.4.1',
   chips=['Saint du jour','Saint de demain','Carte Lovelace incluse','Notifications'], foot='github.com/XAV59213/saintdujour',
   right=lambda: f"""
<div class="glow" style="left:120px;top:120px;width:320px;height:320px;background:#b0893a"></div>
<img class="art" src="assets/saintdujour-logo.png" style="left:40px;top:60px;width:440px;height:248px;border-radius:24px">
<div class="card" style="left:70px;top:350px;width:400px">
 <h4>{mdi('calendar-heart','#b0893a',22)} Saint du jour · 29 juin</h4>
 <div class="big">les Pierre et Paul</div>
 <div class="row" style="margin-top:10px">{mdi('calendar-arrow-right','#3949ab',22)} Demain : fête à souhaiter <span class="pill" style="background:#f6efe0;color:#8a6a24">Rappel</span></div>
</div>"""),
 'date_countdown': dict(vars='--g1:rgba(200,60,120,.5);--g2:rgba(230,170,60,.3);--accent:#ff7eb6;--badge:#ffd36e;--ver:#ffc1dc',
   badge='DÉPÔT PERSONNALISÉ', t1='Souvenirs &amp;', t2='Célébrations', sub='Anniversaires, noces et dates qui comptent', ver='Version 1.2.24',
   chips=['Anniversaires','Noces','Mémorial','Retraite','Cartes Lovelace'], foot='github.com/XAV59213/date_countdown',
   right=lambda: f"""
<div class="glow" style="left:120px;top:150px;width:320px;height:320px;background:#c83c78"></div>
<img class="art" src="assets/date_countdown-logo.png" style="left:70px;top:50px;width:390px;height:262px;border-radius:24px">
<img class="art" src="assets/date_countdown-jourj.png" style="left:30px;top:360px;width:460px;height:169px;border-radius:20px;background:#fff">"""),
 'piscinexa': dict(vars='--g1:rgba(0,150,200,.5);--g2:rgba(0,200,170,.3);--accent:#38d6f5;--badge:#7ff0d8;--ver:#9ee8ff',
   badge='EN TEST · DÉPÔT PERSONNALISÉ', t1='', t2='Piscinexa', sub='Entretenir sa piscine avec Home Assistant', ver='Version 1.0.22',
   chips=['Volume d’eau','Temps de filtration','pH et chlore à ajouter','Journal intégré'], foot='github.com/XAV59213/piscinexa',
   right=lambda: f"""
<div class="glow" style="left:120px;top:120px;width:320px;height:320px;background:#0096c8"></div>
<img class="art" src="assets/piscinexa-icon.png" style="left:230px;top:40px;width:250px;height:250px">
<div class="card" style="left:30px;top:250px;width:440px">
 <h4>{mdi('pool','#0096c8',22)} Ma piscine</h4>
 <div class="row">{mdi('ph','#8e24aa',22)} pH à corriger <span class="pill" style="background:#f3e5f5;color:#6a1b9a">calculé</span></div>
 <div class="row">{mdi('flask','#fb8c00',22)} Chlore à ajouter <span class="pill" style="background:#fff1e0;color:#c25e00">calculé</span></div>
 <div class="row">{mdi('timer-outline','#00897b',22)} Temps de filtration recommandé <span class="pill" style="background:#e0f5f1;color:#00695c">auto</span></div>
 <div class="row">{mdi('water','#1e88e5',22)} Volume d’eau du bassin <span class="pill" style="background:#e3f0ff;color:#1565c0">m³</span></div>
</div>"""),
}

def render(key, out):
    b = BANNERS[key]
    t2 = b['t2']
    html = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body style="{b['vars']}"><div class="left"><span class="badge">{b['badge']}</span>
<h1>{b['t1']}<span class="a">{t2}</span></h1><div class="sub">{b['sub']}</div><div class="ver">{b['ver']}</div>
<div class="chips">{''.join(f'<span class="chip">{c}</span>' for c in b['chips'])}</div></div>
<div class="right">{b['right']()}</div><div class="foot">{b['foot']}</div></body></html>"""
    path = os.path.join(here, f'_{key}.html'); open(path, 'w').write(html)
    subprocess.run([sys.executable, os.path.join(here, '..', 'ha-cover', 'shot.py'), 'file://' + path, os.path.abspath(out), '1200', '630'],
                   check=True, stdout=subprocess.DEVNULL, timeout=120)
    print(out)

if __name__ == '__main__':
    render(sys.argv[1], sys.argv[2])
