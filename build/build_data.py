"""Build data.json for the site from collected raw files."""
import json, collections, sys, re, math
sys.path.insert(0, '.')
from labs_meta import LABS, PROF2LAB, DEPT, NO_PUBS_NEW
from tiers import classify, CONF_T1, CONF_T2, JOUR_T1, JOUR_T2
from taxonomy import TREE, ASSIGN, KW_RAW, KW_LABEL, DBLP_PID, EN, BIG_DESC

members = {}
for l in open('members.jsonl'):
    d = json.loads(l); members[d['id']] = d
corr = json.load(open('corrections.json'))

def venue_of(pre, flag):
    kind, sub = pre.split(':')
    key = ('conf/' if kind == 'c' else 'journals/') + sub + '/x'
    venue = sub + (' (Findings)' if flag == 'F' else ' Workshop' if flag == 'W' else '')
    res = classify(key, venue)
    if res is None:
        return None
    tier, label = res
    if flag == 'W':
        return 'W', sub.upper() + ' 워크숍·EA'
    return tier, label

# ---- per-year venue counts (with corrections) ----
rows = collections.Counter()
for item in open('dblp_year_agg.txt').read().strip().split(';'):
    prof, y, pre, flag, n = item.split('|')
    rows[(prof, int(y), pre, flag)] += int(n)
for prof, y, pre, flag, n, _why in corr['remove']:
    rows[(prof, y, pre, flag)] -= n
    assert rows[(prof, y, pre, flag)] >= 0, (prof, y, pre, flag)

lab_year = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
lab_venue = collections.defaultdict(collections.Counter)
for (prof, y, pre, flag), n in rows.items():
    if n <= 0:
        continue
    v = venue_of(pre, flag)
    if v is None:
        continue
    tier, label = v
    lab = PROF2LAB[prof]
    lab_year[lab][y][tier] += n
    lab_venue[lab][(tier, label)] += n

# ---- intern-authored counts (from earlier aggregate; corrections did not touch intern papers) ----
intern = collections.defaultdict(lambda: [0, 0])
for item in open('dblp_agg.txt').read().strip().split(';'):
    prof, pre, flag, cnt = item.split('|')
    n, c, p = map(int, cnt.split(','))
    intern[PROF2LAB[prof]][0] += c; intern[PROF2LAB[prof]][1] += p

# ---- recent papers ----
drop = set(corr['drop_keys'])
recent = collections.defaultdict(list)
for line in open('recent.tsv', encoding='utf-8'):
    line = line.rstrip('\n')
    if not line:
        continue
    prof, y, pre, flag, title, authors, iv, key = line.split('\t')
    if key in drop:
        continue
    v = venue_of(pre, flag)
    tier, label = v if v else ('기타', pre)
    lab = PROF2LAB[prof]
    if any(r['key'] == key for r in recent[lab]):
        continue
    recent[lab].append({'y': int(y), 'tier': tier, 'venue': label, 'title': title, 'authors': authors,
                        'interns': [x for x in iv.split('/') if x], 'key': key})

# ---- keyword hints ----
kw = {}
for line in KW_RAW.strip().split('\n'):
    prof, rest = line.split(':')
    items = []
    for tok in rest.split(','):
        m = re.match(r'([a-z0-9]+?)(\d+)$', tok)
        if m and int(m.group(2)) >= 2:
            items.append([KW_LABEL.get(m.group(1), m.group(1)), int(m.group(2))])
    kw.setdefault(PROF2LAB[prof], []).extend(items)

MID2BIG = {mid: big for big, _, mids in TREE for mid, _, _ in mids}
NO_PUBS = {'Hypermedia': 'dblp 동명이인 구분 불가', 'GI': 'dblp 동명이인 구분 불가', 'Physical': 'dblp에서 해당 교수 기록을 찾지 못함'}
NO_PUBS.update(NO_PUBS_NEW)
CRAWL = json.load(open('crawl.json'))

def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

