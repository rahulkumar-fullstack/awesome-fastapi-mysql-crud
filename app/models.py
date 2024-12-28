from sqlmodel import SQLModel, Field

# Define the Item model
class Item(SQLModel, table=True):  # 'table=True' makes it a database table
    id: int = Field(default=None, primary_key=True)  # Auto-incrementing primary key
    name: str = Field(index=True)  # Name column with an index for faster queries
    description: str = Field(default=None)  # Optional description
    price: int  # Price column
    quantity: int  # Quantity column
