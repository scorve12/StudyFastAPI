from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from database import SessionLocal, question_crud
#from models import Question

from domain.question import question_schema

router = APIRouter(
    prefix="/api/question",
)

#라우터 객체 등록
@router.get("/list", response_model = list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list