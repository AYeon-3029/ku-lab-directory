import json, re, collections, math, sys
sys.path.insert(0, '.')
from tiers import classify, CONF_T1, CONF_T2, JOUR_T1, JOUR_T2
from taxonomy_k import TREE, ASSIGN, EN, BIG_DESC

DEPT = {'CS': '전산학부', 'GSAI': '김재철AI대학원', 'AIC': 'AI컴퓨팅학과', 'AIS': 'AI시스템학과', 'AX': 'AX학과', 'FX': 'AI미래학과'}
SHORT = {'CASYS-Kwon': 'CASYS (권영진)', 'CASYS-Park': 'CASYS (박종세)', 'CASYS-Huh': 'CASYS (허재혁)', 'CVML-TK': 'CVML Lab', 'CVML-Shim': 'CVML (심현정)',
         'MLV': 'MLV Lab', 'DEAL': 'AI² Lab', 'AN': 'AN Lab', 'Simplexity': 'Algorithms (김은정)', 'Wiederrecht': 'Graph Theory (Wiederrecht)',
         'Ziegler': 'Complexity & Real Computation', 'SGLab': 'SGVR Lab', 'HyunwooKim': 'Hyunwoo Kim Lab', 'SehoonKim': 'Efficient AI Lab',
         'SungsooAhn': 'Sungsoo Ahn Lab', 'KiminLee': 'Kimin Lee Lab', 'SJHwang': 'MLAI Lab', 'ALIN': 'AGI Lab (ALIN)', 'COMSTO': 'MoonLab',
         'EmbeddedAI': 'Embedded AI Lab', 'SoundLab': 'Smart Sound Lab', 'MELab': 'Meta Earth Lab', 'SKimLab': 'Urban Analytics Lab',
         'JonWoojung': 'IP·FinTech Law', 'Forecasting': 'Predictive Analytics Lab', 'SeunghwaLab': 'Intelligent Design Lab', 'KwonLab': 'Kwon Group',
         'IronTiger': 'IS & Business Analytics', 'SongLab': 'Song Lab', 'QCrypto': 'Quantum Crypto Lab', 'DSLab': 'Data Science Lab',
         'ISILab': 'ISI Lab', 'GCLab': 'GC Lab', 'AIPR': 'AIPR Lab', 'IM2': 'IM² Lab', 'DIVE': 'DIVE Lab', 'OptiML': 'OptiML Lab', 'EdLab': 'Edward Choi Lab',
         'SAIL': 'SAIL', 'INA': 'INA', 'WSP': 'WSP Lab', 'CST': 'CST Lab', 'DICE': 'DICE Lab', 'LANADA': 'LANADA', 'CyPhy': 'CyPhy Lab'}
NAMEFIX = {'DEAL': 'AI² 연구실', 'SGLab': '대용량 그래픽스·비전·로보틱스 연구실 (SGVR)', 'ALIN': 'AGI Lab (Algorithmic General Intelligence)',
           'COMSTO': '문재균 교수 연구실 (MoonLab)', 'SoundLab': 'Smart Sound Lab', 'MELab': 'Meta Earth Lab', 'SKimLab': 'Urban Analytics Lab',
           'Forecasting': 'Predictive Analytics Lab', 'SeunghwaLab': '지능형 설계 및 제조 연구실', 'IDOL': 'AI 기반 설계 최적화 연구실 (IDOL)',
           'AAI': '응용 인공지능 연구실', 'KwonLab': 'Kwon Research Group', 'FTPL': 'Future Transport Power Lab', 'DSIL': 'Device-to-System Integration Lab',
           'SAIL': '통계적 인공지능 연구실 (SAIL)', 'INA': 'INA 연구 그룹', 'AIPR': '인공지능 및 확률추론 연구실 (AIPR)', 'DIVE': 'DIVE Lab (데이터 마이닝)'}
FOCUSFIX = {'MELab': '기후 변화와 인간 사회의 상호작용, 지구 시스템 모델링', 'FTPL': '미래 수송 동력·엔진 시스템', 'IronTiger': '정보시스템·비즈니스 애널리틱스, 디지털 플랫폼',
            'SongLab': '분자 기계, 유전자 조절, 신경퇴행성 질환', 'KwonLab': '지반·환경 공학, 데이터 기반 모델링'}
