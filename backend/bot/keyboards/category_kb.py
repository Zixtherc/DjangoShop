from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

choosing_category = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Your Order'),
            KeyboardButton(text='Products'),
            KeyboardButton(text='Info')
        ]
    ],
    resize_keyboard=True
)