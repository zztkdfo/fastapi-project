from pydantic import BaseModel

# UserBase 클래스는 사용자 정보를 나타내는 기본 스키마
class UserBase(BaseModel):
    name: str
    email: str
    age: int

# UserCreate 클래스는 사용자 생성을 위한 스키마
class UserCreate(UserBase):
    # 모든 필드가 필수로 정의되어 있음(pass는 추가 필드가 없다는 의미)
    pass

# UserResponse 클래스는 사용자 응답을 나타내는 스키마
class UserResponse(UserBase):
    id: int
    
    # orm_mode = True는 SQLAlchemy 모델을 Pydantic 스키마로 변환할 때 사용되는 설정
    class Config:
        orm_mode = True
