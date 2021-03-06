from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from utils.states import StatesSettingsExpense, StatesSettingsDeleting
from keyboards.inline import button_settings_group, call_back_settings, button_settings_group_del
from keyboards.default import set_default_button, settings_buttons
from data.dbase.settings import list_settings, add_setting, del_setting
from loader import dp
from .expense import make_list_group_expense
from .profit import make_list_group_profit


@dp.message_handler(text='Добавить')
async def settings(msg: types.Message):
    await msg.answer('Куда добавляем?', reply_markup=button_settings_group)


@dp.callback_query_handler(call_back_settings.filter(group=['expense', 'profit', 'aborting_stg']), state=None)
async def choice_setting(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    data_group = callback_data.get('group')
    if data_group == 'aborting_stg':
        await call.answer()
        await call.message.answer('<i>Операция отменена</i>', reply_markup=settings_buttons)
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
    await msg.answer(f'Категория <b>"{title}"</b> - добавлена', reply_markup=settings_buttons)
    make_list_group_expense(msg.from_user.id, 'expense')
    make_list_group_profit(msg.from_user.id, 'profit')
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
        expense_title += ('<b>' + title + '</b>\n')
    for title in make_list_profit:
        profit_title += ('<b>' + title + '</b>\n')
    await msg.answer(f'Категории расходов:\n'
                     f'{expense_title}'
                     f'-----------------\n'
                     f'Категории доходов:\n'
                     f'{profit_title}', reply_markup=settings_buttons)


@dp.message_handler(text='Удалить')
async def settings(msg: types.Message):
    await msg.answer('От куда будем удалять?', reply_markup=button_settings_group_del)


@dp.callback_query_handler(call_back_settings.filter(group=['expense_del', 'profit_del', 'aborting_stg_del']), state=None)
async def choice_setting_for_del(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer()
    data_group = callback_data.get('group')
    if data_group == 'aborting_stg_del':
        await call.answer()
        await call.message.answer('<i>Операция отменена</i>', reply_markup=settings_buttons)
        await state.reset_data()
    elif data_group == 'expense_del':
        await call.message.answer('Какую категорию удаляем?', reply_markup=set_default_button('expense'))
        await state.update_data(group=data_group)
        await StatesSettingsDeleting.ANSWER_1.set()

        @dp.message_handler(state=StatesSettingsDeleting.ANSWER_1)
        async def del_expense_setting(msg: types.Message):
            title = msg.text
            data = await state.get_data()
            grouping = data.get('group')
            del_setting(msg.from_user.id, title, grouping[:5])
            await msg.answer(f'Категория <b>"{title}"</b> - удалена', reply_markup=settings_buttons)
            make_list_group_expense(msg.from_user.id, 'expense')
            await state.finish()
    else:
        await call.message.answer('Какую категорию удаляем?', reply_markup=set_default_button('profit'))
        await state.update_data(group=data_group)
        await StatesSettingsDeleting.ANSWER_1.set()

        @dp.message_handler(state=StatesSettingsDeleting.ANSWER_1)
        async def del_expense_setting(msg: types.Message):
            title = msg.text
            data = await state.get_data()
            grouping = data.get('group')
            del_setting(msg.from_user.id, title, grouping[:5])
            await msg.answer(f'Категория "{title}" - удалена', reply_markup=settings_buttons)
            make_list_group_profit(msg.from_user.id, 'profit')
            await state.finish()
