import datetime
import re
from typing import Optional, NamedTuple

import dbase
import exceptions

first_user = 'acecrosser'


class Message(NamedTuple):
    amount: int
    type_data: str
    category: str
    name: str


class AddData(NamedTuple):
    id: Optional[int]
    amount: int
    name: str


class GeneralData(NamedTuple):
    amount: int
    type_data: str
    category: str
    name: str
    author: str


def general_data(raw_msg: str) -> GeneralData:
    parsed_general_msg = _parse_general_data(raw_msg)
    add_to_db = dbase.insert_data('MONEY_MOVEMENT', {
        'date': _get_now_datetime(),
        'amount': parsed_general_msg.amount,
        'type': parsed_general_msg.type_data,
        'category': parsed_general_msg.category,
        'name': parsed_general_msg.name,
        'author': first_user
    })
    return GeneralData(amount=parsed_general_msg.amount, type_data=parsed_general_msg.type_data, category=parsed_general_msg.category,
                       name=parsed_general_msg.name, author=first_user)


def _parse_general_data(raw_msg: str) -> Message:
    result_msg = re.match(r'([\d ]+) (\D+) (\D+) (\D+)', raw_msg)
    if not result_msg or not result_msg.group(0) \
            or not result_msg.group(1) or not result_msg.group(2):
        raise exceptions.NotCorrectMessage('Не могу понять сообщение.')
    amount = int(result_msg.group(1))
    type_data = result_msg.group(2)
    category = result_msg.group(3)
    name = result_msg.group(4)
    return Message(amount=amount, type_data=type_data, category=category, name=name)


def echo(name='wat"s up doc'):
    return name

# def add_data(raw_message: str) -> AddData:
#     parsed_msg = _parse_message(raw_message)
#     inserted_row_id = dbase.insert_data('ALL_DATA', {
#         'amount': parsed_msg.amount,
#         'created': _get_now_datetime(),
#         'types': parsed_msg.text
#     })
#     return AddData(id=None, amount=parsed_msg.amount, name=parsed_msg.name)


def add_profit(raw_message: str) -> AddData:
    parsed_msg = _parse_me(raw_message)
    add_to_db = dbase.insert_data('PROFIT', {
        'created': _get_now_datetime(),
        'amount': parsed_msg.amount,
        'name': parsed_msg.name,
    })
    return AddData(id=None, amount=parsed_msg.amount, name=parsed_msg.name)
#
#
# def _parse_message(raw_message: str) -> Message:
#     reg_result = re.match(r'([\d ]+) (.*)', raw_message)
#     if not reg_result or not reg_result.group(0) \
#             or not reg_result.group(1) or not reg_result.group(2):
#         raise exceptions.NotCorrectMessage('Не могу понять сообщение, попробуй в другом формате')
#
#     amount = reg_result.group(1).replace(' ', '')
#     text = reg_result.group(2).strip().lower()
#     # print(amount, text)
#     return Message(amount=amount, name=text)


def _parse_me(raw_msg: str) -> Message:
    reg_result = re.match(r'(Доход) ([\d ]+) (.*)', raw_msg)
    if not reg_result or not reg_result.group(0) or not reg_result.group(2) or not reg_result.group(3):
        raise exceptions.NotCorrectMessage('Не могу понять сообщения, пишит так: Доход-Расход Сумма Имя')
    amount = reg_result.group(2).replace(' ', '')
    name = reg_result.group(3).strip()
    return Message(amount=amount, name=name)


def _get_now_datetime() -> str:
    now_time = datetime.datetime.now()
    format_time = now_time.strftime('%d-%m-%Y %H:%M:%S')
    return format_time




