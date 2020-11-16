import logging
import sqlite3
from datetime import datetime

import psycopg2 as sql
from typing import Dict

sqlite3.OperationalError()

# connect = sqlite3.connect('base.db')
connect = sql.connect(dbname='db_finbot',
                      user='bot_admin',
                      password='PmeT3mn7tPynhVqY254M',
                      host='localhost', port='5432')
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
    values = tuple(column_items.values())
    number = ', '.join(['%s'] * len(column_items.keys()))
    cursor.execute(
        f'INSERT INTO {table} '
        f'({columns})'
        f'VALUES ({number})', values)
    connect.commit()
    # connect.close()
    logging.info('Данные успешно внесены...')


# value_group = {
#         'id_user': 123,
#         'amount': 45,
#         'grouping': 'ежеднев',
#         'title': 'проезд',
#         'time': 2020,
# }
#
# insert_data('expense', value_group)

if __name__ == '__main__':
    make_default_db()
