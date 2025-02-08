# bot/utils/logging.py
import logging
from loguru import logger
from pythonjsonlogger import jsonlogger
from bot.config import settings

class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelname, self.format(record))

def setup_logging():
    logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)
    
    logger.add(
        "logs/bot.log",
        rotation="100 MB",
        retention="10 days",
        enqueue=True,
        backtrace=True,
        diagnose=True,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
    )
    
    # Интеграция с Loki
    class LokiHandler(logging.Handler):
        def emit(self, record):
            # Реализация отправки логов в Loki
            pass
    
    logging.getLogger().addHandler(LokiHandler())