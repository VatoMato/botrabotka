# keyboards/inline.py
from aiogram.utils.keyboard import InlineKeyboardBuilder

def services_catalog():
    builder = InlineKeyboardBuilder()
    builder.button(text="Уборка", callback_data="service_clean")
    builder.button(text="Химчистка", callback_data="service_chem")
    builder.adjust(2)
    return builder.as_markup()

def cleaning_types():
    builder = InlineKeyboardBuilder()
    builder.button(text="Генеральная", callback_data="clean_general")
    builder.button(text="Текущая", callback_data="clean_regular")
    builder.adjust(1)
    return builder.as_markup()