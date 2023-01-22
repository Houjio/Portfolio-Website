from typing import Union
from sqlalchemy.orm import Session

from . import models


def create_access(db: Session, access: models.PydanticAccess):
    db_access = models.Access(
        code = access.code,
        name = access.name,
        coverLetter = access.coverLetter,
        jobType = access.jobType,
        french = access.french,
    )
    db.add(db_access)
    db.commit()

    return access


def get_access_plural(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Access).offset(skip).limit(limit).all()


def get_access(db: Session, code: int) -> Union[models.Access, None]:
    return db.query(models.Access).filter(models.Access.code == code).first()

def update_product(db: Session, access: models.Access, accessUpdate: models.AccessUpdate):
    updateDict = accessUpdate.dict(exclude_none=True)
    for key, value in updateDict.items():
        access.__setattr__(key, value)

    db.add(access)
    db.commit()

    return models.PydanticAccess.from_orm(access)

def delete_product(db: Session, access: models.Access) -> dict:
    db.delete(access)
    db.commit()
    return {"ok": True}
