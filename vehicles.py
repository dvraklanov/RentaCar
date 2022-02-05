import logging
from sqlite3 import IntegrityError
from utils import db


class Vehicles(object):

    def __init__(self):
        self.__db = db
        self.__table_name = 'vehicles'
        self.db_name = db.name

        # Данные требуемые при добавлении автомобиля
        self.spec_list = {'name': 'Название модели', 'number_plate': 'Гос. номер',
                          'body_type': 'Тип кузова', 'wheel_drive': 'Тип привода',
                          'fuel_type': 'Тип топлива', 'power_hp': 'Мощность (л.с.)',
                          'n_seat': 'Кол-во мест', 'gearbox_type': 'КПП',
                          'rental_price': 'Стоимость аренды'}

        # Возможные состояния транспортного средства
        self.status_list = ['Не доступно', 'Доступно', 'В аренде']

    # Получить id и название всех транспортных средств
    def get_all_veh(self, filter={}):
        return self.__db.select(table=self.__table_name,
                                items=['id', 'name', 'status'],
                                filter=filter)

    # Получить характеристики треанспортного средства по id
    def get_spec(self, id: int):
        return self.__db.select(table=self.__table_name,
                                filter={'id': id})[0]

    # Получить уникальные значение столбца характеристики
    def get_uniq_spec(self, col: str):
        return self.__db.select(table=self.__table_name,
                                items=[col], unique=True)

    # Добавить новое транспортное средство
    def add_veh(self, veh_data: dict):
        veh_data_keys = set(veh_data.keys())
        spec_list_keys = set(self.spec_list.keys())

        # Если в атрибутах есть все столбцы
        if veh_data_keys == spec_list_keys:
            self.__db.insert(table=self.__table_name,
                             cols=spec_list_keys,
                             values=[veh_data[spec] for spec in spec_list_keys])

        else:
            # Проверка на недостающие и лишние столбцы
            if spec_list_keys.difference(veh_data_keys):
                msg = f"Columns ({', '.join(spec_list_keys.difference(veh_data_keys))}) not found."
                logging.error(msg)
                raise AttributeError(msg)

            elif veh_data_keys.difference(spec_list_keys):
                msg = f"Table {self.__table_name} haven't column " \
                      f"({', '.join(veh_data_keys.difference(spec_list_keys))})."
                logging.error(msg)
                raise AttributeError(msg)

    # Удаление транспортного средства по id
    def del_veh(self, id: int):
        return self.__db.delete(table=self.__table_name,
                                filter={'id': id})
