import logging
from typing import Dict
from .connect import cursor


def insert_data(table: str, column_items: Dict):
    columns = ', '.join(column_items.keys())
    values = tuple(column_items.values())
    number = ', '.join(['%s'] * len(column_items.keys()))
    cursor.execute(
        f'INSERT INTO {table} '
        f'({columns})'
        f'VALUES ({number})', values)
    logging.info('Данные успешно внесены...')


def today(table: str, id_user: str, period: str):
    cursor.execute(
        f"SELECT sum(amount) "
        f"FROM {table} "
        f"WHERE id_user='{id_user}' "
        f"AND time LIKE '{period}%'"
    )
    summa_today = cursor.fetchone()
    return summa_today


def distinct(table: str, id_user: str, period: str):
    cursor.execute(
        f"SELECT DISTINCT title "
        f"FROM {table} "
        f"WHERE id_user='{id_user}' "
        f"AND time LIKE '{period}%'"
    )
    distinct_data = cursor.fetchall()
    return distinct_data


def sum_title(table: str, id_user: str, period: str, grouping: str) -> float:
    cursor.execute(
        f"SELECT SUM(amount) "
        f"FROM {table} "
        f"WHERE id_user='{id_user}' "
        f"AND grouping LIKE '{grouping}%' "
        f"AND time LIKE '{period}%'"
    )
    title_sum = cursor.fetchone()
    return title_sum
