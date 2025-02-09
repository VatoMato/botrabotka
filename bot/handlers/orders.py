# handlers/orders.py
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from models.order import Order
from models.user import User
from services.yookassa import create_payment
from services.scheduler import schedule_order_close

orders_router = Router()

@orders_router.callback_query(F.data.startswith("create_order_"))
async def create_order(callback: CallbackQuery, state: FSMContext):
    service_type = callback.data.split("_")[2]
    await state.update_data(service_type=service_type)
    await callback.message.answer("Пришлите фото/видео объекта:")

@orders_router.message(F.photo | F.video)
async def handle_media(message: Message, state: FSMContext):
    data = await state.get_data()
    media_id = message.photo[-1].file_id if message.photo else message.video.file_id
    
    # Сохраняем медиа во временное хранилище
    order = await Order.create(
        user_id=message.from_user.id,
        service_type=data['service_type'],
        media_id=media_id
    )
    
    # Создаем платеж
    payment = await create_payment(1000, order.id)
    await message.answer(f"Оплатите заказ: {payment.confirmation.confirmation_url}")

    # Планируем автоматическое закрытие
    await schedule_order_close(order.id)