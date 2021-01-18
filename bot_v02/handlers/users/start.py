from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram.dispatcher import FSMContext
from keyboards.default import default_buttons, settings_buttons, ordering_buttons
from utils.states import StatesSettingsExpense
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    await msg.answer(f'Привет, {msg.from_user.full_name}!\n\n'
                     'Тебя привествует домашний "Бот-Бухгалтер"\n\n'
                     'Данный бот помогает вести журнал расходов-доходов. '
                     'В функционале так же есть некоторые базовые отчеты по учету.\n\n'
                     'Перед началом работы требуется осуществить настройку свойх категорий', reply_markup=default_buttons)


@dp.message_handler(text='Настройки')
async def bot_settings(msg: types.Message):
    await msg.answer(f'Добавить или удалить категорию:', reply_markup=settings_buttons)


@dp.message_handler(text=['Назад', 'На главную'])
async def bot_back(msg: types.Message):
    await msg.answer('Главное меню:', reply_markup=default_buttons)


@dp.message_handler(text='Отчеты')
async def bot_orders(msg: types.Message):
    await msg.answer('Выберите тип отчета:', reply_markup=ordering_buttons)

