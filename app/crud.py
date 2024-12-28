from sqlmodel import Session, select
from app.models import Item

# Get all items
def get_items(db: Session):
    return db.exec(select(Item)).all()  # SQLModel's simplified query syntax

# Get an item by ID
def get_item(db: Session, item_id: int):
    return db.get(Item, item_id)  # Fetch by primary key

# Create a new item
def create_item(db: Session, item: Item):
    db.add(item)
    db.commit()
    db.refresh(item)  # Refresh to get the generated ID
    return item

# Update an existing item
def update_item(db: Session, item_id: int, item_data: dict):
    db_item = db.get(Item, item_id)
    if db_item:
        for key, value in item_data.items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

# Delete an item
def delete_item(db: Session, item_id: int):
    db_item = db.get(Item, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
