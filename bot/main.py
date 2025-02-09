import asyncio
from aiogram import Bot, Dispatcher
from config import Config
from handlers import (
    start_router,
    service_router,
    orders_router,
    payment_router,
    dispute_router
)
from services.database import init_db, close_db
from services.scheduler import start_scheduler

async def main():
    await init_db()
    
    bot = Bot(token=Config.BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_routers(
        start_router,
        service_router,
        orders_router,
        payment_router,
        dispute_router
    )
    
    try:
        await dp.start_polling(bot)
    finally:
        await close_db()

if __name__ == "__main__":
    asyncio.run(main())
    start_scheduler()