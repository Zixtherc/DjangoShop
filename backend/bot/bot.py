import asyncio

from aiogram import Bot,Dispatcher
from bot.config.settings import TOKEN

from bot.handlers.start_bot import start_router
from bot.handlers.orders_handlers import order_router
from bot.handlers.products_handlers import products_router

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(router=start_router)
    dp.include_router(router=products_router)
    dp.include_router(router=order_router)


    
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        print('Bot is running')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Shutting Down')