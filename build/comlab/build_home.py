import json, urllib.parse, base64

def load(p, school):
    d = json.load(open(p))
    out = []
    for l in d['labs']:
        fine = [f for t in (l['tax'] or []) for f in t['fine']]
        kw = [k[0] for k in (l['keywords'] or [])]
        out.append({'s': school, 'id': l['slug'], 'n': l['short'] or l['name'], 'f': l['name'],
                    'p': ', '.join(l['pis']), 'pe': ' '.join(l['pisEn'] or []), 'd': ', '.join(l['depts']),
                    'fo': l['focus'] or '', 'k': ' '.join(fine + kw)})
    tot = sum(l['pubs']['total'] for l in d['labs'] if l['pubs'])
    return out, (len(d['labs']), tot)

# 학교 추가: 아래 목록에 한 줄 추가 (data가 None이면 '준비 중' 카드)
SCHOOLS = [
    dict(id='ku', name='고려대학교', short='고려대', c='#A6192E', soft='#FBEFF1', data='../data.json', mark='ku_mark.png', mk='ku',
         dep='컴퓨터학과, 인공지능학과, 데이터과학과, 전기전자공학부, 기계공학부'),
    dict(id='kaist', name='KAIST', short='KAIST', c='#0B4EA2', soft='#EDF3FB', data='../kaist/data.json', mark='kaist_mark.png', mk='kaist',
         dep='전산학부, 김재철AI대학원, AI대학 4개 학과'),
    dict(id='snu', name='서울대학교', short='서울대', data=None),
    dict(id='yonsei', name='연세대학교', short='연세대', data=None),
]
# 소식: dict(date='2026-11-20', school='ku', lab='IDEA', slug='idea', title='...', url='...')
NEWS = []

# 문의: Formspree 폼 ID (https://formspree.io/f/<ID>). 비어 있으면 메일 앱으로 대신 보내요.
FORMSPREE_ID = ''
DEV = dict(name='김정훈', role='고려대학교 컴퓨터학과', email='rexmang1229@gmail.com',
           github='https://github.com/AYeon-3029', linkedin='https://www.linkedin.com/in/junghoon-kim-aa4a23450/')

ALL = []
for sc in SCHOOLS:
    if sc['data']:
        labs, st = load(sc['data'], sc['id']); sc['n'] = st[0]; ALL += labs
