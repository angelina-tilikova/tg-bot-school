import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from config_reader import config

from handlers import handler_start, handler_stop, handler_procent, handler_formul,handler_dengree, handler_proportion, handler_ineq, handler_link




# Для записей с типом Secret* необходимо 
# вызывать метод get_secret_value(), 
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Диспетчер
dp = Dispatcher()
dp.include_routers(
    handler_start.router, 
    handler_stop.router,
    handler_procent.router, 
    handler_formul.router, 
    handler_dengree.router, 
    handler_proportion.router,
    handler_ineq.router,
    handler_link.router
)


    
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())