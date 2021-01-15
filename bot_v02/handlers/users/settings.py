from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from utils.states import StatesSettingsExpense
from keyboards.inline import button_settings_group, call_back_settings
from data.dbase.settings import list_settings, add_setting
from loader import dp


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
