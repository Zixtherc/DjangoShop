from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Catalog'),
            KeyboardButton(text='Cart')
        ],
        [
            KeyboardButton(text='Create Order'),
            KeyboardButton(text='Your Order')
        ],
        [
            KeyboardButton(text='Info')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Select menu item."
)