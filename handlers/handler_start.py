
from aiogram import types, F
from aiogram.filters.command import Command

from common import resend_message
from keyboards.mainKb import globalKeyBoard

from aiogram import Router, F

router = Router()

text = """
🔓 <b>Добро пожаловать</b>! 🔓\nДанный бот разбирается в математике!
"""

# Хэндлер на команду /start
@router.message(F.text, Command("start"))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=globalKeyBoard, 
        resize_keyboard=True,
        input_field_placeholder="Выберите тему"
        )
    await resend_message(bot=message.bot, message=message, text=text, keyboard=keyboard)
