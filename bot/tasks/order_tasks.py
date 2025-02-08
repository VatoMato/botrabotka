# bot/tasks/order_tasks.py
from celery import Celery
from bot.services.database import db
from bot.models.order import Order
from datetime import datetime, timedelta

app = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/1',
    task_serializer='json',
    result_serializer='json',
)

@app.task
async def auto_close_order(order_id: int):
    async with db.session_factory() as session:
        order = await session.get(Order, order_id)
        if order.status == 'completed':
            order.status = 'closed'
            await session.commit()
            # Уведомление пользователя
            await notify_user(order.user_id, "Заказ закрыт автоматически")

@app.task
async def schedule_closure(order_id: int):
    eta = datetime.utcnow() + timedelta(hours=3)
    auto_close_order.apply_async(args=[order_id], eta=eta)