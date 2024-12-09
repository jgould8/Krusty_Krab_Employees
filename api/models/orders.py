from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)
    tracking_number = Column(String(50), nullable=True)
    order_status = Column(String(50), nullable=False)
    total_price = Column(DECIMAL(10, 2), nullable=False)

    customer = relationship("Customer", back_populates="orders")