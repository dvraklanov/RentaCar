import sqlite3
import logging


class Database(object):

    # Конструктор
    def __init__(self, path: str):
        self.name = path + '.db'
        self.conn = sqlite3.connect(self.name)
        self.cursor = self.conn.cursor()
        logging.debug("Connection to db is opened. Database: {}".format(self.name))

    # Деструктор
    def __del__(self):
        self.cursor.close()
        self.conn.close()

    # Получить данные
    def select(self, table: str, items='*', filter={}, unique=False):
        sql = "SELECT {unique}{items} FROM {table} ".format(items=f"{', '.join(items)}",
                                                            table=table,
                                                            unique=" DISTINCT" if unique else "")
        # Если добавлен фильтр
        if filter:
            filter_str = [str(key) + '=' + (str(value) if type(value) == int else f"'{value}'") for key, value in
                          filter.items()]
            sql += "WHERE {filter}".format(filter=' and '.join(filter_str))

        logging.debug(sql)

        response = self.cursor.execute(sql).fetchall()
        return response

    # Добавить значения
    def insert(self, table: str, cols: list, values: list):
        sql = "INSERT INTO {table} ({cols}) VALUES ({values})".format(table=table, cols=", ".join(cols),
                                                                      values=", ".join(
                                                                          [f"'{value}'" for value in values]))

        logging.debug(sql)
        self.cursor.execute(sql)
        self.conn.commit()

    # Удалить строку значений
    def delete(self, table: str, filter: dict):
        filter_str = [str(key) + '=' + (str(value) if type(value) == int else f"'{value}'") for key, value in
                      filter.items()]
        sql = "DELETE FROM {table} WHERE {filter}".format(table=table,
                                                          filter=' and '.join(filter_str))

        logging.debug(sql)
        self.cursor.execute(sql)
        self.conn.commit()

    # Создание таблицы, если не существует
    def create_table(self, table_name: str, cols: dict):
        cols_str = [f'{col["name"]} {col["type"]} {col.get("param", "").upper()}' for col in cols]
        sql = """
        CREATE TABLE IF NOT EXISTS{table_name}  
        ({cols_str})    
        """.format(table_name=table_name, cols_str=cols_str)

        self.cursor.execute(sql)
        self.conn.commit()
