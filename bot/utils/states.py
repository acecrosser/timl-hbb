from aiogram.dispatcher.filters.state import StatesGroup, State


class StatesExpense(StatesGroup):
    ANSWER_1 = State()
    ANSWER_2 = State()
    ANSWER_3 = State()


class States(StatesGroup):
    ANSWER_1 = State()
    ANSWER_2 = State()
    ANSWER_3 = State()


class StatesSettingsExpense(StatesGroup):
    ANSWER_1 = State()
    ANSWER_2 = State()
    ANSWER_3 = State()


class StatesSettingsDeleting(StatesGroup):
    ANSWER_1 = State()


class StatesChoseGroupExpense(StatesGroup):
    ANSWER_1 = State()


class StatesChoseGroupProfit(StatesGroup):
    ANSWER_1 = State()

