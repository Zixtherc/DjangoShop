# Module
import os, django

# Initialize Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZixtherShop.settings')
django.setup()

# Module
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

# My
from .keyboard import main_keyboard
from bot.requests import create_order, get_orders, get_products
from user.models import User

# Setups
router = Router()
builder = InlineKeyboardBuilder()

class Form(StatesGroup):
    waiting_for_email = State()

#Handlers
@router.message(Command('start'))
async def startBot(message: types.Message):
    await message.answer('Bot is working.', reply_markup=main_keyboard)

@router.message(F.text == 'Info')
async def info(message: types.Message):
    await message.answer('Some info about Us.', reply_markup=main_keyboard)

@router.message(F.text == 'Products')
async def productsInfo(message: types.Message):
    try:
        response = get_products()
        if not response:
            await message.answer('No product in storage.')
            return
        
        else:
            text = 'All products\n'
            for product in response:
                text += f'- Name:{product['product_name']}, price:{product['product_price']}, description:{product['description']}, quantity{product['quantity']}.'
                await message.answer(text)
    except Exception:
        await message.answer(f'An error with finding all products.')
    await message.answer('Products.', reply_markup=main_keyboard)

@router.message(F.text == 'Your Order')
async def orderInfo(message: types.Message, state: FSMContext):
    await message.answer('Status of your order.', reply_markup=main_keyboard)
    await state.set_state(Form.waiting_for_email)

@router.message(Form.waiting_for_email)
async def findOrder(message: types.Message, state: FSMContext):
    try:
        user = User.objects.filter(email= message.text.strip().first)
        if not user:
            await message.answer('User not found')
            await state.clear()
            return 
        response = get_orders(user_id=user.id)

        if not response:
            await message.answer("You don't have an order.")
            await state.clear()
            return
        
        else:
            text= 'Yours orders\n'
            for order in response:
                text += f'- Order #{order['id']}, status:{order['status']}.'
                await message.answer(text)
    except Exception:
        await message.answer('An error with finding your email.')