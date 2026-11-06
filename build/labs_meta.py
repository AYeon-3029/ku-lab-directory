# id, PI(s) Korean, PI English, lab name(ko), lab name short, homepage, fields, one-line focus
FIELDS = {
    'ml': '머신러닝', 'cv': '컴퓨터 비전', 'nlp': '자연어처리', 'speech': '음성·오디오',
    'robot': '로보틱스·자율주행', 'gfx': '그래픽스·XR·HCI', 'data': '데이터·DB·IR',
    'bio': '바이오·의료 AI', 'sys': '시스템·아키텍처', 'net': '네트워크·통신',
    'sec': '보안·프라이버시', 'sepl': 'SE·PL', 'edu': 'AI 교육', 'rf': '회로·RF',
}

LABS = [
    ('IDEA', ['강성구'], ['SeongKu Kang'], '데이터과학 및 응용 연구실', 'IDEA Lab', 'https://idea.korea.ac.kr/', ['data', 'nlp', 'ml'], '추천·검색(IR), LLM 기반 검색·지식 활용'),
    ('DMIS', ['강재우'], ['Jaewoo Kang'], '데이터마이닝 및 인포메이션시스템 연구실', 'DMIS Lab', 'https://dmis.korea.ac.kr', ['nlp', 'bio', 'data'], 'BioNLP, 신약 개발 AI, LLM·RAG'),
    ('IIIXR', ['강형엽'], ['HyeongYeop Kang'], 'IIIXR Lab', 'IIIXR Lab', 'https://iiixr.korea.ac.kr/', ['gfx', 'ml', 'robot'], '캐릭터 애니메이션, 임바디드 에이전트, 3D 장면 생성'),
    ('ICNL', ['곽정호'], ['Jeongho Kwak'], '지능 컴퓨팅 및 네트워킹 연구실', 'ICNL', 'https://icnl.korea.ac.kr', ['net', 'sys'], 'AI-RAN, 엣지/클라우드 컴퓨팅, 위성 온보드 컴퓨팅'),
    ('CSArch', ['구건재'], ['Gunjae Koo'], '컴퓨터 시스템 구조 연구실', 'CSArch Lab', 'https://csarch.korea.ac.kr', ['sys'], 'GPU·가속기 구조, 메모리·스토리지 시스템'),
    ('PALM', ['김동선'], ['Dongsun Kim'], 'PALM Group', 'PALM Group', 'https://darkrsw.github.io/', ['sepl'], '프로그램 자동 수정·소프트웨어 분석'),
    ('SERA', ['김세연'], ['Seyeon Kim'], 'SERA Lab', 'SERA Lab', 'https://seralab.korea.ac.kr/', ['sys', 'net'], 'XR·AI 시스템, 엣지 NPU, LLM 서빙'),
    ('CASL', ['김영근'], ['Younggeun Kim'], '지능형 컴퓨터 구조 및 시스템 연구실', 'CASL', 'https://casl.korea.ac.kr', ['sys'], '온디바이스 AI 최적화, 열·에너지 관리, LLM 추론'),
    ('DXP', ['김정현'], ['Gerard Jounghyun Kim'], '디지털체험 연구실', 'DXP Lab', 'http://dxp.korea.ac.kr', ['gfx'], 'VR/AR·HCI, VR 멀미, 햅틱'),
    ('VisionAI', ['김진규', '이정범'], ['Jinkyu Kim', 'Jungbeom Lee'], '비전 및 인공지능 연구실', 'Vision & AI Lab', 'https://visionai.korea.ac.kr', ['cv', 'robot', 'ml'], 'VLM·VLA, 자율주행, 로봇 조작'),
    ('INI', ['김현철'], ['Hyeoncheol Kim'], '지능인포매틱스 연구실', 'INI Lab', 'https://ini.korea.ac.kr', ['edu', 'ml'], 'AI 교육, 지식 추적, 학습 분석'),
    ('WiDeN', ['김효곤'], ['Hyogon Kim'], '무선데이터통신 연구실', 'WiDeN', 'http://widen.korea.ac.kr', ['net'], 'V2X·차량 통신, 5G, IoT'),
    ('VCAI', ['문경식'], ['Gyeongsik Moon'], 'Visual Computing and AI Lab', 'VCAI Lab', 'https://www.vcai.korea.ac.kr/', ['cv', 'gfx'], '3D 인체·손 복원, 아바타'),
    ('HCL', ['민성기'], ['Sung-Gi Min'], '고속통신 연구실', 'HCL', 'http://hcl.korea.ac.kr', ['net'], '네트워크 프로토콜'),
    ('Hypermedia', ['박성빈'], ['Seongbin Park'], '하이퍼미디어 연구실', 'Hypermedia Lab', '', [], '홈페이지 없음'),
    ('GI', ['박성우'], ['Sungwoo Park'], '생성형 지능시스템 연구실', 'GI Lab', 'https://www.gi.korea.ac.kr/', ['ml'], '생성 모델, 확산 모델, 물리 기반 생성'),
    ('DBS', ['박종혁'], ['Jonghyeok Park'], '데이터베이스 시스템 연구실', 'DBS Lab', 'https://dbs.korea.ac.kr/', ['data', 'sys'], '스토리지·DB 엔진, 클라우드 데이터 시스템'),
    ('PLRG', ['박지혁'], ['Jihyeok Park'], '프로그래밍 언어 연구실', 'PLRG', 'https://plrg.korea.ac.kr/', ['sepl'], 'JavaScript 명세·프로그램 분석, 테스팅'),
    ('AXIS', ['박채용'], ['Chaeyong Park'], '증강경험 및 인터랙티브시스템 연구실', 'AXIS Lab', 'https://axis.korea.ac.kr/', ['gfx'], '햅틱, VR/AR 인터랙션'),
    ('SING', ['백승준'], ['Seung Jun Baek'], '지능시스템망 연구실', 'SING', 'http://sing.korea.ac.kr', ['ml', 'bio', 'sys'], '딥러닝 시스템, LLM, 의료 AI, 그래프 학습'),
    ('ESCA', ['서태원'], ['Taeweon Suh'], '임베디드컴퓨팅 연구실', 'ESCA Lab', 'http://esca.korea.ac.kr', ['sys', 'sec'], 'RISC-V 프로세서, AI 가속기, 하드웨어 보안'),
    ('MIIL', ['서홍석'], ['Paul Hongsuck Seo'], 'Multimodal Interactive Intelligence Lab', 'MIIL', 'https://miil.korea.ac.kr/', ['cv', 'nlp', 'ml'], '멀티모달 학습, 비디오 이해, 생성 AI'),
    ('SELENE', ['안가빈'], ['Gabin An'], 'SELENE Lab', 'SELENE Lab', 'https://ku-selene.github.io/', ['sepl'], 'LLM 기반 결함 위치 추정, SE 자동화'),
    ('SSL', ['양경식'], ['Gyeongsik Yang'], '시스템 소프트웨어 연구실', 'System Software Lab', 'https://ss.korea.ac.kr', ['sys', 'ml'], 'AI 시스템 SW, 클라우드, LLM 서빙'),
    ('MES', ['오상은'], ['Sangeun Oh'], 'Mobile Embedded Systems Lab', 'MES Lab', 'https://mes.korea.ac.kr/', ['sys'], '모바일·온디바이스 LLM, 실시간·열 관리'),
    ('PRL', ['오학주'], ['Hakjoo Oh'], '소프트웨어 분석 연구실', 'SAL@KU', 'http://prl.korea.ac.kr', ['sepl'], '프로그램 분석·합성, 자동 디버깅'),
    ('SSP', ['우승훈'], ['Seunghoon Woo'], '소프트웨어 보안 연구실', 'SSP Lab', 'https://ssp.korea.ac.kr/', ['sec', 'sepl'], '오픈소스 SW 보안, 취약점 탐지'),
    ('DCC', ['유헌창'], ['Heonchang Yu'], '분산클라우드컴퓨팅 연구실', 'D&C Lab', 'https://ds.korea.ac.kr', ['sys'], '분산 딥러닝, 서버리스, LLM 서빙'),
    ('AI-Yook', ['육동석'], ['Dongsuk Yook'], '인공지능 연구실', 'KU AI Lab', 'http://ai.korea.ac.kr/~yook/', ['speech', 'ml'], '음성 인식·변환, 대규모 학습'),
    ('DAIS', ['윤수식'], ['Susik Yoon'], 'Data and Adaptive Intelligence Systems Lab', 'DAIS Lab', 'http://dais.korea.ac.kr', ['data', 'ml', 'nlp'], '데이터 스트림, 적응형 AI, 시계열·추천'),
    ('PIXEL', ['이상민'], ['Sangmin Lee'], 'PIXEL Lab', 'PIXEL Lab', 'https://sites.google.com/view/pixel-lab-ai', ['cv', 'ml'], '멀티모달·소셜 AI, 비디오 이해'),
    ('Physical', ['이재훈'], ['Jaehoon Lee'], '피지컬컴퓨팅 연구실', 'Physical Computing Lab', 'https://sites.google.com/site/mplabku', ['net', 'sys'], '모바일·임베디드 시스템'),
    ('MMW', ['이주섭'], ['Juseop Lee'], 'Microwave/Millimeter-Wave Lab', 'MMW Lab', 'https://sites.google.com/view/juseoplee', ['rf'], '마이크로파·밀리미터파 회로, 필터'),
    ('CCS', ['이희조'], ['Heejo Lee'], '컴퓨터보안 연구실', 'CCS Lab', 'https://ccs.korea.ac.kr', ['sec', 'sepl'], '오픈소스 취약점 탐지, 바이너리 분석, SBOM'),
    ('IBEL', ['인호'], ['Hoh Peter In'], '지능형 블록체인 공학 연구실', 'IBEL', 'https://ibel.korea.ac.kr/', ['sec', 'sys'], '블록체인, 스마트 컨트랙트 보안, ZKP'),
    ('NLP&AI', ['임희석'], ['Heuiseok Lim'], '자연어처리 & 인공지능 연구실', 'NLP&AI Lab', 'http://nlp.korea.ac.kr', ['nlp'], 'LLM, 다국어·검색, AI 에이전트'),
    ('LI', ['장부루'], ['Buru Chang'], '언어 및 지능 연구실', 'LI Lab', 'https://lilab.korea.ac.kr', ['nlp', 'cv'], 'RAG, VLM, 대화 시스템'),
    ('S2', ['전유석'], ['Yuseok Jeon'], 'Secure Software Lab', 'S2 Lab', 'https://s2-lab.github.io/', ['sec'], '시스템·SW 보안, 퍼징, 메모리 안전성'),
    ('SMRL', ['정성우'], ['Sung Woo Chung'], 'SoC 및 마이크로프로세서 연구실', 'SMRL', 'http://smrl.korea.ac.kr', ['sys'], '열 관리, 프로세서 구조, ECC'),
    ('IELab', ['정순영'], ['Soon Young Jung'], 'Intelligence Engineering Lab', 'IE Lab', 'https://kuielab.github.io/', ['speech', 'ml', 'data'], '음원 분리, 생성 모델, 산업 AI'),
    ('DataX', ['정연돈'], ['Yon Dohn Chung'], 'DataX Lab', 'DataX Lab', 'https://dx.korea.ac.kr/', ['data', 'sec', 'ml'], '데이터 프라이버시, 연합학습, 벡터 DB'),
    ('HVCL', ['정원기'], ['Won-Ki Jeong'], 'High-performance Visual Computing Lab', 'HVCL', 'http://hvcl.korea.ac.kr', ['gfx', 'bio', 'cv'], '시각화, 바이오메디컬 영상 처리'),
    ('PRISM', ['정형진'], ['Hyungjin Chung'], 'PRISM Lab', 'PRISM Lab', 'http://prism.korea.ac.kr/', ['ml', 'cv'], '확산 모델, 역문제·영상 복원'),
    ('RAIN', ['주창희'], ['Changhee Joo'], 'RAIN Lab', 'RAIN Lab', 'http://rain.korea.ac.kr', ['net', 'ml'], '무선 네트워크 최적화, 강화학습'),
    ('Media', ['한정현'], ['JungHyun Han'], '미디어 연구실', 'Media Lab', 'http://media.korea.ac.kr', ['gfx'], '그래픽스, VR/AR, 게임'),
    ('ISSL', ['허준범'], ['Junbeom Hur'], '정보시스템보안 연구실', 'ISS Lab', 'https://issl.korea.ac.kr/', ['sec'], '네트워크 보안, AI 보안, 암호'),
]
# professor -> lab id
PROF2LAB = {}
for row in LABS:
    for p in row[1]:
        PROF2LAB[p] = row[0]

