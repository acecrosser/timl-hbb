from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import default_buttons, settings_buttons, ordering_buttons
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    await msg.answer(f'Привет, <b>{msg.from_user.full_name}</b>!\n\n'
                     'Тебя привествует домашний "Бот-Бухгалтер"\n\n'
                     'Данный бот помогает вести журнал расходов-доходов. '
                     'В функционале так же есть некоторые базовые отчеты по учету.\n\n'
                     'Перед началом работы требуется осуществить <b>настройку</b> свойх категорий',
                     reply_markup=default_buttons)


@dp.message_handler(text='Настройки')
async def bot_settings(msg: types.Message):
    await msg.answer(f'<b>Добавить</b> или <b>удалить</b> категорию?', reply_markup=settings_buttons)


@dp.message_handler(text=['Назад'])
async def bot_back(msg: types.Message):
    await msg.answer('Главное меню', reply_markup=default_buttons)


@dp.message_handler(text='Отчеты')
async def bot_orders(msg: types.Message):
    await msg.answer('Выберите тип отчета:', reply_markup=ordering_buttons)

