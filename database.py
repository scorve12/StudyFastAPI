from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#데이터베이스 루트디렉토리 설정
SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

#
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False}   
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#autocommit = True를 할 경우 commit이 없기 때문에 rollback또한 할 수 없다.

Base = declarative_base() 