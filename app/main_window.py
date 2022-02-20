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
        self.veh_filter = dict()

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
        self.ui.veh_table.cellClicked.connect(self.set_spec_table)
        self.ui.find_btn.clicked.connect(self.find_by_filter)

        """Действия при запуске программы"""
        self.set_veh_table()
        self.fill_checkbox()

    # Заполынение таблицы траснпорта
    def set_veh_table(self):

        all_veh = self.vehicle_data.get_all_veh(filter=self.veh_filter)
        self.ui.veh_table.setRowCount(0)
        self.ui.veh_table.setRowCount(len(all_veh))

        for i, vehicle in enumerate(all_veh):
            self.ui.veh_table.setItem(i, 0, QTableWidgetItem(str(vehicle['id'])))
            self.ui.veh_table.setItem(i, 1, QTableWidgetItem(str(vehicle['name'])))
            self.ui.veh_table.setItem(i, 2, QTableWidgetItem(str(self.vehicle_data.status_list[vehicle['status']])))

    # Заполнение таблицы с информацией
    def set_spec_table(self):

        self.ui.spec_table.setRowCount(0)
        id = self.ui.veh_table.item(self.ui.veh_table.currentItem().row(), 0).text()
        data = self.vehicle_data.get_spec(id=id)
        cols = self.vehicle_data.cols[1:]
        self.ui.spec_table.setRowCount(len(cols))

        for i, col in enumerate(cols):
            self.ui.spec_table.setItem(i, 0, QTableWidgetItem(self.vehicle_data.spec_list.get(col, col)))
            item = str(data.get(col, i))
            self.ui.spec_table.setItem(i, 1, QTableWidgetItem(item if col != 'status' else
                                                              self.vehicle_data.status_list[int(item)]))

    def fill_checkbox(self):

        cols = self.vehicle_data.cols[1:]
        for col in cols:
            if hasattr(self.ui, col+'_v'):

                checkbox = self.ui.__getattribute__(col+'_v')
                for item in self.vehicle_data.get_uniq_spec(col):
                    checkbox.addItem(str(item))

    def find_by_filter(self):

        cols = self.vehicle_data.cols[1:]
        for col in cols:
            if hasattr(self.ui, col + '_v'):
                checkbox_v = self.ui.__getattribute__(col + '_v').currentText()
                if checkbox_v:
                    self.veh_filter[col] = checkbox_v

        self.set_veh_table()
        self.veh_filter.clear()


