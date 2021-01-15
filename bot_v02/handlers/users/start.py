from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram.dispatcher import FSMContext
from keyboards.default import default_buttons
from utils.states import StatesSettingsExpense
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    await msg.answer(f'Привет, {msg.from_user.full_name}! \n'
                     f'\n'
                     f'Тебя привествует Бот-Бухгалтер.\n'
                     f'Сначало предлагаю, осуществить настройку свойх категорий', reply_markup=default_buttons)


@dp.message_handler(text='Настройки')
async def bot_settings(msg: types.Message):
    await msg.answer(f'Пока хреново с настройками {msg.from_user.username}')