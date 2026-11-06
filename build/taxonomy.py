# 3-level taxonomy: 대분류 > 중분류 > 세부 분야
# Designed to extend to 전기전자공학부 later (반도체 소자, 회로, 신호처리, 전력·제어 can be added as new 대분류/중분류).
TREE = [
    ('ai', '인공지능', [
        ('ml', '머신러닝 (ML)', ['생성 모델', '연속·적응 학습', '도메인 적응·전이학습', '신뢰성·강건성', '연합학습', '그래프 학습', '효율적 학습·경량화', '학습 이론·확률 모델']),
        ('rl', '강화학습 (RL)', ['강화학습', '오프라인·멀티에이전트 RL', '월드 모델']),
        ('cv', '컴퓨터 비전 (Vision)', ['3D 인체·아바타', '3D 장면·Gaussian Splatting', '비디오 이해', '영상 생성·편집', '영상 복원·역문제', '자율주행 인지']),
        ('nlp', 'LLM·자연어처리', ['LLM', '검색 증강 생성(RAG)', '추론', '대화·감성', 'LLM 안전성·정렬']),
        ('mm', '멀티모달', ['비전-언어 모델(VLM)', '오디오-비주얼', '비전-언어-행동(VLA)']),
        ('speech', '음성·오디오', ['음성 인식·변환', '음성 합성', '음원 분리·음악']),
        ('robot', '로보틱스', ['임바디드 에이전트', '로봇 조작', '자율주행', '로봇 학습·휴머노이드']),
        ('brain', '뇌·인지 AI', ['뇌-컴퓨터 인터페이스(BCI)', '뇌 영상 분석', '인지과학·지각']),
        ('dm', '데이터·검색', ['추천 시스템', '정보 검색', '시계열·데이터 스트림', '그래프 마이닝']),
        ('app', 'AI 응용', ['의료·바이오 AI', '신약·화학 AI', '바이오NLP', 'AI 교육', 'AI for Science', '센서·행동 인식(HAR)']),
    ]),
    ('sys', '시스템·하드웨어', [
        ('arch', '컴퓨터 구조', ['AI 가속기·NPU', 'PIM·메모리 시스템', '프로세서(RISC-V)', '열·전력 관리', '메모리 신뢰성(ECC)']),
        ('aisys', 'AI 시스템', ['LLM 서빙·추론 최적화', '온디바이스 AI', '분산 학습']),
        ('ossys', '시스템 소프트웨어', ['클라우드·서버리스', '운영체제·가상화', '스토리지']),
        ('embed', '모바일·임베디드', ['모바일 시스템', '실시간 시스템']),
        ('db', '데이터베이스', ['DB 엔진·인덱싱', '벡터 DB', '분산 트랜잭션']),
        ('rf', '회로·RF', ['마이크로파·밀리미터파 필터']),
    ]),
    ('net', '네트워크·통신', [
        ('wireless', '무선·모바일 네트워크', ['5G/6G·AI-RAN', 'mmWave', 'V2X·차량 통신', '위성 통신']),
        ('edge', '엣지·클라우드 네트워킹', ['엣지 컴퓨팅·오프로딩', '비디오 스트리밍·QoE', '데이터센터 네트워크']),
        ('netopt', '네트워크 최적화', ['자원 할당·스케줄링', '학습 기반 네트워크 제어']),
    ]),
    ('sec', '보안·프라이버시', [
        ('swsec', '소프트웨어 보안', ['취약점 탐지', '퍼징', '바이너리 분석', '오픈소스 공급망', '메모리 안전성']),
        ('syssec', '시스템·네트워크 보안', ['하드웨어·사이드채널', '프로토콜·IoT 보안', '인증']),
        ('aisec', 'AI 보안', ['적대적 공격·방어', 'LLM 프라이버시']),
        ('crypto', '암호·블록체인', ['블록체인·스마트 컨트랙트', '영지식 증명', '응용 암호']),
        ('privacy', '데이터 프라이버시', ['차분 프라이버시', '프라이버시 보존 데이터 수집']),
    ]),
    ('ee', '전기전자·제어', [
        ('ic', '집적회로', ['디지털 회로·SoC', '아날로그·혼성신호 회로', 'RF·초고주파 회로', '바이오·센서 인터페이스 IC']),
        ('comm', '통신·신호처리 이론', ['무선 통신 이론', '양자 정보', '영상·신호처리']),
        ('ctrl', '제어·메카트로닉스', ['제어 이론', '메카트로닉스·소프트 로봇']),
        ('power', '전력·에너지', ['전력전자·변환', '전력 시스템·스마트그리드', '전기기기']),
        ('semi', '반도체·소자', ['차세대 반도체 소자', '메모리·뉴로모픽 소자', '디스플레이·광소자', '나노·유연 전자소자']),
    ]),
    ('sw', '소프트웨어·프로그래밍 언어', [
        ('pa', '프로그램 분석·합성', ['정적 분석', '프로그램 합성']),
        ('debug', '테스팅·디버깅', ['결함 위치 추정', '자동 수정', '테스트 생성·퍼징']),
        ('llm4se', 'LLM 기반 SE', ['코드 마이그레이션', 'LLM 신뢰성 평가', '코드 검색·리뷰']),
        ('pl', '프로그래밍 언어', ['JavaScript·언어 명세']),
    ]),
    ('hci', '그래픽스·인터랙션', [
        ('gfx', '그래픽스·애니메이션', ['캐릭터 애니메이션', '렌더링', '물리 시뮬레이션']),
        ('xr', 'VR/AR', ['VR 멀미', 'VR 인터랙션', 'AR']),
        ('haptic', '햅틱', ['햅틱 인터페이스', '진동촉각']),
        ('vis', '시각화', ['과학·의료 시각화']),
        ('ux', 'HCI', ['모바일 인터랙션', '사용자 연구']),
    ]),
]

