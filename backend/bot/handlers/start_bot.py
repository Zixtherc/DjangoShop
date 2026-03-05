# Module
from aiogram import types, F, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# My
from ..keyboard import main_keyboard

# Setups
builder = InlineKeyboardBuilder()
start_router = Router()

@start_router.message(Command('start'))
async def startBot(message: types.Message):
    await message.answer('Bot is working.', reply_markup=main_keyboard)

@start_router.message(F.text == 'Info')
async def info(message: types.Message):
    await message.answer('Some info about Us.', reply_markup=main_keyboard)