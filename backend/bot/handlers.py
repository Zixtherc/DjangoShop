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

from asgiref.sync import sync_to_async

# My
from .keyboard import main_keyboard
from bot.requests import create_order, get_orders, get_product
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
    # try:
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
    # except Exception:
    #     await message.answer(f'An error with finding all products.')

@router.message(F.text == 'Your Order')
async def orderInfo(message: types.Message, state: FSMContext):
    await message.answer('Send your email.', reply_markup=main_keyboard)
    await state.set_state(Form.waiting_for_email)

@router.message(Form.waiting_for_email)
async def findOrder(message: types.Message, state: FSMContext):
    email_input = message.text.strip()
    user = await User.objects.filter(email=email_input).afirst()

    if not user:
        await message.answer('User not found')
        await state.clear()
        return 

    try:
        user.tg_id = message.from_user.id
        await user.asave()

        response = await get_orders(user_id=user.id)

        if not response:
            await message.answer("You don't have an order.")
        else:
            text = "Your orders:\n" + "\n".join(
                [f"- Order #{o['id']}, status: {o['status']}" for o in response]
            )
            await message.answer(text)
            
    except Exception as e:
        print(f"Error: {e}")
        await message.answer('An error occurred while finding your email.')
    
    finally:
        await state.clear()