import sqlite3


class Database(object):

    # Конструктор
    def __init__(self, path: str):
        self.db_name = path + '.db'
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        print("Connection to db is opened. Database: {}".format(self.db_name))

    # Деструктор
    def __del__(self):
        self.conn.close()
        print("Connection to db is closed")

    # Получить данные из базы
    def select(self, table: tuple, items='*', where=''):
        sql = "SELECT {items} FROM {table} ".format(items=items, table=table)
        if where: sql += "WHERE {where}".format(where=where)
        print(sql)
        response = self.cursor.execute(sql).fetchall()
        return response

    # Добавить значения в базу
    def insert(self, table: str, cols: str, values: tuple):
        sql = "INSERT INTO {table} {cols} VALUES {values}".format(table=table, cols=str(cols).replace("'", ""),
                                                                  values=str(values))
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
