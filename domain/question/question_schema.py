import datetime

from pydantic import BaseModel


#스키마 정의
class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True