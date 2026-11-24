"""Venue tier classification for dblp records (key prefix + booktitle).

T1/T2 follow korea-ai-labs.vercel.app/venues where that list covers a venue.
Venues outside that list (security, systems, networking, SE/PL, extra arch/HCI)
are added under the same spirit: flagship venues of a field -> T1,
strong second-tier / letters / broad journals -> T2. Everything else -> 기타.
Workshops, Findings-as-T2, extended abstracts, domestic venues handled explicitly.
"""
import re

# ---- conferences (dblp key: conf/<x>/...) ----
CONF_T1 = {
    # from reference list
    'nips': 'NeurIPS', 'iclr': 'ICLR', 'icml': 'ICML', 'cvpr': 'CVPR', 'eccv': 'ECCV', 'iccv': 'ICCV',
    'mm': 'ACM MM', 'acl': 'ACL', 'emnlp': 'EMNLP', 'naacl': 'NAACL', 'aaai': 'AAAI', 'ijcai': 'IJCAI',
    'miccai': 'MICCAI', 'hpca': 'HPCA', 'micro': 'MICRO', 'isca': 'ISCA', 'asplos': 'ASPLOS', 'dac': 'DAC',
    'kdd': 'KDD', 'cikm': 'CIKM', 'www': 'WWW', 'sigir': 'SIGIR', 'sigmod': 'SIGMOD', 'vldb': 'VLDB',
    'icra': 'ICRA', 'iros': 'IROS', 'corl': 'CoRL', 'rss': 'RSS', 'icassp': 'ICASSP', 'interspeech': 'INTERSPEECH',
    'chi': 'CHI', 'uist': 'UIST', 'cscw': 'CSCW', 'siggraph': 'SIGGRAPH', 'siggrapha': 'SIGGRAPH Asia',
    'colt': 'COLT', 'atal': 'AAMAS', 'icde': 'ICDE', 'wsdm': 'WSDM', 'icdm': 'ICDM', 'isscc': 'ISSCC',
    'iccad': 'ICCAD', 'vlsic': 'VLSI Symposium', 'vlsit': 'VLSI Symposium', 'mobisys': 'MobiSys',
    'infocom': 'INFOCOM', 'eurosys': 'EuroSys', 'mobicom': 'MobiCom', 'ics': 'ICS', 'usenix': 'USENIX ATC',
    'huc': 'UbiComp',
    # added (outside reference list)
    'sp': 'IEEE S&P', 'ccs': 'CCS', 'uss': 'USENIX Security', 'ndss': 'NDSS',
    'osdi': 'OSDI', 'sosp': 'SOSP', 'nsdi': 'NSDI', 'fast': 'FAST', 'sc': 'SC', 'ppopp': 'PPoPP',
    'sigcomm': 'SIGCOMM', 'sensys': 'SenSys',
    'icse': 'ICSE', 'sigsoft': 'FSE', 'kbse': 'ASE', 'issta': 'ISSTA', 'pldi': 'PLDI', 'popl': 'POPL',
    'vr': 'IEEE VR', 'ismar': 'ISMAR', 'ifaamas': 'AAMAS', 'mlsys': 'MLSys', 'sigmetrics': 'SIGMETRICS',
    'visualization': 'IEEE VIS',
    # added for KAIST (theory, crypto, PL/verification, more systems)
    'stoc': 'STOC', 'focs': 'FOCS', 'soda': 'SODA', 'crypto': 'CRYPTO', 'eurocrypt': 'EUROCRYPT',
    'cav': 'CAV', 'lics': 'LICS', 'oopsla': 'OOPSLA', 'imc': 'IMC', 'eurographics': 'Eurographics',
    'iclr2': 'ICLR', 'hpdc2': 'HPDC',
}
CONF_T2 = {
    'cdc': 'IEEE CDC', 'amcc': 'ACC', 'asscc': 'A-SSCC',
    'aistats': 'AISTATS', 'uai': 'UAI', 'wacv': 'WACV', 'icip': 'ICIP', 'colm': 'COLM', 'date': 'DATE',
    'pakdd': 'PAKDD', 'ismir': 'ISMIR', 'iui': 'IUI', 'apvis': 'PacificVis', 'bmvc': 'BMVC', 'accv': 'ACCV',
    'icpr': 'ICPR', '3dim': '3DV', 'eacl': 'EACL', 'coling': 'COLING', 'lrec': 'LREC', 'ijcnlp': 'IJCNLP-AACL',
    'sac': 'ACM SAC', 'icc': 'IEEE ICC', 'ecai': 'ECAI', 'pkdd': 'ECML-PKDD', 'smc': 'IEEE SMC',
    'bigcomp': 'BigComp', 'isbi': 'ISBI', 'embc': 'EMBC', 'chil': 'CHIL', 'ACMdis': 'DIS', 'assets': 'ASSETS',
    'fat': 'FAccT', 'emsoft': 'EMSOFT', 'IEEEpact': 'PACT', 'cicc': 'CICC', 'esscirc': 'ESSERC',
    'bigdataconf': 'IEEE BigData', 'collas': 'CoLLAs', 'pg': 'Pacific Graphics',
    # added
    'ecir': 'ECIR', 'recsys': 'RecSys', 'edbt': 'EDBT', 'dasfaa': 'DASFAA',
    'dsn': 'DSN', 'raid': 'RAID', 'acsac': 'ACSAC', 'ccs-asia': 'AsiaCCS', 'asiaccs': 'AsiaCCS',
    'esorics': 'ESORICS', 'eurosp': 'EuroS&P', 'middleware': 'Middleware', 'cloud': 'SoCC',
    'IEEEcloud': 'IEEE CLOUD', 'ipps': 'IPDPS', 'icdcs': 'ICDCS', 'hpdc': 'HPDC', 'icpp': 'ICPP',
    'iiswc': 'IISWC', 'iccd': 'ICCD', 'islped': 'ISLPED', 'cgo': 'CGO', 'cc': 'CC', 'ecoop': 'ECOOP',
    'icsm': 'ICSME', 'wcre': 'SANER', 'msr': 'MSR', 'icst': 'ICST', 'esem': 'ESEM', 'issre': 'ISSRE',
    'globecom': 'GLOBECOM', 'mobihoc': 'MobiHoc', 'conext': 'CoNEXT', 'wcnc': 'WCNC', 'ipsn': 'IPSN',
    'icnp': 'ICNP', 'vrst': 'VRST', 'mhci': 'MobileHCI', 'codes': 'CODES+ISSS', 'cases': 'CASES',
    'aspdac': 'ASP-DAC', 'rtss': 'RTSS', 'rtas': 'RTAS', 'haptics': 'IEEE Haptics', 'whc': 'World Haptics',
    'icbc2': 'IEEE ICBC', 'icbc': 'IEEE ICBC', 'kr': 'KR', 'aied': 'AIED', 'edm': 'EDM', 'lak': 'LAK',
    'ispass': 'ISPASS', 'europar': 'Euro-Par', 'secon': 'IEEE SECON', 'ccgrid': 'CCGrid', 'sas': 'SAS',
    'dyspan': 'IEEE DySPAN', 'bibm': 'IEEE BIBM', 'icwsm': 'ICWSM', 'lctrts': 'LCTES',
    # added for KAIST
    'icalp': 'ICALP', 'esa': 'ESA', 'stacs': 'STACS', 'compgeom': 'SoCG', 'ipco': 'IPCO', 'approx': 'APPROX/RANDOM',
    'innovations': 'ITCS', 'coco': 'CCC', 'asiacrypt': 'ASIACRYPT', 'tcc': 'TCC', 'pkc': 'PKC', 'ches': 'CHES',
    'fse': 'FSE (Crypto)', 'qcrypt': 'QCrypt', 'tqc': 'TQC', 'concur': 'CONCUR', 'tacas': 'TACAS', 'csl': 'CSL',
    'mfcs': 'MFCS', 'iwpec': 'IPEC', 'isaac': 'ISAAC', 'wg': 'WG', 'sgp': 'SGP', 'i3d': 'I3D', 'sca': 'SCA',
    'ec': 'ACM EC', 'wine': 'WINE', 'isit': 'IEEE ISIT', 'hri': 'HRI', 'cogsci': 'CogSci', 'conll': 'CoNLL',
    'aistats2': 'AISTATS', 'eurosec': 'EuroSec', 'woot': 'WOOT', 'fpga': 'FPGA', 'fccm': 'FCCM', 'hotchips': 'Hot Chips',
    'socc': 'SoCC', 'apsys': 'APSys', 'systor': 'SYSTOR', 'eics': 'EICS', 'tei': 'TEI', 'iswc': 'ISWC', 'icmi': 'ICMI',
    'cogsima': 'CogSIMA', 'l4s': 'L@S', 'ijcb': 'IJCB', 'fg': 'IEEE FG', 'aaai2': 'AAAI',
}
# ---- journals (dblp key: journals/<x>/...) ----
JOUR_T1 = {
    'automatica': 'Automatica', 'tac': 'IEEE TAC', 'scirobotics': 'Science Robotics',
    'tmlr': 'TMLR', 'tnn': 'IEEE TNNLS', 'pami': 'TPAMI', 'mia': 'Medical Image Analysis', 'jssc': 'JSSC',
    'tvcg': 'IEEE TVCG', 'ijrr': 'IJRR', 'trob': 'IEEE T-RO', 'ijcv': 'IJCV', 'tip': 'IEEE TIP',
    'tkde': 'IEEE TKDE', 'tmc': 'IEEE TMC', 'tc': 'IEEE Trans. Computers', 'tmi': 'IEEE TMI',
    'jmlr': 'JMLR', 'tacl': 'TACL', 'ncomms': 'Nature Communications', 'natcomm': 'Nature Communications',
    'sciadv': 'Science Advances', 'tcyb': 'IEEE TCYB', 'tit': 'IEEE Trans. Inf. Theory', 'pvldb': 'VLDB',
    'pacmmod': 'SIGMOD', 'imwut': 'IMWUT', 'pacmhci': 'CSCW', 'tog': 'ACM TOG (SIGGRAPH)',
    # added
    'pacmpl': 'PLDI/POPL/OOPSLA', 'pacmse': 'FSE', 'tse': 'IEEE TSE', 'tosem': 'ACM TOSEM',
    'tpds': 'IEEE TPDS', 'jsac': 'IEEE JSAC', 'ton': 'IEEE/ACM ToN', 'twc': 'IEEE TWC', 'tcom': 'IEEE TCOM',
    'tcad': 'IEEE TCAD', 'tochi': 'ACM TOCHI', 'vldb': 'VLDB Journal', 'pomacs': 'SIGMETRICS (POMACS)',
    'comsur': 'IEEE COMST', 'csur': 'ACM Computing Surveys', 'npjdm': 'npj Digital Medicine',
    'tie': 'IEEE TIE', 'tsg': 'IEEE Trans. Smart Grid',
    # added for KAIST
    'jacm': 'J. ACM', 'siamcomp': 'SIAM J. Comput.', 'joc': 'J. Cryptology', 'nature': 'Nature', 'science': 'Science',
    'natmi': 'Nature Machine Intelligence', 'pnas': 'PNAS', 'cell': 'Cell', 'nar': 'Nucleic Acids Research',
    'tcas': 'TCAS', 'toplas': 'ACM TOPLAS', 'tissec': 'ACM TOPS',
}
JOUR_T2 = {
    'tcst': 'IEEE TCST', 'tii': 'IEEE TII', 'tbcas': 'IEEE TBioCAS', 'wcl': 'IEEE WCL', 'lssc': 'IEEE SSC-L',
    'nn': 'Neural Networks', 'pr': 'Pattern Recognition', 'access': 'IEEE Access', 'srep': 'Scientific Reports',
    'eswa': 'ESWA', 'plosone': 'PLOS ONE', 'cal': 'IEEE CAL', 'kbs': 'Knowledge-Based Systems',
    'ral': 'IEEE RA-L', 'tits': 'IEEE T-ITS', 'taslp': 'IEEE TASLP', 'spl': 'IEEE SPL', 'ijon': 'Neurocomputing',
    'ml': 'Machine Learning', 'tsmc': 'IEEE TSMC', 'tifs': 'IEEE TIFS', 'prl': 'Pattern Recognition Letters',
    'tmm': 'IEEE TMM', 'ivc': 'Image and Vision Computing', 'cviu': 'CVIU', 'isci': 'Information Sciences',
    'inffus': 'Information Fusion', 'eaai': 'EAAI', 'asc': 'Applied Soft Computing', 'sensors': 'Sensors',
    'electronics': 'Electronics', 'titb': 'IEEE JBHI', 'tnsre': 'IEEE TNSRE', 'cbm': 'Comput. Biol. Med.',
    'bioinformatics': 'Bioinformatics', 'bib': 'Briefings in Bioinformatics', 'artmed': 'AI in Medicine',
    'iotj': 'IEEE IoT Journal', 'tvlsi': 'IEEE TVLSI', 'tcasI': 'TCAS-I', 'tecs': 'ACM TECS', 'micro': 'IEEE Micro',
    'cluster': 'Cluster Computing', 'kais': 'KAIS', 'tkdd': 'ACM TKDD', 'tist': 'ACM TIST', 'datamine': 'DMKD',
    'tase': 'IEEE TASE', 'scidata': 'Scientific Data', 'advsci': 'Advanced Science',
    'neuroimage': 'NeuroImage', 'jcheminf': 'J. Cheminformatics', 'jmir': 'JMIR', 'tetc': 'IEEE TETC',
    # added
    'taco': 'ACM TACO', 'tdsc': 'IEEE TDSC', 'compsec': 'Computers & Security', 'tvt': 'IEEE TVT',
    'icl': 'IEEE Commun. Letters', 'network': 'IEEE Network', 'cgf': 'Computer Graphics Forum',
    'ijmms': 'IJHCS', 'toh': 'IEEE Trans. Haptics', 'ese': 'Empirical SE', 'jss': 'J. Syst. Softw.',
    'infsof': 'IST', 'tnsm': 'IEEE TNSM', 'comcom': 'Computer Communications', 'cn': 'Computer Networks',
    'popets': 'PoPETs', 'tcc': 'IEEE TCC', 'fgcs': 'FGCS', 'jpdc': 'JPDC', 'tops': 'ACM TOPS',
    'tiot': 'ACM TIOT', 'tomccap': 'ACM TOMM', 'cee': 'Comput. Electr. Eng.',
    'tsc': 'IEEE TSC', 'cm': 'IEEE Commun. Mag.', 'taes': 'IEEE TAES', 'wcl': 'IEEE WCL', 'tnse': 'IEEE TNSE',
    'tos': 'ACM TOS', 'ploscb': 'PLOS Comput. Biol.', 'jcisd': 'JCIM', 'aiedu': 'IJAIED', 'tors': 'ACM TORS',
    'ijhci': 'IJHCI', 'cvm': 'Computational Visual Media', 'cacm': 'Commun. ACM', 'tci': 'IEEE TCI',
    'thms': 'IEEE THMS', 'jbi': 'J. Biomed. Inform.',
    # added for KAIST
    'algorithmica': 'Algorithmica', 'talg': 'ACM TALG', 'jcss': 'JCSS', 'siamdm': 'SIAM J. Discrete Math.',
    'jgt': 'J. Graph Theory', 'jct': 'JCTB', 'combinatorica': 'Combinatorica', 'dcc': 'Des. Codes Cryptogr.',
    'tosc': 'ToSC', 'tches': 'TCHES', 'lmcs': 'LMCS', 'tocl': 'ACM TOCL', 'cad': 'Computer-Aided Design',
    'jsac2': 'IEEE JSAC', 'tsp': 'IEEE TSP', 'jstsp': 'IEEE JSTSP', 'tbme': 'IEEE TBME', 'tcsvt': 'IEEE TCSVT',
    'mlst': 'Mach. Learn. Sci. Technol.', 'patterns': 'Patterns', 'bmcbi': 'BMC Bioinformatics',
}


