from sqlalchemy import Column, Text, Integer, String, Boolean
from sqlalchemy.orm import relationship

from typing import Optional
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from pydantic import BaseModel

from .database import Base


class Acess(Base):
    __tablename__ = "acess"

    code = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    coverLetter = Column(Text)
    french = Column(Boolean)

PydanticAcess = sqlalchemy_to_pydantic(Acess)


class AcessUpdate(BaseModel):
    name: Optional[str]
    coverLetter: Optional[str]
    french: Optional[bool]

class KeyResponse(BaseModel):
    sucess: bool
    key: int