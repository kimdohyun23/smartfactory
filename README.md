\# Smart Factory Manufacturing AI Portfolio



전기공학 도메인 지식에 데이터 분석, 머신러닝, 백엔드, 클라우드 기술을 결합하여  

\*\*제조 AI / 스마트팩토리 취업용 포트폴리오\*\*를 구축하는 프로젝트입니다.



\## 최종 목표



단순 데이터 분석 프로젝트가 아니라 아래 전체 흐름을 직접 구현하는 것을 목표로 합니다.



```text

설비 / 센서 / 생산 데이터

&#x20;       ↓

Python 데이터 수집·전처리

&#x20;       ↓

EDA / 통계 / 제조 KPI 분석

&#x20;       ↓

Machine Learning 기반 예측

&#x20;       ↓

FastAPI 또는 Python AI API

&#x20;       ↓

Spring Boot Backend

&#x20;       ↓

MySQL / PostgreSQL

&#x20;       ↓

Dashboard / MES 형태의 서비스

&#x20;       ↓

Docker

&#x20;       ↓

Cloud 배포

# Week01 - Manufacturing Production Data Analysis

## 프로젝트 소개
제조 생산 데이터를 활용하여 생산량, 불량률, 가동률을 분석하는 프로젝트입니다.

## 사용 기술
- Python
- Pandas
- Matplotlib

## 데이터 컬럼
| 컬럼 | 설명 |
|------|------|
| date | 생산 날짜 |
| machine_id | 설비 번호 |
| production_count | 생산 수량 |
| defect_count | 불량 수량 |
| operating_rate | 설비 가동률 |

## 분석 과정
1. CSV 데이터 로딩
2. 불량률 계산
3. KPI(생산량, 불량률, 가동률) 분석
4. 생산량 추이 시각화
5. 불량률 시각화
6. 가동률 시각화

## 결과
- 총 생산량: 8,520개
- 평균 생산량: 1,217.1개
- 불량률 2% 이상 날짜 탐지
- 생산량/불량률/가동률 그래프 생성

## 배운 점
- Pandas를 이용한 제조 데이터 분석
- 파생변수(defect_rate) 생성
- Matplotlib 시각화