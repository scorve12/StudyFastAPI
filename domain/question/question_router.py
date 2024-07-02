from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from database import SessionLocal
from models import Question

from domain.question import question_schema

router = APIRouter(
    prefix="/api/question",
)

#라우터 객체 등록
@router.get("/list", response_model = list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    with get_db() as db:
        _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list