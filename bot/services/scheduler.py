# services/scheduler.py
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils.helpers import close_order
from services.database import close_db

scheduler = AsyncIOScheduler()

async def schedule_order_close(order_id: str):
    scheduler.add_job(
        close_order,
        'date',
        run_date=calculate_deadline(),
        args=[order_id]
    )

def start_scheduler():
    scheduler.start()
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        close_db()