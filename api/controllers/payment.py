from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.payment import Payment as PaymentModel
from ..schemas.payment import PaymentCreate, PaymentUpdate


def create(db: Session, request: PaymentCreate):
    new_payment = PaymentModel(
        payment_type=request.payment_type,
        transaction_status=request.transaction_status,
        card_info=request.card_information,
    )
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment


def read_all(db: Session):
    return db.query(PaymentModel).all()


def read_one(db: Session, payment_id: int):
    payment = db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
    if not payment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Payment with ID {payment_id} not found",
        )
    return payment


def update(db: Session, request: PaymentUpdate, payment_id: int):
    payment = db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
    if not payment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Payment with ID {payment_id} not found",
        )

    if request.payment_type is not None:
        payment.payment_type = request.payment_type
    if request.transaction_status is not None:
        payment.transaction_status = request.transaction_status
    if request.card_information is not None:
        payment.card_info = request.card_information

    db.commit()
    db.refresh(payment)
    return payment


def delete(db: Session, payment_id: int):
    payment = db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
    if not payment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Payment with ID {payment_id} not found",
        )

    db.delete(payment)
    db.commit()
    return {"detail": f"Payment with ID {payment_id} has been deleted"}