from datetime import datetime
from keyboards.inline.keyboard import call_back_order, expense_buttons_order
from aiogram import types
from aiogram.types import CallbackQuery
from loader import dp
from data.dbase.models import today, distinct, sum_title
from aiogram.dispatcher.filters.builtin import Command


@dp.message_handler(Command('order'))
async def what_order(msg: types.Message):
    await msg.answer('Выберите категорию отчета:', reply_markup=expense_buttons_order)


@dp.callback_query_handler(call_back_order.filter(group=['сегодня', 'неделю', 'месяц']))
async def make_order_expense(call: CallbackQuery, callback_data: dict):
    await call.answer()
    id_user = call.from_user.id
    period = {
        'сегодня': datetime.now().strftime('%Y-%m-%d'),
        'неделю': datetime.now().strftime('%Y-%m-%d'),
        'месяц': datetime.now().strftime('%Y-%m'),
    }
    data_group = callback_data.get('group')
    choose_period = period[data_group]
    data = today('expense', id_user, choose_period)
    await call.message.answer(f'Ваши расходы за {data_group}: {data[0]} руб.')


@dp.message_handler(Command('dist'))
async def make_order(msg: types.Message):
    work_data = distinct("expense", "5093906", "2020-11")
    end_list = ''
    for i in work_data:
        sum = sum_title('expense', '5093906', '2020-11', i[0])
        end_list += f'{i[0]} --- {sum[0]} руб.\n'
    await msg.answer(f'Отчет по расходам за выбранный период: \n\n {end_list}')
