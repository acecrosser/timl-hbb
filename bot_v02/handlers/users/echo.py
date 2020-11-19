from aiogram import types
from loader import dp


@dp.message_handler()
async def echo_auto(msg: types.Message):
    await msg.answer(msg.text)
    await msg.answer('Есть команды /order')
