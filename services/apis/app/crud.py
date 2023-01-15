from typing import Union
from sqlalchemy.orm import Session

from . import models


def create_acess(db: Session, acess: models.PydanticAcess):
    db_acess = models.Acess(
        code = acess.code,
        name = acess.name,
        coverLetter = acess.coverLetter,
        french = acess.french,
    )
    db.add(db_acess)
    db.commit()

    return acess


def get_acess_plural(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Acess).offset(skip).limit(limit).all()


def get_acess(db: Session, code: int) -> Union[models.Acess, None]:
    return db.query(models.Acess).filter(models.Acess.code == code).first()

def update_product(db: Session, acess: models.Acess, acessUpdate: models.AcessUpdate):
    updateDict = acessUpdate.dict(exclude_none=True)
    for key, value in updateDict.items():
        acess.__setattr__(key, value)

    db.add(acess)
    db.commit()

    return models.PydanticAcess.from_orm(acess)

def delete_product(db: Session, acess: models.Acess) -> dict:
    db.delete(acess)
    db.commit()
    return {"ok": True}
