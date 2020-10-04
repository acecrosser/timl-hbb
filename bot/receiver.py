from typing import Optional, NamedTuple
import dbase
import datetime
import re


class NotCorrectMessage(Exception):
    pass


class Message(NamedTuple):
    amount: int
    text: str


class AddData(NamedTuple):
    id: Optional[int]
    amount: int
    name: str


def add_data(raw_message: str) -> AddData:
    parsed_msg = _parse_message(raw_message)
    inserted_row_id = dbase.insert_data('ALL_DATA', {
        'amount': parsed_msg.amount,
        'created': _get_now_datetime(),
        'types': parsed_msg.text
    })
    return AddData(id=None, amount=parsed_msg.amount, name=parsed_msg.text)


def _parse_message(raw_message: str) -> Message:
    reg_result = re.match(r'([\d ]+) (.*)', raw_message)
    if not reg_result or not reg_result.group(0) \
            or not reg_result.group(1) or not reg_result.group(2):
        raise NotCorrectMessage('Не могу понять сообщение, попробуй в другом формате')

    amount = reg_result.group(1).replace(' ', '')
    text = reg_result.group(2).strip().lower()
    # print(amount, text)
    return Message(amount=amount, text=text)


def _get_now_datetime() -> str:
    now_time = datetime.datetime.now()
    format_time = now_time.strftime('%d-%m-%Y %H:%M:%S')
    return format_time




