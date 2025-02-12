# bot\handlers\payments.py     Измененно по Промту 19
from aiogram import Router, F
from aiogram.types import Message, ContentType
from aiohttp import web
from models.order import Order
from services.yookassa import YooKassaService

payment_router = Router()

async def payment_webhook(request: web.Request):
    try:
        event = await YooKassaService.validate_webhook(request)
        if event.event == 'payment.succeeded':
            payment = event.object
            order_id = payment.metadata.get('order_id')
            if order_id:
                order = await Order.get(id=int(order_id))
                order.status = "paid"
                await order.save()
        return web.Response(status=200)
    except Exception as e:
        print(f"Webhook error: {str(e)}")
        return web.Response(status=400)

@payment_router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message):
    # ... существующий код обработки платежей через Telegram ...