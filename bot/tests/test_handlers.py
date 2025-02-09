# bot\tests\test_handlers.py
import pytest
from aiogram import Dispatcher
from aiogram.methods import SendMessage
from handlers.start import cmd_start

@pytest.mark.asyncio
async def test_start_handler():
    dispatcher = Dispatcher()
    result = await cmd_start(dispatcher, message=MockMessage())
    assert isinstance(result, SendMessage)
    assert "Добро пожаловать" in result.text

class MockMessage:
    from_user = MockUser()
    answer = lambda self, text: text

class MockUser:
    id = 12345
    first_name = "Test"
    last_name = "User"