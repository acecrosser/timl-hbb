from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


default_buttons = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True,
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
    resize_keyboard=True,
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

