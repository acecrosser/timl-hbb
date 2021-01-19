from datetime import datetime
from aiogram import types
from data.dbase.models import distinct, sum_title, today
from keyboards.default import ordering_buttons
from loader import dp


def general_make_order(table, id_user, month) -> str:
    work_data = distinct(name='grouping', table=table, id_user=id_user, period=month)
    end_list = ''
    for i in work_data:
        sum = sum_title(table=table, id_user=id_user, period=month, grouping=i[0], name='grouping')
        end_list += f'{str(i[0]).title()} - <b>{sum[0]}</b>\n'
    return end_list


@dp.message_handler(text='Общий')
async def default_order(msg: types.Message):
    id_user = msg.from_user.id
    month = datetime.now().strftime('%Y-%m')
    order_expense = general_make_order('expense', id_user, month)
    summa_expense = today('expense', id_user, month)
    orders_profit = general_make_order('profit', id_user, month)
    summa_profit = today('profit', id_user, month)
    result = int(summa_profit[0]) - int(summa_expense[0])
    await msg.answer(f'<b>Расходы: [  {summa_expense[0]}  ]</b>\n\n'
                     f'{order_expense}\n'
                     f'-----------------\n\n'
                     f'<b>Доходы: [  {summa_profit[0]}  ]</b>\n\n'
                     f'{orders_profit}\n'
                     f'-----------------\n'
                     f'<b>Итого: {result}</b>')


@dp.message_handler(text='Годовой')
async def year_order(msg: types.Message):
    await msg.answer('Годовой отчет находится в разработке...', reply_markup=ordering_buttons)
