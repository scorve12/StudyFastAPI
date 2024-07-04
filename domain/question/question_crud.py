from datetime import datetime

from domain.question.question_schema import QuestionCreate
from models import Question
from sqlalchemy.orm import Session


def get_question_list(db: Session):
    question_list = db.query(Question)\
        .order_by(Question.create_date.desc())\
        .all()
    return question_list

def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question

def create_question(db: Session, question_cerate: QuestionCreate):
    db_question = Question(subject=question_cerate.subject,
                           content=question_cerate.content,
                           create_date=datetime.new())
    db.add(db_question)
    db.commit