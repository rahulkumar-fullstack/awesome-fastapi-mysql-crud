from fastapi import FastAPI
from app.database import create_tables
from app.routers import items

# Define the lifespan context manager
def lifespan(app: FastAPI):
    # Startup logic
    print("Starting up our FastAPI CRUD...")
    create_tables()  # Create database tables
    
    yield  # This separates startup and shutdown logic
    
    # Shutdown logic
    print("Shutting down our FastAPI CRUD...")

# Initialize FastAPI app with title and lifespan
app = FastAPI(
    title="FastAPI CRUD with SQLModel and MySQL",  # Title of the application
    lifespan=lifespan  # Lifespan context manager for startup and shutdown
)

# Include routers
app.include_router(items.router)
