# bot/handlers/orders.py
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from bot.models import Order, User
from bot.services import storage
from bot.tasks import schedule_closure

async def start_order_creation(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state("order_creation")
    await callback.message.answer("Прикрепите фото/видео объекта:")

async def process_media(message: types.Message, state: FSMContext):
    media_urls = []
    if message.photo:
        file = await message.photo[-1].download(destination_file="temp.jpg")
        url = await storage.upload_file(file.read(), "orders", f"{message.from_user.id}_{file.name}")
        media_urls.append(url)
    
    async with state.proxy() as data:
        data['media'] = media_urls
    
    await message.answer("Опишите объем работ:")

async def finalize_order(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        async with db.session() as session:
            user = await session.get(User, message.from_user.id)
            order = Order(
                user_id=user.id,
                media_urls=json.dumps(data['media']),
                description=message.text
            )
            session.add(order)
            await session.commit()
            schedule_closure.delay(order.id)
    
    await state.finish()
    await message.answer("Заказ создан!")