from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Your Order'),
            KeyboardButton(text='Products'),
            KeyboardButton(text='Info')
        ]
    ],
    resize_keyboard=True
)