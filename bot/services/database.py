# bot/services/database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from bot.config import settings

class Database:
    def __init__(self):
        self.engine = create_async_engine(
            settings.DATABASE_URL,
            pool_size=20,
            max_overflow=10,
            pool_pre_ping=True
        )
        self.session_factory = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def get_session(self):
        async with self.session_factory() as session:
            yield session

db = Database()