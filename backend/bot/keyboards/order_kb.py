from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

creating_order = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Your Order'),
            KeyboardButton(text='Products'),
            KeyboardButton(text='Info')
        ]
    ],
    resize_keyboard=True
)