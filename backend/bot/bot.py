import asyncio

from aiogram import Bot,Dispatcher
from bot.config.settings import TOKEN

from .handlers import router

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(router=router)
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        print('Bot is running')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Shutting Down')