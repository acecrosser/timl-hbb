from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from data.dbase.settings import list_settings


call_back_expense = CallbackData('exp', 'group')
call_back_order = CallbackData('order', 'group')
call_back_profit = CallbackData('prf', 'group')
call_back_profit_order = CallbackData('p_order', 'group')
call_back_settings = CallbackData('stg', 'group')
call_back_order_grouping = CallbackData('orders_group', 'group')


def set_buttons(grouping: str, callback, id_user):
    settings = list_settings(id_user=id_user, grouping=grouping)
    set_list = []
    for i in settings:
        inline_but = InlineKeyboardButton(f'{i[0]}', callback_data=callback.new(group=f'{str(i[0]).lower()}'))
        set_list.append(inline_but)
    inline_but = InlineKeyboardButton('Отмена', callback_data=callback.new(group='aborting'))
    set_list.append(inline_but)
    return InlineKeyboardMarkup(row_width=2).add(*set_list)


button_chose_what_group_order_make = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Расходы', callback_data=call_back_order_grouping.new(group='expense_order'))
        ],
        [
            InlineKeyboardButton('Доходы', callback_data=call_back_order_grouping.new(group='profit_order'))
        ],
        [
            InlineKeyboardButton('Отмена', callback_data=call_back_order_grouping.new(group='aborting_order'))
        ]
    ]
)


button_settings_group = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Расходы', callback_data=call_back_settings.new(group='expense'))
        ],
        [
            InlineKeyboardButton('Доходы', callback_data=call_back_settings.new(group='profit'))
        ],
        [
            InlineKeyboardButton('Отмена', callback_data=call_back_settings.new(group='aborting_stg'))
        ]

    ]
)

button_settings_group_del = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Расходы', callback_data=call_back_settings.new(group='expense_del'))
        ],
        [
            InlineKeyboardButton('Доходы', callback_data=call_back_settings.new(group='profit_del'))
        ],
        [
            InlineKeyboardButton('Отмена', callback_data=call_back_settings.new(group='aborting_stg_del'))
        ]

    ]
)


# expense_buttons_order = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton('За сегодня', callback_data=call_back_order.new(group='сегодня')),
#         ],
#         [
#             InlineKeyboardButton('Текущий месяц', callback_data=call_back_order.new(group='текущий месяц'))
#         ],
#         [
#             InlineKeyboardButton('Прошлый месяц', callback_data=call_back_order.new(group='прошлый месяц'))
#         ]
#     ]
# )


# profit_buttons = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton('Постоянный', callback_data=call_back_profit.new(group='постоянный'))
#         ],
#         [
#             InlineKeyboardButton('Дополнительный', callback_data=call_back_profit.new(group='дополнительный'))
#         ],
#         [
#             InlineKeyboardButton('Отмена', callback_data=call_back_profit.new(group='aborting'))
#         ]
#     ]
# )

# profit_buttons_order = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton('Текущий месяц', callback_data=call_back_profit_order.new(group='д текущий месяц'))
#         ],
#         [
#             InlineKeyboardButton('Прошлый месяц', callback_data=call_back_profit_order.new(group='д прошлый месяц'))
#         ]
#     ]
# )
