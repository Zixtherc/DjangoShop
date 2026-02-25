import asyncio

from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command
from bot.config.settings import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def startBot(message: types.Message):
    await message.answer('Bot is working')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Shutting Down')