from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from bot.handlers import register_handlers
from bot.utils.tracing import setup_tracing
from bot.config import load_config

async def start_bot():
    # Загрузка конфигурации
    config = load_config()
    
    # Инициализация бота и диспетчера
    bot = Bot(token=config.TELEGRAM_TOKEN)
    storage = RedisStorage2(host=config.REDIS_HOST, port=config.REDIS_PORT)
    dp = Dispatcher(bot, storage=storage)
    
    # Подключение middleware
    dp.middleware.setup(...)  # Пример: TracingMiddleware
    
    # Регистрация обработчиков
    register_handlers(dp)
    
    # Настройка трейсинга
    setup_tracing("telegram-bot")
    
    # Запуск поллинга (или вебхуков)
    await dp.start_polling()

# Для запуска через ASGI (если используется вебхук):
# app = dp.asgi_app