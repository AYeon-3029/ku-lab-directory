import json
ref = {}
for it in open('ref_venues.txt').read().strip().split('; '):
    n, t = it.rsplit('|', 1); ref[n.strip()] = t.strip()
alias = {'INFOCOM': 'IEEE INFOCOM', 'IEEE VIS': 'VIS', 'IEEE CAL': 'IEEE Computer Architecture Letters',
         'Comput. Biol. Med.': 'Computers in Biology and Medicine', 'AI in Medicine': 'Artificial Intelligence in Medicine',
         'CVIU': 'Computer Vision and Image Understanding', 'ESWA': 'Expert Systems with Applications',
         'EAAI': 'Engineering Applications of Artificial Intelligence', 'KAIS': 'Knowledge and Information Systems',
         'DMKD': 'Data Mining and Knowledge Discovery', 'ACM TECS': 'ACM Transactions on Embedded Computing Systems',
         'IEEE Trans. Inf. Theory': 'IEEE Transactions on Information Theory', 'IEEE Trans. Computers': 'IEEE Transactions on Computers',
         'ACM TOG (SIGGRAPH)': 'SIGGRAPH', 'IEEE ICC': 'IEEE ICC', 'IEEE SMC': 'IEEE SMC', 'Medical Image Analysis': 'Medical Image Analysis'}
def isref(l):
    return l in ref or alias.get(l) in ref
d = json.load(open('data.json'))
d['tierRef'] = {t: [[v, isref(v)] for v in d['tierRef'][t]] for t in ('T1', 'T2')}
json.dump(d, open('data.json', 'w'), ensure_ascii=False)
html = open('site/template.html').read().replace('__DATA__', json.dumps(d, ensure_ascii=False).replace('</', '<\\/'))
open('site/index.html', 'w').write(html)
print('ok', len(html))
art = html.replace('<link rel="preconnect" href="https://cdn.jsdelivr.net">\n', '')
art = '\n'.join(l for l in art.split('\n') if 'cdn.jsdelivr.net/gh/orioncactus' not in l)
open('site/artifact.html', 'w').write(art)
