import pdb

import databases
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker
# from databases import Database, DatabaseURL
from starlette.config import Config

env = Config('.env')

app = FastAPI()

SQLALCHEMY_DATABASE_URL = env('DB_URL')

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
database = databases.Database(SQLALCHEMY_DATABASE_URL)
Base: DeclarativeMeta = declarative_base()
