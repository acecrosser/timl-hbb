from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import receiver
import exceptions
import interface


API_TOKEN = '1104987716:AAGF8AfDDSoBBXuzoPbUvHIJNM7M0DK6H9Q'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
db = Dispatcher(bot, storage=storage)


@db.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    await msg.answer('Тебя приветсвует Timl-bot! \n'
                     'Формат внесения в базу: \n'
                     'Cумма Тип Категория Источник \n\n'
                     'Пример: \n'
                     '15000 доход аванс работа')


@db.message_handler()
async def add_data(msg: types.Message):
    try:
        data = receiver.general_data(msg.text)
    except exceptions.NotCorrectMessage as e:
        await msg.answer(str(e))
        return
    answer_msg = (
        f'В базу внесена сумма - {data.amount} р.\n'
        f'Тип: {data.type_data} \n'
        f'Категория: {data.category} \n'
        f'Источник: {data.name}\n'
        f'Автор: {data.author}')
    await msg.answer(answer_msg)


if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)
