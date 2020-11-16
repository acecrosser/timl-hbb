import logging
from datetime import datetime
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline import expense_buttons, call_back_expense
from data.dbase.models import insert_data
from utils.states import StatesExpense
from data.dbase.models import make_default_db
from sqlite3 import OperationalError
from keyboards.default import default_buttons


from loader import dp


@dp.message_handler(lambda msg: msg.text.startswith('Расход'))
async def expense_answer(msg: types.Message):
    await msg.answer('Выберите категорию расхода:', reply_markup=expense_buttons)


@dp.callback_query_handler(call_back_expense.filter(), state=None)
async def chose_group(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    await call.message.answer('Введите сумму расхода:')
    data_group = callback_data.get('group')
    await state.update_data(group=data_group)
    await StatesExpense.ANSWER_1.set()


@dp.message_handler(state=StatesExpense.ANSWER_1)
async def take_summa(msg: types.Message, state: FSMContext):
    summa = msg.text
    await state.update_data(summa=summa)
    await msg.answer(f'Имя расхода:')
    await StatesExpense.next()


@dp.message_handler(state=StatesExpense.ANSWER_2)
async def make_expense(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    group = data.get('group')
    summa = data.get('summa')
    name = msg.text
    value_group = {
        'id_user': msg.from_user.id,
        'amount': summa,
        'grouping': group,
        'title': name,
        'time': datetime.now()
    }
    try:
        insert_data('expense', value_group)
    except OperationalError:
        make_default_db()
        insert_data('expense', value_group)
    await msg.answer(f'<b>Расход добавлен</b>\n'
                     f'Сумма: {summa} руб.\n'
                     f'Имя расхода - {name.title()}. \n'
                     f'Группа расходов - "{str(group).title()}" \n',
                     reply_markup=default_buttons)
    await state.finish()

