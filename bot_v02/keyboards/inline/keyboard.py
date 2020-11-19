from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


call_back_expense = CallbackData('exp', 'group')
call_back_order = CallbackData('order', 'group')
call_back_profit = CallbackData('prf', 'group')

expense_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Ежедневные', callback_data=call_back_expense.new(group='ежедневные')),
        ],
        [
            InlineKeyboardButton('Недельные', callback_data=call_back_expense.new(group='недельные')),
        ],
        [
            InlineKeyboardButton('Ежемесячные', callback_data=call_back_expense.new(group='ежемесячные'))
        ]
    ]
)

expense_buttons_order = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('За сегодня', callback_data=call_back_order.new(group='сегодня')),
        ],
        [
            InlineKeyboardButton('За неделю', callback_data=call_back_order.new(group='неделю')),
        ],
        [
            InlineKeyboardButton('За месяц', callback_data=call_back_order.new(group='месяц'))
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
    ]
)