"""Connection"""

import os
from dotenv import load_dotenv
from rich.console import Console
from sqlalchemy import Engine, text, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import (
    database_exists as db_exist,
    create_database as create_db,
)
from models.model import Base

console: Console = Console()

load_dotenv(override=True)

db_name: str = "health"
db_url: str = (
    f"postgresql+psycopg://{os.getenv('USER')}:"
    f"{os.getenv('PASSWORD')}@{os.getenv('HOST')}:"
    f"{os.getenv('PORT')}/{db_name}"
)

engine: Engine = create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)
session = Session()


def create_database(name: str):
    """Creating database"""
    console.clear()

    if not db_exist(engine.url):
        console.print(
            f"databaze neexistuje!\nVytvarim DB: {name}",
            style="green",
        )
        create_db(engine.url)

        with session.connection() as conn:
            temp = conn.execute(text("SELECT version();"))
            console.print(temp.fetchone())
            console.print("databaze vytvorena", style="blue")
    else:
        console.log("Databaze jiz existuje", style="blue")
        with session.connection() as conn:
            temp = conn.execute(text("SELECT version();"))
            console.print(temp.fetchone())


def create_tables():
    """Vytvori tably v DB: health"""

    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_database("health")
    create_tables()
