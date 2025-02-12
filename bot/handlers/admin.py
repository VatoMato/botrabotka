# bot\handlers\admin.py        Исправлено по Промту 14
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from models.user import User
from models.order import Order
from bot.config import Config

admin_router = Router()

# Фильтр с проверкой существования from_user
async def admin_filter(message: Message) -> bool:
    return message.from_user is not None and message.from_user.id in Config.ADMINS

@admin_router.message(Command("admin"), admin_filter)
async def admin_panel(message: Message):
    text = (
        "📊 Админ-панель:\n"
        "Статистика за последние 24 часа:\n"
        f"Пользователи: {await User.all().count()}\n"
        f"Заказы: {await Order.filter(status='completed').count()}"
    )
    await message.answer(text)

@admin_router.callback_query(F.data == "force_close_order")
async def force_close_order(callback: CallbackQuery):
    # Проверка доступности сообщения и его текста
    if not callback.message or not isinstance(callback.message, Message):
        await callback.answer("Сообщение недоступно")
        return
    
    message_text = callback.message.text
    if not message_text:
        await callback.answer("Текст сообщения отсутствует")
        return
    
    # Безопасное извлечение order_id
    try:
        order_id_part = message_text.split("#")[1]
        order_id = order_id_part.split()[0].strip()
    except (IndexError, AttributeError):
        await callback.answer("Ошибка в формате заказа")
        return
    
    # Проверка существования заказа
    order = await Order.get_or_none(id=order_id)
    if not order:
        await callback.answer("Заказ не найден")
        return
    
    order.status = "force_closed"
    await order.save()
    await callback.answer("Заказ принудительно закрыт")