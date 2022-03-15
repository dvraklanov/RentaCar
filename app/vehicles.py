from typing import NoReturn

from app.database import Database


class Vehicles(object):

    def __init__(self, db: Database):
        self.__db = db
        self.__table_name = 'vehicles'
        self.db_name = db.name
        self.cols = self.__db.get_table_cols(table=self.__table_name)

        # Данные требуемые при добавлении автомобиля
        self.spec_list = {'name': 'Модель', 'number_plate': 'Гос. номер',
                          'body_type': 'Тип кузова', 'wheel_drive': 'Тип привода',
                          'fuel_type': 'Тип топлива', 'power_hp': 'Мощность (л.с.)',
                          'n_seat': 'Кол-во мест', 'gearbox_type': 'Тип КПП',
                          'rental_price': 'Стоимость (руб./сут.)', 'status': 'Статус',
                          'leased_from': 'Начало аренды', 'leased_to': 'Окончание аренды',
                          'cust_id': 'Id арендатора'}

        # Возможные состояния транспортного средства
        self.status_list = ['Не доступно', 'Доступно', 'В аренде']

    # Получить id и название всех транспортных средств
    def get_all_veh(self, filter: Database.ItemData = {}) -> Database.ItemsList:
        return self.__db.select(table=self.__table_name, cols=['id', 'name', 'status'], filter=filter)

    # Получить характеристики треанспортного средства по id
    def get_spec(self, veh_id: int) -> Database.ItemsList:
        return self.__db.select(table=self.__table_name, filter={'id': veh_id})[0]

    # Получить уникальные значение столбца характеристики
    def get_uniq_spec(self, col: str) -> Database.ItemsList:
        data = self.__db.select(table=self.__table_name, cols=[col], unique=True)
        data_list = [item[col] for item in data]
        return data_list

    # Отредактировать значения в существующей записи
    def edit_spec(self, veh_id: int, new_values: Database.ItemData) -> NoReturn:
        self.__db.update(table=self.__table_name,
                         new_values=new_values, filter={'id': veh_id})

    # Добавить новое транспортное средство
    def add_veh(self, veh_data: dict) -> NoReturn:
        self.__db.insert(table=self.__table_name,
                         cols=list(veh_data.keys()),
                         values=[veh_data[key] for key in veh_data.keys()])

    # Удаление транспортного средства по id
    def del_veh(self, veh_id: int) -> NoReturn:
        self.__db.delete(table=self.__table_name,
                         filter={'id': veh_id})
