import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from body import menu
from object import config, microtik
from aiogram import F
API_TOKEN = config.token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)


async def main():
    dp = Dispatcher()
    dp.message.register(menu.on_start_command, Command(commands='start'))
    dp.message.register(menu.choice_object, F.text == "Начать прослушивание микротика на объекте🛂")
    dp.callback_query.register(microtik.work, lambda c: c.data.startswith('_'))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
