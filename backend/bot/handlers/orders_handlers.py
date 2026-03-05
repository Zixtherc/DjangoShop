# Module
import os, django

# Initialize Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZixtherShop.settings')
django.setup()

# Module
from aiogram import types, Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

# My
from ..keyboard import main_keyboard
from bot.requests import create_order, get_orders
from user.models import User

# Setups
order_router = Router()
builder = InlineKeyboardBuilder()

class Form(StatesGroup):
    waiting_for_email = State()

@order_router.message(F.text == 'Your Order')
async def orderInfo(message: types.Message, state: FSMContext):
    await message.answer('Send your email.', reply_markup=main_keyboard)
    await state.set_state(Form.waiting_for_email)

@order_router.message(Form.waiting_for_email)
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