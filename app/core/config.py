# 환경 변수 설정을 위한 라이브러리
# BaseSettings는 환경 변수를 쉽게 관리할 수 있게 해주는 클래스
from pydantic import BaseSettings

# 환경 변수 설정
class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"

# 환경 변수 설정 인스턴스 생성
# 이 인스턴스를 통해 애플리케이션 전체에서 설정값에 접근 가능
settings = Settings()
