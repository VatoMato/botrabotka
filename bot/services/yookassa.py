# services\yookassa.py
from yookassa import Configuration, Payment
from config import Config

Configuration.account_id = Config.YOOKASSA_SHOP_ID
Configuration.secret_key = Config.YOOKASSA_SECRET_KEY

async def create_payment(amount, order_id):
    payment = Payment.create({
        "amount": {
            "value": amount,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://t.me/your_bot"
        },
        "metadata": {
            "order_id": str(order_id)
        }
    })
    return payment