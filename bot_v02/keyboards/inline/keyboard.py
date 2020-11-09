from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


profit_button = InlineKeyboardButton('Ежедневные', callback_data='everyday_profit')
profit_buttons = InlineKeyboardMarkup().add(profit_button)

