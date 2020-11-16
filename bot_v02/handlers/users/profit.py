from datetime import datetime
from aiogram import types
from keyboards.inline import profit_buttons, call_back_profit
from aiogram.types import CallbackQuery
from data.dbase.models import insert_data
from aiogram.dispatcher import FSMContext
from utils.states import States
from data.dbase.models import make_default_db
from sqlite3 import OperationalError
import logging


from loader import dp


@dp.message_handler(lambda msg: msg.text.startswith('Доход'))
async def profit_answer(msg: types.Message):
    await msg.answer('Выберите категорию дохода:', reply_markup=profit_buttons)


@dp.callback_query_handler(call_back_profit.filter(), state=None)
async def chose_group(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    # logging.info(callback_data)
    await call.message.answer('Введите сумму дохода:')
    data_group = callback_data.get('group')
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
                     f'Имя дохода - {name.title()}. \n'
                     f'Группа дохода - "{str(group).title()}" \n')
    await state.finish()