# lab id -> [(mid, [fine...]), ...]  (첫 항목이 대표 분야)
ASSIGN = {
    'SDML': [('ml', ['학습 이론·확률 모델', '도메인 적응·전이학습', '효율적 학습·경량화']), ('dm', ['시계열·데이터 스트림'])],
    'DMLab': [('rl', ['강화학습', '오프라인·멀티에이전트 RL']), ('ml', ['생성 모델']), ('nlp', ['LLM 안전성·정렬'])],
    'AILAB': [('app', ['의료·바이오 AI']), ('dm', ['시계열·데이터 스트림']), ('nlp', ['LLM'])],
    'SLPL': [('speech', ['음성 인식·변환', '음성 합성']), ('mm', ['비전-언어 모델(VLM)']), ('nlp', ['LLM'])],
    'CogSys': [('brain', ['인지과학·지각']), ('haptic', ['진동촉각']), ('ml', ['신뢰성·강건성'])],
    'UTL': [('ml', ['도메인 적응·전이학습', '연속·적응 학습']), ('robot', ['임바디드 에이전트']), ('cv', ['영상 생성·편집'])],
    'VGI': [('ml', ['연속·적응 학습', '생성 모델', '도메인 적응·전이학습']), ('cv', ['비디오 이해', '3D 장면·Gaussian Splatting']), ('mm', ['오디오-비주얼'])],
    'MILab': [('brain', ['뇌 영상 분석', '뇌-컴퓨터 인터페이스(BCI)']), ('app', ['의료·바이오 AI']), ('ml', ['학습 이론·확률 모델', '도메인 적응·전이학습'])],
    'Seo-H': [('app', ['의료·바이오 AI']), ('ml', ['생성 모델'])],
    'TAIL': [('ml', ['신뢰성·강건성', '생성 모델']), ('nlp', ['LLM 안전성·정렬']), ('aisec', ['적대적 공격·방어'])],
    'BREIN': [('brain', ['뇌 영상 분석']), ('app', ['의료·바이오 AI'])],
    'DILab': [('nlp', ['LLM', '추론']), ('ml', ['효율적 학습·경량화'])],
    'CVLAB': [('cv', ['3D 장면·Gaussian Splatting', '3D 인체·아바타', '자율주행 인지']), ('mm', ['비전-언어 모델(VLM)']), ('aisec', ['적대적 공격·방어'])],
    'EIL': [('ml', ['학습 이론·확률 모델', '효율적 학습·경량화', '신뢰성·강건성'])],
    'PRML': [('brain', ['뇌-컴퓨터 인터페이스(BCI)']), ('speech', ['음성 합성']), ('cv', ['3D 인체·아바타']), ('ml', ['생성 모델'])],
    'DRILab': [('robot', ['로봇 학습·휴머노이드'])],
    'HUI': [('app', ['센서·행동 인식(HAR)']), ('ml', ['생성 모델']), ('mm', ['비전-언어-행동(VLA)'])],
    'RIL': [('robot', ['로봇 학습·휴머노이드', '로봇 조작'])],
    'AIImg': [('cv', ['영상 복원·역문제', '영상 생성·편집']), ('ml', ['생성 모델'])],
    'AGI': [('mm', ['비전-언어 모델(VLM)']), ('app', ['AI for Science']), ('rl', ['강화학습']), ('nlp', ['LLM 안전성·정렬'])],
    'MAILab': [('app', ['의료·바이오 AI']), ('brain', ['뇌-컴퓨터 인터페이스(BCI)']), ('rl', ['강화학습'])],
    'SPL': [('brain', ['뇌-컴퓨터 인터페이스(BCI)'])],
    'Jung-W': [('nlp', ['검색 증강 생성(RAG)', 'LLM']), ('db', ['DB 엔진·인덱싱'])],
    'IDEA': [('dm', ['추천 시스템', '정보 검색']), ('nlp', ['검색 증강 생성(RAG)', 'LLM']), ('ml', ['연속·적응 학습'])],
    'DMIS': [('nlp', ['LLM', '검색 증강 생성(RAG)', '추론']), ('app', ['바이오NLP', '신약·화학 AI', '의료·바이오 AI'])],
    'IIIXR': [('gfx', ['캐릭터 애니메이션']), ('robot', ['임바디드 에이전트']), ('rl', ['월드 모델']), ('cv', ['3D 장면·Gaussian Splatting']), ('ml', ['생성 모델'])],
    'ICNL': [('wireless', ['5G/6G·AI-RAN', '위성 통신']), ('edge', ['엣지 컴퓨팅·오프로딩']), ('netopt', ['자원 할당·스케줄링'])],
    'CSArch': [('arch', ['AI 가속기·NPU', 'PIM·메모리 시스템']), ('aisys', ['LLM 서빙·추론 최적화'])],
    'PALM': [('debug', ['결함 위치 추정', '자동 수정']), ('llm4se', ['코드 검색·리뷰'])],
    'SERA': [('edge', ['비디오 스트리밍·QoE']), ('aisys', ['온디바이스 AI', 'LLM 서빙·추론 최적화']), ('wireless', ['5G/6G·AI-RAN'])],
    'CASL': [('aisys', ['온디바이스 AI', 'LLM 서빙·추론 최적화']), ('arch', ['열·전력 관리']), ('ml', ['연합학습', '효율적 학습·경량화'])],
    'DXP': [('xr', ['VR 멀미', 'VR 인터랙션']), ('ux', ['사용자 연구'])],
    'VisionAI': [('mm', ['비전-언어 모델(VLM)', '비전-언어-행동(VLA)']), ('robot', ['자율주행', '로봇 조작', '임바디드 에이전트']), ('cv', ['자율주행 인지', '3D 장면·Gaussian Splatting']), ('ml', ['생성 모델'])],
    'INI': [('app', ['AI 교육']), ('nlp', ['LLM'])],
    'WiDeN': [('wireless', ['V2X·차량 통신', '위성 통신']), ('edge', ['비디오 스트리밍·QoE'])],
    'VCAI': [('cv', ['3D 인체·아바타']), ('gfx', ['캐릭터 애니메이션'])],
    'HCL': [('wireless', ['V2X·차량 통신'])],
    'Hypermedia': [],
    'GI': [('ml', ['생성 모델'])],
    'DBS': [('db', ['DB 엔진·인덱싱', '벡터 DB']), ('ossys', ['스토리지'])],
    'PLRG': [('pl', ['JavaScript·언어 명세']), ('pa', ['정적 분석', '프로그램 합성'])],
    'AXIS': [('haptic', ['햅틱 인터페이스', '진동촉각']), ('xr', ['VR 인터랙션'])],
    'SING': [('ml', ['생성 모델', '그래프 학습']), ('app', ['의료·바이오 AI']), ('nlp', ['검색 증강 생성(RAG)']), ('wireless', ['mmWave'])],
    'ESCA': [('arch', ['AI 가속기·NPU', '프로세서(RISC-V)']), ('syssec', ['하드웨어·사이드채널'])],
    'MIIL': [('mm', ['비전-언어 모델(VLM)', '오디오-비주얼']), ('cv', ['비디오 이해', '영상 생성·편집']), ('nlp', ['추론'])],
    'SELENE': [('debug', ['결함 위치 추정', '자동 수정']), ('llm4se', ['코드 마이그레이션', 'LLM 신뢰성 평가'])],
    'SSL': [('aisys', ['분산 학습', 'LLM 서빙·추론 최적화']), ('ossys', ['클라우드·서버리스', '운영체제·가상화']), ('edge', ['데이터센터 네트워크'])],
    'MES': [('embed', ['모바일 시스템', '실시간 시스템']), ('aisys', ['온디바이스 AI']), ('arch', ['열·전력 관리']), ('ux', ['모바일 인터랙션'])],
    'PRL': [('pa', ['정적 분석', '프로그램 합성']), ('debug', ['결함 위치 추정', '테스트 생성·퍼징']), ('llm4se', ['코드 마이그레이션'])],
    'SSP': [('swsec', ['오픈소스 공급망', '취약점 탐지', '바이너리 분석'])],
    'DCC': [('ossys', ['클라우드·서버리스']), ('aisys', ['분산 학습', 'LLM 서빙·추론 최적화'])],
    'AI-Yook': [('speech', ['음성 인식·변환']), ('aisys', ['분산 학습'])],
    'DAIS': [('dm', ['시계열·데이터 스트림', '정보 검색', '그래프 마이닝']), ('nlp', ['LLM'])],
    'PIXEL': [('mm', ['오디오-비주얼', '비전-언어 모델(VLM)']), ('cv', ['비디오 이해', '3D 장면·Gaussian Splatting']), ('app', ['의료·바이오 AI'])],
    'Physical': [('embed', ['모바일 시스템'])],
    'MMW': [('rf', ['마이크로파·밀리미터파 필터'])],
    'CCS': [('swsec', ['취약점 탐지', '퍼징', '바이너리 분석', '오픈소스 공급망']), ('syssec', ['프로토콜·IoT 보안'])],
    'IBEL': [('crypto', ['블록체인·스마트 컨트랙트', '영지식 증명', '응용 암호'])],
    'NLP&AI': [('nlp', ['LLM', '검색 증강 생성(RAG)', '추론', '대화·감성'])],
    'LI': [('nlp', ['LLM 안전성·정렬', '대화·감성', '검색 증강 생성(RAG)']), ('mm', ['비전-언어 모델(VLM)'])],
    'S2': [('swsec', ['퍼징', '메모리 안전성', '취약점 탐지']), ('aisec', ['LLM 프라이버시'])],
    'SMRL': [('arch', ['열·전력 관리', 'PIM·메모리 시스템', '메모리 신뢰성(ECC)'])],
    'IELab': [('speech', ['음원 분리·음악']), ('ml', ['생성 모델'])],
    'DataX': [('privacy', ['차분 프라이버시', '프라이버시 보존 데이터 수집']), ('db', ['분산 트랜잭션', '벡터 DB']), ('app', ['의료·바이오 AI'])],
    'HVCL': [('vis', ['과학·의료 시각화']), ('app', ['의료·바이오 AI']), ('cv', ['영상 복원·역문제'])],
    'PRISM': [('ml', ['생성 모델']), ('cv', ['영상 복원·역문제', '영상 생성·편집']), ('app', ['의료·바이오 AI'])],
    'RAIN': [('netopt', ['자원 할당·스케줄링', '학습 기반 네트워크 제어']), ('wireless', ['mmWave'])],
    'Media': [('gfx', ['렌더링', '물리 시뮬레이션']), ('xr', ['AR', 'VR 인터랙션']), ('cv', ['3D 장면·Gaussian Splatting'])],
    'ISSL': [('syssec', ['하드웨어·사이드채널', '프로토콜·IoT 보안', '인증']), ('aisec', ['적대적 공격·방어']), ('crypto', ['응용 암호'])],
}