AI_LABS = [
    ('SDML', ['Anh Tong'], ['Anh Tong'], 'Stochastic Dynamics and Machine Learning Lab', 'SDML Lab', 'https://sdml-ku.github.io/', [], '확률적 동역학·Neural ODE, 시계열, 효율적 미세조정'),
    ('DMLab', ['이병준'], ['Byung-Jun Lee'], 'Decision Making Lab', 'DMLab', 'https://dmlab.korea.ac.kr/', [], '강화학습(오프라인·멀티에이전트), 확산 모델 기반 의사결정'),
    ('AILAB', ['이창희'], ['Changhee Lee'], 'Actionable Intelligence Lab', 'The AI-LAB', 'https://sites.google.com/view/actionable-intelligence/', [], '의료·헬스케어 ML, 시계열, 임상 의사결정'),
    ('SLPL', ['김찬우'], ['Chanwoo Kim'], 'Speech and Language Processing Lab', 'SLP Lab', 'https://slpl.korea.ac.kr/home/', [], '음성 인식·합성, 멀티모달 LLM'),
    ('CogSys', ['Christian Wallraven'], ['Christian Wallraven'], 'Cognitive Systems Lab', 'Cognitive Systems Lab', 'https://cogsys.korea.ac.kr/', [], '인지과학·정신물리학, 인간-AI 정렬, 햅틱 지각'),
    ('UTL', ['김동현'], ['Donghyun Kim'], 'Universal Transfer Learning Lab', 'UTL Lab', 'https://utl.korea.ac.kr/', [], '전이학습·도메인 적응, 머신 언러닝, 임바디드 AI'),
    ('VGI', ['박경문'], ['Gyeong-Moon Park'], 'Vision & Generative Intelligence Lab', 'VGI Lab', 'https://vgi.korea.ac.kr/', [], '연속 학습, 생성 모델, 비디오·3D 비전'),
    ('MILab', ['석흥일'], ['Heung-Il Suk'], 'Machine Intelligence Lab', 'MILab', 'https://milab.korea.ac.kr/', [], '뇌 영상·의료 영상 분석, BCI, 베이지안 딥러닝'),
    ('Seo-H', ['서현석'], ['Hyunseok Seo'], '서현석 교수 연구실', 'Seo Lab', '', [], '의료 영상 AI, 생성 모델'),
    ('TAIL', ['정종헌'], ['Jongheon Jeong'], 'Trustworthy AI Lab', 'TAIL', 'https://tail.korea.ac.kr/', [], '신뢰할 수 있는 AI, 강건성, 생성 모델 워터마크·정렬'),
    ('BREIN', ['성준경'], ['Joon-Kyung Seong'], 'Brain Reverse Engineering by Intelligent Neuroimaging Lab', 'BREIN Lab', 'http://brein.korea.ac.kr/lab/', [], '뇌 영상(신경영상) 분석, 알츠하이머, 생체신호'),
    ('DILab', ['이상근'], ['SangKeun Lee'], 'Data Intelligence Lab', 'DI Lab', 'http://dilab.korea.ac.kr', [], 'LLM·자연어처리, 효율적 미세조정, 한국어 언어모델'),
    ('CVLAB', ['김상필'], ['Sangpil Kim'], 'Computer Vision Lab', 'CVLAB', 'https://kuaicv.com/', [], '3D 비전·Gaussian Splatting, 멀티모달 융합, 자율주행, AI 워터마크'),
    ('EIL', ['박세준'], ['Sejun Park'], 'Efficient Inference and Learning Lab', 'EIL', 'https://eil-research.github.io/', [], '신경망 표현력 이론, 효율적 추론·학습'),
    ('PRML', ['이성환'], ['Seong-Whan Lee'], '패턴인식 및 머신러닝 연구실', 'PR&ML Lab', 'http://pr.korea.ac.kr/', [], '패턴인식, 뇌-컴퓨터 인터페이스, 음성 합성, 컴퓨터 비전'),
    ('DRILab', ['이승규'], ['Seoungkyou Lee'], 'DRI Lab', 'DRI Lab', 'https://sites.google.com/view/drilab/home', [], '다중 로봇, 경로 계획'),
    ('HUI', ['서승호'], ['Sungho Suh'], 'Human-centric Ubiquitous Intelligence Lab', 'HUI Lab', 'https://sites.google.com/view/sunghosuh/home', [], '웨어러블 센서·행동 인식(HAR), 생성 모델, VLA'),
    ('RIL', ['최성준'], ['Sungjoon Choi'], 'Robot Intelligence Lab', 'Robot Intelligence Lab', 'https://sites.google.com/view/sungjoon-choi/home', [], '로봇 학습, 휴머노이드 모션'),
    ('AIImg', ['최성준'], ['Sungjoon Choi'], 'AI Imaging Lab', 'AI Imaging Lab', 'https://aii.korea.ac.kr', [], '계산 이미징, 영상 복원, 확산·플로우 생성 모델'),
    ('AGI', ['김성웅'], ['Sungwoong Kim'], 'Artificial General Intelligence Lab', 'AGI Lab', 'https://agi.korea.ac.kr/', [], '멀티모달 LLM, AI for Science, 선호 최적화'),
    ('MAILab', ['감태의'], ['Tae-Eui Kam'], 'Medical Artificial Intelligence Lab', 'MAILAB', 'http://mailab.korea.ac.kr/', [], '의료 영상, EEG·BCI, 의료 AI'),
    ('SPL', ['정원주'], ['Wonzoo Chung'], 'Statistical Intelligence Lab', 'Statistical Intelligence Lab', 'http://spl.korea.ac.kr', [], '통계적 신호처리, EEG·BCI'),
    ('Jung-W', ['정우환'], ['Woohwan Jung'], '정우환 교수 연구실', 'Jung Lab', '', [], 'NLP·정보 추출, RAG, 데이터베이스'),
]
DEPT = {r[0]: ['컴퓨터학과'] for r in LABS}
DEPT['SING'] = ['컴퓨터학과', '인공지능학과']
for r in AI_LABS:
    DEPT[r[0]] = ['인공지능학과']
