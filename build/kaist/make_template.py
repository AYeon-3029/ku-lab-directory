import re, urllib.parse
t = open('../site/template.html').read()
def sub(a, b, n=1):
    global t
    assert t.count(a) >= n, a[:60]
    t = t.replace(a, b)
# colors
sub('--crimson:#A6192E; --crimson-ink:#8A1426; --crimson-soft:#FBEFF1; --crimson-line:#F0D3D8;',
    '--crimson:#0B4EA2; --crimson-ink:#14285C; --crimson-soft:#EDF3FB; --crimson-line:#CADCF2;')
sub('--t1:#A6192E; --t2:#E08A97;', '--t1:#0B4EA2; --t2:#7FA9DD;')
t = t.replace('#A6192E', '#0B4EA2').replace('#8A1426', '#14285C').replace('#FFD7DD', '#BFD6F2').replace('#ffd7dd', '#BFD6F2')
t = re.sub(r'rgba\(166,\s*25,\s*46', 'rgba(11,78,162', t)
t = t.replace('%23A6192E', '%230B4EA2').replace('%238A1426', '%2314285C')
# texts
t = t.replace('컴랩 · 고려대 — 고려대 컴퓨터 분야 연구실', '컴랩 · KAIST — 카이스트 컴퓨터·AI 연구실')
t = t.replace('컴랩 · 고려대', '컴랩 · KAIST')
t = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="KAIST 전산학부·김재철AI대학원·AI대학 연구실을 연구 분야, 학회 등급(T1/T2), 학부 인턴, 졸업생 진로로 정리한 디렉토리">', t)
desc = 'KAIST 전산학부·김재철AI대학원·AI대학(AI컴퓨팅·AI시스템·AX·AI미래학과) 연구실 __N__곳을 연구 분야, 2024–26 논문 실적(T1/T2), 학부 인턴, 졸업생 진로로 한눈에 비교해 보세요.'
t = re.sub(r'(<meta (?:property="og:description"|name="twitter:description") content=")[^"]*"', lambda m: m.group(1) + desc + '"', t)
t = re.sub(r'(<meta property="og:image:alt" content=")[^"]*"', lambda m: m.group(1) + '컴랩 · KAIST — 카이스트 컴퓨터·AI 연구실 __N__곳"', t)
t = t.replace('https://ku-lab-directory.vercel.app/ku/og.png', 'https://ku-lab-directory.vercel.app/kaist/og.png')
t = t.replace('<meta property="og:url" content="https://ku-lab-directory.vercel.app/ku/">', '<meta property="og:url" content="https://ku-lab-directory.vercel.app/kaist/">')
sub('data-page="ku"', 'data-page="kaist"')
sub('컴랩 · Korea University', '컴랩 · KAIST')
sub('<h1 id="heroTitle">고려대 컴퓨터학과 연구실 디렉토리</h1>', '<h1 id="heroTitle">KAIST 컴퓨터·AI 연구실 디렉토리</h1>')
sub("const depts = [['전체',true,''],['컴퓨터학과',false,''],['인공지능학과',false,''],['데이터과학과',false,''],['전기전자공학부',false,''],['기계공학부',false,'']];",
    "const depts = [['전체',true,''],['전산학부',false,''],['김재철AI대학원',false,''],['AI컴퓨팅학과',false,''],['AI시스템학과',false,''],['AX학과',false,''],['AI미래학과',false,'']];")
sub("$('#heroTitle').textContent = `고려대 ${", "$('#heroTitle').textContent = `KAIST ${")
sub("parts.push(`고려대학교 ${l.depts[0]}", "parts.push(`KAIST ${l.depts[0]}")
# crests -> simple monogram icons (not official emblems)
def icon(bg, txt, fs):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="10" fill="{bg}"/><text x="20" y="26" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="{fs}" fill="#fff">{txt}</text></svg>'
    return 'data:image/svg+xml,' + urllib.parse.quote(s, safe='')
