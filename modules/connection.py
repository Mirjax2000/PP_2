"""Connection"""

import os
from dotenv import load_dotenv
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv(override=True)

DB: Engine = create_engine(
    f"postgresql+psycopg://{os.getenv('USER')}:"
    f"{os.getenv('PASSWORD')}@{os.getenv('HOST')}:"
    f"{os.getenv('PORT')}"
)

Session = sessionmaker(bind=DB)
session = Session()


if __name__ == "__main__":
    print(DB.url)
