import datetime

from pydantic import BaseModel

from domain.answer.answer_schema import Answer

#스키마 정의
class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answer: list[Answer] = []

    class Config:
        orm_mode = True