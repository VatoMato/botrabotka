# handlers/start.py
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Услуги'), KeyboardButton(text='Мои заказы')],
            [KeyboardButton(text='Помощь'), KeyboardButton(text='О нас')]
        ],
        resize_keyboard=True,
        input_field_placeholder=' '
    )
    await message.answer("Добро пожаловать!", reply_markup=markup)