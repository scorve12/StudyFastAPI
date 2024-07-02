from typing import Optional
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import models
from database import engine

from domain.question import question_router

#models연결
models.Base.metadata.create_all(bind=engine)

#FastAPI객체 할당
app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def hello():
    return {"message":"안녕하세요. 클라이언트"}

#router객체 포함
app.include_router(question_router.router)