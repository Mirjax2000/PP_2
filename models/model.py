"""DB model"""

from typing import Any
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base: Any = declarative_base()


class Bmi(Base):
    """vytvareni tablu"""

    __tablename__ = "bmis"


if __name__ == "__main__":
    pass
