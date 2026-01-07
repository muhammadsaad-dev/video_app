from fastapi import FastAPI
from backend.api.v1.endpoints import users  # Add backend.
from backend.database import engine         # Add backend.
from backend.models import Base             # Add backend.

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Video Sharing Platform API")

app.include_router(users.router, prefix="/users", tags=["users"])