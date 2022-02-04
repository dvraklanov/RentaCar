import sqlite3


class Database(object):

    def __init__(self, path: str):
        self.db_name = path + '.db'
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        print("Connection to db is opened. Database: {}".format(self.db_name))

    def __del__(self):
        self.conn.close()
        print("Connection to db is closed")

    def select(self, table: str, items='*', where=''):
        sql = "SELECT {items} FROM {table} ".format(items=items, table=table)
        if where: sql += "WHERE {where}".format(where=where)
        print(sql)
        response = self.cursor.execute(sql).fetchall()
        return response

    def insert(self, table: str, cols: str, values: tuple):
        sql = "INSERT INTO {table} {cols} VALUES {values}".format(table=table, cols=str(cols).replace("'", ""),
                                                                  values=str(values))
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
