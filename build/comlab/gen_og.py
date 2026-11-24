import sys
from playwright.sync_api import sync_playwright
LOGO = lambda c1, c2, c3: f'<svg viewBox="0 0 40 40"><rect x="2" y="3" width="36" height="34" rx="9" fill="{c1}"/><rect x="2" y="3" width="36" height="9" rx="9" fill="{c2}"/><rect x="2" y="9" width="36" height="3" fill="{c2}"/><circle cx="9" cy="8" r="1.5" fill="{c3}"/><circle cx="13.5" cy="8" r="1.5" fill="{c3}"/><circle cx="18" cy="8" r="1.5" fill="{c3}"/><path d="M10 18L16 23.5L10 29" stroke="#fff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/><rect x="19" y="27" width="10" height="3" rx="1.2" fill="#fff"/></svg>'
def page(c1, c2, c3, dot, eyebrow, title, line, sub, chips):
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{{box-sizing:border-box}}body{{margin:0;width:1200px;height:630px;font-family:"Noto Sans CJK KR",sans-serif;background:#fff;color:#1D2029;position:relative;overflow:hidden}}
.bar{{position:absolute;left:0;top:0;bottom:0;width:14px;background:{c1}}}
.wrap{{position:absolute;left:96px;right:96px;top:84px}}.top{{display:flex;align-items:center;gap:26px}}
.top svg{{width:112px;height:112px}}.k{{font:600 22px/1 "DejaVu Sans Mono",monospace;color:{c1};letter-spacing:.02em}}
h1{{margin:12px 0 0;font-size:66px;font-weight:800;letter-spacing:-.02em;line-height:1.05}}
p{{margin:44px 0 0;font-size:36px;font-weight:700;line-height:1.35}}p span{{color:{c1}}}
.sub{{margin-top:14px;font-size:25px;font-weight:500;color:#4B5160}}
.chips{{position:absolute;left:96px;bottom:70px;display:flex;gap:12px}}.chips b{{font-size:21px;font-weight:600;color:#4B5160;border:2px solid #E6E8EC;border-radius:999px;padding:9px 20px}}
.grid{{position:absolute;right:-40px;top:-40px;width:420px;height:420px;background-image:radial-gradient({dot} 2.2px,transparent 2.4px);background-size:28px 28px}}
</style></head><body><div class="grid"></div><div class="bar"></div><div class="wrap"><div class="top">{LOGO(c1,c2,c3)}<div><div class="k">{eyebrow}</div><h1>{title}</h1></div></div>
<p>{line}</p><div class="sub">{sub}</div></div><div class="chips">{''.join(f'<b>{c}</b>' for c in chips)}</div></body></html>'''
jobs = [
 ('/home/claude/work/site/og.png', page('#A6192E','#8A1426','#FFD7DD','#F0D3D8','$ 컴랩 · KOREA UNIVERSITY','컴랩 · 고려대','고려대 컴퓨터 분야 연구실 <span>132곳</span>, 한 번에 찾아보기','연구 분야별 탐색 · 2024–26 논문 실적(T1/T2) · 학부 인턴 · 졸업생 진로',['컴퓨터학과','인공지능학과','데이터과학과','전기전자공학부','기계공학부'])),
 ('/home/claude/work/kaist/site/og.png', page('#0B4EA2','#14285C','#BFD6F2','#CFE0F4','$ 컴랩 · KAIST','컴랩 · KAIST','KAIST 컴퓨터·AI 연구실 <span>97곳</span>, 한 번에 찾아보기','연구 분야별 탐색 · 2024–26 논문 실적(T1/T2) · 학부 인턴 · 졸업생 진로',['전산학부','김재철AI대학원','AI컴퓨팅학과','AI시스템학과','AX·AI미래학과'])),
 ('/home/claude/work/comlab/og.png', page('#1D2029','#3A3F4B','#C9CDD6','#E3E5EA','$ comlab --schools','컴랩','대학 컴퓨터·AI 연구실을 <span>한곳에서</span> 비교하기','고려대 132곳 · KAIST 97곳 · 연구 분야 · 논문 실적 · 학부 인턴 · 졸업생 진로',['고려대학교','KAIST','더 많은 학교가 곧 추가돼요'])),
]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width':1200,'height':630})
    for out, html in jobs:
        open('/tmp/og.html','w').write(html); pg.goto('file:///tmp/og.html'); pg.wait_for_timeout(200); pg.screenshot(path=out)
    b.close()
print('ok')
