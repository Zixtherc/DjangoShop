# Module
import os, django

# Initialize Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZixtherShop.settings')
django.setup()

# Module
from aiogram import types, Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.requests import get_product

# Setups
products_router = Router()
builder = InlineKeyboardBuilder()

class Form(StatesGroup):
    waiting_for_email = State()

@products_router.message(F.text == 'Products')
async def productsInfo(message: types.Message):
    try:
        response = await get_product()
        if not response:
            await message.answer('No product in storage.')
            return
        
        else:
            text = 'All products\n'
            for product in response:
                text += f'- Name:{product['product_name']}, price:{product['product_price']}, description:{product['description']}, quantity{product['quantity']}.'
                await message.answer(text)
            else:
                await message.answer("We don't have a product that meets your requirements.")
    except Exception:
        await message.answer(f'An error with finding all products.')