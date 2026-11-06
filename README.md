# KU Computer Science Directory

고려대학교 컴퓨터 분야 연구실 디렉토리 (컴퓨터학과·인공지능학과·데이터과학과·전기전자공학부·기계공학부, 132개 연구실). 정적 사이트 한 장(`index.html`)이라 빌드 없이 Vercel에 바로 올릴 수 있습니다.
- 목록: 대분류 → 중분류 → 세부 분야 3단계 필터, 검색, 정렬
- 상세: `#lab-<id>` 해시 주소로 연구실별 페이지 (논문 실적·연도별 등급, 자주 낸 학회, 최근 논문, 연구 분야, 학부 인턴, 구성원, 비슷한 연구실)
- 분야 바로가기: `#area-ai`, `#area-ai-mm`, `#area-ai-mm-0` (세부 분야는 목록 순번)

## 배포 (Vercel)
1. 이 폴더를 GitHub 저장소로 올립니다.
2. Vercel → Add New Project → 저장소 선택 → Framework Preset: **Other**, Build Command/Output Directory는 비워 둡니다.
3. Deploy. (CLI: 이 폴더에서 `npx vercel --prod`)

## 데이터 다시 만들기
```
cd build && ./build.sh      # ../index.html 재생성
```
| 파일 | 내용 |
|---|---|
| `labs_meta.py` | 연구실 이름·교수·홈페이지·한 줄 소개 |
| `taxonomy.py` | 3단계 분류 트리(`TREE`), 연구실별 분류(`ASSIGN`), dblp pid, 제목 키워드 |
| `members.jsonl` | 구성원·인턴(현재/예전) 명단 — 2026-11-06 랩 홈페이지 기준 |
| `dblp_year_agg.txt` | 교수별 2024–26 논문을 `교수|연도|c:학회 또는 j:저널|플래그(F=Findings, W=워크숍)|편수`로 집계 |
| `dblp_agg.txt` | 위와 같되 연도 대신 `편수,현재인턴저자,예전인턴저자` |
| `corrections.json` | 동명이인·프로시딩 편집 등 제외 목록 |
| `recent.tsv` | 연구실별 최근 논문(최대 5편/교수) |
| `tiers.py`, `ref_venues.txt` | T1/T2 분류표와 korea-ai-labs 원본 목록 |
| `template.html` | 페이지 템플릿 (`__DATA__` 자리에 데이터 주입) |

새 학과 추가: `labs_meta.py`·`taxonomy.py`(ASSIGN, 필요하면 TREE에 대분류 추가)·`members.jsonl`·dblp 파일에 행 추가 → `build.sh`.
