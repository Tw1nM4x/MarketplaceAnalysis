from aiogram.dispatcher.filters.state import State, StatesGroup


class UserStates(StatesGroup):
	registration_login = State()
	registration_password = State()



class AdminStates(StatesGroup):
	add_quiz_date = State()
	add_quiz_question = State()
	add_quiz_photo = State()
	add_quiz_exp_photo = State()