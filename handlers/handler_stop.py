from aiogram import types, F
from aiogram.filters.command import Command

from common import resend_message
from keyboards.mainKb import globalStopKeyBoard

from aiogram import Router, F


router = Router()

text = '''
🔒 <b>До свидания</b>! 🔒\nЖдем вас снова в мире математики!
'''


@router.message(F.text, Command("stop"))
async def cmd_stop(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=globalStopKeyBoard, 
        resize_keyboard=True,
        input_field_placeholder="для начала введите /start"
        )
    await resend_message(bot=message.bot, message=message, text=text, keyboard=keyboard )
    