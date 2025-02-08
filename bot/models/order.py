# bot/models/order.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from .sharding import get_shard

Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    service_type = Column(String)
    status = Column(String, default='created')
    media_urls = Column(String)  # JSON список URL медиафайлов
    created_at = Column(DateTime)
    
    __table_args__ = {
        'postgresql_partition_by': 'HASH (user_id)',
        'postgresql_partitions': '4'
    }

    @classmethod
    async def create(cls, session, **kwargs):
        shard_id = get_shard(kwargs['user_id'])
        async with session.bind(shard_id=shard_id) as shard_session:
            order = cls(**kwargs)
            shard_session.add(order)
            await shard_session.commit()
            return order