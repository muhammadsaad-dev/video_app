
from fastapi import FastAPI
from api.v1.endpoints import users
from database import engine
from models import Base

# Create tables (only if you're not using Alembic for migrations yet)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Video Sharing Platform API")

# Include Routers
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def root():
    return {"message": "Welcome to the Video API"}