from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_db
from app.models import Item
from app.crud import get_items, get_item, create_item, update_item, delete_item

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/", response_model=list[Item])
def read_items(db: Session = Depends(get_db)):
    return get_items(db)

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=Item)
def create_new_item(item: Item, db: Session = Depends(get_db)):
    return create_item(db, item)

@router.put("/{item_id}", response_model=Item)
def update_existing_item(item_id: int, item: Item, db: Session = Depends(get_db)):
    updated_item = update_item(db, item_id, item.dict(exclude_unset=True))
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/{item_id}")
def delete_existing_item(item_id: int, db: Session = Depends(get_db)):
    deleted_item = delete_item(db, item_id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted successfully"}
