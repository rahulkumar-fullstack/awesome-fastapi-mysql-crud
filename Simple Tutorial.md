
## **Creating a Simple CRUD Application with FastAPI and MySQL**

#### **1. Prerequisites**

- Python 3.8 or higher
- MySQL Server installed
- Virtual environment setup

---

#### **2. Project Setup**

##### **2.1 Project Structure**
- Create this files and folder with this latest pattern

```
crud_fastapi/
├── .env                    # Environment file
├── app/
│   ├── __init__.py          # Make the folder a Python package
│   ├── main.py              # FastAPI main file
│   ├── database.py          # Database connection setup
│   ├── models.py            # SQLModel models
│   ├── crud.py              # CRUD operations
│   ├── routers/
│   │   ├── items.py         # API routes
├── requirements.txt         # Dependencies
```

---

#### **3. Step-by-Step Guide**

---

#### **3.1 Setting Up Database**

1. **Install MySQL Connector**:
   ```bash
   pip install mysql-connector-python
   ```

2. **Create MySQL Database**:
   - Open MySQL terminal and create a database:
     ```sql
     CREATE DATABASE mydatabase;
     ```

---

#### **3.2 Setting Up `.env`**

1. **Create `.env` File**:
   ```plaintext
   DATABASE_URL=mysql+mysqlconnector://username:password@localhost:3306/mydatabase
   ```

---

#### **3.3 FastAPI Application Setup**

1. **Install Required Packages**:
   ```bash
   pip install fastapi uvicorn sqlmodel python-dotenv
   ```

2. **Database Connection** (`app/database.py`):

   ```python
   from sqlmodel import SQLModel, create_engine, Session
   from dotenv import load_dotenv
   import os

   load_dotenv()

   DATABASE_URL = os.getenv("DATABASE_URL")
   engine = create_engine(DATABASE_URL)

   def get_db():
       with Session(engine) as session:
           yield session

   def create_tables():
       SQLModel.metadata.create_all(engine)
   ```

3. **SQLModel Models** (`app/models.py`):

   ```python
   from sqlmodel import SQLModel, Field

   class Item(SQLModel, table=True):
       id: int = Field(default=None, primary_key=True)
       name: str = Field(index=True)
       description: str = Field(default=None)
       price: int
       quantity: int
   ```

4. **CRUD Operations** (`app/crud.py`):

   ```python
   from sqlmodel import Session, select
   from app.models import Item

   def get_items(db: Session):
       return db.exec(select(Item)).all()

   def get_item(db: Session, item_id: int):
       return db.get(Item, item_id)

   def create_item(db: Session, item: Item):
       db.add(item)
       db.commit()
       db.refresh(item)
       return item

   def update_item(db: Session, item_id: int, item_data: dict):
       db_item = db.get(Item, item_id)
       if db_item:
           for key, value in item_data.items():
               setattr(db_item, key, value)
           db.commit()
           db.refresh(db_item)
       return db_item

   def delete_item(db: Session, item_id: int):
       db_item = db.get(Item, item_id)
       if db_item:
           db.delete(db_item)
           db.commit()
       return db_item
   ```

5. **API Routes** (`app/routers/items.py`):

   ```python
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
   ```

6. **FastAPI Main File** (`app/main.py`):

   ```python
   from fastapi import FastAPI
   from app.database import create_tables
   from app.routers import items

   def lifespan(app: FastAPI):
       print("Starting up...")
       create_tables()
       yield
       print("Shutting down...")

   app = FastAPI(title="FastAPI CRUD with SQLModel and MySQL", lifespan=lifespan)
   app.include_router(items.router)
   ```

---

#### **3.4 Running the Application**

1. Start the FastAPI server:

   ```bash
   uvicorn app.main:app --reload
   ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

---

### **Summary**

In this tutorial, you have learned how to set up a CRUD application using FastAPI, SQLModel, and MySQL with the recommended use of `.env` for configuration and the modern `lifespan` event handling for startup/shutdown management.

--- 

😀😁😎