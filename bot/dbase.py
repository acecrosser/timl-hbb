import sqlite3
import os
from typing import Dict, List, Tuple

connect = sqlite3.connect(os.path.join('dbase', 'data.db'))
cursor = connect.cursor()


def insert_data(table: str, column_values: Dict):
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    how_many = ', '.join('?' * len(column_values.keys()))
    cursor.executemany(
        f'INSERT INTO {table} '
        f'({columns}) '
        f'VALUES ({how_many})',
        values)
    connect.commit()
