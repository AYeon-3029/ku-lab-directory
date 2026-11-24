"""KAIST taxonomy: KU tree + theory, social computing, AI-convergence groups."""
import sys, copy
sys.path.insert(0, '..')
from taxonomy import TREE as _KT, EN as _KEN, BIG_DESC as _KBD

TREE = copy.deepcopy(_KT)
B = {b: mids for b, _, mids in TREE}
def addfine(big, mid, items):
    for i, (m, n, f) in enumerate(B[big]):
        if m == mid:
            B[big][i] = (m, n, f + [x for x in items if x not in f])
addfine('ai', 'ml', ['최적화·딥러닝 이론', '설명가능 AI(XAI)', '분자·과학 ML'])
addfine('ai', 'nlp', ['LLM 에이전트', '전산언어학'])
addfine('ai', 'cv', ['계산 사진학·이미징', '3D 생성·기하 처리'])
addfine('sys', 'arch', ['보안 하드웨어', '칩렛·3D 패키징'])
addfine('sys', 'ossys', ['네트워크 시스템'])
addfine('sys', 'db', ['GPU 그래프 처리'])
addfine('sec', 'syssec', ['블록체인·네트워크 보안', '웹·브라우저 보안'])
addfine('sw', 'pa', ['바이너리 분석·디컴파일'])
addfine('sw', 'pl', ['WebAssembly·Rust', '프로그램 검증'])
addfine('hci', 'ux', ['인터랙션 기법·장치'])
B['hci'].append(('social', '소셜·인간중심 컴퓨팅', ['인간-AI 상호작용', '온라인 커뮤니티·모더레이션', '전산사회과학', '디지털 헬스·모바일 센싱', '교육·크라우드소싱']))
TREE.insert(5, ('theory', '전산이론', [
    ('algo', '알고리즘·그래프 이론', ['매개변수 복잡도', '구조적 그래프 이론', '계산 복잡도', '계산기하학', '실수 연산 이론']),
    ('tcrypt', '암호 이론·양자', ['양자 암호·양자 계산', '대칭키·증명가능 보안', '격자·동형암호']),
]))
TREE.append(('axf', 'AI 융합·미래', [
    ('sci', 'AI for Science·Engineering', ['물리 기반 AI', '설계 최적화·디지털 트윈', '시스템 생물학', '기후·지구 시스템', '수송·동력 시스템']),
    ('policy', 'AI 사회·정책', ['AI 거버넌스·안전', '법·금융·핀테크', '도시 데이터 분석', '경영·정보시스템', '확률적 예측']),
]))
TREE = [(b, n, B.get(b, mids)) for b, n, mids in TREE]

EN = dict(_KEN)
EN.update({'최적화·딥러닝 이론': 'Optimization Deep Learning Theory', '설명가능 AI(XAI)': 'Explainable AI XAI Interpretability',
    '분자·과학 ML': 'Molecular ML AI for Science', 'LLM 에이전트': 'LLM Agents', '전산언어학': 'Computational Linguistics',
    '계산 사진학·이미징': 'Computational Photography Imaging', '3D 생성·기하 처리': '3D Generation Geometry Processing',
    '보안 하드웨어': 'Secure Hardware', '칩렛·3D 패키징': 'Chiplet 3D IC Packaging', '네트워크 시스템': 'Networked Systems RDMA SmartNIC',
    'GPU 그래프 처리': 'GPU Graph Query Processing', '블록체인·네트워크 보안': 'Blockchain Network Security', '웹·브라우저 보안': 'Web Browser Security',
    '바이너리 분석·디컴파일': 'Binary Analysis Decompilation', 'WebAssembly·Rust': 'WebAssembly Rust', '프로그램 검증': 'Program Verification Formal Methods',
    '인터랙션 기법·장치': 'Interaction Techniques Devices', '인간-AI 상호작용': 'Human-AI Interaction', '온라인 커뮤니티·모더레이션': 'Online Communities Moderation',
    '전산사회과학': 'Computational Social Science', '디지털 헬스·모바일 센싱': 'Digital Health Mobile Sensing', '교육·크라우드소싱': 'Education Crowdsourcing Learning at Scale',
    '매개변수 복잡도': 'Parameterized Complexity', '구조적 그래프 이론': 'Structural Graph Theory Graph Minors', '계산 복잡도': 'Computational Complexity',
    '계산기하학': 'Computational Geometry', '실수 연산 이론': 'Real Computation Computable Analysis', '양자 암호·양자 계산': 'Quantum Cryptography Quantum Computing',
    '대칭키·증명가능 보안': 'Symmetric-key Provable Security', '격자·동형암호': 'Lattice Homomorphic Encryption FHE',
    '물리 기반 AI': 'Physics-Informed AI Scientific ML', '설계 최적화·디지털 트윈': 'Design Optimization Digital Twin', '시스템 생물학': 'Systems Biology',
    '기후·지구 시스템': 'Climate Earth System', '수송·동력 시스템': 'Transport Power Engines', 'AI 거버넌스·안전': 'AI Governance Safety Policy',
    '법·금융·핀테크': 'Law Finance FinTech IP', '도시 데이터 분석': 'Urban Analytics', '경영·정보시스템': 'Information Systems Business', '확률적 예측': 'Probabilistic Forecasting'})
