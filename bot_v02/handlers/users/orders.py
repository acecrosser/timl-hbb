from datetime import datetime
from keyboards.inline.keyboard import call_back_order, expense_buttons_order
from aiogram import types
from aiogram.types import CallbackQuery
from loader import dp
from data.dbase.models import today
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
