import logging
from .database import Database


class Customers(object):

    def __init__(self, db: Database):
        self.db = db
        self.db_name = db.name
        self.table_name = 'customers'
        self.cols = self.db.get_table_cols(self.table_name)
        self.fields_labels = ['name', 'lastname', 'surname', 'pass_id']

    # Получить id и данные всех клиентов
    def get_all_cust(self, filter=None):
        if filter is None:
            filter = {}
        return self.db.select(table=self.table_name, cols=['id'] + self.fields_labels,
                              filter=filter)

    def get_cust(self, cust_id: int):
        return self.db.select(table=self.table_name, filter={'id': cust_id})[0]

    # Отредактировать значения в существующей записи
    def edit_cust(self, cust_id: int, new_values: Database.ItemData):
        self.db.update(table=self.table_name,
                       new_values=new_values, filter={'id': cust_id})

    # Удалить запись о клиенте
    def del_cust(self, cust_id: int):
        self.db.delete(table=self.table_name,
                       filter={'id': cust_id})
