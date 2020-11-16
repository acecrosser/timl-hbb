from aiogram import types
from loader import dp
from data.dbase.models import today
from aiogram.dispatcher.filters.builtin import Command


@dp.message_handler(Command('order'))
async def make_order(msg: types.Message):
    id_user = msg.from_user.id
    data = today('expense', id_user)
    await msg.answer(f'Ваши расходы за сегодня: {data[0]}')
