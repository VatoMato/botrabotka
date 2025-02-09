# bot\utils\validators.py
import re
from aiogram.types import Message
from datetime import datetime

PHONE_REGEX = re.compile(r"^\+7\d{10}$")
DATE_REGEX = re.compile(r"^\d{2}\.\d{2}\.\d{4}$")

async def validate_phone(message: Message) -> bool:
    return bool(PHONE_REGEX.match(message.text))

async def validate_date(message: Message) -> bool:
    if not DATE_REGEX.match(message.text):
        return False
    try:
        datetime.strptime(message.text, "%d.%m.%Y")
        return True
    except ValueError:
        return False