DEPT['DILab'] = ['인공지능학과', '컴퓨터학과']
LABS = LABS + AI_LABS
PROF2LAB = {}
for row in LABS:
    for p in row[1]:
        PROF2LAB[p] = row[0]

PROF2LAB['최성준'] = 'RIL'
PROF2LAB['최성준#2'] = 'AIImg'

from new_labs import EE as _EE, ME as _ME
_first = dict(PROF2LAB)
EE_LABS = [(r[0], [r[1].split('#')[0]], [r[2]], r[3], r[4], r[5], [], r[6]) for r in _EE]
ME_LABS = [(r[0], [r[1]], [r[2]], r[3], r[4], r[5], [], r[6]) for r in _ME]
for r in EE_LABS: DEPT[r[0]] = ['전기전자공학부']
for r in ME_LABS: DEPT[r[0]] = ['기계공학부']
LABS = LABS + EE_LABS + ME_LABS
for r in _EE + _ME:
    PROF2LAB.setdefault(r[1], r[0])
PROF2LAB['이병준#EE'] = 'PowerSys'
NO_PUBS_NEW = {r[0]: r[8] for r in _EE + _ME if r[8]}
# 데이터과학과: 정보대학 교수진이 겸무 (데이터 중심 연구실)
def _tag_ds():
    from taxonomy import ASSIGN
    for lid, a in ASSIGN.items():
        d = DEPT.get(lid, [])
        if any(x in d for x in ('컴퓨터학과', '인공지능학과')) and any(mid in ('dm', 'db') for mid, _ in a):
            DEPT[lid] = d + ['데이터과학과']
_tag_ds()
if 'DMIS' in DEPT and '데이터과학과' not in DEPT['DMIS']: DEPT['DMIS'] = DEPT['DMIS'] + ['데이터과학과']