labs = []
for (lid, pis, pis_en, name, short, url, _fields, focus) in LABS:
    m = members.get(lid, {})
    cur = m.get('interns_cur'); past = m.get('interns_past')
    pubs_ok = lid not in NO_PUBS
    years = {}
    tot = collections.Counter()
    for y in (2024, 2025, 2026):
        c = lab_year[lid][y]
        years[y] = {'T1': c['T1'], 'T2': c['T2'], 'W': c['W'], 'etc': c['기타']}
        tot.update(c)
    total = sum(tot.values())
    venues = sorted(lab_venue[lid].items(), key=lambda x: (-x[1], x[0][1]))
    assign = ASSIGN.get(lid, [])
    rec = {
        'id': lid, 'slug': slug(lid), 'depts': DEPT.get(lid, ['컴퓨터학과']), 'pis': pis, 'pisEn': pis_en, 'name': name, 'short': short, 'url': url, 'focus': focus,
        'tax': [{'big': MID2BIG[mid], 'mid': mid, 'fine': fine} for mid, fine in assign],
        'siteDead': bool(m.get('site_dead')),
        'members': None if m.get('site_dead') else {k: m.get(k) for k in ('phd', 'integ', 'ms', 'grad', 'postdoc', 'other')},
        'internsCur': max(len(cur) if cur is not None else 0, m.get('interns_cur_count') or 0) if (cur is not None or m.get('interns_cur_count')) else None,
        'internsPast': (m.get('interns_past_count') or len(past or [])) if m.get('past_listed') else None,
        'internCountOnly': bool(m.get('interns_cur_count')),
        'hp': CRAWL.get(lid),
        'pastListed': bool(m.get('past_listed')),
        'internNamesKoreanOnly': bool(cur) and all(not n.isascii() for n in cur),
        'memberSrc': m.get('src'), 'pubSrc': m.get('pubs'), 'note': m.get('note', ''),
        'dblp': [f'https://dblp.org/pid/{DBLP_PID[p]}.html' for p in pis if p in DBLP_PID and pubs_ok],
        'pubs': None if not pubs_ok else {
            'total': total, 'T1': tot['T1'], 'T2': tot['T2'], 'W': tot['W'], 'etc': tot['기타'],
            'years': years, 'internCalc': lid in intern, 'internCur': intern[lid][0], 'internPast': intern[lid][1],
            'venues': [[t, lbl, n] for (t, lbl), n in venues],
            'recent': sorted(recent[lid], key=lambda r: (0 if r['interns'] else 1, -r['y'])),
        },
        'keywords': kw.get(lid, [])[:8],
        'pubNote': NO_PUBS.get(lid, ''),
    }
    labs.append(rec)

ALUM = json.load(open('alumni.json'))
for l in labs:
    l['alumni'] = ALUM.get(l['id'])
# similarity: weighted overlap of fine/mid tags
def vec(l):
    v = collections.Counter()
    for i, t in enumerate(l['tax']):
        w = 1.0 if i == 0 else 0.7
        v['m:' + t['mid']] += w
        for f in t['fine']:
            v['f:' + f] += w
    return v
vecs = {l['id']: vec(l) for l in labs}
def cos(a, b):
    num = sum(a[k] * b[k] for k in a)
    den = math.sqrt(sum(x * x for x in a.values())) * math.sqrt(sum(x * x for x in b.values()))
    return num / den if den else 0
for l in labs:
    sims = sorted(((cos(vecs[l['id']], vecs[o['id']]), o['id']) for o in labs if o['id'] != l['id']), reverse=True)
    l['similar'] = [i for s, i in sims[:4] if s > 0.15]

data = {
    'generated': '2026-11-06', 'dept': '컴퓨터학과',
    'en': EN, 'tree': [{'id': b, 'name': bn, 'desc': BIG_DESC[b], 'mids': [{'id': m, 'name': mn, 'fine': f} for m, mn, f in mids]} for b, bn, mids in TREE],
    'labs': labs,
    'corrections': corr['remove'],
    'tierRef': {
        'T1': sorted(set(list(CONF_T1.values()) + list(JOUR_T1.values()))),
        'T2': sorted(set(list(CONF_T2.values()) + list(JOUR_T2.values()))),
    },
}
json.dump(data, open('data.json', 'w'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    for l in labs:
        p = l['pubs']
        print(f"{l['id']:10} {l['slug']:10} tax={[t['mid'] for t in l['tax']]} pubs={p and (p['total'], p['T1'], p['T2'], p['W'], p['etc'], len(p['recent']))} sim={l['similar']}")
