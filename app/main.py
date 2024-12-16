from fastapi import FastAPI
from app.api import user

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
  
# 라우터 등록
app.include_router(user.router, prefix="/users", tags=["Users"])
