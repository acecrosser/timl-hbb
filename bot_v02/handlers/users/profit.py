from datetime import datetime
from aiogram import types
from data.dbase.settings import list_settings
from keyboards.inline import profit_buttons, call_back_profit, set_buttons, call_back_profit
from aiogram.types import CallbackQuery
from data.dbase.models import insert_data
from aiogram.dispatcher import FSMContext
from utils.states import States
from data.dbase.connect import make_default_db
from psycopg2 import OperationalError
from loader import dp

list_group_profit = []


def make_list_group_profit():
    settings = list_settings(id_user='5093906', grouping='profit')
    for group in settings:
        list_group_profit.append(str(group[0]).lower())
    list_group_profit.append('aborting')
    return list_group_profit


@dp.message_handler(lambda msg: msg.text.startswith('Доход'))
async def profit_answer(msg: types.Message):
    await msg.answer('Выберите категорию дохода:', reply_markup=set_buttons('profit', call_back_profit))
    make_list_group_profit()


@dp.callback_query_handler(call_back_profit.filter(group=list_group_profit), state=None)
async def chose_group(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    data_group = callback_data.get('group')
    if data_group == 'aborting':
        await call.answer()
        await call.message.answer('Операция отменена')
        await state.reset_data()
    else:
        await call.message.answer('Введите сумму дохода:')
        await state.update_data(group=data_group)
        await States.ANSWER_1.set()


@dp.message_handler(state=States.ANSWER_1)
async def take_summa(msg: types.Message, state: FSMContext):
    summa = msg.text
    await state.update_data(summa=summa)
    await msg.answer(f'Имя дохода:')
    await States.next()


@dp.message_handler(state=States.ANSWER_2)
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
        insert_data('profit', value_group)
    except OperationalError:
        make_default_db()
        insert_data('profit', value_group)
    await msg.answer(f'<b>Доход добавлен</b>\n'
                     f'Сумма: {summa} руб.\n'
                     f'Имя дохода - {name.capitalize()}. \n'
                     f'Группа дохода - "{str(group).capitalize()}" \n')
    await state.finish()
