from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import default_buttons

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    await msg.answer(f'Привет, {msg.from_user.full_name}! \n'
                     f'\n'
                     f'Тебя привествует Бот-Бухгалтер.\n'
                     f'Сперва предлагаю, осуществить настройку свойх категорий', reply_markup=default_buttons)