from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from config import settings # Ensure the relative import matches your structure

db_name = settings.DB_NAME
db_host = settings.DB_HOST
db_port = settings.DB_PORT
db_password = settings.DB_PASSWORD
db_user = settings.DB_USER

DATABASE_URL = (
    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

# Added pool_pre_ping to prevent "Gone away" errors with Postgres
engine = create_engine(
    DATABASE_URL, 
    pool_pre_ping=True
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Helper function to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()