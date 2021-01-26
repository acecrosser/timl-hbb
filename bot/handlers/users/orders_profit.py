from datetime import datetime
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.default import set_default_button, ordering_buttons
from loader import dp
from data.dbase.models import sum_title, distinct_group
from keyboards.inline.keyboard import call_back_order_grouping
from utils import StatesChoseGroupProfit


@dp.callback_query_handler(call_back_order_grouping.filter(group=['profit_order', 'aborting_order']))
async def order_expense(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    data_group = callback_data.get('group')
    if data_group == 'aborting_order':
        await call.answer()
        await call.message.answer('<i>Операция отменена</i>', reply_markup=ordering_buttons)
        await state.reset_data()
    else:
        await call.message.answer('Выберите категорию:', reply_markup=set_default_button('profit'))
        await state.update_data(group=data_group)
        await StatesChoseGroupProfit.ANSWER_1.set()

        @dp.message_handler(state=StatesChoseGroupProfit.ANSWER_1)
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
