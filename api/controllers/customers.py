from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.customers import Customer
from ..schemas.customers import CustomerCreate, CustomerUpdate


def create(db: Session, request: CustomerCreate):
    existing_customer = db.query(Customer).filter(Customer.email == request.email).first()
    if existing_customer:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    new_customer = Customer(
        name=request.name,
        email=request.email,
        phone_number=request.phone_number,
        address=request.address
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


def read_all(db: Session):
    customers = db.query(Customer).all()
    return customers


def read_one(db: Session, customer_id: int):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with ID {customer_id} not found"
        )
    return customer


def update(db: Session, request: CustomerUpdate, customer_id: int):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with ID {customer_id} not found"
        )

    if request.name:
        customer.name = request.name
    if request.email:
        customer.email = request.email
    if request.phone_number:
        customer.phone_number = request.phone_number
    if request.address:
        customer.address = request.address

    db.commit()
    db.refresh(customer)

    return customer



def delete(db: Session, customer_id: int):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Customer with ID {customer_id} not found"
        )

    db.delete(customer)
    db.commit()

    return {"detail": "Customer deleted successfully"}
