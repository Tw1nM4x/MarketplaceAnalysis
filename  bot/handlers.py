import asyncio
from settings import get_settings
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

bot = Bot(token=get_settings().TOKEN)
dp = Dispatcher(bot)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


async def main():
    await dp.start_polling(bot)

