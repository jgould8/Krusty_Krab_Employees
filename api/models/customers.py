from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(15), nullable=False)
    address = Column(String(200), nullable=True)

    orders = relationship("Order", back_populates="customer")
    reviews = relationship("Rating", back_populates="customer")