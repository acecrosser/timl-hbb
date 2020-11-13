from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


profit_button = InlineKeyboardButton('Ежедневный', callback_data='everyday_profit')
profit_buttons = InlineKeyboardMarkup().add(profit_button)


call_back_expense = CallbackData('exp', 'group')

expense_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Ежедневный', callback_data=call_back_expense.new(group='day')),
        ],
        [
            InlineKeyboardButton('Недельный', callback_data=call_back_expense.new(group='week')),
        ],
        [
            InlineKeyboardButton('Ежемесячный', callback_data=call_back_expense.new(group='month'))
        ]
    ]
)