# dblp title-keyword hits (2024–26, keyword regex on titles; shown as hints only)
KW_LABEL = {'rec': '추천', 'llm': 'LLM', 'rag': '검색·RAG', 'cl': '연속 학습', 'eff': '효율화·경량화', 'diff': '생성·확산 모델',
            'ir': '검색·랭킹', 'med': '의료', 'ondev': '모바일·엣지', 'ts': '시계열·스트림', 'reason': '추론', 'drug': '신약·분자',
            'graph': '그래프', 'bionlp': '바이오', 'hci': '인터랙션', 'human3d': '인체·모션', 'vla': '임바디드·조작', 'vr': 'VR/AR',
            'scene3d': '3D 장면', 'agent': '에이전트', 'synth': '합성·수정', 'netopt': '네트워크', 'sat': '위성', 'thermal': '열·에너지',
            'llm4se': '코드', 'net6g': '5G/6G·무선', 'serving': '추론·서빙', 'drive': '자율주행·차량', 'cloud': '클라우드',
            'mem': '메모리·스토리지', 'gpu': 'GPU·가속기', 'vuln': '취약점', 'video': '비디오', 'robust': '신뢰성·강건성', 'vlm': '멀티모달',
            'fed': '연합학습', 'edu': '교육', 'speech': '음성·오디오', 'vis': '시각화', 'haptic': '햅틱', 'gfx': '그래픽스', 'v2x': 'V2X',
            'db': 'DB·질의', 'rl': '강화학습', 'js': 'JavaScript', 'test': '테스팅', 'proganal': '프로그램 분석', 'fuzz': '퍼징', 'oss': '오픈소스',
            'binary': '바이너리', 'dist': '분산·병렬', 'rt': '실시간', 'chain': '블록체인', 'crypto': '암호', 'privacy': '프라이버시',
            'aisec': '공격·방어', 'music': '음악', 'wm': '월드 모델', 'da': '도메인 적응·전이', 'bci': 'EEG·BCI', 'har': '행동 인식·센서', 'robot': '로봇', 'percep': '지각·인지', 'sci': 'AI for Science'}
