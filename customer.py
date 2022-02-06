import logging
from database import Database


class Customers(object):

    def __init__(self, db: Database):
        self.__db = db
        self.__table_name = 'customers'

    # Получить id и название всех транспортных средств
    def get_all_cust(self, filter={}):
        return self.__db.select(table=self.__table_name,
                                items=['id', 'name', 'score'],
                                filter=filter)

    def get_cust(self, id: int):
        return self.__db.select(table=self.__table_name,
                                filter={'id': id})[0]

    def del_cust(self, id: int):
        self.__db.delete(table=self.__table_name,
                         filter={'id': id})
