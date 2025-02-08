# bot/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_TOKEN: str
    DATABASE_URL: str = "postgresql+asyncpg://user:pass@host/dbname"
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    YOOKASSA_SHOP_ID: str
    YOOKASSA_SECRET_KEY: str
    MINIO_ENDPOINT: str = "minio:9000"
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_USE_SSL: bool = False
    
    class Config:
        env_file = ".env"

settings = Settings()