KW_RAW = """Anh Tong:ts1,da1
이병준:rl7,diff5,llm4,eff3,reason2,vlm2,robust2
이창희:ts6,llm5
김찬우:speech5,eff2
Christian Wallraven:human3d5,med2,drive2,video2
김동현:diff7,da5,eff3,graph3,cl2,video2,scene3d2
박경문:video6,diff4,da4,human3d4,scene3d4,percep3,speech3,cl3
석흥일:med15,diff7,da5,bci5,eff3,ts2
서현석:diff2
정종헌:robust8,diff5
성준경:med2
이상근:llm10,sci6,eff4,human3d3,reason3,robust2
김상필:scene3d15,human3d10,robust10,diff9,video6,vlm6,percep3,graph3
박세준:diff2,scene3d2
이성환:human3d24,speech24,diff20,bci18,robust15,percep12,eff10,llm8
이승규:robot2
서승호:percep16,har15,human3d12,diff5,eff4,vlm3
김성웅:diff3,rl3,robot2,llm2,robust2,human3d2
감태의:med17,bci13,diff8,rl6,sci6,graph5,rag5,da4
정원주:bci3
정우환:llm4,rag2
강성구:rec17,llm9,rag8,cl6,eff4,diff4,ir3,med3,ondev3,ts2
강재우:llm19,med12,reason10,drug8,diff4,graph4,bionlp4,rag4,hci3,ondev3
강형엽:human3d6,vla4,vr4,scene3d3,agent3,hci3,synth2,reason2,diff2
곽정호:netopt11,ondev10,sat8,thermal4,net6g3,serving3,drive3,cloud2,mem2
구건재:gpu18,eff7,mem4,llm3,serving3,ondev2,thermal2
김동선:synth5,llm4se4
김세연:video4,ondev3,serving3,netopt2,ts2,thermal2
김영근:eff6,ondev5,fed3,llm2,thermal2,mem2
김정현:vr21,human3d9,hci3,drive3,speech2
김진규:scene3d11,reason4,vlm4,robust4,diff4,drive4,ts3,cl3,human3d3
김현철:edu18,llm11,diff4,vlm3,reason2
김효곤:drive2,ondev2,v2x2
문경식:human3d10,scene3d7
민성기:v2x1,netopt1
박종혁:db2,graph2
박지혁:js3,graph2
박채용:haptic5,human3d3,vr2,hci2
백승준:netopt4,dist3,diff2,med2,graph2,scene3d2
서태원:gpu9,eff6,crypto3,llm2,ondev2
서홍석:diff5,speech3,vlm2,graph2,synth2,video2,rag2,eff2
안가빈:llm6,synth3,test2
오상은:ondev9,hci4,thermal2,rt2,serving2,mem2
오학주:test3,proganal2,synth2,fuzz1
우승훈:oss4,vuln3,llm4se2,binary1
유헌창:cloud10,dist6,ondev5,gpu3,serving3,mem2
육동석:dist1
윤수식:ts8,netopt5,llm5,rag2,cl2
이상민:med3,vlm3,speech3,rag2,video2,scene3d2
이정범:diff2,vlm1,reason1,agent1
이주섭:net6g1
이희조:vuln4,fuzz3,llm4se2,oss2,binary1
인호:chain11,crypto3,privacy3,graph2,robust2
임희석:llm30,rag12,robust7,diff6,reason3,vlm3,eff3
장부루:llm5,robust3,vlm3,aisec2
전유석:llm2,synth2,fuzz1,test1,proganal1,vuln1
정성우:eff6,serving4,thermal4,gpu3,llm2,mem2
정연돈:privacy4
정원기:med8,diff7,eff4,scene3d2
정형진:diff11,med5,scene3d4,video3,human3d3
주창희:ir3,eff3,dist3,net6g3,netopt3,ondev2
한정현:scene3d4,hci3,vr3,vis3,rt2
허준범:aisec10,crypto4,mem3,drive2,privacy2,vuln2
양경식:dist3,gpu2,llm1,mem1,cloud1"""

