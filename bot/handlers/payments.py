# bot/handlers/payments.py
from aiogram import types
from yookassa import Payment, Configuration
from bot.config import settings

Configuration.account_id = settings.YOOKASSA_SHOP_ID
Configuration.secret_key = settings.YOOKASSA_SECRET_KEY

async def create_payment(order_amount: float, description: str) -> str:
    payment = Payment.create({
        "amount": {
            "value": order_amount,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": settings.PAYMENT_RETURN_URL
        },
        "capture": True,
        "description": description
    })
    return payment.confirmation.confirmation_url

async def process_payment_callback(callback: types.CallbackQuery):
    # Логика верификации платежа
    payment_id = callback.data.split(':')[1]
    payment = Payment.find_one(payment_id)
    
    if payment.status == 'succeeded':
        await callback.message.answer("Оплата прошла успешно!")
        # Обновление статуса заказа в БД
    else:
        await callback.message.answer("Ошибка оплаты")