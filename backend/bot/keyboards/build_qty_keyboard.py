from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def build_qty_kb(product_id: int, qty: int):
    builder = InlineKeyboardBuilder()

    builder.row(
        types.InlineKeyboardButton(
            text="—",
            callback_data=f"qty_{product_id}_minus"
        ),
        types.InlineKeyboardButton(
            text=str(qty),
            callback_data="noop"
        ),
        types.InlineKeyboardButton(
            text="+",
            callback_data=f"qty_{product_id}_plus"
        )
    )

    builder.row(
        types.InlineKeyboardButton(
            text="Add to cart.",
            callback_data=f"cart_{product_id}_{qty}"
        )
    )

    return builder.as_markup()