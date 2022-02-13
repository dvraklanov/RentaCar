import logging

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem

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

        # Установка доп. параметров интерфейса
        self.ui.veh_table.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)  # Запрет на редактирование данных в таблице

        self.ui.veh_table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Fixed)  # Запрет на редактирование размеров колонок таблицы

        # Установка ширины отдельных колонок таблицы
        self.ui.veh_table.setColumnWidth(0, 50)
        self.ui.veh_table.setColumnWidth(1, 450)
        self.ui.veh_table.setColumnWidth(2, 50)

        self.db = Database("app/data/test_db")
        self.vehicle_data = Vehicles(self.db)

        logging.info(self.vehicle_data.get_all_veh())

    def set_veh_table(self, filter={}):
        all_veh = self.vehicle_data.get_all_veh(filter=filter)
        logging.info(all_veh)

        for i, vehicle in enumerate(all_veh):
            self.ui.veh_table.insertRow(i)
            self.ui.veh_table.setItem(i, 0, QTableWidgetItem(str(vehicle[1])))
            self.ui.veh_table.setItem(i, 1, QTableWidgetItem(str(self.vehicle_data.status_list[vehicle[2]])))
