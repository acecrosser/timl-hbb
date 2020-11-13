import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline import expense_buttons, call_back_expense
from data.dbase.models import insert_data
from utils.states import States

from loader import dp, bot


@dp.message_handler(lambda msg: msg.text.startswith('Расход'))
async def expense_answer(msg: types.Message):
    await msg.answer('Выберите категорию расхода', reply_markup=expense_buttons)


@dp.callback_query_handler(call_back_expense.filter(), state=None)
async def chose_group(call: CallbackQuery, callback_data: dict):
    await call.answer()
    logging.info(f'call = {callback_data}')
    await call.message.answer('Введите сумму расхода:')
    await States.ANSWER_1.set()


@dp.message_handler(state=States.ANSWER_1)
async def take_summa(msg: types.Message, state: FSMContext):
    summa = msg.text
    await state.update_data(summa=summa)
    await msg.answer(f'Теперь укажи имя расхода:')
    await States.next()


@dp.message_handler(state=States.ANSWER_2)
async def make_expense(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    summa = data.get('summa')
    name = msg.text
    await msg.answer(f'Ты указал {summa} руб., за {name}.')