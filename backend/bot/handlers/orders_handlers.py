# Module
import os, django, random, string

# Initialize Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZixtherShop.settings')
django.setup()

# Module
from aiogram import types, Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, FSInputFile

# My
from ..keyboards.main_kb import main_keyboard
from ..keyboards.order_kb import creating_order
from bot.requests import create_order, get_orders, get_categories, get_product, add_to_cart
from user.models import User
from ZixtherShop.settings import BASE_DIR


# Setups
order_router = Router()

class Form(StatesGroup):
    waiting_for_email = State()

    choosing_category = State()
    waiting_for_name = State()
    waiting_for_description = State()

    create_order_email = State()

@order_router.message(F.text == 'Your Order')
async def orderInfo(message: types.Message, state: FSMContext):
    await message.answer('Send your email.', reply_markup=creating_order)
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

@order_router.message(F.text == 'Create Order')
async def choosingCategory(message: types.Message, state: FSMContext):
    category_builder = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        category_builder.add(
            InlineKeyboardButton(
                text=category.category_name,
                callback_data=f'category_{category.id}',
        )
    )
    await message.answer(
        'Choose category:', 
        reply_markup=category_builder.adjust(2).as_markup()
    )

@order_router.callback_query(F.data.startswith('category_'))
async def choosingProducts(callback: types.CallbackQuery):
    category_id = callback.data.split('_')[-1]
    
    products = await get_product(category_id=category_id)
    
    if not products:
        await callback.message.answer("No products in this category.")
        await callback.answer()
        return
    
    for product in products:
        buy_builder = InlineKeyboardBuilder()
        buy_builder.add(types.InlineKeyboardButton(
            text=f"Add in cart {product.name}",
            callback_data=f"cart_{product.id}")
        )

    # for product in products:
    #     buy_builder = InlineKeyboardBuilder()
    #     buy_builder.add(types.InlineKeyboardButton(
    #         text=f"Add in cart {product.name}",
    #         callback_data=f"cart_{product.id}")
    #     )
    #     image_path = os.path.join(BASE_DIR, 'media', str(product.image))
        
    #     caption_text = f"{product.name}\n\n{product.description}\n\nPrice: {product.price} ₴"

    #     if os.path.exists(image_path):
    #         await callback.message.answer_photo(
    #             photo=FSInputFile(image_path),
    #             caption=caption_text,
    #             reply_markup=buy_builder.as_markup(),
    #             parse_mode="Markdown"
    #         )
    #     else:
    #         await callback.message.answer(
    #             f"{caption_text}\nLost Photo.",
    #             reply_markup=buy_builder.as_markup(),
    #             parse_mode="Markdown"
    #         )
    # await callback.answer()


@order_router.callback_query(F.data.startwith('cart_'))
async def addToCart(callback: types.CallbackQuery):
    cart = await add_to_cart(product_id=callback.data.split('_')[-1], user_id= callback.from_user.id, quantity=None)
    # in progress     

@order_router.callback_query(F.data.startswith('buy_'))
async def buyProduct(callback: types.CallbackQuery):
    product_id = callback.data.split('_')[-1]
    product = await get_product(product_id=product_id)

    unique_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k= 6))
    CARD = '4483 8200 3075 8402'

    buy_builder = InlineKeyboardBuilder() 
    buy_builder.add(types.InlineKeyboardButton(
            text=f"Confirm",
            callback_data=f"confirm_{product.id}_{unique_code}")
    )
    
    order = await create_order(user= callback.from_user.id, products_id=product_id)
    await callback.message.answer(
        "<b>Payment Information</b>\n\n"
        f"<b>Amount:</b> {int(product.price)} UAH\n"
        f"<b>Card:</b> <code>{CARD}</code>\n"
        f"<b>Comment:</b> <code>{unique_code}</code>\n\n"
        "After payment, click the button below.",
        reply_markup=buy_builder.as_markup(),
        parse_mode='HTML'
    )


@order_router.callback_query(F.data.startswith('confirm_'))
async def confirmOrder( callback: types.CallbackQuery):
    pass