NO_PUBS = {'MELab': 'dblp 미등재 (기후·지구과학 분야)', 'SKimLab': 'dblp 미등재 (도시계획 분야)', 'DALI': 'dblp에서 해당 교수 기록을 찾지 못함',
           'JonWoojung': 'dblp 미등재 (법학 분야)', 'SongLab': 'dblp 미등재 (생명과학 분야)', 'FTPL': 'dblp 미등재 (기계공학 분야)',
           'KwonLab': 'dblp에 2024–26 기록 없음 (토목·지반 분야)'}
INTERN_HITS = {'NetSP': 2, 'LKLab': 6}
INTERN_CALC = {'NetSP', 'KIXLab', 'CVML-TK', 'MLV', 'RIRO', 'NLPCL', 'VisualAI', 'MLML', 'GLOW', 'LKLab', 'OSI', 'SJHwang', 'SoundLab'}
PIDS = json.load(open('pids.json'))

fac = [l.rstrip('\n').split('\t') for l in open('faculty.tsv') if not l.startswith('#') and l.strip()]
crawl = {}
for l in open('crawl.tsv'):
    if l.startswith('#') or not l.strip(): continue
    f = (l.rstrip('\n').split('\t') + [''] * 11)[:11]
    crawl[f[0]] = f

def num(x): return int(x) if x.strip() else None

def venue_of(pre, flag):
    kind, sub = pre.split(':')
    key = ('conf/' if kind == 'c' else 'journals/') + sub + '/x'
    venue = sub + (' (Findings)' if flag == 'F' else ' Workshop' if flag == 'W' else '')
    res = classify(key, venue)
    if res is None: return None
    tier, label = res
    if flag == 'W': return 'W', sub.upper() + ' 워크숍·EA'
    return tier, label

