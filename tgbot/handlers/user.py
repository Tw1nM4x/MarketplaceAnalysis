from aiogram import Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types.input_media import InputMedia
from aiogram.dispatcher.filters import Text

from tgbot.handlers.admin import send_admin_mess
from tgbot.handlers.growing_products import growing_products
from tgbot.keyboards.reply import get_reply_user, ReplyMarkupName
from tgbot.misc.states import UserStates
from tgbot.keyboards.inline import get_inline_user, MarkupName
from tgbot.open_weather import get_weather


async def start(message: types.Message):
    await message.bot.send_chat_action(message.chat.id, 'typing')
    await UserStates.start.set()
    markup = get_reply_user(MarkupName.start)
    await message.answer('''<b>👋🏻 Привет!</b> Я дам вам рекомендации по выбору одежды в зависимости от текущей погоды!\n
<b>Чтобы я показал вам, что надеть:</b>
✍🏻 Напишите название вашего населенного пункта или
🗺 Отправьте свою геолокацию!''', parse_mode="html", reply_markup=markup)

async def location(message: types.Message, state: FSMContext):
    # Получение геолокации от пользователя
    coord = [message.location.latitude, message.location.longitude]

    # Вывод полученных координат
    await message.answer(f"Ваши координаты: {coord[0]}, {coord[1]}")

    text = get_weather(coord)
    await message.answer(text)


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
    dp.register_message_handler(location, content_types='location', state='*')

    dp.register_message_handler(help2, state=UserStates.help)
    dp.register_callback_query_handler(start_growing_products, Text(startswith="monthly_turnover"), state=UserStates.start)
    dp.register_callback_query_handler(start_product_position, Text(startswith="product_position"), state=UserStates.start)
    dp.register_callback_query_handler(start_fastgrowing_products, Text(startswith="fastgrowing_products"), state=UserStates.start)
    dp.register_message_handler(password, state=UserStates.registration_password)

