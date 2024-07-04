from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from starlette import status

from database import get_db
#from database import SessionLocal, question_crud
from models import Question

from domain.question import question_schema, question_crud

router = APIRouter(
    prefix="/api/question",
)

#라우터 객체 등록
@router.get("/list", response_model = list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list

@router.post("/creat", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_cerate=_question_create)
#response_model 대신 HTTP204를 사용했다. 
#응답할 것이 없으면 204를 리턴한다.