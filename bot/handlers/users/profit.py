from datetime import datetime
from aiogram import types
from data.dbase.settings import list_settings
from keyboards.default import default_buttons
from keyboards.inline import set_buttons, call_back_profit
from aiogram.types import CallbackQuery
from data.dbase.models import insert_data, sum_title
from aiogram.dispatcher import FSMContext
from utils.states import States
from data.dbase.connect import make_default_db
from psycopg2 import OperationalError
from keyboards.default import set_button_for_choice
from loader import dp, bot

list_group_profit = set()


def make_list_group_profit(id_user: str, grouping: str):
    settings = list_settings(id_user=id_user, grouping=grouping)
    for group in settings:
        list_group_profit.add(str(group[0]).lower())
    list_group_profit.add('aborting')
    return list_group_profit


@dp.message_handler(text='Доход')
async def profit_answer(msg: types.Message):
    make_list_group_profit(msg.from_user.id, 'profit')
    await msg.answer('Выберите категорию:', reply_markup=set_buttons('profit', call_back_profit, msg.from_user.id))


@dp.callback_query_handler(call_back_profit.filter(group=list_group_profit), state=None)
async def chose_group(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    data_group = callback_data.get('group')
    if data_group == 'aborting':
        await call.answer()
        await call.message.answer('<i>Операция отменена</i>', reply_markup=default_buttons)
        await state.reset_data()
    else:
        await call.message.answer('Введите сумму')
        await state.update_data(group=data_group)
        await States.ANSWER_1.set()


@dp.message_handler(state=States.ANSWER_1)
async def take_summa(msg: types.Message, state: FSMContext):
    summa = msg.text
    summa = ''.join(summa.split())
    if not summa.isdigit():
        await msg.answer(f'<b>{summa}</b> - это не цифра, попробуй еще раз')
    else:
        data = await state.get_data()
        group = data.get('group')
        period = datetime.now().strftime('%Y-%m')
        await state.update_data(summa=summa)
        await msg.answer(f'Источник:', reply_markup=set_button_for_choice(
            'profit', msg.from_user.id, group, period
        ))
        await States.next()


@dp.message_handler(state=States.ANSWER_2)
async def make_profit(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    group = data.get('group')
    summa = data.get('summa')
    name = msg.text
    value_group = {
        'id_user': msg.from_user.id,
        'amount': int(summa),
        'grouping': group,
        'title': name,
        'time': datetime.now()
    }
    try:
        insert_data('profit', value_group)
    except OperationalError:
        make_default_db()
        insert_data('profit', value_group)

    periods = datetime.now().strftime('%Y-%m')
    _name = 'grouping'
    total_amount = sum_title('profit', msg.from_user.id, periods, group, _name)

    await msg.answer(f'<b>Доход добавлен</b>\n\n'
                     f'Сумма - <b>{summa}</b>\n'
                     f'Источник - {name.capitalize()}\n'
                     f'Категория - {str(group).capitalize()}\n\n'
                     f'Текущий месяц: [  <b>{total_amount[0]}  ]</b>',
                     reply_markup=default_buttons)
    await state.finish()
