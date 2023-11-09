from aiogram import Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types.input_media import InputMedia
from aiogram.dispatcher.filters import Text

from tgbot.misc.states import UserStates
from tgbot.keyboards.inline import get_inline_user, MarkupName

async def start(message: types.Message):
    await message.bot.send_chat_action(message.chat.id, 'typing')
    await message.answer('''<b>👋🏻 Привет! Я ваш надежный помощник в анализе товаров с маркетплейсов Wildberries и Ozon.</b> 
    
Что вы можете узнать благодаря мне:

🔹 Месячный оборот товара;
🔹 Насколько товар популярен по сравнению с другими товарами;
🔹 Товарные остатки и на каких складах находится товар;
🔹 По какой цене товар продавался за последние 2 недели, для определения оптимальной цены;
🔹 Позицию товара по запросу;
🔹 Поиск товаров, быстро набирающих спрос''',
parse_mode="html")
    await message.answer('''<b>👋🏻 Привет! Я ваш надежный помощник в анализе товаров с маркетплейсов Wildberries и Ozon.</b> 

    Что вы можете узнать благодаря мне:

    🔹 Месячный оборот товара;
    🔹 Насколько товар популярен по сравнению с другими товарами;
    🔹 Товарные остатки и на каких складах находится товар;
    🔹 По какой цене товар продавался за последние 2 недели, для определения оптимальной цены;
    🔹 Позицию товара по запросу;
    🔹 Поиск товаров, быстро набирающих спрос''',
                         parse_mode="html",
                         reply_markup=markup)

async def login(call: types.CallbackQuery, state: FSMContext):
    print("SSSS")
    await UserStates.registration_password.set()
    await call.message.answer(
        '<i>Придумайте и введите логин:</i>',
        parse_mode='html')

async def password(message: types.CallbackQuery, state: FSMContext):
    await message.answer(
        '<i>Придумайте и введите пароль:</i>',
        parse_mode='html')

def user(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state='*')
    dp.register_callback_query_handler(login, Text(startswith="registration_login"), state='*')
    dp.register_message_handler(password, state=UserStates.registration_password)

