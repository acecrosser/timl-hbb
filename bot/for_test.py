import re
from typing import NamedTuple


class NotCorrectMessage(Exception):
    pass


class Message(NamedTuple):
    amount: int
    text: str


def _parse_message(raw_message: str) -> Message:
    reg_result = re.match(r'([\d ]+) (.*)', raw_message)
    if not reg_result or not reg_result.group(0) \
            or not reg_result.group(1) or not reg_result.group(2):
        raise NotCorrectMessage('Не могу понять сообщение, попробуй в другом формате')

    amount = reg_result.group(1).replace(' ', '')
    text = reg_result.group(2).strip().lower()
    print(amount, text)
    return Message(amount=amount, text=text)


_parse_message('3000 Людей')


def _parse_me(raw_msg: str) -> Message:
    reg_result = re.match(r'(["Доход"] +) ([\d] +) (.*)', raw_msg)
    if not reg_result or not reg_result.group(0) or not reg_result.group(2) or not reg_result.group(3):
        raise NotCorrectMessage('Не могу понять сообщения, пишит так: Доход/Расход Сумма Имя')
    amount = reg_result.group(1).replace(' ', '')
    name = reg_result.group(2).strip()
    return Message(amount=amount, text=name)


_parse_me('Доход 5000 Пузанков')