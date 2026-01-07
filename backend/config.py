from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    SECRET_KEY: str 
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    # Updated syntax for Pydantic Settings v2
    model_config = SettingsConfigDict(
        env_file="backend/.env", 
        env_file_encoding="utf-8",
        extra="ignore" # This prevents errors if you have extra stuff in your .env
    )

settings = Settings()