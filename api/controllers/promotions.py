from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.promotions import Promotion as PromotionModel
from ..schemas.promotions import PromotionCreate, PromotionUpdate


def create(db: Session, request: PromotionCreate):
    new_promotion = PromotionModel(
        code=request.code,
        expiration_date=request.expiration_date,
    )
    db.add(new_promotion)
    db.commit()
    db.refresh(new_promotion)
    return new_promotion


def read_all(db: Session):
    return db.query(PromotionModel).all()


def read_one(db: Session, promotion_id: int):
    promotion = db.query(PromotionModel).filter(PromotionModel.id == promotion_id).first()
    if not promotion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Promotion with ID {promotion_id} not found",
        )
    return promotion


def update(db: Session, request: PromotionUpdate, promotion_id: int):
    promotion = db.query(PromotionModel).filter(PromotionModel.id == promotion_id).first()
    if not promotion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Promotion with ID {promotion_id} not found",
        )

    if request.code is not None:
        promotion.code = request.code
    if request.expiration_date is not None:
        promotion.expiration_date = request.expiration_date

    db.commit()
    db.refresh(promotion)
    return promotion


def delete(db: Session, promotion_id: int):
    promotion = db.query(PromotionModel).filter(PromotionModel.id == promotion_id).first()
    if not promotion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Promotion with ID {promotion_id} not found",
        )

    db.delete(promotion)
    db.commit()
    return {"detail": f"Promotion with ID {promotion_id} has been deleted"}

