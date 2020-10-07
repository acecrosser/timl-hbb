from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          KeyboardButton, InlineKeyboardButton, \
                          InlineKeyboardMarkup


button = KeyboardButton('Доход')
show_button = ReplyKeyboardMarkup(resize_keyboard=True).add(button)


