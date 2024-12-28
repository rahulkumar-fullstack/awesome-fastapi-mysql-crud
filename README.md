# FastAPI CRUD with MySQL

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/fastapi-0.95-green)
![SQLModel](https://img.shields.io/badge/sqlmodel-0.0.9-lightgrey)
![MySQL](https://img.shields.io/badge/mysql-connector-blue)

**A simple CRUD application built with FastAPI, SQLModel, and MySQL for managing items.**

## Features

- Create, Read, Update, and Delete (CRUD) operations
- Uses SQLModel for database models
- Environment variables managed through `.env` file
- FastAPI Lifespan context for managing application lifecycle
- RESTful API with auto-generated documentation with OpenAI

## Prerequisites

- Python 3.8 or higher
- MySQL server installed
- Virtual environment

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rahulkumar-fullstack/awesome-fastapi-mysql-crud.git
   
   cd awesome-fastapi-mysql-crud
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create and configure `.env` file:

   ```plaintext
   DATABASE_URL=mysql+mysqlconnector://username:password@localhost:3306/mydatabase
   ```

## Project Structure

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

## Usage

1. **Run the application**:

   ```bash
   uvicorn app.main:app --reload
   ```

2. Access the API documentation at:

   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints

- `GET /items/` - Retrieve all items
- `POST /items/` - Create a new item
- `GET /items/{item_id}` - Retrieve an item by ID
- `PUT /items/{item_id}` - Update an existing item
- `DELETE /items/{item_id}` - Delete an item by ID

## Contributors

- [Rahulkumar Gupta](https://github.com/rahulkumar-fullstack)

## License

This project is licensed under the __MIT License__. See the LICENSE file for details.

---
