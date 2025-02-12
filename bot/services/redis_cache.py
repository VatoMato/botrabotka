# bot\services\redis_cache.py
from redis import asyncio as aioredis
from models.user import User

redis = aioredis.from_url("redis://localhost")

async def cache_user_data(user_id: int):
    cached = await redis.get(f"user_{user_id}")
    if not cached:
        user = await User.get(tg_id=user_id)
        await redis.setex(f"user_{user_id}", 3600, user.json())
    return cached