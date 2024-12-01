"""DB model"""

from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Bmi(Base):
    """vytvareni tablu"""

    __tablename__ = "bmis"

    bmi_id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False
    )
    bmi_number = Column(Float, nullable=False)
    bmi_text = Column(String(50), nullable=False)

    def __repr__(self):
        return f"bmi_id: {self.bmi_id}, bmi_number: {self.bmi_number}, bmi_text: {self.bmi_text}."

    def __str__(self):
        return f"ID: {self.bmi_id}, BMI hodnota: {self.bmi_number} --> {self.bmi_text}."


if __name__ == "__main__":
    pass
