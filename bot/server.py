from aiogram import Bot, Dispatcher, types, executor
import receiver
import exceptions
import interface


API_TOKEN = '1104987716:AAGF8AfDDSoBBXuzoPbUvHIJNM7M0DK6H9Q'

bot = Bot(token=API_TOKEN)
bd = Dispatcher(bot)


@bd.callback_query_handler(lambda c: c.data and c.data.startswith('insert'))
async def process_callback_button(callback_query: types.CallbackQuery):
    get_text = callback_query.data[-1]
    if get_text.isdigit():
        get_text = int(get_text)
    if get_text == 1:
        print('бананы')
        await bot.send_message(callback_query.from_user.id, 'Введите сумму')
        await bot.answer_callback_query(callback_query.id, 'Введите сумму')
    if get_text == 0:
        print('апельсины')
        await bot.answer_callback_query(callback_query.id, 'Апельсины')
    else:
        await bot.answer_callback_query(callback_query.id)
    # await bot.send_message(callback_query.from_user.id, 'Сработало если что')


@bd.message_handler(commands=['test'])
async def check_button(msg: types.Message):
    await msg.reply('тут текст', reply_markup=interface.show_inline_button)


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


@bd.message_handler()
async def add_profit(msg: types.Message):
    data = receiver.general_data('Доход' + msg.text)
    answer_ = f'Доход в размере {data.amount} добавлен в базу'
    await msg.answer(answer_)
