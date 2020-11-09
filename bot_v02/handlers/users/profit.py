from aiogram import types
from keyboards.inline import profit_buttons

from loader import dp


@dp.message_handler(lambda msg: msg.text.startswith('Доход'))
async def profit_answer(msg: types.Message):
    await msg.answer('Выберите категорию', reply_markup=profit_buttons)