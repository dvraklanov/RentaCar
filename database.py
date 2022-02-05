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

    # Получить данные из базы
    def select(self, table: str, items='*', filter={}):
        sql = "SELECT {items} FROM {table} ".format(items=f"{', '.join(items)}",
                                                    table=table)

        if filter:
            filter_str = [str(key) + '=' + (str(value) if type(value) == int else f"'{value}'") for key, value in
                          filter.items()]
            sql += "WHERE {filter}".format(filter=' and '.join(filter_str))

        logging.debug(sql)

        response = self.cursor.execute(sql).fetchall()
        return response

    # Добавить значения в базу
    def insert(self, table: str, cols: list, values: list):
        sql = "INSERT INTO {table} ({cols}) VALUES ({values})".format(table=table, cols=", ".join(cols),
                                                                      values=", ".join(
                                                                          [f"'{value}'" for value in values]))
        logging.debug(sql)
        self.cursor.execute(sql)
        self.conn.commit()

    def delete(self, table: str, filter: dict):
        filter_str = [str(key) + '=' + (str(value) if type(value) == int else f"'{value}'") for key, value in
                      filter.items()]
        sql = "DELETE FROM {table} WHERE {filter}".format(table=table,
                                                          filter=' and '.join(filter_str))
        logging.debug(sql)
        self.cursor.execute(sql)
        self.conn.commit()
