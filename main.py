from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from starlette.middleware.cors import CORSMiddleware

import models
from database import engine

from domain.answer import answer_router
from domain.question import question_router

#models연결
models.Base.metadata.create_all(bind=engine)

#FastAPI객체 할당
app = FastAPI()
template = Jinja2Templates(directory="templates")

origins = [
    "http://127.0.0.0:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return template.TemplateResponse("test.html", {"request": "request"})

@app.get("/hello")
def hello():
    return {"message":"안녕하세요. 클라이언트"}

#router객체 포함
app.include_router(question_router.router)
app.include_router(answer_router.router)