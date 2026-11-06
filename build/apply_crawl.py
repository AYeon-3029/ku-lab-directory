# crawl_raw.txt (연구실 홈페이지 2차 크롤링) -> crawl.json, members.jsonl 보정
import json, re
from tiers import CONF_T1, CONF_T2, JOUR_T1, JOUR_T2

ALIAS = {'T-RO': 'trob', 'TPAMI': 'pami', 'TVLSI': 'tvlsi', 'JSSC': 'jssc', 'TMC': 'tmc', 'TNSRE': None,
         'TII': 'tii', 'TCAS': 'tcasI', 'TOCS': 'tocs', 'TCOM': 'tcom', 'TCOMM': 'tcom', 'TVT': 'tvt', 'RA-L': 'ral', 'MICCAI': 'miccai', 'VIS': 'vis', 'TVCG': 'tvcg', 'ToN': 'ton',
         'TNSM': 'tnsm', 'TOSEM': 'tosem', 'TIP': 'tip', 'TASLP': 'taslp', 'IJRR': 'ijrr', 'JFR': 'jfr',
         'CAL': 'cal', 'TMLR': 'tmlr', 'TBME': 'tbme', 'ToH': 'toh', 'ECML-PKDD': 'pkdd', 'INTERSPEECH': 'interspeech',
         'WHC': 'haptics'}

def tier(tok):
    k = ALIAS.get(tok, tok.lower())
    if not k: return None
    for d, t in ((CONF_T1, 'T1'), (JOUR_T1, 'T1'), (CONF_T2, 'T2'), (JOUR_T2, 'T2')):
        if k in d: return t
    return None

# 수동 확인/보정 (구성원 페이지 직접 확인 또는 자동 집계 판독)
MAN = {
 'MINT': dict(phd=1, integ=15, ms=11, postdoc=2, U=5, past=1),
 'IDEA': dict(U=11), 'AIM': dict(U=2),
 'PIXEL': dict(U=1), 'AILAB': dict(U=3), 'ICQ': dict(phd=1, integ=2, ms=7, U=2), 'DeepIP': dict(U=5),
 'SigLearn': dict(phd=2, ms=3, postdoc=1, U=1), 'SMR': dict(phd=8, ms=6), 'PELab': dict(integ=12, ms=10, U=7),
 'CDAL': dict(U=1), 'CSL': dict(phd=4, ms=3, U=7), 'MNC': dict(phd=11, ms=7, postdoc=1, U=8),
 'ShinLab': dict(phd=4, integ=2, postdoc=2, U=6), 'POL': dict(integ=5), 'DCLab': dict(U=2),
 'Kilby': dict(U=6), 'AI-Yook': dict(U=0), 'BASIC': dict(U=0), 'BIRC': dict(U=0), 'MAILab': dict(U=0),  # 이름 2줄 표기로 2배 집계 → 절반
}
SUSPECT_GRAD = {'Kilby', 'MAILab', 'SLPL', 'CCS', 'uGrid', 'HSISL'}  # 자동 집계 이상치: 대학원생 수 미반영

rows = {}
for line in open('crawl_raw.txt', encoding='utf-8'):
    p = line.rstrip('\n').split('\t')
    if len(p) < 2: continue
    lid = p[0]; f = dict(x.split('=', 1) for x in p[1:] if '=' in x)
    F = f.get('F', '')
    m = re.search(r'P(\d+) I(\d+) M(\d+) D(\d+) U(\d+)', F)
    K = dict(zip('PIMDU', map(int, m.groups()))) if m else None
    n = f.get('n', '0'); n = int(n) if n.isdigit() else 0
    yc = {}
    for x in filter(None, f.get('yc', '').split(',')):
        y, c = x.split(':'); yc['20' + y] = int(c)
    ven = []
    for x in filter(None, f.get('tk', '').split(',')):
        t, _, c = x.rpartition(':')
        if c.isdigit(): ven.append((t, int(c)))
    t1 = min(n, sum(c for t, c in ven if tier(t) == 'T1'))
    t2 = min(n - t1, sum(c for t, c in ven if tier(t) == 'T2'))
    w = f.get('w', '0'); w = int(w) if w.isdigit() else 0
    rows[lid] = dict(K=K, n=n, yc=yc, w=w, t1=t1, t2=t2, venues=[t for t, c in ven if len(t) <= 14][:8])

crawl = {k: {'n': v['n'], 'years': v['yc'], 'T1': v['t1'], 'T2': v['t2'], 'W': v['w'], 'venues': v['venues']}
         for k, v in rows.items() if v['n'] >= 3}
json.dump(crawl, open('crawl.json', 'w'), ensure_ascii=False, indent=0)

labs = {l['id']: l for l in json.load(open('data.json'))['labs']}
mem = {}
for l in open('members.jsonl', encoding='utf-8'):
    d = json.loads(l); mem[d['id']] = d
changed = []
for lid, v in rows.items():
    if lid not in labs: continue
    d = mem.get(lid) or {'id': lid, 'phd': None, 'integ': None, 'ms': None, 'postdoc': None, 'other': None,
                         'interns_cur': None, 'interns_past': [], 'past_listed': False, 'src': labs[lid]['url'],
                         'pubs': '', 'note': ''}
    man = MAN.get(lid, {})
    K = v['K']
    U = man.get('U', K['U'] if K else 0)
    # 대학원생 수: 기존 값 없을 때만 자동 집계(이상치 제외) 또는 수동 값 사용
    for key, kk in (('phd', 'P'), ('integ', 'I'), ('ms', 'M'), ('postdoc', 'D')):
        if key in man: d[key] = man[key]
        elif d.get(key) is None and K and sum(K[c] for c in 'PIM') > 0 and lid not in SUSPECT_GRAD:
            d[key] = K[kk]
    cur = d.get('interns_cur')
    curn = len(cur) if isinstance(cur, list) else None
    if U and (curn is None or ('U' in man and U > curn)):
        d['interns_cur_count'] = U
        changed.append((lid, curn, U))
    elif K is not None and curn is None and d.get('src') is None:
        d['src'] = labs[lid]['url']
    if man.get('U')==0 and lid in ('BIRC',) and d.get('interns_cur') is None:
        d['interns_cur']=[]
    if 'past' in man and not d.get('interns_past'):
        d['interns_past_count'] = man['past']; d['past_listed'] = True
    if not d.get('src'): d['src'] = labs[lid]['url']
    d['crawl2'] = True
    mem[lid] = d
open('members.jsonl', 'w', encoding='utf-8').write('\n'.join(json.dumps(x, ensure_ascii=False) for x in mem.values()) + '\n')
print('crawl pubs', len(crawl), 'intern updates', len(changed))
print(changed)
