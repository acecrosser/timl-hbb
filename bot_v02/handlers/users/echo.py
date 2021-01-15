from aiogram import types
from loader import dp
from keyboards.default import default_buttons, settings_buttons


@dp.message_handler()
async def echo_auto(msg: types.Message):
    await msg.answer('Есть следующие команды: \n\n'
                     '<b>ОТЧЕТЫ ПО РАСХОДАМ.</b> \n'
                     '<b>Текущий месяц:</b> \n'
                     'Сумма расходов - /summa \n'
                     'Подробный очет - /full_order \n\n'
                     '<b>Прошлый месяц:</b> \n'
                     'Общий отчет - /past_month \n\n'
                     '<b>ОТЧЕТЫ ПО ДОХОДАМ.</b> \n'
                     '<b>Текущий месяц:</b> \n'
                     'Сумма доходов - /p_summa \n'
                     'Подобродный отчет - /p_full_order', reply_markup=default_buttons)
