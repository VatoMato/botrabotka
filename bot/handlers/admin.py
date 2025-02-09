# bot\handlers\admin.py
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from models.user import User
from models.order import Order

admin_router = Router()

# Фильтр для проверки админских прав
async def admin_filter(message: Message) -> bool:
    return str(message.from_user.id) in Config.ADMINS

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
    order_id = callback.message.text.split("#")[1]
    order = await Order.get(id=order_id)
    order.status = "force_closed"
    await order.save()
    await callback.answer("Заказ принудительно закрыт")