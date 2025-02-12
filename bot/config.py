# bot\config.py    Исправленно по Промту 13,14
from dotenv import load_dotenv
import os

load_dotenv()

def get_env_var(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"Переменная окружения {name} не найдена")
    return value

class Config:
    BOT_TOKEN = get_env_var("BOT_TOKEN")
    ADMIN_ID = int(get_env_var("ADMIN_ID"))  # Важно преобразование в int
    ADMINS = [ADMIN_ID]  # Теперь содержит целые числа
    YOOKASSA_SHOP_ID = get_env_var("YOOKASSA_SHOP_ID")
    YOOKASSA_SECRET_KEY = get_env_var("YOOKASSA_SECRET_KEY")
    WEBHOOK_URL = "https://your-domain.com"  # Публичный адрес вашего сервера

    POSTGRES_DB = get_env_var("POSTGRES_DB")
    POSTGRES_USER = get_env_var("POSTGRES_USER")
    POSTGRES_PASSWORD = get_env_var("POSTGRES_PASSWORD")
    POSTGRES_HOST = get_env_var("POSTGRES_HOST")
    
    DATABASE_URL = f"asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"