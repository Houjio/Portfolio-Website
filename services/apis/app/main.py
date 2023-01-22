from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, crud

from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# CORS Access

origins = [
    "http://0.0.0.0",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database tables

models.Base.metadata.create_all(bind=engine)

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def ping():
    return {"ping": "pong"}


@app.post("/access/", response_model=models.PydanticAccess)
def create_one_access(access: models.PydanticAccess, db: Session = Depends(get_db)):
    return crud.create_access(db=db, access=access)


@app.get("/access/", response_model=List[models.PydanticAccess])
def read_all_access(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    access = crud.get_access_plural(db, skip=skip, limit=limit)
    return [models.PydanticAccess.from_orm(a) for a in access]


@app.get("/access/{code}", response_model=models.PydanticAccess)
def read_access(code: int, db: Session = Depends(get_db)):
    db_access = crud.get_access(db, code=code)
    if db_access is None:
        raise HTTPException(status_code=404, detail="Access not found")
    return models.PydanticAccess.from_orm(db_access)


@app.patch("/access/{code}", response_model=models.PydanticAccess)
def update_access(code: int, accessUpdate: models.AccessUpdate,  db: Session = Depends(get_db)):
    db_access = crud.get_access(db, code=code)
    if db_access is None:
        raise HTTPException(status_code=404, detail="Access not found")

    return crud.update_product(db, db_access, accessUpdate)


@app.delete("/access/{code}")
def update_access(code: int, db: Session = Depends(get_db)):
    db_access = crud.get_access(db, code=code)
    if db_access is None:
        raise HTTPException(status_code=404, detail="Access not found")

    return crud.delete_product(db, db_access)
