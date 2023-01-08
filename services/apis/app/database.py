from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABSE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
    user='user', password='password', server='192.168.111.9', database='db')

engine = create_engine(DATABSE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
