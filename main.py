import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


from app.handlers import user


logging.basicConfig(level=logging.INFO)


dp = Dispatcher()


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TG_TOKEN'),default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(user)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выключение бота')
        