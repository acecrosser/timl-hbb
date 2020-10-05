from aiogram import Bot, Dispatcher, types, executor
import receiver

API_TOKEN = '1328164745:AAFvR9tm2ivPlJsU1OGCpjjjdoOXct3GjaE'

bot = Bot(token=API_TOKEN)
bd = Dispatcher(bot)


@bd.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    await msg.answer('Тебя приветсвует timl-bot!')


@bd.message_handler()
async def add_data(msg: types.Message):
    try:
        data = receiver.add_data(msg.text)
    except receiver.NotCorrectMessage as e:
        await msg.answer(str(e))
        return
    answer_msg = (
        f'Добавили в общую базу {data.amount} р., - {data.name}')
    await msg.answer(answer_msg)


@bd.message_handler(commands=['profit'])
async def add_profit(msg: types.Message):
    try:
        data = receiver.add_profit(msg.text)
    except receiver.NotCorrectMessage as e:
        await msg.answer(str(e))
        return
    answer_profit = (
        f'Додход от {data.name} в сумме {data.amount} добавлен в базу')
    await msg.answer(answer_profit)


if __name__ == '__main__':
    executor.start_polling(bd, skip_updates=True)