DBLP_PID = {'최성준': '81/618', 'Anh Tong': '177/9366', '이병준': '130/1678-1', '이창희': '58/2092', '김찬우': '62/79-1', 'Christian Wallraven': '96/549', '김동현': '33/6749-6', '박경문': '166/0276', '석흥일': '90/5988', '서현석': '157/5076', '정종헌': '241/5923', '성준경': '23/6581', '이상근': '73/3458-1', '김상필': '182/2231', '박세준': '155/9882', '이성환': 'l/SeongWhanLee', '이승규': '142/2828', '서승호': '48/10247', '김성웅': '74/8063', '감태의': '128/6310', '정원주': '71/80', '정우환': '193/7295', '강성구': '251/9613', '강재우': 'k/JaewooKang', '강형엽': '159/5774', '곽정호': '12/9796', '구건재': '47/4693',
            '김동선': '10/2501-1', '김세연': '60/10494-1', '김영근': '294/6642-1', '김정현': '94/5578', '김진규': '52/4354-1',
            '김현철': '27/2653', '김효곤': '34/2646', '문경식': '185/6852', '민성기': '08/1780', '박종혁': '199/9310', '박지혁': '144/4242',
            '박채용': '239/8038', '백승준': '227/0467-1', '서태원': '63/677', '서홍석': '172/0938', '안가빈': '225/3675', '양경식': '181/1435',
            '오상은': '140/7997', '오학주': '13/7537', '우승훈': '201/9210', '유헌창': '80/2696', '육동석': '14/2605', '윤수식': '179/5307',
            '이상민': '68/311-1', '이정범': '218/6736', '이주섭': '53/9902', '이희조': '75/4485', '인호': 'i/HohPeterIn', '임희석': '127/4881',
            '장부루': '221/3390', '전유석': '125/8622', '정성우': '46/2413', '정순영': '45/3571', '정연돈': '65/6972', '정원기': '70/5286',
            '정형진': '262/0382', '주창희': 'j/ChangheeJoo', '한정현': '59/10857', '허준범': '21/1967'}

