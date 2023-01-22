from sqlalchemy import Column, Text, Integer, String, Boolean

from typing import Optional
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from pydantic import BaseModel

from .database import Base


class Access(Base):
    __tablename__ = "access"

    code = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    coverLetter = Column(Text)
    jobType = Column(Integer)
    french = Column(Boolean)


PydanticAccess = sqlalchemy_to_pydantic(Access)


class AccessUpdate(BaseModel):
    name: Optional[str]
    coverLetter: Optional[str]
    jobType: Optional[int]
    french: Optional[bool]
