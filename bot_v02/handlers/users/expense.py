import logging
from datetime import datetime
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline import call_back_expense, set_buttons, call_back_expense
from data.dbase.models import insert_data
from utils.states import StatesExpense
from data.dbase.connect import make_default_db
from psycopg2 import OperationalError
from keyboards.default import default_buttons
from data.dbase.settings import list_settings
from loader import dp


def make_list_group():
    settings = list_settings(id_user='5093906', grouping='expense')
    list_group = [str(group[0]).lower() for group in settings]
    list_group.append('aborting')
    return list_group


@dp.message_handler(lambda msg: msg.text.startswith('Расход'))
async def expense_answer(msg: types.Message):
    await msg.answer('Выберите категорию расхода:', reply_markup=set_buttons('expense', call_back_expense))


@dp.callback_query_handler(call_back_expense.filter(group=make_list_group()), state=None)
async def chose_group(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    data_group = callback_data.get('group')
    if data_group == 'aborting':
        await call.answer()
        await call.message.answer('Операция отменена')
        await state.reset_data()
    else:
        await call.message.answer('Введите сумму расхода:')
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

