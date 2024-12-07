from pydantic import BaseModel, EmailStr
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    address: Optional[str]

class CustomerCreate(CustomerBase):
    pass  # No additional fields for creation

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True