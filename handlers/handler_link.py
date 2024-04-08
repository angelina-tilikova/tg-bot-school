from aiogram import types, F

from common import resend_message_without_preview


from aiogram import Router, F

from aiogram.utils.markdown import hide_link


router = Router()



text = ''' 
ПОЛЕЗНЫЕ ССЫЛКИ:

- <a href="https://spacemath.xyz/procenti/">Полезная ин-фа.Нет степеней, остальное есть(нажмите на текст)</a>

- <a href="https://youclever.org/book/stepen-i-ee-svojstva-1/">Свойства степеней</a>
'''

@router.message(F.text == "📩 Полезные ссылки")
async def with_puree(message: types.Message):
    await resend_message_without_preview(bot=message.bot, message=message, text=text)
