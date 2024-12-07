from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.resources import Resource as ResourceModel
from ..schemas.resources import ResourceCreate, ResourceUpdate


def create(db: Session, request: ResourceCreate):
    new_resource = ResourceModel(
        name=request.ingredient_name,
        amount=request.amount,
        unit=request.unit,
    )
    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)
    return new_resource


def read_all(db: Session):
    return db.query(ResourceModel).all()


def read_one(db: Session, resource_id: int):
    resource = db.query(ResourceModel).filter(ResourceModel.id == resource_id).first()
    if not resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Resource with ID {resource_id} not found",
        )
    return resource


def update(db: Session, request: ResourceUpdate, resource_id: int):
    resource = db.query(ResourceModel).filter(ResourceModel.id == resource_id).first()
    if not resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Resource with ID {resource_id} not found",
        )

    if request.ingredient_name is not None:
        resource.name = request.ingredient_name
    if request.amount is not None:
        resource.amount = request.amount
    if request.unit is not None:
        resource.unit = request.unit

    db.commit()
    db.refresh(resource)
    return resource


def delete(db: Session, resource_id: int):
    resource = db.query(ResourceModel).filter(ResourceModel.id == resource_id).first()
    if not resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Resource with ID {resource_id} not found",
        )

    db.delete(resource)
    db.commit()
    return {"detail": f"Resource with ID {resource_id} has been deleted"}

