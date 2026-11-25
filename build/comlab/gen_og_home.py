# 메인(/) 카카오톡·링크 미리보기 이미지 (1200x630)
import base64, json
from playwright.sync_api import sync_playwright
b64 = lambda f: base64.b64encode(open(f, 'rb').read()).decode()
ku_n = len(json.load(open('../data.json'))['labs']); ka_n = len(json.load(open('../kaist/data.json'))['labs'])
LOGO = '<svg viewBox="0 0 40 40"><rect x="2" y="3" width="36" height="34" rx="9" fill="#1D2029"/><path d="M10 14L18 21L10 28" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"/><rect x="20" y="25" width="11" height="4.5" rx="1.5" fill="#fff"/></svg>'
html = f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{{box-sizing:border-box}}body{{margin:0;width:1200px;height:630px;font-family:"Noto Sans CJK KR",sans-serif;background:#fff;color:#16181D;position:relative;overflow:hidden}}
.l{{position:absolute;left:84px;top:70px;width:560px}}
.brand{{display:flex;align-items:center;gap:16px}}.brand svg{{width:58px;height:58px}}.brand b{{font-size:40px;font-weight:900;letter-spacing:-.03em}}
h1{{margin:58px 0 0;font-size:68px;line-height:1.16;font-weight:900;letter-spacing:-.045em}}
.q{{margin-top:44px;height:76px;border:2.5px solid #D5D8DE;border-radius:22px;display:flex;align-items:center;gap:16px;padding:0 26px;font-size:25px;color:#9AA0AA;font-weight:500}}
.q svg{{width:28px;height:28px;flex:none}}
.s{{margin-top:22px;font-size:24px;color:#4A505C;font-weight:500}}
.r{{position:absolute;left:700px;top:56px;width:440px;display:grid;gap:18px}}
.c{{height:208px;border-radius:28px;color:#fff;position:relative;overflow:hidden;padding:30px 32px}}
.c b{{font-size:40px;font-weight:900;letter-spacing:-.03em;position:relative}}
.c span{{position:absolute;left:32px;bottom:26px;font-size:24px;font-weight:500}}.c span em{{font-style:normal;font-size:52px;font-weight:900;margin-right:4px}}
.ku{{background:#A6192E}}.ka{{background:#0B4EA2}}
.c img{{position:absolute;opacity:.16}}
.ku img{{height:330px;right:-40px;top:-62px}}.ka img{{width:200px;right:30px;bottom:34px}}
.w{{height:66px;border:2.5px dashed #D5D8DE;border-radius:22px;display:flex;align-items:center;padding:0 28px;font-size:23px;color:#8A909C;font-weight:600}}
</style></head><body>
<div class="l"><div class="brand">{LOGO}<b>컴랩</b></div>
<h1>어떤 연구실을<br>찾고 있나요?</h1>
<div class="q"><svg viewBox="0 0 24 24" fill="none" stroke="#8A909C" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>연구 분야, 연구실 이름, 교수 이름</div>
<div class="s">대학 컴퓨터·AI 연구실 {ku_n+ka_n}곳을 한 번에 검색해요</div></div>
<div class="r">
<div class="c ku"><img src="data:image/png;base64,{b64('ku_mark.png')}"><b>고려대학교</b><span><em>{ku_n}</em>곳</span></div>
<div class="c ka"><img src="data:image/png;base64,{b64('kaist_mark.png')}"><b>KAIST</b><span><em>{ka_n}</em>곳</span></div>
<div class="w">서울대학교 · 연세대학교 준비 중</div>
</div></body></html>'''
with sync_playwright() as p:
    br = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = br.new_page(viewport={'width': 1200, 'height': 630})
    open('/tmp/og_home.html', 'w').write(html); pg.goto('file:///tmp/og_home.html'); pg.wait_for_timeout(300); pg.screenshot(path='og.png')
    br.close()
print('ok')