BIG_DESC = dict(_KBD)
BIG_DESC.update({'theory': '알고리즘, 그래프 이론, 계산 복잡도, 암호 이론, 양자',
                 'axf': 'AI for Science·Engineering, AI 정책·법·경영',
                 'hci': '그래픽스, VR/AR, 햅틱, 시각화, HCI, 소셜 컴퓨팅'})

ASSIGN = {
 'NetSP': [('syssec', ['블록체인·네트워크 보안', '프로토콜·IoT 보안']), ('crypto', ['블록체인·스마트 컨트랙트'])],
 'CySec': [('syssec', ['하드웨어·사이드채널', '보안 하드웨어']), ('aisec', ['적대적 공격·방어']), ('embed', ['실시간 시스템'])],
 'WebEng': [('edge', ['엣지 컴퓨팅·오프로딩']), ('debug', ['결함 위치 추정']), ('dm', ['시계열·데이터 스트림'])],
 'CASYS-Kwon': [('ossys', ['운영체제·가상화', '스토리지', '네트워크 시스템']), ('syssec', ['하드웨어·사이드채널'])],
 'LDIS': [('db', ['DB 엔진·인덱싱', 'GPU 그래프 처리']), ('aisys', ['LLM 서빙·추론 최적화'])],
 'DEAL': [('cv', ['영상 복원·역문제']), ('app', ['의료·바이오 AI']), ('mm', ['비전-언어 모델(VLM)']), ('wireless', ['5G/6G·AI-RAN'])],
 'SWTV': [('debug', ['테스트 생성·퍼징']), ('pa', ['정적 분석'])],
 'InfoLab': [('db', ['GPU 그래프 처리', 'DB 엔진·인덱싱']), ('ml', ['그래프 학습'])],
 'VCLab': [('cv', ['계산 사진학·이미징', '3D 장면·Gaussian Splatting']), ('gfx', ['렌더링'])],
 'ECL': [('arch', ['AI 가속기·NPU', '열·전력 관리']), ('embed', ['실시간 시스템'])],
 'Simplexity': [('algo', ['매개변수 복잡도', '구조적 그래프 이론', '계산 복잡도'])],
 'KIXLab': [('social', ['인간-AI 상호작용', '교육·크라우드소싱']), ('ux', ['사용자 연구']), ('nlp', ['LLM'])],
 'CVML-TK': [('cv', ['3D 인체·아바타', '자율주행 인지']), ('robot', ['로봇 조작'])],
 'DICE': [('vis', ['과학·의료 시각화']), ('ux', ['사용자 연구'])],
 'MLV': [('mm', ['비전-언어 모델(VLM)']), ('cv', ['비디오 이해', '3D 장면·Gaussian Splatting']), ('ml', ['그래프 학습', '효율적 학습·경량화'])],
 'PLRG': [('pl', ['JavaScript·언어 명세', 'WebAssembly·Rust']), ('debug', ['테스트 생성·퍼징']), ('pa', ['정적 분석'])],
 'AN': [('ossys', ['네트워크 시스템']), ('edge', ['데이터센터 네트워크']), ('social', ['전산사회과학'])],
 'BigDyL': [('ml', ['그래프 학습', '학습 이론·확률 모델']), ('dm', ['추천 시스템', '시계열·데이터 스트림'])],
 'RIRO': [('robot', ['로봇 조작', '로봇 학습·휴머노이드']), ('mm', ['비전-언어-행동(VLA)'])],
 'CASYS-Park': [('arch', ['AI 가속기·NPU', 'PIM·메모리 시스템']), ('aisys', ['LLM 서빙·추론 최적화'])],
 'NLPCL': [('nlp', ['검색 증강 생성(RAG)', 'LLM 안전성·정렬', '전산언어학']), ('app', ['바이오NLP'])],
 'CGV': [('app', ['의료·바이오 AI']), ('gfx', ['물리 시뮬레이션']), ('haptic', ['햅틱 인터페이스']), ('vis', ['과학·의료 시각화'])],
 'SPIRAL': [('debug', ['결함 위치 추정']), ('llm4se', ['LLM 신뢰성 평가']), ('edge', ['엣지 컴퓨팅·오프로딩'])],
 'VisualAI': [('cv', ['3D 생성·기하 처리', '영상 생성·편집']), ('ml', ['생성 모델'])],
 'WSP': [('syssec', ['웹·브라우저 보안']), ('aisec', ['LLM 프라이버시', '적대적 공격·방어']), ('swsec', ['퍼징'])],
 'NCLab': [('social', ['디지털 헬스·모바일 센싱', '교육·크라우드소싱']), ('embed', ['모바일 시스템'])],
 'CST': [('social', ['온라인 커뮤니티·모더레이션', '인간-AI 상호작용'])],
 'CPS': [('embed', ['모바일 시스템', '실시간 시스템']), ('nlp', ['LLM 에이전트']), ('ossys', ['운영체제·가상화'])],
 'MLML': [('rl', ['월드 모델', '강화학습']), ('ml', ['생성 모델']), ('nlp', ['추론'])],
 'AMI': [('cv', ['3D 인체·아바타', '3D 장면·Gaussian Splatting', '비디오 이해']), ('mm', ['오디오-비주얼'])],
 'UILab': [('nlp', ['LLM', 'LLM 안전성·정렬']), ('social', ['전산사회과학', '교육·크라우드소싱'])],
 'Wiederrecht': [('algo', ['구조적 그래프 이론', '매개변수 복잡도'])],
 'COINSE': [('debug', ['결함 위치 추정', '자동 수정', '테스트 생성·퍼징']), ('llm4se', ['LLM 신뢰성 평가'])],
 'SGLab': [('cv', ['3D 장면·Gaussian Splatting']), ('robot', ['임바디드 에이전트']), ('gfx', ['렌더링'])],
 'HCIL': [('ux', ['인터랙션 기법·장치']), ('xr', ['VR 인터랙션']), ('haptic', ['진동촉각'])],
 'ICLab': [('social', ['디지털 헬스·모바일 센싱', '인간-AI 상호작용']), ('ux', ['사용자 연구'])],
 'DMLab': [('dm', ['시계열·데이터 스트림']), ('ml', ['신뢰성·강건성']), ('aisys', ['온디바이스 AI'])],
 'CryptLab': [('tcrypt', ['대칭키·증명가능 보안', '격자·동형암호']), ('crypto', ['응용 암호', '영지식 증명'])],
 'NMAIL': [('brain', ['뇌-컴퓨터 인터페이스(BCI)']), ('robot', ['로봇 학습·휴머노이드']), ('ml', ['신뢰성·강건성'])],
 'Ziegler': [('algo', ['실수 연산 이론', '계산 복잡도'])],
 'DSLab': [('social', ['전산사회과학']), ('nlp', ['LLM 안전성·정렬']), ('app', ['AI for Science'])],
 'SoftSec': [('swsec', ['바이너리 분석', '퍼징']), ('pa', ['바이너리 분석·디컴파일'])],
 'GCLab': [('algo', ['계산기하학']), ('gfx', ['렌더링'])],
 'ISILab': [('app', ['센서·행동 인식(HAR)']), ('embed', ['모바일 시스템'])],
 'QCrypto': [('tcrypt', ['양자 암호·양자 계산', '격자·동형암호']), ('algo', ['계산 복잡도'])],
 'CyPhy': [('syssec', ['프로토콜·IoT 보안', '하드웨어·사이드채널']), ('embed', ['모바일 시스템'])],
 'PSL': [('pa', ['정적 분석', '프로그램 합성']), ('debug', ['테스트 생성·퍼징', '결함 위치 추정'])],
 'CASYS-Huh': [('arch', ['PIM·메모리 시스템', '보안 하드웨어', 'AI 가속기·NPU'])],
 'VLLab': [('ml', ['생성 모델', '그래프 학습']), ('mm', ['비전-언어 모델(VLM)'])],
 'BDI': [('ml', ['그래프 학습']), ('dm', ['그래프 마이닝']), ('nlp', ['추론'])],
 'CDSN': [('app', ['센서·행동 인식(HAR)']), ('edge', ['엣지 컴퓨팅·오프로딩']), ('aisys', ['온디바이스 AI'])],
 'KEAI': [('nlp', ['대화·감성', 'LLM']), ('mm', ['비전-언어 모델(VLM)'])],
 'LANADA': [('rl', ['강화학습']), ('aisys', ['분산 학습']), ('wireless', ['5G/6G·AI-RAN', '위성 통신'])],
 'AIPR': [('rl', ['강화학습', '오프라인·멀티에이전트 RL']), ('nlp', ['LLM 안전성·정렬'])],
 'IM2': [('robot', ['로봇 조작']), ('rl', ['강화학습'])],
 'SehoonKim': [('aisys', ['LLM 서빙·추론 최적화']), ('ml', ['효율적 학습·경량화']), ('nlp', ['LLM 에이전트'])],
 'CVLAB': [('cv', ['3D 장면·Gaussian Splatting', '영상 생성·편집']), ('ml', ['생성 모델'])],
 'GLOW': [('ml', ['생성 모델']), ('cv', ['영상 생성·편집', '3D 생성·기하 처리'])],
 'HyunwooKim': [('nlp', ['추론', 'LLM']), ('brain', ['인지과학·지각'])],
 'LKLab': [('nlp', ['LLM', '추론', '검색 증강 생성(RAG)'])],
 'DIVE': [('dm', ['그래프 마이닝', '추천 시스템']), ('ml', ['그래프 학습'])],
 'ALIN': [('ml', ['생성 모델', '신뢰성·강건성']), ('nlp', ['LLM 에이전트']), ('cv', ['영상 생성·편집'])],
 'CVML-Shim': [('cv', ['영상 생성·편집']), ('mm', ['비전-언어 모델(VLM)']), ('ml', ['생성 모델'])],
 'SungsooAhn': [('ml', ['분자·과학 ML', '생성 모델']), ('app', ['신약·화학 AI'])],
 'MLI': [('ml', ['효율적 학습·경량화', '생성 모델']), ('app', ['의료·바이오 AI'])],
 'BISPL': [('app', ['의료·바이오 AI']), ('cv', ['영상 복원·역문제', '영상 생성·편집']), ('ml', ['생성 모델'])],
 'STAI': [('ml', ['신뢰성·강건성']), ('nlp', ['LLM 에이전트', 'LLM 안전성·정렬'])],
 'OSI': [('ml', ['효율적 학습·경량화', '연합학습']), ('nlp', ['LLM', '추론'])],
 'OptiML': [('ml', ['최적화·딥러닝 이론', '학습 이론·확률 모델'])],
 'KiminLee': [('nlp', ['LLM 안전성·정렬', 'LLM 에이전트']), ('rl', ['강화학습'])],
 'SIML': [('ml', ['학습 이론·확률 모델', '생성 모델'])],
 'CLVR': [('robot', ['로봇 학습·휴머노이드', '로봇 조작']), ('rl', ['오프라인·멀티에이전트 RL'])],
 'DAVIAN': [('cv', ['영상 생성·편집']), ('nlp', ['LLM']), ('speech', ['음성 인식·변환'])],
 'EdLab': [('app', ['의료·바이오 AI', '바이오NLP']), ('nlp', ['LLM 에이전트'])],
 'SAIL': [('ml', ['설명가능 AI(XAI)']), ('dm', ['시계열·데이터 스트림'])],
 'INA': [('aisys', ['LLM 서빙·추론 최적화', '분산 학습']), ('edge', ['비디오 스트리밍·QoE', '데이터센터 네트워크'])],
 'SJHwang': [('nlp', ['검색 증강 생성(RAG)', 'LLM']), ('ml', ['생성 모델']), ('cv', ['3D 인체·아바타'])],
 'IMPACT': [('ic', ['바이오·센서 인터페이스 IC', '아날로그·혼성신호 회로']), ('arch', ['AI 가속기·NPU'])],
 'DSIL': [('arch', ['칩렛·3D 패키징']), ('ic', ['디지털 회로·SoC'])],
 'COMSTO': [('ml', ['도메인 적응·전이학습', '신뢰성·강건성']), ('aisys', ['분산 학습'])],
 'EmbeddedAI': [('aisys', ['온디바이스 AI']), ('ml', ['효율적 학습·경량화']), ('dm', ['시계열·데이터 스트림'])],
 'EPIC': [('ic', ['디지털 회로·SoC']), ('arch', ['AI 가속기·NPU'])],
 'SEED': [('ic', ['디지털 회로·SoC', '아날로그·혼성신호 회로'])],
 'SoundLab': [('speech', ['음원 분리·음악', '음성 합성'])],
 'MELab': [('sci', ['기후·지구 시스템'])],
 'SKimLab': [('policy', ['도시 데이터 분석'])],
 'DALI': [('policy', ['AI 거버넌스·안전'])],
 'JonWoojung': [('policy', ['법·금융·핀테크'])],
 'Forecasting': [('policy', ['확률적 예측'])],
 'SeunghwaLab': [('sci', ['물리 기반 AI', '설계 최적화·디지털 트윈'])],
 'KwonLab': [('sci', ['물리 기반 AI'])],
 'SBML': [('sci', ['시스템 생물학']), ('app', ['의료·바이오 AI'])],
 'AAI': [('ml', ['생성 모델']), ('nlp', ['LLM 안전성·정렬'])],
 'SongLab': [('sci', ['시스템 생물학'])],
 'IDOL': [('sci', ['설계 최적화·디지털 트윈'])],
 'IronTiger': [('policy', ['경영·정보시스템'])],
 'FTPL': [('sci', ['수송·동력 시스템'])],
}
