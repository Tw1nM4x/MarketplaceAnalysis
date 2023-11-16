from aiogram import Dispatcher
from aiogram.types import Message


async def growing_products(message: Message):
    await message.reply("Hello, admin!")

def growing_products(dp: Dispatcher):
    pass