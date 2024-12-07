from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.menu_items import MenuItem
from ..schemas.menu_items import MenuItemCreate, MenuItemUpdate


def create(db: Session, request: MenuItemCreate):
    existing_item = db.query(MenuItem).filter(MenuItem.name == request.name).first()
    if existing_item:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Menu item with this name already exists"
        )

    new_item = MenuItem(
        name=request.name,
        price=request.price,
        calories=request.calories,
        food_category=request.category
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


def read_all(db: Session):
    menu_items = db.query(MenuItem).all()
    return menu_items


def read_one(db: Session, item_id: int):
    menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if not menu_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Menu item with ID {item_id} not found"
        )
    return menu_item


def update(db: Session, request: MenuItemUpdate, item_id: int):
    menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()

    if not menu_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Menu item with ID {item_id} not found"
        )

    if request.name:
        menu_item.name = request.name
    if request.price is not None:
        menu_item.price = request.price
    if request.calories is not None:
        menu_item.calories = request.calories
    if request.category:
        menu_item.food_category = request.category

    db.commit()
    db.refresh(menu_item)

    return menu_item


def delete(db: Session, item_id: int):
    menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()

    if not menu_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Menu item with ID {item_id} not found"
        )

    db.delete(menu_item)
    db.commit()

    return {"detail": "Menu item deleted successfully"}
