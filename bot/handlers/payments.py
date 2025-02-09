#  handlers/payment.py
from aiogram import Router
from aiogram.types import Message
from yookassa import Payment
from models.order import Order

payment_router = Router()

@payment_router.message(F.successful_payment)
async def successful_payment(message: Message):
    payment_info = message.successful_payment
    payment = Payment.find_one(payment_info.provider_payment_charge_id)
    
    order = await Order.get(id=payment.metadata.order_id)
    order.status = "paid"
    await order.save()
    
    await message.answer("Оплата прошла успешно! Ваш заказ активирован.")