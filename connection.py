"""Conection to DB"""

import os
from dotenv import load_dotenv
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv(override=True)

DB: Engine = create_engine(
    f"postgresql+psycopg://{os.getenv('USER',"postgres")}:"
    f"{os.getenv('PASSWORD')}@{os.getenv('HOST', "localhost")}:"
    f"{os.getenv('PORT',"5432")}/{os.getenv('DB')}"
)

Session = sessionmaker(bind=DB)
session = Session()
