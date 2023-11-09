from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
import enum

class MarkupName(enum.Enum):
    start = 1

def get_inline_user(markup_name, param=None):
    markup = None

    if (markup_name == MarkupName.start):
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                InlineKeyboardButton('Регистрация', callback_data='registration_login'),
                ]
            ]
        )
        return markup

    return markup

