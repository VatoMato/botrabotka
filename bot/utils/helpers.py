# utils/helpers.py
from datetime import datetime, timedelta

def calculate_deadline(hours: int = 3) -> datetime:
    return datetime.now() + timedelta(hours=hours)

async def delete_media(media_id: str):
    # Логика удаления медиа из хранилища
    pass

async def close_order(order_id: str):
    order = await Order.get(id=order_id)
    if order.status == "completed":
        await delete_media(order.media_id)
        await order.delete()