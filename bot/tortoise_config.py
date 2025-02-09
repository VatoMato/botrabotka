# bot\migrations\tortoise_config.py
from config import Config

TORTOISE_ORM = {
    "connections": {"default": Config.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["models.user", "models.order", "aerich.models"],
            "default_connection": "default",
        }
    },
}