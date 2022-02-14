import logging
from pprint import pformat

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView

from .ui.ui_main_window import Ui_MainWindow
from .vehicles import Vehicles
from .database import Database


# Главное окно приложения расширяет класс QWidget
class MainWindow(QMainWindow):

    # Конструктор
    def __init__(self):
        # Инициализация родительского класса
        super(MainWindow, self).__init__()

        # Установка интерфейса
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        """Объекты для работы с данными"""

        self.db = Database("app/data/test_db")
        self.vehicle_data = Vehicles(self.db)

        """Установка доп. параметров интерфейса"""

        # Запрет на редактирование данных в таблицах
        self.ui.veh_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.spec_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Запрет на редактирование размеров колонок таблиц
        self.ui.veh_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.ui.spec_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        # Выбор всей строки при нажатии
        self.ui.veh_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.spec_table.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Установка ширины отдельных колонок таблицы
        self.ui.veh_table.setColumnWidth(0, 40)
        self.ui.veh_table.setColumnWidth(1, 350)

        """Установка функционала элементов интерфейса"""
        self.set_veh_table()

        self.ui.veh_table.cellClicked.connect(self.set_spec_table)

    def set_veh_table(self, filter={}):
        all_veh = self.vehicle_data.get_all_veh(filter=filter)
        logging.info(all_veh)

        for i, vehicle in enumerate(all_veh):
            self.ui.veh_table.insertRow(i)
            self.ui.veh_table.setItem(i, 0, QTableWidgetItem(str(vehicle['id'])))
            self.ui.veh_table.setItem(i, 1, QTableWidgetItem(str(vehicle['name'])))
            self.ui.veh_table.setItem(i, 2, QTableWidgetItem(str(self.vehicle_data.status_list[vehicle['status']])))

    def set_spec_table(self):

        self.ui.spec_table.clear()
        id = self.ui.veh_table.item(self.ui.veh_table.currentItem().row(), 0).text()
        data = self.vehicle_data.get_spec(id=id)
        cols = self.vehicle_data.cols[1:]
        self.ui.spec_table.setRowCount(len(cols))
        logging.info(f'id: {id}\n' + pformat(data))

        for i, col in enumerate(cols):
            self.ui.spec_table.setItem(i, 0, QTableWidgetItem(self.vehicle_data.spec_list.get(col, col)))
            self.ui.spec_table.setItem(i, 1, QTableWidgetItem(str(data.get(col, i))))
