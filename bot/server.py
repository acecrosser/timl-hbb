from aiogram import Bot, Dispatcher, types, executor
import receiver
import exceptions
import interface


API_TOKEN = '1328164745:AAFvR9tm2ivPlJsU1OGCpjjjdoOXct3GjaE'

bot = Bot(token=API_TOKEN)
bd = Dispatcher(bot)


@bd.message_handler(commands=['test'])
async def check_button(msg: types.Message):
    await msg.reply('тут текст', reply_markup=interface.show_button)


@bd.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    await msg.answer('Тебя приветсвует Timl-bot! \n'
                     'Формат внесения в базу: \n'
                     'Cумма Тип Категория Источник \n\n'
                     'Пример: \n'
                     '15000 доход аванс работа')


@bd.message_handler()
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
    executor.start_polling(bd, skip_updates=True)
