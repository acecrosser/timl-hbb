from datetime import datetime
from keyboards.inline.keyboard import call_back_order, expense_buttons_order
from aiogram import types
from aiogram.types import CallbackQuery
from loader import dp
from data.dbase.models import today, distinct, sum_title
from aiogram.dispatcher.filters.builtin import Command
from .orders import general_make_order


@dp.message_handler(Command('summa'))
async def what_order(msg: types.Message):
    await msg.answer('Выберите категорию отчета:', reply_markup=expense_buttons_order)


@dp.callback_query_handler(call_back_order.filter(group=['сегодня', 'текущий месяц', 'прошлый месяц']))
async def make_order_expense(call: CallbackQuery, callback_data: dict):
    await call.answer()
    id_user = call.from_user.id
    past_month = str(datetime.now().year) + '-' + str(datetime.now().month-1)
    period = {
        'сегодня': datetime.now().strftime('%Y-%m-%d'),
        'текущий месяц': datetime.now().strftime('%Y-%m'),
        'прошлый месяц': past_month
    }
    data_group = callback_data.get('group')
    choose_period = period[data_group]
    data = today('expense', id_user, choose_period)
    await call.message.answer(f'Ваши расходы за {data_group} -- <b>{data[0]}</b> руб.')


@dp.message_handler(Command('full_order'))
async def make_order(msg: types.Message):
    id_user = msg.from_user.id
    month = datetime.now().strftime('%Y-%m')
    order = general_make_order('expense', id_user, month)
    await msg.answer(f'Отчет по расходам за текущий месяц: \n\n{order}')


@dp.message_handler(Command('past_month'))
async def make_order(msg: types.Message):
    id_user = msg.from_user.id
    month = str(datetime.now().year) + '-' + str(datetime.now().month-1)
    order = general_make_order('expense', id_user, month)
    await msg.answer(f'Отчет за прошлый месяц: \n\n{order}')
