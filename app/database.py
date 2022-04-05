from typing import List, Dict, Tuple, Union, NoReturn
import logging
import sqlite3


class Database(object):
    ItemData = Dict[str, Union[str, int]]
    ItemsList = List[ItemData]
    ColName = List[str]
    ColValue = List[Union[str, int]]

    # Конструктор
    def __init__(self, path: str):
        self.name = path + '.db'
        self.conn, self.cursor = self.connect()
        logging.debug("Connection to db is opened. Database: {}".format(self.name))

    # Деструктор
    def __del__(self):
        if hasattr(self, 'cursor'):
            self.cursor.close()
            self.conn.close()

    # Подключение к базе
    def connect(self) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:

        try:
            conn = sqlite3.connect(self.name)
            cursor = conn.cursor()
            return conn, cursor
        except sqlite3.OperationalError as e:
            logging.error(f"Ошибка при подключении к базе {self.name}")
            raise e

    # Получить данные
    def select(self, table: str, filter: ItemData = {}, cols: ColName = (), unique: bool = False)\
            -> ItemsList:

        if not cols:
            cols = '*'

        sql = "SELECT {unique}{items} FROM {table} ".format(items=f"{', '.join(cols)}",
                                                            table=table,
                                                            unique="DISTINCT " if unique else "")
        # Если добавлен фильтр
        if filter:
            filter_str = ' and '.join(
                [str(key) + '=' + (str(value) if type(value) == int else f"'{value}'") for key, value in
                 filter.items()])
            sql += "WHERE {filter}".format(filter=filter_str)

        try:
            data = self.cursor.execute(sql).fetchall()
            cols = cols if cols != "*" else self.get_table_cols(table=table)
            data_to_dict = [{col: item for col, item in zip(cols, row)} for row in data]
            logging.debug(sql)
            return data_to_dict
        except (sqlite3.IntegrityError, sqlite3.OperationalError) as e:
            logging.error(f"\n{e}\nОшибка при отправке SQL. Проверьте запрос:\n{sql}")

    # Добавить значения
    def insert(self, table: str, cols: ColName, values: ColValue) -> NoReturn:
        sql = "INSERT INTO {table} ({cols}) VALUES ({values})".format(table=table, cols=", ".join(cols),
                                                                      values=", ".join(
                                                                          [f"'{value}'" for value in values]))

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            logging.debug(sql)
        except (sqlite3.IntegrityError, sqlite3.OperationalError) as e:
            logging.error(f"\n{e}\nОшибка при отправке SQL. Проверьте запрос:\n{sql}")

    def update(self, table: str, new_values: ItemData, filter: ItemData) -> NoReturn:
        # Преобразование словаря в строку вида: "столбец" = значение, ...
        new_values_str = ','.join(
            [str(key) + '=' + (str(value) if type(value) == int else f"'{value}'") for key, value in
             new_values.items()])

        # Преобразование словаря в строку вида: "столбец" = значение and ...
        filter_str = ' and '.join(
            [str(key) + '=' + (str(value) if type(value) == int else f"'{value}'") for key, value in
             filter.items()])

        sql = "UPDATE {table} SET {new_values} WHERE {filter}".format(table=table,
                                                                      new_values=new_values_str,
                                                                      filter=filter_str)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            logging.debug(sql)
        except (sqlite3.IntegrityError, sqlite3.OperationalError) as e:
            logging.error(f"\n{e}\nОшибка при отправке SQL. Проверьте запрос:\n{sql}")

    # Удалить строку значений
    def delete(self, table: str, filter: ItemData) -> NoReturn:
        # Преобразование словаря в строку вида: "столбец" = значение, ...
        filter_str = [str(key) + '=' + (str(value) if type(value) == int else f"'{value}'") for key, value in
                      filter.items()]
        sql = "DELETE FROM {table} WHERE {filter}".format(table=table,
                                                          filter=' and '.join(filter_str))

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            logging.debug(sql)
        except (sqlite3.IntegrityError, sqlite3.OperationalError) as e:
            logging.error(f"\n{e}\nОшибка при отправке SQL. Проверьте запрос:\n{sql}")

    # Создание таблицы, если не существует (пока не используется, таблица создается в ручную)
    def create_table(self, table_name: str, cols: dict) -> NoReturn:
        cols_str = [f'{col["name"]} {col["type"]} {col.get("param", "").upper()}' for col in cols]
        sql = """
        CREATE TABLE IF NOT EXISTS{table_name}  
        ({cols_str})    
        """.format(table_name=table_name, cols_str=cols_str)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            logging.debug(sql)
        except (sqlite3.IntegrityError, sqlite3.OperationalError) as e:
            logging.error(f"\n{e}\nОшибка при отправке SQL. Проверьте запрос:\n{sql}")

    # Получение информации о таблице
    def get_table_info(self, table: str) -> List:

        sql = f"pragma table_info({table})"
        try:
            data = self.cursor.execute(sql).fetchall()
            logging.debug(sql)
            return data
        except (sqlite3.IntegrityError, sqlite3.OperationalError) as e:
            logging.error(f"\n{e}\nОшибка при отправке SQL. Проверьте запрос:\n{sql}")

    # Получение название столбцов в таблице
    def get_table_cols(self, table: str) -> List[str]:

        sql = f"SELECT name FROM PRAGMA_TABLE_INFO('{table}')"
        try:
            data = self.cursor.execute(sql).fetchall()
            data = list(map(lambda x: x[0], data))
            logging.debug(sql)
            return data
        except (sqlite3.IntegrityError, sqlite3.OperationalError) as e:
            logging.error(f"\n{e}\nОшибка при отправке SQL. Проверьте запрос:\n{sql}")

    def get_last_added_id(self) -> int:

        sql = "SELECT last_insert_rowid()"

        try:
            data = self.cursor.execute(sql).fetchone()[0]
            logging.debug(sql)
            return data
        except (sqlite3.IntegrityError, sqlite3.OperationalError) as e:
            logging.error(f"\n{e}\nОшибка при отправке SQL. Проверьте запрос:\n{sql}")