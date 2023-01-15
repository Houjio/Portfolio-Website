from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, crud
# from . import models, schemas, crud

from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# CORS Acess

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


@app.post("/acess/", response_model=models.PydanticAcess)
def create_one_acess(acess: models.PydanticAcess, db: Session = Depends(get_db)):
    return crud.create_acess(db=db, acess=acess)


@app.get("/acess/", response_model=List[models.PydanticAcess])
def read_all_acess(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    acess = crud.get_acess_plural(db, skip=skip, limit=limit)
    return [models.PydanticAcess.from_orm(a) for a in acess]


@app.get("/acess/{code}", response_model=models.PydanticAcess)
def read_acess(code: int, db: Session = Depends(get_db)):
    db_acess = crud.get_acess(db, code=code)
    if db_acess is None:
        raise HTTPException(status_code=404, detail="Acess not found")
    return models.PydanticAcess.from_orm(db_acess)


@app.patch("/acess/{code}", response_model=models.PydanticAcess)
def update_acess(code: int, acessUpdate: models.AcessUpdate,  db: Session = Depends(get_db)):
    db_acess = crud.get_acess(db, code=code)
    if db_acess is None:
        raise HTTPException(status_code=404, detail="Acess not found")

    return crud.update_product(db, db_acess, acessUpdate)


@app.delete("/acess/{code}")
def update_acess(code: int, db: Session = Depends(get_db)):
    db_acess = crud.get_acess(db, code=code)
    if db_acess is None:
        raise HTTPException(status_code=404, detail="Acess not found")

    return crud.delete_product(db, db_acess)
