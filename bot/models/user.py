# bot/models/user.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from bot.services.database import db

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, unique=True)
    full_name = Column(String)
    discount_tier = Column(Integer, default=0)
    balance = Column(Float, default=0.0)
    
    @property
    def discount_percent(self) -> float:
        tiers = {
            0: 0.0,
            1: 0.10,
            2: 0.15,
            3: 0.20,
            4: 0.25
        }
        return tiers.get(self.discount_tier, 0.0)
    
    async def update_tier(self, session):
        order_count = await session.execute(
            select(func.count(Order.id))
            .where(Order.user_id == self.id)
        )
        count = order_count.scalar()
        self.discount_tier = min(count // 15, 4)