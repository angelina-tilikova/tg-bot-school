from aiogram import types, F
from aiogram.filters.command import Command

from common import resend_message


from aiogram import Router, F

from aiogram.utils.markdown import hide_link

router = Router()

@router.message(F.text == "➗ Пропорции")
async def cmd_hidden_link(message: types.Message):
    answer = f"{hide_link('https://disk.yandex.ru/i/vqZzhKrUQg61oQ')}" + f"{text}"
    await resend_message(bot=message.bot, message=message, text=answer)



text = ''' 
<b>Пропо́рция</b> — равенство отношений двух [и более] пар чисел a, b и c, d, т. е. равенство вида a:b=c:d, 
в этом случае a и d называют крайними, b и c — средними членами пропорции.
Так же пропорции могут быть вида: a/b = c/d, но и в этом случае
a и d называют крайними, b и c — средними членами пропорции.
Для пропорции будет верно выражение:
<b> Произведение крайних членов равно произведению средних членов пропорции.</b>
<b>ab = cd.</b>
'''


# @router.message(F.text == "➗ Пропорции")
# async def with_puree(message: types.Message):
#     await resend_message(bot=message.bot, message=message, text=text)