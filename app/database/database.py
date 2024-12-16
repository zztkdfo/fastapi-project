from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL

# connect_args={"check_same_thread": False} 는 SQLite 데이터베이스를 사용할 때 스레드 관련 제한을 해제하는 설정
# SQLite는 기본적으로 같은 연결을 여러 스레드에서 사용하는 것을 허용하지 않습니다. 이는 SQLite가 기본적으로 스레드에 안전하지 않기 때문
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 메타데이터를 사용하여 데이터베이스 엔진을 생성
metadata = MetaData()

# 세션 생성을 위한 팩토리 함수
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 테이블을 정의하는 데 사용되는 기본 클래스
Base = declarative_base(metadata=metadata)
