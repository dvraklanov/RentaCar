import logging
from database import Database


class Customers(object):

    def __init__(self, db: Database):
        self.__db = db
        self.__table_name = 'customers'

    # Получить id и имя всех клиентов в базе
    def get_all_cust(self, filter={}):
        return self.__db.select(table=self.__table_name,
                                items=['id', 'name', 'score'],
                                filter=filter)

    # Получить информацию о клиенте по id
    def get_cust(self, id: int):
        return self.__db.select(table=self.__table_name,
                                filter={'id': id})[0]

    # Добавить новое транспортное средство
    def add_cust(self, cust_data: dict):
        self.__db.insert(table=self.__table_name,
                         cols=list(cust_data.keys()),
                         values=[cust_data[key] for key in cust_data.keys()])

    # Отредактировать значения в существующей записи
    def edit_cust(self, id: int, new_values: dict):
        self.__db.update(table=self.__table_name,
                         new_values=new_values, filter={'id': id})

    # Удаление клиента
    def del_cust(self, id: int):
        self.__db.delete(table=self.__table_name,
                         filter={'id': id})
