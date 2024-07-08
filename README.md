# StudyFastAPI
for FastAPI
ref(https://wikidocs.net/176222#pydantic)
AWS배포

### 기초 명령어
```
#실행
uvicorn main:app --reload
```

### OpenSource
```
from typing import Optional
from fastapi import FastAPI
``` 

### Directory 
```
StudyFastAPI
├─ database.py
├─ domain
│  ├─ answer
│  ├─ question
│  └─ user
├─ main.py
├─ models.py
├─ README.md
├─ test
└─ __pycache__
   └─ main.cpython-312.pyc
```

* \test
* \domain : 도메인 디렉토리
* database.py : 데이터베이스 설정 파일
* main.py : app 객체 
* models.py : 모델파일
