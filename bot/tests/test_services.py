# bot\tests\test_services.py
import pytest
from tortoise import Tortoise
from models.user import User
from services.database import init_db

@pytest.fixture(scope="module")
async def db():
    await init_db()
    yield
    await Tortoise.close_connections()

@pytest.mark.asyncio
async def test_user_creation(db):
    user = await User.create(tg_id=12345, full_name="Test User")
    assert user.id is not None
    assert user.discount == 0

@pytest.mark.asyncio
async def test_discount_calculation(db):
    user = await User.create(tg_id=67890, full_name="Test User 2")
    for _ in range(15):
        await Order.create(user=user, service_type="test", amount=100)
    
    await apply_discount(user.tg_id)
    updated_user = await User.get(tg_id=67890)
    assert updated_user.discount == 10