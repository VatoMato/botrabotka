# bot\handlers\services.py
from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline import services_catalog, cleaning_types

service_router = Router()

@service_router.callback_query(F.data.startswith("service_"))
async def handle_service(callback: CallbackQuery):
    service_type = callback.data.split("_")[1]
    if service_type == "clean":
        await callback.message.edit_text(
            "Выберите тип уборки:",
            reply_markup=cleaning_types()
        )