from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.dbase.settings import list_settings


def set_default_button(grouping: str):
    settings = list_settings(id_user='5093906', grouping=grouping)
    set_list = []
    for i in settings:
        set_list.append([KeyboardButton(f'{i[0]}')])
    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, keyboard=set_list)


default_buttons = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=False,
    keyboard=[
        [
            KeyboardButton('Доход'),
            KeyboardButton('Расход')
        ],
        [
            KeyboardButton('Отчеты'),
            KeyboardButton('Настройки')
        ]
    ]
)

settings_buttons = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=False,
    keyboard=[
        [
            KeyboardButton('Добавить'),
            KeyboardButton('Удалить')
        ],
        [
            KeyboardButton('Список'),
            KeyboardButton('Назад')
        ],
    ]
)

ordering_buttons = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=False,
    keyboard=[
        [
            KeyboardButton('По категориям'),
            KeyboardButton('Общий'),
        ],
        [
            KeyboardButton('Годовой'),
            KeyboardButton('Назад')
        ]
    ]
)