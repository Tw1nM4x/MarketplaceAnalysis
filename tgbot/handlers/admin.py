from aiogram import Dispatcher
from aiogram.types import Message


async def admin_start(message: Message):
    await message.reply("Hello, admin!")

async def send_admin_mess(message: Message):
    print(message)
    await message.answer('☑️ Ваше обращение принято!\n'
                         '⚙️ Мы уже начали работу, над вашей проблемой!',
                         parse_mode="html")

def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
