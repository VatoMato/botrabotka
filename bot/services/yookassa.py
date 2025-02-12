# bot\services\yookassa.py     Изменен по Промту 12, 18

from yookassa import Configuration, Payment, Webhook
from config import Config
import asyncio
from aiohttp import web  # Добавляем импорт для работы с web.Request

Configuration.account_id = Config.YOOKASSA_SHOP_ID
Configuration.secret_key = Config.YOOKASSA_SECRET_KEY

from yookassa.domain.common import SecurityHelper     # Изменен по Промту 18

def is_trusted_ip(ip: str) -> bool:                   # Изменен по Промту 18
    return SecurityHelper().is_ip_trusted(ip)  # Проверка доверенных IP ЮKassa:cite[5]

from yookassa.domain.notification import WebhookNotificationFactory     # Изменен по Промту 18

class YooKassaService:                                # Изменен по Промту 18
    @staticmethod
    async def validate_webhook(request: web.Request):     # Изменен по Промту 18
        event_json = await request.json()
        return WebhookNotificationFactory().create(event_json)  # Правильный метод:cite[5]:cite[8]
    
    @staticmethod
    async def create_payment(amount: float, order_id: int, bot_username: str):
        try:
            payment_data = {
                "amount": {
                    "value": f"{amount:.2f}",
                    "currency": "RUB"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": f"https://t.me/{bot_username}?start=order_{order_id}"
                },
                "metadata": {
                    "order_id": str(order_id),
                    "bot_username": bot_username
                },
                "capture": True
            }

            result = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: Payment.create(payment_data)
            )
            
            if not getattr(result, 'id', None):
                raise ValueError("Не удалось создать платеж в ЮKassa")
                
            return result
        
        except Exception as e:
            print(f"YooKassa API Error: {str(e)}")
            raise