agg, recent = {}, collections.defaultdict(list)
for fn in ('dblp_raw1.txt', 'dblp_raw2.txt'):
    for line in open(fn, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line: continue
        if '~' in line:
            lid, y, pre, flag, title, authors, iv, key = line.split('~')
            if re.match(r"Editor|Korea Day", title): continue
            v = venue_of(pre, flag); tier, label = v if v else ('기타', pre)
            recent[lid].append({'y': int(y), 'tier': tier, 'venue': label, 'title': title, 'authors': authors, 'interns': [], 'key': key})
        else:
            lid, rest = line.split('=', 1)
            agg[lid] = [x.split('|') for x in rest.split(',') if x]

MID2BIG = {mid: big for big, _, mids in TREE for mid, _, _ in mids}
def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
CAP = {'samsung': 'Samsung', 'lg': 'LG', 'naver': 'Naver', 'kakao': 'Kakao', 'google': 'Google', 'meta': 'Meta', 'microsoft': 'Microsoft', 'nvidia': 'NVIDIA',
       'hyundai': 'Hyundai', 'sk': 'SK', 'krafton': 'KRAFTON', 'qualcomm': 'Qualcomm', 'intel': 'Intel', 'ibm': 'IBM', 'line': 'LINE', 'ncsoft': 'NCSOFT',
       'etri': 'ETRI', 'kist': 'KIST', 'professor': '교수 임용', 'postdoc': '포닥', 'startup': '창업'}
ACA = {'etri', 'kist', 'professor', 'postdoc'}

labs = []
for lid, ko, en, dcodes, labname, url, area in fac:
    c = crawl.get(lid)
    ko_disp = re.sub(r'\(.*\)', '', ko)
    pubs_ok = lid in PIDS and lid not in NO_PUBS and lid in agg
    years = {y: {'T1': 0, 'T2': 0, 'W': 0, 'etc': 0} for y in (2024, 2025, 2026)}
    tot = collections.Counter(); ven = collections.Counter()
    for y, pre, flag, n in agg.get(lid, []):
        v = venue_of(pre, flag)
        if v is None: continue
        tier, label = v; n = int(n); y = int(y)
        k = {'T1': 'T1', 'T2': 'T2', 'W': 'W'}.get(tier, 'etc')
        years[y][k] += n; tot[tier] += n; ven[(tier, label)] += n
    total = sum(tot.values())
    hp = None; members = None; icur = None; alumni = None
    if c:
        phd, ms, pd, it, hn, y4, y5, y6, al, src = [num(x) if i < 8 else x for i, x in enumerate(c[1:11])]
        if any(v is not None for v in (phd, ms, pd)):
            members = {'phd': phd or 0, 'integ': 0, 'ms': ms or 0, 'grad': None, 'postdoc': pd or 0, 'other': 0}
        icur = it
        if hn and hn >= 5:
            hp = {'n': hn, 'years': {'2024': y4 or 0, '2025': y5 or 0, '2026': y6 or 0}, 'T1': None, 'T2': None, 'W': 0, 'venues': []}
        if al:
            items = [(k, int(v)) for k, v in (x.split(':') for x in al.split(','))]
            n = sum(v for _, v in items); aca = sum(v for k, v in items if k in ACA)
            alumni = {'n': n, 'acaPct': round(aca * 100 / n), 'indPct': 100 - round(aca * 100 / n),
                      'ind': [CAP.get(k, k) for k, _ in items if k not in ACA], 'aca': [CAP.get(k, k) for k, _ in items if k in ACA],
                      'extra': '졸업생 페이지 언급 횟수 기준', 'src': src or url, 'srcName': '연구실 홈페이지 Alumni 페이지'}
        src = c[10] or None
    else:
        src = None
    rec = {
        'id': lid, 'slug': slug(lid), 'depts': [DEPT[d] for d in dcodes.split(',')], 'pis': [ko_disp], 'pisEn': [en],
        'name': NAMEFIX.get(lid, labname), 'short': SHORT.get(lid, lid), 'url': url, 'focus': FOCUSFIX.get(lid, area),
        'tax': [{'big': MID2BIG[mid], 'mid': mid, 'fine': fine} for mid, fine in ASSIGN.get(lid, [])],
        'siteDead': False, 'members': members,
        'internsCur': icur, 'internsPast': None, 'internCountOnly': False, 'hp': hp, 'pastListed': False, 'internNamesKoreanOnly': False,
        'memberSrc': src, 'pubSrc': None, 'note': '', 
        'dblp': [f'https://dblp.org/pid/{p}.html' for p in PIDS.get(lid, [])] if pubs_ok else [],
        'pubs': None if not pubs_ok else {
            'total': total, 'T1': tot['T1'], 'T2': tot['T2'], 'W': tot['W'], 'etc': tot['기타'], 'years': years,
            'internCalc': lid in INTERN_CALC, 'internCur': INTERN_HITS.get(lid, 0), 'internPast': 0,
            'venues': [[t, lb, n] for (t, lb), n in sorted(ven.items(), key=lambda x: (-x[1], x[0][1]))],
            'recent': sorted(recent[lid], key=lambda r: -r['y'])},
        'keywords': [], 'pubNote': NO_PUBS.get(lid, '' if pubs_ok else 'dblp 매칭 보류'), 'alumni': alumni}
    labs.append(rec)

def vec(l):
    v = collections.Counter()
    for i, t in enumerate(l['tax']):
        w = 1.0 if i == 0 else 0.7
        v['m:' + t['mid']] += w
        for f in t['fine']: v['f:' + f] += w
    return v
vecs = {l['id']: vec(l) for l in labs}
def cos(a, b):
    num_ = sum(a[k] * b[k] for k in a); den = math.sqrt(sum(x * x for x in a.values())) * math.sqrt(sum(x * x for x in b.values()))
    return num_ / den if den else 0
for l in labs:
    sims = sorted(((cos(vecs[l['id']], vecs[o['id']]), o['id']) for o in labs if o['id'] != l['id']), reverse=True)
    l['similar'] = [i for s, i in sims[:4] if s > 0.15]

ref = {}
for it in open('../ref_venues.txt').read().strip().split('; '):
    n, t = it.rsplit('|', 1); ref[n.strip()] = t.strip()
T1 = sorted(set(list(CONF_T1.values()) + list(JOUR_T1.values()))); T2 = sorted(set(list(CONF_T2.values()) + list(JOUR_T2.values())))
data = {'generated': '2026-11-19', 'dept': '전산학부', 'en': EN,
        'tree': [{'id': b, 'name': bn, 'desc': BIG_DESC.get(b, ''), 'mids': [{'id': m, 'name': mn, 'fine': f} for m, mn, f in mids]} for b, bn, mids in TREE],
        'labs': labs, 'corrections': [], 'tierRef': {'T1': [[v, v in ref] for v in T1], 'T2': [[v, v in ref] for v in T2]}}
json.dump(data, open('data.json', 'w'), ensure_ascii=False)
html = open('site/template.html').read().replace('__N__', str(len(labs))).replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
open('site/index.html', 'w').write(html)
art = '\n'.join(l for l in html.split('\n') if 'cdn.jsdelivr.net/gh/orioncactus' not in l).replace('<link rel="preconnect" href="https://cdn.jsdelivr.net">\n', '')
open('site/artifact.html', 'w').write(art)
print('ok', len(labs), len(html), sum(1 for l in labs if l['pubs']), sum(1 for l in labs if not l['tax']))
