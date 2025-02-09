# handlers/dispute.py
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

dispute_router = Router()

@dispute_router.callback_query(F.data == "dispute_order")
async def start_dispute(callback: CallbackQuery):
    await callback.message.answer("Пришлите фото/видео отчет для оспаривания:")

@dispute_router.message(F.photo | F.video)
async def handle_dispute_media(message: Message):
    # Логика обработки спора
    await message.answer("Ваш спор принят в обработку. Мы свяжемся с вами в течение 24 часов.")