## 프로젝트 구조

fastapi-project/
├── app/
│ ├──`__init__`.py
│ ├── main.py # FastAPI 앱의 진입점
│ ├── core/ # 핵심 설정 및 유틸리티
│ │ ├── `__init__`.py
│ │ ├── config.py # 환경 변수 및 설정 파일
│ ├── database/ # 데이터베이스 관련 코드
│ │ ├── `__init__`.py
│ │ ├── database.py # DB 연결 설정
│ │ ├── session.py # 세션 관리
│ ├── models/ # 모델 정의
│ │ ├── `__init__`.py
│ │ ├── user.py # User 모델
│ │ ├── dept.py # Dept 모델
│ │ ├── job.py # Job 모델
│ ├── schemas/ # Pydantic 스키마 정의
│ │ ├── `__init__`.py
│ │ ├── user.py # User 스키마
│ │ ├── dept.py # Dept 스키마
│ │ ├── job.py # Job 스키마
│ ├── api/ # API 라우터
│ │ ├── `__init__`.py
│ │ ├── user.py # User API
│ │ ├── dept.py # Dept API
│ │ ├── job.py # Job API
│ ├── services/ # 비즈니스 로직
│ │ ├── `__init__`.py
│ │ ├── user_service.py
│ │ ├── dept_service.py
│ │ ├── job_service.py
│ ├── tests/ # 테스트 코드
│ │ ├── `__init__`.py
│ │ ├── test_user.py # User 관련 테스트
│ │ ├── test_dept.py # Dept 관련 테스트
│ │ ├── test_job.py # Job 관련 테스트
├── .env # 환경 변수 설정 파일
├── requirements.txt # Python 패키지 목록
