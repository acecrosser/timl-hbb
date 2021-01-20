from datetime import datetime
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default import set_default_button, ordering_buttons
from loader import dp
from data.dbase.models import distinct, sum_title, today, distinct_group
from aiogram.dispatcher.filters.builtin import Command
from keyboards.inline.keyboard import call_back_profit_order, profit_buttons_order
from keyboards.inline.keyboard import call_back_order_grouping
from utils import StatesChoseGroupExpense
from .orders import general_make_order


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
    order = general_make_order('profit', id_user, month)
    await msg.answer(f'Отчет доходы текущий месяц: \n\n{order}')


@dp.callback_query_handler(call_back_order_grouping.filter(group=['profit_order', 'aborting_order']))
async def order_expense(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    data_group = callback_data.get('group')
    if data_group == 'aborting_order':
        await call.answer()
        await call.message.answer('Операция отменена')
        await state.reset_data()
    else:
        await call.message.answer('Выберите категорию:', reply_markup=set_default_button('profit'))
        await state.update_data(group=data_group)
        await StatesChoseGroupExpense.ANSWER_1.set()

        @dp.message_handler(state=StatesChoseGroupExpense.ANSWER_1)
        async def make_order_expense(msg: types.Message):
            grouping = msg.text.lower()
            month = datetime.now().strftime('%Y-%m')
            data_chose_group = distinct_group('title', 'profit', msg.from_user.id, month, grouping)

            ordering_field = {}
            for key, item in data_chose_group:
                ordering_field[key] = ordering_field.get(key, 0) + item

            normal_list = ''
            for k, i in ordering_field.items():
                normal_list += f'{str(k).title()} - <b>{i}</b>\n'

            _name = 'grouping'
            total_amount = sum_title('profit', msg.from_user.id, month, grouping, _name)

            await msg.answer(f'Категория: <b>{grouping.title()}</b>\n'
                             f'Тип: <b>Доходы</b>\n\n'
                             f'{normal_list}\n'
                             f'-----------------\n'
                             f'Сумма: <b>{total_amount[0]}</b>',
                             reply_markup=ordering_buttons)
            await state.finish()
