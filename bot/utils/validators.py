# bot\utils\validators.py     Исправленно по Промту 15
import re
from aiogram.types import Message
from datetime import datetime

PHONE_REGEX = re.compile(r"^\+7\d{10}$")
DATE_REGEX = re.compile(r"^\d{2}\.\d{2}\.\d{4}$")

async def validate_phone(message: Message) -> bool:
    text = message.text or ""
    return bool(PHONE_REGEX.fullmatch(text))

async def validate_date(message: Message) -> bool:
    text = message.text or ""
    if not DATE_REGEX.fullmatch(text):
        return False
    try:
        datetime.strptime(text, "%d.%m.%Y")
        return True
    except ValueError:
        return False