from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, nullable=False)
    expiration_date = Column(DateTime, nullable=False)