ku_n = SCHOOLS[0]['n']; ka_n = SCHOOLS[1]['n']
kus = (ku_n,); kas = (ka_n,)
IDX = json.dumps(ALL, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

FAV = 'data:image/svg+xml,' + urllib.parse.quote('<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect x="2" y="3" width="36" height="34" rx="9" fill="#1D2029"/><path d="M10 14L18 21L10 28" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"/><rect x="20" y="25" width="11" height="4.5" rx="1.5" fill="#fff"/></svg>', safe='/:=')
LOGO = '<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="2" y="3" width="36" height="34" rx="9" fill="#1D2029"/><path d="M10 14L18 21L10 28" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"/><rect x="20" y="25" width="11" height="4.5" rx="1.5" fill="#fff"/></svg>'
CHIPS = ['LLM', '컴퓨터 비전', '강화학습', '로보틱스', '보안', '추천 시스템', '반도체', '그래픽스']

ACTIVE = [sc for sc in SCHOOLS if sc['data']]
SC = json.dumps({sc['id']: [sc['c'], sc['soft']] for sc in ACTIVE})
SN = json.dumps({sc['id']: sc['short'] for sc in ACTIVE}, ensure_ascii=False)
TOTAL = sum(sc['n'] for sc in ACTIVE)
def school_card(sc):
    if not sc['data']:
        return f'<div class="sch wait"><span class="big">{sc["name"]}</span><span class="st">준비 중</span></div>'
    return (f'<a class="sch on" href="/{sc["id"]}/" style="--c:{sc["c"]};--s:{sc["soft"]}">' +
            (f'<img class="mark" alt="" src="data:image/png;base64,{base64.b64encode(open(sc["mark"],"rb").read()).decode()}" data-k="{sc["mk"]}">' if sc.get('mark') else '') +
            f'<span class="big">{sc["name"]}</span><span class="dep">{sc["dep"]}</span>'
            f'<span class="row"><span class="n"><b>{sc["n"]}</b>곳</span></span></a>')
SCH_HTML = ''.join(school_card(sc) for sc in SCHOOLS)
SCMAP = {sc['id']: sc for sc in ACTIVE}
def news_item(n):
    sc = SCMAP[n['school']]
    return (f'<li><a href="{n["url"]}" target="_blank" rel="noopener"><time>{n["date"][5:].replace("-", ".")}</time>'
            f'<span class="tag" style="color:{sc["c"]};background:{sc["soft"]}">{sc["short"]}</span>'
            f'<span class="nt"><b>{n["lab"]}</b>{n["title"]}</span></a></li>')
NEWS_HTML = ('<ul class="news">' + ''.join(news_item(n) for n in sorted(NEWS, key=lambda x: x['date'], reverse=True)[:8]) + '</ul>') if NEWS else \
    '<div class="empty"><b>연구실 소식을 모으고 있어요.</b><span>새 논문, 수상, 인턴·학생 모집 공고를 학교 구분 없이 최신순으로 보여 줄 예정이에요.</span></div>'

html = f'''<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>컴랩 — 대학 컴퓨터·AI 연구실 찾기</title>
<meta name="description" content="고려대 {kus[0]}곳, KAIST {kas[0]}곳. 컴퓨터·AI 연구실을 분야, 교수, 키워드로 한 번에 찾아보세요.">
<meta property="og:type" content="website"><meta property="og:site_name" content="컴랩"><meta property="og:url" content="https://ku-lab-directory.vercel.app/">
<meta property="og:title" content="컴랩 — 대학 컴퓨터·AI 연구실 찾기">
<meta property="og:description" content="고려대 {kus[0]}곳, KAIST {kas[0]}곳. 연구 분야, 2024–26 논문 실적, 학부 인턴, 졸업생 진로로 연구실을 비교해 보세요.">
<meta property="og:image" content="https://ku-lab-directory.vercel.app/og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="ko_KR"><meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#ffffff">
<link rel="icon" href="{FAV}">
<link rel="preconnect" href="https://cdn.jsdelivr.net">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css" media="print" onload="this.media='all'">
<style>
:root{{--ink:#16181D;--ink2:#4A505C;--ink3:#8A909C;--rule:#E4E6EA;--bg2:#F4F5F7;--ku:#A6192E;--kus:#FBEFF1;--ka:#0B4EA2;--kas:#EDF3FB}}
*{{box-sizing:border-box}}html{{-webkit-tap-highlight-color:transparent}}
body{{margin:0;font-family:"Pretendard Variable",Pretendard,-apple-system,"Apple SD Gothic Neo","Noto Sans KR",sans-serif;color:var(--ink);background:#fff;-webkit-font-smoothing:antialiased;min-height:100vh;display:flex;flex-direction:column}}
a{{color:inherit;text-decoration:none}}
.wrap{{width:100%;max-width:1040px;margin:0 auto;padding:0 24px}}
header .wrap{{display:flex;align-items:center;gap:10px;height:64px}}
header svg{{width:30px;height:30px}}header b{{font-size:18px;font-weight:800;letter-spacing:-.02em}}
main{{flex:1}}

.find{{max-width:720px;margin:0 auto;padding:12vh 0 0;text-align:center}}
h1{{margin:0;font-size:clamp(30px,4.6vw,46px);line-height:1.2;letter-spacing:-.035em;font-weight:800}}
.sub{{margin:14px 0 0;color:var(--ink2);font-size:16px;line-height:1.6}}
.box{{position:relative;margin:34px 0 0;text-align:left}}
.box svg{{position:absolute;left:20px;top:50%;transform:translateY(-50%);color:var(--ink3);pointer-events:none}}
#q{{width:100%;height:60px;border:1.5px solid #D5D8DE;border-radius:16px;padding:0 20px 0 52px;font:inherit;font-size:17px;color:var(--ink);background:#fff;outline:none;transition:border-color .15s,box-shadow .15s}}
#q::placeholder{{color:#A3A8B2}}
#q:focus{{border-color:var(--ink);box-shadow:0 0 0 4px rgba(22,24,29,.07)}}
.chips{{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin:16px 0 0}}
.chips button{{font:inherit;font-size:14px;font-weight:600;color:var(--ink2);background:var(--bg2);border:0;border-radius:999px;padding:8px 14px;cursor:pointer}}
.chips button:hover{{background:#E8EAEE;color:var(--ink)}}
.chips button:focus-visible,.res a:focus-visible,.door:focus-visible{{outline:2px solid var(--ink);outline-offset:2px}}

.res{{max-width:720px;margin:22px auto 0;text-align:left}}
.res .meta{{font-size:13.5px;color:var(--ink3);margin:0 4px 8px;display:flex;justify-content:space-between}}
.res ul{{list-style:none;margin:0;padding:0;border:1px solid var(--rule);border-radius:16px;overflow:hidden}}
.res li+li{{border-top:1px solid var(--rule)}}
.res a{{display:grid;grid-template-columns:auto 1fr;gap:2px 12px;padding:14px 18px;align-items:baseline}}
.res a:hover{{background:#FAFAFB}}
.tag{{grid-row:span 2;align-self:start;font-size:12px;font-weight:700;border-radius:6px;padding:3px 7px;margin-top:2px}}
.tag{{color:var(--c);background:var(--s)}}
.nm{{font-size:16px;font-weight:700}}.nm small{{font-size:13.5px;font-weight:500;color:var(--ink3);margin-left:6px}}
.ds{{font-size:13.5px;color:var(--ink2);line-height:1.5}}
mark{{background:#FFF1B8;color:inherit;border-radius:2px}}
.none{{padding:28px;text-align:center;color:var(--ink2);font-size:14.5px;border:1px dashed #D5D8DE;border-radius:16px}}
.more{{display:block;width:100%;margin-top:8px;font:inherit;font-size:14px;font-weight:600;color:var(--ink2);background:var(--bg2);border:0;border-radius:12px;padding:12px;cursor:pointer}}

.block{{margin:72px 0 0}}
h2{{font-size:20px;font-weight:800;letter-spacing:-.02em;margin:0 0 14px}}
.schools{{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px}}
.sch{{border-radius:18px;padding:22px 22px 18px;display:flex;flex-direction:column;min-height:176px;position:relative;overflow:hidden}}
.sch.on{{background:var(--c);color:#fff;transition:transform .2s ease}}
.sch .big{{font-size:24px;font-weight:850;letter-spacing:-.03em}}
.sch .dep{{font-size:13px;opacity:.8;margin-top:6px;line-height:1.55}}
.sch .row{{margin-top:auto;padding-top:18px;display:flex;justify-content:space-between;align-items:flex-end;gap:8px}}
.sch .n{{font-size:14px;opacity:.9}}.sch .n b{{font-size:26px;font-weight:800;margin-right:2px}}
.sch .go{{font-size:13.5px;font-weight:700;background:rgba(255,255,255,.16);border-radius:9px;padding:8px 12px;white-space:nowrap}}
.sch .mark{{position:absolute;opacity:.13;pointer-events:none;user-select:none;right:20px;bottom:18px}}.mark[data-k=ku]{{height:240px;right:-10px;top:-44px;bottom:auto;opacity:.15}}.mark[data-k=kaist]{{width:min(168px,calc(100% - 100px));right:16px;bottom:20px}}.sch>span{{position:relative}}
.sch.wait{{border:1.5px dashed #D5D8DE;color:var(--ink3)}}
.sch.wait .st{{margin-top:auto;font-size:13.5px;font-weight:600}}
@media (hover:hover) and (pointer:fine){{.sch.on:hover{{transform:translateY(-3px)}}.sch.on:hover .go{{background:rgba(255,255,255,.26)}}}}
.sch:focus-visible{{outline:2px solid var(--ink);outline-offset:3px}}
.news{{list-style:none;margin:0;padding:0;border-top:1px solid var(--rule)}}
.news li{{border-bottom:1px solid var(--rule)}}
.news a{{display:grid;grid-template-columns:52px auto 1fr;gap:12px;align-items:baseline;padding:14px 4px}}
.news time{{font-size:13px;color:var(--ink3);font-weight:600}}.news .tag{{font-size:12px;font-weight:700;border-radius:6px;padding:3px 7px}}
.nt{{font-size:15px;line-height:1.5}}.nt b{{margin-right:8px}}
.empty{{background:var(--bg2);border-radius:18px;padding:26px 24px;display:grid;gap:6px;font-size:14.5px;color:var(--ink2);line-height:1.6}}
.empty b{{color:var(--ink);font-size:15.5px}}
.brand{{display:flex;align-items:center;gap:10px}}
.page{{max-width:640px;margin:0 auto;padding:7vh 0 0}}
.page h1{{font-size:clamp(28px,4vw,38px);margin:0 0 10px}}
.page .hint{{margin:0 0 26px}}
.two{{display:grid;grid-template-columns:1.5fr 1fr;gap:40px;align-items:start}}
.hint{{margin:-6px 0 16px;color:var(--ink2);font-size:14.5px;line-height:1.6}}
#ask{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
#ask label{{display:grid;gap:6px;font-size:13.5px;font-weight:650;color:var(--ink2)}}#ask .full{{grid-column:1/-1}}
#ask .opt{{font-weight:500;color:var(--ink3)}}
#ask input,#ask select,#ask textarea{{font:inherit;font-size:15px;font-weight:500;color:var(--ink);border:1.5px solid #D5D8DE;border-radius:12px;padding:11px 13px;background:#fff;outline:none;width:100%}}
#ask textarea{{resize:vertical;min-height:120px;line-height:1.55}}
#ask input:focus,#ask select:focus,#ask textarea:focus{{border-color:var(--ink)}}
#ask .hp{{position:absolute;left:-9999px;width:1px;height:1px}}
.send{{display:flex;align-items:center;gap:14px;flex-wrap:wrap}}
.send button{{font:inherit;font-size:15px;font-weight:700;color:#fff;background:var(--ink);border:0;border-radius:12px;padding:12px 20px;cursor:pointer}}
.send button:disabled{{opacity:.5;cursor:default}}.send button:focus-visible{{outline:2px solid var(--ink);outline-offset:3px}}
#askmsg{{font-size:14px;color:var(--ink2)}}#askmsg.ok{{color:#1A7F4B;font-weight:650}}#askmsg.err{{color:#B42318}}
.dev .card{{background:var(--bg2);border-radius:18px;padding:24px;display:grid;gap:4px}}
.dev .dn{{font-size:20px;font-weight:800}}.dev .dr{{font-size:14px;color:var(--ink2)}}
.dev p{{margin:12px 0 4px;font-size:14px;line-height:1.65;color:var(--ink2)}}
.links{{list-style:none;margin:8px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:8px}}
.links a{{display:inline-block;font-size:13.5px;font-weight:650;background:#fff;border:1px solid var(--rule);border-radius:999px;padding:7px 12px}}
.links a:hover{{border-color:var(--ink3)}}
footer{{margin-top:64px;border-top:1px solid var(--rule);padding:22px 0 40px;font-size:12.5px;color:var(--ink3);line-height:1.7}}
footer a{{text-decoration:underline}}
@media (max-width:680px){{
  .wrap{{padding:0 16px}}.find{{padding-top:7vh}}.sub{{font-size:15px}}
  #q{{height:54px;font-size:16px}}
  .block{{margin-top:52px}}.schools{{grid-template-columns:1fr 1fr;gap:10px}}.sch{{min-height:150px;padding:18px 16px 16px}}.sch .big{{font-size:19px}}.sch .dep{{display:none}}.mark[data-k=ku]{{height:196px;right:-12px;top:-38px;bottom:auto}}.mark[data-k=kaist]{{width:min(112px,calc(100% - 80px));right:12px;bottom:18px}}.sch .go{{display:none}}.news a{{grid-template-columns:auto 1fr;}}.news time{{grid-column:1/-1}}
  .res a{{padding:13px 14px}}
  .two{{grid-template-columns:1fr;gap:44px}}#ask{{grid-template-columns:1fr}}
}}
@media (prefers-reduced-motion:reduce){{.sch,#q{{transition:none}}}}
</style></head><body>
<header><div class="wrap"><a class="brand" href="/">{LOGO}<b>컴랩</b></a>
<!--CL-BURGER--></div></header>
<main class="wrap">
  <section class="find">
    <h1>어떤 연구실을 찾고 있나요?</h1>
    <p class="sub">{len(ACTIVE)}개 학교, 연구실 {TOTAL}곳을 한 번에 검색해요.</p>
    <div class="box" role="search">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
      <input id="q" type="search" autocomplete="off" placeholder="연구 분야, 연구실 이름, 교수 이름" aria-label="연구실 검색" aria-controls="res">
    </div>
    <div class="chips" id="chips">{''.join(f'<button type="button">{c}</button>' for c in CHIPS)}</div>
  </section>
  <section class="res" id="res" aria-live="polite"></section>

  <section class="block" aria-labelledby="h-sch">
    <h2 id="h-sch">학교별로 보기</h2>
    <div class="schools">{SCH_HTML}</div>
  </section>
  <section class="block" aria-labelledby="h-news">
    <h2 id="h-news">연구실 소식</h2>
    {NEWS_HTML}
  </section>
  <section class="block two" id="contact">
    <div class="ask" aria-labelledby="h-ask">
      <h2 id="h-ask">문의하기</h2>
      <p class="hint">연구실 정보가 틀렸거나, 추가됐으면 하는 학교가 있거나, 오류를 발견했다면 알려 주세요.</p>
      <form id="ask" novalidate>
        <label>문의 종류<select name="종류">
          <option>연구실 정보 수정</option><option>학교·연구실 추가 요청</option><option>오류 제보</option><option>기타</option>
        </select></label>
        <label><span>관련 연구실 <span class="opt">(선택)</span></span><input name="연구실" placeholder="예: 고려대 DAVIAN"></label>
        <label class="full">내용<textarea name="내용" rows="5" required placeholder="무엇을 고치면 좋을지 적어 주세요"></textarea></label>
        <label class="full"><span>답장 받을 이메일 <span class="opt">(선택)</span></span><input name="email" type="email" placeholder="you@example.com"></label>
        <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" class="hp" aria-hidden="true">
        <div class="full send"><button type="submit">문의 보내기</button><span id="askmsg" role="status"></span></div>
      </form>
    </div>
    <div class="dev" aria-labelledby="h-dev">
      <h2 id="h-dev">만든 사람</h2>
      <div class="card">
        <b class="dn">{DEV["name"]}</b>
        <span class="dr">{DEV["role"]}</span>
        <p>연구실을 고를 때 필요한 정보를 한곳에서 비교하고 싶어서 만들었어요. 학생 개인이 만든 사이트라 학교와는 관련이 없어요.</p>
        <ul class="links">
          <li><a href="mailto:{DEV["email"]}">{DEV["email"]}</a></li>
          {f'<li><a href="{DEV["github"]}" target="_blank" rel="noopener">GitHub</a></li>' if DEV["github"] else ''}
          {f'<li><a href="{DEV["linkedin"]}" target="_blank" rel="noopener">LinkedIn</a></li>' if DEV["linkedin"] else ''}
        </ul>
      </div>
    </div>
  </section>
</main>
<footer><div class="wrap">출처는 각 대학·연구실 홈페이지와 <a href="https://dblp.org" target="_blank" rel="noopener">dblp</a>예요. 학회 등급은 분류일 뿐 연구실 순위가 아니에요.</div></footer>
<script>
const L={IDX};
const SN={SN};const SC={SC};
const norm=s=>(s||'').toLowerCase().replace(/[\\s·\\-_/(),.]/g,'');
L.forEach(l=>{{l._n=norm(l.n+l.f);l._p=norm(l.p+l.pe);l._f=norm(l.fo);l._k=norm(l.k+' '+l.d);}});
const q=document.getElementById('q'),res=document.getElementById('res');
let shown=8;
const esc=s=>s.replace(/[&<>"]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}})[c]);
function hl(s,t){{ if(!t) return esc(s); const i=s.toLowerCase().indexOf(t.toLowerCase()); return i<0?esc(s):esc(s.slice(0,i))+'<mark>'+esc(s.slice(i,i+t.length))+'</mark>'+esc(s.slice(i+t.length)); }}
function run(){{
  const raw=q.value.trim(), t=norm(raw);
  if(!t){{res.innerHTML='';return;}}
  const hits=[];
  L.forEach(l=>{{ let s=0; if(l._n.includes(t)) s=3; else if(l._p.includes(t)) s=2.5; else if(l._f.includes(t)) s=2; else if(l._k.includes(t)) s=1; if(s) hits.push([s,l]); }});
  hits.sort((a,b)=>b[0]-a[0]);
  if(!hits.length){{res.innerHTML='<div class="none">“'+esc(raw)+'”에 맞는 연구실이 없어요. 다른 키워드나 영어 이름으로 검색해 보세요.</div>';return;}}
    res.innerHTML='<p class="meta"><span>연구실 '+hits.length+'곳</span><span>'+Object.keys(SN).map(k=>SN[k]+' '+hits.filter(h=>h[1].s===k).length).join(' · ')+'</span></p><ul>'+
    hits.slice(0,shown).map(([,l])=>'<li><a href="/'+l.s+'/#lab-'+encodeURIComponent(l.id)+'"><span class="tag" style="--c:'+SC[l.s][0]+';--s:'+SC[l.s][1]+'">'+SN[l.s]+'</span><span class="nm">'+hl(l.n,raw)+(l.f!==l.n?'<small>'+hl(l.f,raw)+'</small>':'')+'</span><span class="ds">'+hl(l.p,raw)+' 교수 · '+hl(l.fo||l.d,raw)+'</span></a></li>').join('')+'</ul>'+
    (hits.length>shown?'<button class="more" type="button" id="more">'+(hits.length-shown)+'곳 더 보기</button>':'');
  const m=document.getElementById('more'); if(m) m.onclick=()=>{{shown+=20;run();}};
}}
q.addEventListener('input',()=>{{shown=8;run();}});
document.getElementById('chips').addEventListener('click',e=>{{ if(e.target.tagName==='BUTTON'){{ q.value=e.target.textContent; shown=8; run(); q.focus(); }} }});
const FS='{FORMSPREE_ID}', DEVMAIL='{DEV["email"]}';
const F=document.getElementById('ask'), M=document.getElementById('askmsg');
F.addEventListener('submit',async e=>{{
  e.preventDefault();
  const fd=new FormData(F), body=(fd.get('내용')||'').trim();
  if(!body){{M.className='err';M.textContent='내용을 적어 주세요.';F.querySelector('textarea').focus();return;}}
  const em=(fd.get('email')||'').trim();
  if(em && !F.querySelector('[name=email]').checkValidity()){{M.className='err';M.textContent='이메일 주소 형식을 확인해 주세요.';return;}}
  if(!FS){{
    const sub='[컴랩 문의] '+fd.get('종류'), NL=String.fromCharCode(10), txt='관련 연구실: '+(fd.get('연구실')||'-')+NL+'답장 이메일: '+(em||'-')+NL+NL+body;
    location.href='mailto:'+DEVMAIL+'?subject='+encodeURIComponent(sub)+'&body='+encodeURIComponent(txt);
    M.className='';M.textContent='메일 앱에서 보내기를 눌러 주세요.';return;
  }}
  const b=F.querySelector('button'); b.disabled=true; M.className=''; M.textContent='보내는 중…';
  try{{
    const r=await fetch('https://formspree.io/f/'+FS,{{method:'POST',body:fd,headers:{{Accept:'application/json'}}}});
    if(!r.ok) throw 0;
    F.reset(); M.className='ok'; M.textContent='문의를 보냈어요. 고마워요!';
  }}catch(_){{ M.className='err'; M.textContent='보내지 못했어요. 잠시 후 다시 시도하거나 '+DEVMAIL+'로 메일 주세요.'; }}
  b.disabled=false;
}});
</script>
</body></html>'''

import re
c0 = html.index('  <section class="block two" id="contact">'); c1 = html.index('</main>')
contact_sec = html[c0:c1]
ask = contact_sec[contact_sec.index('<div class="ask"'):contact_sec.index('<div class="dev"')]
dev = contact_sec[contact_sec.index('<div class="dev"'):contact_sec.rindex('</section>')]
j0 = html.index("const FS='"); j1 = html.rindex('</script>')
contact_js = html[j0:j1]
base = html[:c0] + html[c1:j0] + html[j1:]          # main page
def sub_page(page, title, desc, body, js=''):
    h = base
    a = h.index('<main class="wrap">') + len('<main class="wrap">'); b = h.index('</main>')
    h = h[:a] + '\n  <section class="page">' + body + '</section>\n' + h[b:]
    s0 = h.index('<script>\nconst L='); s1 = h.index('</script>', s0) + len('</script>')
    h = h[:s0] + ('<script>\n' + js + '</script>' if js else '') + h[s1:]
    h = re.sub(r'<title>[^<]*</title>', f'<title>{title} — 컴랩</title>', h)
    h = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{title} — 컴랩">', h)
    h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', h)
    h = h.replace('og:url" content="https://ku-lab-directory.vercel.app/"', f'og:url" content="https://ku-lab-directory.vercel.app/{page}/"')
    return h.replace('<body>', f'<body data-page="{page}">')
ask_body = ask.replace('<div class="ask" aria-labelledby="h-ask">','<div class="ask">').replace('<h2 id="h-ask">문의하기</h2>','<h1>문의하기</h1>')
dev_body = dev.replace('<div class="dev" aria-labelledby="h-dev">','<div class="dev">').replace('<h2 id="h-dev">만든 사람</h2>','<h1>만든 사람</h1>')
pages = {
  'index.html': base.replace('<body>', '<body data-page="home">'),
  'contact/index.html': sub_page('contact', '문의하기', '컴랩에 연구실 정보 수정, 학교 추가 요청, 오류 제보를 보내 주세요.', ask_body, contact_js),
  'about/index.html': sub_page('about', '만든 사람', '컴랩을 만든 사람을 소개해요.', dev_body),
}
import os
import drawer
PG={'index.html':'home','contact/index.html':'contact','about/index.html':'about'}
for p, h in pages.items():
    h = drawer.apply(h, PG[p])
    os.makedirs(os.path.dirname(p) or '.', exist_ok=True)
    open(p, 'w').write(h)
    open(p.replace('index.html', 'artifact.html'), 'w').write(h.replace('<link rel="preconnect" href="https://cdn.jsdelivr.net">\n', '').replace('<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css" media="print" onload="this.media=\'all\'">\n', ''))
print(TOTAL, len(IDX))
