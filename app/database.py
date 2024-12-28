from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the database URL from the environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the database engine
engine = create_engine(DATABASE_URL)

# Dependency to get a database session for each request
def get_db():
    with Session(engine) as session:
        yield session

# Function to create database tables
def create_tables():
    SQLModel.metadata.create_all(engine)
