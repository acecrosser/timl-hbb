from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    ANSWER_1 = State()
    ANSWER_2 = State()
    ANSWER_3 = State()