EN = {'디지털 회로·SoC':'Digital Circuits SoC VLSI','아날로그·혼성신호 회로':'Analog Mixed-Signal Circuits','RF·초고주파 회로':'RF Microwave THz Circuits','바이오·센서 인터페이스 IC':'Biomedical Sensor Interface IC','무선 통신 이론':'Wireless Communication Theory MIMO','양자 정보':'Quantum Information Quantum Computing','영상·신호처리':'Signal Image Processing','제어 이론':'Control Theory','메카트로닉스·소프트 로봇':'Mechatronics Soft Robotics','전력전자·변환':'Power Electronics','전력 시스템·스마트그리드':'Power Systems Smart Grid','전기기기':'Electric Machines','차세대 반도체 소자':'Semiconductor Devices','메모리·뉴로모픽 소자':'Memory Neuromorphic Devices','디스플레이·광소자':'Display Optoelectronics','나노·유연 전자소자':'Nano Flexible Electronics','생성 모델':'Generative Models','강화학습':'Reinforcement Learning','연속·적응 학습':'Continual Learning','신뢰성·강건성':'Robustness & Trustworthy AI','연합학습':'Federated Learning','그래프 학습':'Graph Learning GNN','효율적 학습·경량화':'Efficient ML Model Compression',
'3D 인체·아바타':'3D Human Avatar Pose','3D 장면·Gaussian Splatting':'3D Scene Gaussian Splatting NeRF','비디오 이해':'Video Understanding','영상 생성·편집':'Image Video Generation Editing Diffusion','영상 복원·역문제':'Image Restoration Inverse Problems','자율주행 인지':'Autonomous Driving Perception Occupancy',
'LLM':'Large Language Models LLM','검색 증강 생성(RAG)':'Retrieval-Augmented Generation RAG','추론':'LLM Reasoning','대화·감성':'Dialogue Systems Emotional Support','LLM 안전성·정렬':'Alignment AI Safety Hallucination Jailbreak',
'비전-언어 모델(VLM)':'Vision-Language Models VLM Multimodal','오디오-비주얼':'Audio-Visual Learning Multimodal','비전-언어-행동(VLA)':'Vision-Language-Action VLA',
'음성 인식·변환':'Speech Recognition Voice Conversion','음원 분리·음악':'Music Source Separation Audio',
'임바디드 에이전트':'Embodied Agents','로봇 조작':'Robot Manipulation','자율주행':'Autonomous Driving','월드 모델':'World Models','오프라인·멀티에이전트 RL':'Offline Multi-agent RL','로봇 학습·휴머노이드':'Robot Learning Humanoid','도메인 적응·전이학습':'Domain Adaptation Transfer Learning','학습 이론·확률 모델':'Learning Theory Probabilistic Bayesian','음성 합성':'Speech Synthesis TTS','뇌-컴퓨터 인터페이스(BCI)':'Brain-Computer Interface BCI EEG','뇌 영상 분석':'Neuroimaging Brain MRI','인지과학·지각':'Cognitive Science Perception','AI for Science':'AI for Science','센서·행동 인식(HAR)':'Human Activity Recognition Wearable Sensors',
'추천 시스템':'Recommender Systems','정보 검색':'Information Retrieval Search','시계열·데이터 스트림':'Time Series Data Streams','그래프 마이닝':'Graph Mining Community Search',
'의료·바이오 AI':'Healthcare Medical AI','신약·화학 AI':'AI Drug Discovery Chemistry','바이오NLP':'Biomedical NLP','AI 교육':'AI for Education Knowledge Tracing',
'AI 가속기·NPU':'AI Accelerators NPU GPU','PIM·메모리 시스템':'Processing-in-Memory PIM HBM','프로세서(RISC-V)':'RISC-V Processor','열·전력 관리':'Thermal Power Energy Management','메모리 신뢰성(ECC)':'Memory Reliability ECC DRAM',
'LLM 서빙·추론 최적화':'LLM Serving Inference','온디바이스 AI':'On-device Edge AI','분산 학습':'Distributed Training',
'클라우드·서버리스':'Cloud Serverless Kubernetes','운영체제·가상화':'Operating Systems Virtualization','스토리지':'Storage','모바일 시스템':'Mobile Systems','실시간 시스템':'Real-time Systems',
'DB 엔진·인덱싱':'Database Engine Indexing','벡터 DB':'Vector Database HNSW','분산 트랜잭션':'Distributed Transactions','마이크로파·밀리미터파 필터':'Microwave Millimeter-wave Filter RF',
'5G/6G·AI-RAN':'5G 6G AI-RAN O-RAN Wireless','mmWave':'mmWave','V2X·차량 통신':'V2X Vehicular Communication','위성 통신':'Satellite LEO',
'엣지 컴퓨팅·오프로딩':'Edge Computing Offloading','비디오 스트리밍·QoE':'Video Streaming QoE Conferencing','데이터센터 네트워크':'Datacenter Networking',
'자원 할당·스케줄링':'Resource Allocation Scheduling','학습 기반 네트워크 제어':'Learning-based Network Control',
'취약점 탐지':'Vulnerability Detection','퍼징':'Fuzzing','바이너리 분석':'Binary Analysis','오픈소스 공급망':'Open-source Supply Chain SBOM','메모리 안전성':'Memory Safety Type Confusion',
'하드웨어·사이드채널':'Hardware Side-channel','프로토콜·IoT 보안':'Protocol IoT Security','인증':'Authentication',
'적대적 공격·방어':'Adversarial Attacks AI Security','LLM 프라이버시':'LLM Privacy Membership Inference',
'블록체인·스마트 컨트랙트':'Blockchain Smart Contracts','영지식 증명':'Zero-Knowledge Proofs ZKP','응용 암호':'Applied Cryptography Post-Quantum',
'차분 프라이버시':'Differential Privacy','프라이버시 보존 데이터 수집':'Privacy-preserving Data Collection',
'정적 분석':'Static Program Analysis','프로그램 합성':'Program Synthesis','결함 위치 추정':'Fault Localization','자동 수정':'Automated Program Repair','테스트 생성·퍼징':'Test Generation Fuzzing',
'코드 마이그레이션':'Code Migration LLM','LLM 신뢰성 평가':'LLM Evaluation','코드 검색·리뷰':'Code Search Review','JavaScript·언어 명세':'JavaScript Language Specification',
'캐릭터 애니메이션':'Character Animation Motion','렌더링':'Rendering Ray Tracing','물리 시뮬레이션':'Physics Simulation',
'VR 멀미':'VR Cybersickness','VR 인터랙션':'VR Interaction','AR':'Augmented Reality AR',
'햅틱 인터페이스':'Haptic Interfaces','진동촉각':'Vibrotactile','과학·의료 시각화':'Scientific Medical Visualization','모바일 인터랙션':'Mobile Interaction','사용자 연구':'User Study HCI'}
BIG_DESC = {'ee':'집적회로, 통신 이론, 제어, 전력, 반도체 소자','ai':'','sys':'컴퓨터 구조, AI 시스템, 시스템 SW, 모바일, DB, 회로','net':'무선·모바일, 엣지·클라우드, 네트워크 최적화','sec':'SW 보안, 시스템 보안, AI 보안, 암호, 프라이버시','sw':'프로그램 분석, 테스팅·디버깅, LLM4SE, PL','hci':'그래픽스, VR/AR, 햅틱, 시각화, HCI'}

from new_labs import EE as _EE, ME as _ME, PIDS as _PIDS
for _k,_v in _PIDS.items(): DBLP_PID.setdefault(_k,_v)
for _r in _EE + _ME:
    ASSIGN[_r[0]] = _r[7]
