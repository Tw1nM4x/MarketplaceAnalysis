from aiogram import Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types.input_media import InputMedia
from aiogram.dispatcher.filters import Text

from tgbot.handlers.admin import send_admin_mess
from tgbot.handlers.growing_products import growing_products
from tgbot.misc.states import UserStates
from tgbot.keyboards.inline import get_inline_user, MarkupName

async def start(message: types.Message):
    await message.bot.send_chat_action(message.chat.id, 'typing')
    await UserStates.start.set()
    markup = get_inline_user(MarkupName.start)
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

async def location(message: types.Message):
    # Получение геолокации от пользователя
    latitude = message.location.latitude
    longitude = message.location.longitude
    print(latitude)
    print(longitude)
    # Вывод полученных координат
    await message.answer(f"Ваши координаты: {latitude}, {longitude}")



async def functions(message: types.Message):
    await message.bot.send_chat_action(message.chat.id, 'typing')
    await message.answer('''<b>Вот что умеет бот:</b> 

🔹 Месячный оборот товара;
🔹 Насколько товар популярен по сравнению с другими товарами;
🔹 Товарные остатки и на каких складах находится товар;
🔹 По какой цене товар продавался за последние 2 недели, для определения оптимальной цены;
🔹 Позицию товара по запросу;
🔹 Поиск товаров, быстро набирающих спрос''',
                         parse_mode="html")

async def help(message: types.Message):
    await UserStates.help.set()
    print(message)
    await message.bot.send_chat_action(message.chat.id, 'typing')
    await message.answer('🛠 Если у вас возникли технические неполадки,'
                         'напишите ниже <b>одним сообщением</b> вашу проблему.\n\n'
                         '<i>Было бы замечательно, если вы могли бы предоставить скриншоты и '
                         'подробное описание возникшей проблемы.</i>',
                         parse_mode="html")

async def help2(message: types.Message, state: FSMContext):
    await state.reset_state()

    await message.bot.send_chat_action(message.chat.id, 'typing')

    await send_admin_mess(message)

    await message.answer('☑️ Ваше обращение принято!\n'
                         '⚙️ Мы уже начали работу, над вашей проблемой!',
                         parse_mode="html")

async def start_growing_products(call: types.CallbackQuery, state: FSMContext):
    await growing_products(call.message)

async def start_product_position(call: types.CallbackQuery, state: FSMContext):
    print("SSSS")
    await UserStates.registration_password.set()
    await call.message.answer(
        '<i>Придумайте и введитеsлогин:</i>',
        parse_mode='html')

async def start_fastgrowing_products(call: types.CallbackQuery, state: FSMContext):
    print("SSSS")
    await UserStates.registration_password.set()
    await call.message.answer(
        '<i>ssПридумайте и введите лsafadsогин:</i>',
        parse_mode='html')

async def password(message: types.CallbackQuery, state: FSMContext):
    await message.answer(
        '<i>Придумайте и введите пароль:</i>',
        parse_mode='html')

def user(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state='*')
    dp.register_message_handler(functions, commands="functions", state='*')
    dp.register_message_handler(help, commands="help", state='*')
    dp.register_message_handler(location, content_types='location')

    dp.register_message_handler(help2, state=UserStates.help)
    dp.register_callback_query_handler(start_growing_products, Text(startswith="monthly_turnover"), state=UserStates.start)
    dp.register_callback_query_handler(start_product_position, Text(startswith="product_position"), state=UserStates.start)
    dp.register_callback_query_handler(start_fastgrowing_products, Text(startswith="fastgrowing_products"), state=UserStates.start)
    dp.register_message_handler(password, state=UserStates.registration_password)

