from typing import Optional
from fastapi import FastAPI

import models
from database import engine

#models연결
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return{"item_id": item_id, "q":q}