# bot\services\web_server.py
from aiohttp import web
from bot.handlers.payments import payment_webhook  # Исправленый импорт по Промту 18

app = web.Application()
app.router.add_post('/yookassa-webhook', payment_webhook)

async def start_web():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()