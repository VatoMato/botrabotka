# bot\utils\logger.py
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger(name: str = "bot"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    # Консольный логгер
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # Файловый логгер с ротацией
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    file_handler = RotatingFileHandler(
        logs_dir / "bot.log",
        maxBytes=5*1024*1024,  # 5MB
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger