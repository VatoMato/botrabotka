# bot\keyboards\main_menu.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Услуги'), KeyboardButton(text='Мои заказы')],
            [KeyboardButton(text='Помощь'), KeyboardButton(text='Мои скидки')]
        ],
        resize_keyboard=True,
        input_field_placeholder='Выберите действие'
    )

def admin_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Статистика'), KeyboardButton(text='Активные заказы')],
            [KeyboardButton(text='Споры'), KeyboardButton(text='Рассылка')]
        ],
        resize_keyboard=True
    )