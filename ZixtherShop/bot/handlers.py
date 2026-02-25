# Module
import os, django

# Initialize Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZixtherShop.settings')
django.setup()

# Module
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

# My
from .keyboard import main_keyboard
from products.models import Product

# Setups
router = Router()
builder = InlineKeyboardBuilder()


#Handlers
@router.message(Command('start'))
async def startBot(message: types.Message):
    await message.answer('Bot is working.', reply_markup=main_keyboard)

@router.message(F.text == 'Info')
async def info(message: types.Message):
    await message.answer('Some info about Us.', reply_markup=main_keyboard)

@router.message(F.text == 'Products')
async def productsInfo(message: types.Message):
    await message.answer('Products.', reply_markup=main_keyboard)

@router.message(F.text == 'Your Order')
async def orderInfo(message: types.Message):
    await message.answer('Status of your order.', reply_markup=main_keyboard)