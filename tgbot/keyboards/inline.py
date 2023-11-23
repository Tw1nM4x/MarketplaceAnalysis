from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
import enum

class MarkupName(enum.Enum):
    start = 1
    profile = 2

def get_inline_user(markup_name, param=None):
    markup = None

    if (markup_name == MarkupName.start):
        markup = ReplyKeyboardMarkup(
            keyboard=[
                [
                KeyboardButton('Поделиться геолокацией 📍', request_location=True)
                ]
            ], row_width=1
            )
        return markup
    if (markup_name == MarkupName.profile):
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                InlineKeyboardButton('Преобрести/продлить подписку', callback_data='buy_sub'),
                ]
            ]
        )
        return markup

    return markup

