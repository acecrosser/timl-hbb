from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from utils.states import StatesSettingsExpense, StatesSettingsDeleting
from keyboards.inline import button_settings_group, call_back_settings, button_settings_group_del
from keyboards.inline import set_buttons, call_back_expense, call_back_profit
from keyboards.default import set_default_button, default_buttons
from data.dbase.settings import list_settings, add_setting, del_setting
from loader import dp
from .expense import make_list_group_expense, list_group
from .profit import make_list_group_profit, list_group_profit


@dp.message_handler(text='Добавить')
async def settings(msg: types.Message):
    await msg.answer('Выберите раздел:', reply_markup=button_settings_group)


@dp.callback_query_handler(call_back_settings.filter(group=['expense', 'profit', 'aborting_stg']), state=None)
async def choice_setting(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    data_group = callback_data.get('group')
    if data_group == 'aborting_stg':
        await call.answer()
        await call.message.answer('Операция отменена')
        await state.reset_data()
    else:
        await call.message.answer('Введите имя категории:')
        await state.update_data(group=data_group)
        await StatesSettingsExpense.ANSWER_1.set()


@dp.message_handler(state=StatesSettingsExpense.ANSWER_1)
async def _setting(msg: types.Message, state: FSMContext):
    title = msg.text
    await state.update_data(title=title)
    data = await state.get_data()
    grouping = data.get('group')
    title = data.get('title')
    add_setting(msg.from_user.id, title, grouping)
    await msg.answer(f'Категория "{title}" - добавлена')
    make_list_group_expense()
    make_list_group_profit()
    await state.finish()


@dp.message_handler(text='Список')
async def get_list(msg: types.Message):
    expense_data = list_settings(msg.from_user.id, grouping='expense')
    profit_data = list_settings(msg.from_user.id, grouping='profit')
    make_list_expense = [get_title[0] for get_title in expense_data]
    make_list_profit = [get_title[0] for get_title in profit_data]
    expense_title = ''
    profit_title = ''
    for title in make_list_expense:
        expense_title += title + ',\n'
    for title in make_list_profit:
        profit_title += title + ',\n'
    await msg.answer(f'Список категорий:\n\n'
                     f'Категории расходов:\n'
                     f'{expense_title} \n\n'
                     f'Категории доходов:\n'
                     f'{profit_title}')


@dp.message_handler(text='Удалить')
async def settings(msg: types.Message):
    await msg.answer('От куда будем удалять:', reply_markup=button_settings_group_del)


@dp.callback_query_handler(call_back_settings.filter(group=['expense_del', 'profit_del', 'aborting_stg_del']), state=None)
async def choice_setting_for_del(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    data_group = callback_data.get('group')
    if data_group == 'aborting_stg_del':
        await call.answer()
        await call.message.answer('Операция отменена')
        await state.reset_data()
    elif data_group == 'expense_del':
        await call.message.answer('Введите имя категории для удаления:', reply_markup=set_default_button('expense'))
        await state.update_data(group=data_group)
        await StatesSettingsDeleting.ANSWER_1.set()

        @dp.message_handler(state=StatesSettingsDeleting.ANSWER_1)
        async def del_expense_setting(msg: types.Message):
            title = msg.text
            del_setting(msg.from_user.id, title)
            await msg.answer('Категория удалена успешно', reply_markup=default_buttons)
            make_list_group_expense()
            await state.finish()
    else:
        await call.message.answer('Введите имя категории для удаления:', reply_markup=set_default_button('profit'))
        await state.update_data(group=data_group)
        await StatesSettingsDeleting.ANSWER_1.set()

        @dp.message_handler(state=StatesSettingsDeleting.ANSWER_1)
        async def del_expense_setting(msg: types.Message):
            title = msg.text
            del_setting(msg.from_user.id, title)
            await msg.answer('Категория удалена успешно', reply_markup=default_buttons)
            make_list_group_expense()
            await state.finish()

