from config.config import TELEGRAM_BOT_TOKEN

import asyncio
import logging
from aiogram import Bot, Dispatcher
from app.handlers.common import router as command_router


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(command_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())