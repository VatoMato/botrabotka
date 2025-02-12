# bot\tests\test_handlers.py     Исправленно по Промту 17
import pytest
from aiogram import Dispatcher
from aiogram.methods import SendMessage
from handlers.start import cmd_start

class MockUser:
    id = 12345
    first_name = "Test"
    last_name = "User"

class MockMessage:
    from_user = MockUser()
    answer = lambda self, text: text

@pytest.mark.asyncio
async def test_start_handler():
    dispatcher = Dispatcher()
    result = await cmd_start(dispatcher, message=MockMessage())
    assert isinstance(result, SendMessage)
    assert "Добро пожаловать" in result.text