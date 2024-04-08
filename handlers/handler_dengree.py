from aiogram import types, F

from common import resend_message


from aiogram import Router, F

from aiogram.utils.markdown import hide_link


router = Router()

@router.message(F.text == "🆙 Свойства степеней")
async def cmd_hidden_link(message: types.Message):
    answer = f"{hide_link('https://disk.yandex.ru/i/Tc_p0c-wxNE39g')}" + f"{text}"
    await resend_message(bot=message.bot, message=message, text=answer)

text = ''' 
СВОЙСТВА СТЕПЕНЕЙ
'''


# @router.message(F.text == "🆙 Свойства степеней")
# async def with_puree(message: types.Message):
#     await resend_message(bot=message.bot, message=message, text=text)