t = re.sub(r"const INFO_DEPTS = \[[^\]]*\];", "const INFO_DEPTS = ['전산학부'];", t)
t = re.sub(r"const CREST_INFO = 'data:image/png;base64,[^']*';", "const CREST_INFO = '" + icon('#14285C', 'SoC', 13) + "';", t)
t = re.sub(r"const CREST_ENG = 'data:image/png;base64,[^']*';", "const CREST_ENG = '" + icon('#0B4EA2', 'AI', 16) + "';", t)
t = t.replace("const c = INFO_DEPTS.includes(d) ? '정보대학' : '공과대학';", "const c = INFO_DEPTS.includes(d) ? '공과대학' : 'AI대학';")
t = t.replace("e.c==='정보대학'?CREST_INFO:CREST_ENG", "e.c==='공과대학'?CREST_INFO:CREST_ENG")
t = t.replace('.dept-b img{height:18px;width:auto;flex:none}', '.dept-b img{height:18px;width:18px;flex:none;border-radius:5px}')
t = t.replace('.ds img{height:46px;width:auto}', '.ds img{height:42px;width:42px;border-radius:11px}')
t = t.replace('.ds img{height:36px}', '.ds img{height:34px;width:34px}')
t = t.replace('<span>KOREA UNIVERSITY · LABS</span>', '<span>KAIST · LABS</span>')
t = t.replace('placeholder="예: MINT Lab, 지능시스템망 연구실, 교수 이름, World Model, LLM 서빙"', 'placeholder="예: KIXLab, 데이터 마이닝 연구실, 교수 이름, World Model, LLM 서빙"')
t = t.replace("<div>T1 추정<b>${hp.T1}</b></div><div>T2 추정<b>${hp.T2}</b></div>", "${hp.T1!=null?`<div>T1 추정<b>${hp.T1}</b></div><div>T2 추정<b>${hp.T2}</b></div>`:''}")
t = t.replace("'연구실 홈페이지 기준 (2026-11-06)'", "'연구실 홈페이지 기준 (2026-11-19, 자동 집계라 실제와 다를 수 있어요)'")
t = t.replace('</style>', '''
.tile.on{background:#E6EFFA;border-color:#8DB2E3}
.tile.on .tk{color:#14285C}.tile.on .te{color:#4A6894}.tile.on .tn{color:#4A6894}.tile.on .tn b{color:#14285C}
@media (hover:hover) and (pointer:fine){.tile.on:hover{background:#DCE8F8;border-color:#7FA6DC}}
.selbar .x{background:#E6EFFA;color:#14285C;box-shadow:inset 0 0 0 1px #C3D7F1}
@media (hover:hover) and (pointer:fine){.selbar .x:hover{background:#DCE8F8}}
.allb.on{background:#E6EFFA;color:#14285C;border-color:#8DB2E3}
</style>''', 1)
LOGO = 'data:image/png;base64,' + open('kaist_logo.b64').read().strip()
t = re.sub(r"function deptBadges\(l\)\{.*?\n", lambda m: "function deptBadges(l){ return `<div class=\"depts\"><span class=\"dept-b\"><img src=\"${KLOGO}\" alt=\"KAIST\">${deptGroups(l).map(e => `<i>${e.c}</i>${e.ds.map(esc).join(' · ')}`).join('<i class=\"sep\">/</i>')}</span></div>`; }\n", t, count=1, flags=re.S)
t = re.sub(r"function deptSide\(l\)\{.*?\n", lambda m: "function deptSide(l){ return `<div class=\"dside\"><div class=\"ds\"><img src=\"${KLOGO}\" alt=\"KAIST\"><div>${deptGroups(l).map(e => `<i>${e.c}</i><b>${e.ds.map(esc).join(' · ')}</b>`).join('')}</div></div></div>`; }\n", t, count=1, flags=re.S)
t = t.replace("const INFO_DEPTS = ['전산학부'];", "const INFO_DEPTS = ['전산학부'];\nconst KLOGO = '" + LOGO + "';")
t = t.replace('.dept-b img{height:18px;width:18px;flex:none;border-radius:5px}', '.dept-b img{height:13px;width:auto;flex:none;margin-right:2px}.dept-b i.sep{color:var(--line);margin:0 2px}')
t = t.replace('.ds img{height:42px;width:42px;border-radius:11px}', '.ds img{height:30px;width:auto}.ds i+b{margin-bottom:4px}')
t = t.replace('.ds img{height:34px;width:34px}', '.ds img{height:24px;width:auto}')
open('site/template.html', 'w').write(t)
left = [w for w in ['고려대', 'korea.ac', '정보대학', '컴퓨터학과', 'A6192E'] if w in t]
print('left:', left)
