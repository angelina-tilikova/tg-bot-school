from aiogram import types, F


from common import resend_message


from aiogram import Router, F

from aiogram.utils.markdown import hide_link



router = Router()


@router.message(F.text == "🧮 Неравенства")
async def cmd_hidden_link(message: types.Message):
    answer = f"{hide_link('https://disk.yandex.ru/i/z5t6I0-1CZPHuQ')}" + f"{text}"
    await resend_message(bot=message.bot, message=message, text=answer)
   

text = """
Неравенство — алгебраическое выражение, в котором используются знаки ≠ , &lt;, &gt;, ≤, ≥.
Числовое неравенство — это такое неравенство, в записи которого по обе стороны от знака находятся числа или числовые выражения.
Решение — значение переменной, при котором неравенство становится верным.
Решить неравенство значит найти множество, для которых оно выполняется.
Квадратное неравенство выглядит так: 
ax^2 + bx + c &gt; (&lt;; ≥; ≤; ≠ ) 0
где x — переменная,
a, b, c — числа,
при этом а ≠ 0.
Квадратное неравенство можно решить двумя способами:
графический метод;
метод интервалов. """



# @router.message(F.text == "🧮 Неравенства")
# async def with_puree(message: types.Message):
#     await resend_message(bot=message.bot, message=message, text=text)