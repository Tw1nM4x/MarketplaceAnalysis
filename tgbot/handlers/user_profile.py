from aiogram import Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types.input_media import InputMedia
from aiogram.dispatcher.filters import Text

from tgbot.misc.states import UserStates
from tgbot.keyboards.inline import get_inline_user, MarkupName


async def profile(message: types.Message):
	await message.bot.send_chat_action(message.chat.id, 'typing')
	markup = get_inline_user(MarkupName.profile)
	sub = 'Отсутствует'
	sub_days = '—'

	await message.answer(f'📊<b>Ваш профиль:</b> @{message.from_user.username}\n\n'
	                     f'👤<b>Имя:</b> {message.from_user.first_name} \n'
	                     f'💎<b>Подписка:</b> {sub}\n\n'
	                     f'⏳<b>До оконачия подписки:</b> {sub_days}',
						  parse_mode="html",
						  reply_markup=markup)

async def buy_sub(message: types.Message):
	await message.bot.send_chat_action(message.chat.id, 'typing')
	markup = get_inline_user(MarkupName.profile)
	await message.answer(f'💎<b>Покупка подписки</b>\n\n',
						  parse_mode="html",
						  reply_markup=markup)

def user_profile(dp: Dispatcher):
	dp.register_message_handler(profile, commands="profile", state='*')
	dp.register_callback_query_handler(buy_sub, Text(startswith="buy_sub"), state='*')
