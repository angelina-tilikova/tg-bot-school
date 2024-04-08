from aiogram import types, F
from aiogram.filters.command import Command

from common import resend_message


from aiogram import Router, F

from aiogram.utils.markdown import hide_link

router = Router()

@router.message(F.text == "🔪 Формулы сокращенного умножения")
async def cmd_hidden_link(message: types.Message):
    answer = f"{hide_link('https://disk.yandex.ru/i/UkAgg5gy-xqxqQ')}" + f"{text}"
    await resend_message(bot=message.bot, message=message, text=answer)


text = ''' 
ФОРМУЛЫ СОКРАЩЕННОГО УМНОЖЕНИЯ
'''


# @router.message(F.text == "🔪 Формулы сокращенного умножения")
# async def with_puree(message: types.Message):
#     await resend_message(bot=message.bot, message=message, text=text)