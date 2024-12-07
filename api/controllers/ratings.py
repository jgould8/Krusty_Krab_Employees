from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.ratings import Rating as RatingModel
from ..schemas.ratings import RatingCreate, RatingUpdate


def create(db: Session, request: RatingCreate):
    new_rating = RatingModel(
        customer_id=request.customer_id,
        menu_item_id=request.menu_item_id,
        review_text=request.review_text,
        score=request.score,
    )
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return new_rating


def read_all(db: Session):
    return db.query(RatingModel).all()


def read_one(db: Session, rating_id: int):
    rating = db.query(RatingModel).filter(RatingModel.id == rating_id).first()
    if not rating:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Rating with ID {rating_id} not found",
        )
    return rating


def update(db: Session, request: RatingUpdate, rating_id: int):
    rating = db.query(RatingModel).filter(RatingModel.id == rating_id).first()
    if not rating:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Rating with ID {rating_id} not found",
        )

    if request.review_text is not None:
        rating.review_text = request.review_text
    if request.score is not None:
        rating.score = request.score

    db.commit()
    db.refresh(rating)
    return rating


def delete(db: Session, rating_id: int):
    rating = db.query(RatingModel).filter(RatingModel.id == rating_id).first()
    if not rating:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Rating with ID {rating_id} not found",
        )

    db.delete(rating)
    db.commit()
    return {"detail": f"Rating with ID {rating_id} has been deleted"}

