# bot\services\database.py
from tortoise import Tortoise
from config import Config
from models.order import Order
from models.user import User

async def init_db():
    await Tortoise.init(
        db_url=Config.DATABASE_URL,
        modules={'models': ['models.user', 'models.order']}
    )
    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close_connections()

async def get_user_orders(user_id: int):
    return await Order.filter(user_id=user_id).all()

async def apply_discount(user_id: int):
    user = await User.get(tg_id=user_id)
    order_count = await user.orders.filter(status="completed").count()
    
    if order_count >= 41:
        user.discount = 25
    elif order_count >= 31:
        user.discount = 20
    elif order_count >= 16:
        user.discount = 15
    elif order_count >= 1:
        user.discount = 10
    
    await user.save()