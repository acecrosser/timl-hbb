from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_profit = KeyboardButton('Доход')
button_expense = KeyboardButton('Расход')
button_settings = KeyboardButton('Настройки')

default_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

default_buttons.row(button_profit, button_expense)
default_buttons.add(button_settings)

