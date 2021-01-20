from datetime import datetime

from aiogram.dispatcher import FSMContext

from keyboards.default import set_default_button, ordering_buttons
from keyboards.inline.keyboard import call_back_order, expense_buttons_order, set_buttons, call_back_expense
from keyboards.inline.keyboard import call_back_order_grouping
from aiogram import types
from aiogram.types import CallbackQuery
from loader import dp
from data.dbase.models import today, distinct_group, sum_title
from aiogram.dispatcher.filters.builtin import Command
from .orders import general_make_order
from utils.states import StatesChoseGroupExpense


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


@dp.callback_query_handler(call_back_order_grouping.filter(group=['expense_order', 'aborting_order']), state=None)
async def order_expense(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    data_group = callback_data.get('group')
    if data_group == 'aborting_order':
        await call.answer()
        await call.message.answer('Операция отменена')
        await state.reset_data()
    else:
        await call.message.answer('Выберите категорию:', reply_markup=set_default_button('expense'))
        await state.update_data(group=data_group)
        await StatesChoseGroupExpense.ANSWER_1.set()

        @dp.message_handler(state=StatesChoseGroupExpense.ANSWER_1)
        async def make_order_expense(msg: types.Message):
            grouping = msg.text.lower()
            month = datetime.now().strftime('%Y-%m')
            data_chose_group = distinct_group('title', 'expense', msg.from_user.id, month, grouping)

            ordering_field = {}
            for key, item in data_chose_group:
                ordering_field[key] = ordering_field.get(key, 0) + item

            normal_list = ''
            for k, i in ordering_field.items():
                normal_list += f'{str(k).title()} - <b>{i}</b>\n'

            _name = 'grouping'
            total_amount = sum_title('expense', msg.from_user.id, month, grouping, _name)

            await msg.answer(f'Категория: <b>{grouping.title()}</b>\n'
                             f'Тип: <b>Расходы</b>\n\n'
                             f'{normal_list}\n'
                             f'-----------------\n'
                             f'Сумма: <b>{total_amount[0]}</b>',
                             reply_markup=ordering_buttons)
            await state.finish()

