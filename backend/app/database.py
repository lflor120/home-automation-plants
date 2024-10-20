from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends
from typing import Annotated
from dotenv import load_dotenv
import os

load_dotenv()
SQLALCHEMY_DATABASE_URL=os.environ["DATABASE_URL"]

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SessionDep = Annotated[Session, Depends(get_db)]