def classify(key, venue, title=''):
    """Return (tier, label) or None to skip (preprint / non-paper)."""
    if not key:
        return None
    parts = key.split('/')
    kind, sub = parts[0], parts[1] if len(parts) > 1 else ''
    if kind not in ('conf', 'journals'):
        return None
    if sub in ('corr', 'iacr'):
        return None  # arXiv preprints are not counted
    v = venue or ''
    if re.search(r'workshop|\(Workshops?\)|Companion|Extended Abstracts|Adjunct|Demo|Poster|Doctoral|Student Research', v, re.I):
        return ('기타', v.split('(')[0].strip() + ' (workshop/EA)')
    findings = 'Findings' in v
    if kind == 'conf':
        if findings and sub in ('acl', 'emnlp', 'naacl', 'eacl', 'ijcnlp', 'cvpr'):
            return ('T2', CONF_T1.get(sub, CONF_T2.get(sub, sub.upper())) + ' Findings')
        if sub in CONF_T1:
            return ('T1', CONF_T1[sub])
        if sub in CONF_T2:
            return ('T2', CONF_T2[sub])
        return ('기타', v.split('(')[0].strip() or sub)
    else:
        if sub in JOUR_T1:
            return ('T1', JOUR_T1[sub])
        if sub in JOUR_T2:
            return ('T2', JOUR_T2[sub])
        return ('기타', v or sub)
