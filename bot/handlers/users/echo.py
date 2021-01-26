from aiogram import types
from loader import dp
from keyboards.default import default_buttons


@dp.message_handler()
async def echo_auto(msg: types.Message):
    await msg.answer('Не могу распознать команду, попробуйте выбрать из меню: ', reply_markup=default_buttons)