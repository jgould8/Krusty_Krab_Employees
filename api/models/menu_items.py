from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    calories = Column(Integer, nullable=True)
    food_category = Column(String(50), nullable=True)

    reviews = relationship("Rating", back_populates="menu_item")