import asyncio, json, subprocess, sys, tempfile, time, urllib.request, base64, websockets
url, out, w, h = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
d = tempfile.mkdtemp()
p = subprocess.Popen(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars',
    '--user-data-dir='+d,'--remote-debugging-port=9334',f'--window-size={w},{h}','about:blank'],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    for _ in range(60):
        try:
            tabs = json.load(urllib.request.urlopen('http://127.0.0.1:9334/json')); break
        except Exception: time.sleep(0.5)
    ws_url = [t for t in tabs if t['type']=='page'][0]['webSocketDebuggerUrl']
    async def run():
        async with websockets.connect(ws_url, max_size=200_000_000) as ws:
            n = 0
            async def call(m, **params):
                nonlocal n; n += 1; i = n
                await ws.send(json.dumps({'id': i, 'method': m, 'params': params}))
                while True:
                    r = json.loads(await ws.recv())
                    if r.get('id') == i: return r.get('result', r)
            await call('Emulation.setDeviceMetricsOverride', width=w, height=h, deviceScaleFactor=1, mobile=w < 600)
            await call('Page.enable')
            await call('Page.navigate', url=url)
            await asyncio.sleep(float(sys.argv[5]) if len(sys.argv)>5 else 3)
            y = 0
            if len(sys.argv)>6:   # expression JS facultative ; si elle renvoie un nombre, la capture commence à cette ordonnée
                ev = await call('Runtime.evaluate', expression=sys.argv[6], awaitPromise=True, returnByValue=True)
                v = ev.get('result', {}).get('value')
                if isinstance(v, (int, float)): y = max(0, int(v))
                await asyncio.sleep(2)
            r = await call('Page.captureScreenshot', format='png', captureBeyondViewport=True,
                           clip={'x':0,'y':y,'width':w,'height':h,'scale':1})
            open(out,'wb').write(base64.b64decode(r['data']))
    asyncio.run(asyncio.wait_for(run(), 60))
    print('ok', out)
finally:
    p.kill()
