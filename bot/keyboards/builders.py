# bot\keyboards\builders.py
from aiogram.utils.keyboard import InlineKeyboardBuilder

def dynamic_pagination(total_pages: int, current_page: int) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    
    if current_page > 1:
        builder.button(text="⬅️ Назад", callback_data=f"page_{current_page-1}")
    if current_page < total_pages:
        builder.button(text="Вперед ➡️", callback_data=f"page_{current_page+1}")
        
    builder.adjust(2)
    return builder