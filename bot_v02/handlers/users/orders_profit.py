from datetime import datetime
from aiogram import types
from aiogram.types import CallbackQuery
from loader import dp
from data.dbase.models import distinct, sum_title, today
from aiogram.dispatcher.filters.builtin import Command
from keyboards.inline.keyboard import call_back_profit_order, profit_buttons_order


@dp.message_handler(Command('p_summa'))
async def what_order(msg: types.Message):
    await msg.answer('Выберите тип отчета:', reply_markup=profit_buttons_order)


@dp.callback_query_handler(call_back_profit_order.filter(group=['д текущий месяц', 'д прошлый месяц']))
async def make_order_profit(call: CallbackQuery, callback_data: dict):
    await call.answer()
    id_user = call.from_user.id
    past_month = str(datetime.now().year) + '-' + str(datetime.now().month-1)
    period = {
        'д текущий месяц': datetime.now().strftime('%Y-%m'),
        'д прошлый месяц': past_month
    }
    data_group = callback_data.get('group')
    choose_period = period[data_group]
    data = today('profit', id_user, choose_period)
    await call.message.answer(f'Ваши доходы за {data_group[2:]} -- <b>{data[0]}</b> руб.')


@dp.message_handler(Command('p_full_order'))
async def make_order(msg: types.Message):
    id_user = msg.from_user.id
    month = datetime.now().strftime('%Y-%m')
    work_data = distinct("profit", id_user=id_user, period=month)
    end_list = ''
    for i in work_data:
        sum = sum_title('profit', id_user=id_user, period=month, title=i[0])
        end_list += f'{i[0]} --- <b>{sum[0]}</b> руб.\n'
    await msg.answer(f'Отчет по доходам за текущий месяц: \n\n{end_list}')
