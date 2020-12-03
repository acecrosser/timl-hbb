from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


call_back_expense = CallbackData('exp', 'group')
call_back_order = CallbackData('order', 'group')
call_back_profit = CallbackData('prf', 'group')
call_back_profit_order = CallbackData('p_order', 'group')

expense_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Ежедневные', callback_data=call_back_expense.new(group='ежедневные')),
        ],
        [
            InlineKeyboardButton('Продукты', callback_data=call_back_expense.new(group='продукты')),
        ],
        [
            InlineKeyboardButton('Постоянные', callback_data=call_back_expense.new(group='постоянные'))
        ],
        [
            InlineKeyboardButton('Редкие', callback_data=call_back_expense.new(group='редкие'))
        ],
        [
            InlineKeyboardButton('Отмена', callback_data=call_back_expense.new(group='aborting'))
        ]
    ]
)

expense_buttons_order = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('За сегодня', callback_data=call_back_order.new(group='сегодня')),
        ],
        [
            InlineKeyboardButton('Текущий месяц', callback_data=call_back_order.new(group='текущий месяц'))
        ],
        [
            InlineKeyboardButton('Прошлый месяц', callback_data=call_back_order.new(group='прошлый месяц'))
        ]
    ]
)


profit_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Постоянный', callback_data=call_back_profit.new(group='постоянный'))
        ],
        [
            InlineKeyboardButton('Дополнительный', callback_data=call_back_profit.new(group='дополнительный'))
        ],
        [
            InlineKeyboardButton('Отмена', callback_data=call_back_profit.new(group='aborting'))
        ]
    ]
)

profit_buttons_order = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Текущий месяц', callback_data=call_back_profit_order.new(group='д текущий месяц'))
        ],
        [
            InlineKeyboardButton('Прошлый месяц', callback_data=call_back_profit_order.new(group='д прошлый месяц'))
        ]
    ]
)
