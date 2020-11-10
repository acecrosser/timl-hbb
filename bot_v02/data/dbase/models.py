import sqlite3
from typing import Dict


connect = sqlite3.connect('base.db')
cursor = connect.cursor()


def make_default_db():
    cursor.execute('CREATE TABLE profit '
                   '(id_user integer, amount real, grouping text, title text, time text)')
    cursor.execute('CREATE TABLE expense '
                   '(id_user integer, amount real, grouping text, title text, time text)')
    connect.commit()
    print('БД успешно создана')


def insert_data(table: str, column_items: Dict):
    columns = ', '.join(column_items.keys())
    values = [tuple(column_items.values())]
    number = ', '.join('?' * len(column_items.keys()))
    cursor.executemany(
        f'INSERT INTO {table} '
        f'({columns})'
        f'VALUES ({number})', values)
    connect.commit()


def give_cursor():
    return cursor

