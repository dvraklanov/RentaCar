from utils import db


class Vehicles(object):

    def __init__(self):
        self.__db = db
        self.__table_name = 'vehicles'
        self.db_name = db.name

    # Получить id и название всех транспортных средств
    def get_all_veh(self, filter={}):
        return self.__db.select(table=self.__table_name, items=['id', 'name'], filter=filter)

    # Получить характеристики треанспортного средства по id
    def get_spec(self, id: int):
        return self.__db.select(table=self.__table_name, filter={'id': id})[0]

    def add_veh(self, name: str, class_: str):
        self.__db.insert(table=self.__table_name, cols=['name', 'class'], values=[name, class_])

    def del_veh(self, id: int):
        return self.__db.delete(table=self.__table_name, filter={'id': id})
