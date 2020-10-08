from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          KeyboardButton, InlineKeyboardButton, \
                          InlineKeyboardMarkup
import receiver


get_user = KeyboardButton('Авторизоваться', request_contact=True)
get_location = KeyboardButton('Локация', request_location=True)

profit_button = InlineKeyboardButton('Доход', callback_data='insert1')
expenses_button = InlineKeyboardButton('Расход', callback_data='insert0')


show_button = ReplyKeyboardMarkup(one_time_keyboard=True,
                                  resize_keyboard=True).row(profit_button,
                                                            expenses_button)

show_inline_button = InlineKeyboardMarkup().add(profit_button, expenses_button)



