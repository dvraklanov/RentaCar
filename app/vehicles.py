from app.database import Database


class Vehicles(object):

    def __init__(self, db: Database):
        self.__db = db
        self.__table_name = 'vehicles'
        self.db_name = db.name
        self.cols = self.__db.get_table_cols(table=self.__table_name)

        # Данные требуемые при добавлении автомобиля
        self.spec_list = {'name': 'Название модели', 'number_plate': 'Гос. номер',
                          'body_type': 'Тип кузова', 'wheel_drive': 'Тип привода',
                          'fuel_type': 'Тип топлива', 'power_hp': 'Мощность (л.с.)',
                          'n_seat': 'Кол-во мест', 'gearbox_type': 'КПП',
                          'rental_price': 'Стоимость аренды (руб./сут.)', 'status': 'Статус',
                          'leased_from': 'Начало аренды', 'leased_to': 'Окончание аренды'}

        # Возможные состояния транспортного средства
        self.status_list = ['Не доступно', 'Доступно', 'В аренде']

    # Получить id и название всех транспортных средств
    def get_all_veh(self, filter=None):
        if filter is None:
            filter = {}
        return self.__db.select(table=self.__table_name,
                                items=['id', 'name', 'status'],
                                filter=filter)

    # Получить характеристики треанспортного средства по id
    def get_spec(self, id: int):
        return self.__db.select(table=self.__table_name,
                                filter={'id': id})[0]

    # Получить уникальные значение столбца характеристики
    def get_uniq_spec(self, col: str):
        data = self.__db.select(table=self.__table_name,
                                items=[col], unique=True)
        data_list = [item[col] for item in data]
        return data_list

    # Отредактировать значения в существующей записи
    def edit_spec(self, id: int, new_values: dict):
        self.__db.update(table=self.__table_name,
                         new_values=new_values, filter={'id': id})

    # Добавить новое транспортное средство
    def add_veh(self, veh_data: dict):
        self.__db.insert(table=self.__table_name,
                         cols=list(veh_data.keys()),
                         values=[veh_data[key] for key in veh_data.keys()])

    # Удаление транспортного средства по id
    def del_veh(self, id: int):
        self.__db.delete(table=self.__table_name,
                         filter={'id': id})
