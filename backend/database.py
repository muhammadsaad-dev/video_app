from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

db_name = settings.DB_NAME
db_host = settings.DB_HOST
db_port = settings.DB_PORT
db_password = settings.DB_PASSWORD
db_user = settings.DB_USER

DATABASE_URL = (
    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)