import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, html
from aiogram.types import Message
from aiogram.filters.command import Command
from datetime import datetime
from aiogram.enums import ParseMode
from common import resend_message
from config_reader import config

from handlers import handler_start

from KeyboardButton import text1, text2

# Для записей с типом Secret* необходимо 
# вызывать метод get_secret_value(), 
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Диспетчер
dp = Dispatcher()
dp.include_routers(handler_start.router)

@dp.message(F.text == "📈 Проценты")
async def with_puree(message: types.Message):
    await resend_message(bot=bot, message=message, text=text1)
    
@dp.message(F.text == "🔪 Формулы сокращенного умножения")
async def with_puree(message: types.Message):
    await resend_message(bot=bot, message=message, text=text2)
    
# Хэндлер на команду /stop
@dp.message(Command("stop"))
async def cmd_start(message: types.Message):
    await resend_message(bot=bot, message=message, text="🔒 <b>До свидания</b>! 🔒\nЖдем вас снова в мире математики!", keyboard=types.reply_keyboard_remove.ReplyKeyboardRemove())


    
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())