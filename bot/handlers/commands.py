# bot/handlers/commands.py
from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def start_command(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Услуги'), KeyboardButton(text='Мои заказы')],
            [KeyboardButton(text='Помощь'), KeyboardButton(text='О нас')]
        ],
        resize_keyboard=True,
        input_field_placeholder=' '
    )
    await message.answer("Добро пожаловать!", reply_markup=keyboard)

async def services_handler(callback: types.CallbackQuery):
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton(text=service, callback_data=f"service_{service}")
        for service in ['Уборка', 'Химчистка', 'Озоновая дезинфекция', 'Электрика', 'Сантехника']
    ]
    inline_keyboard.add(*buttons)
    await callback.message.edit_text("Выберите категорию:", reply_markup=inline_keyboard)