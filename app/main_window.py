import os
import logging
import shutil

from typing import NoReturn

from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QCloseEvent, QPixmap
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView
from .ui.ui_main_window import Ui_MainWindow
from .vehicle_form import VehicleForm
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

        self.veh_form_valid = {"number_plate": {"func": lambda x: x not in self.vehicle_data.get_uniq_spec("number_plate"),
                                                "msg": "Автомобиль с введеным гос. номером уже существует в базе."},
                               "n_seat": {"func": lambda x: x.isdigit(),
                                          "msg": f"{self.vehicle_data.spec_dict['n_seat']} должно быть числом"},
                               "power_hp": {"func": lambda x: x.isdigit(),
                                            "msg": f"{self.vehicle_data.spec_dict['power_hp']} должно быть числом"},
                               "name": {"func": lambda x: not x.isdigit(),
                                        "msg": "Введите корректное название авто."},
                               "rental_price": {"func": lambda x: x.isdigit(),
                                                "msg": f"{self.vehicle_data.spec_dict['rental_price']} должно быть числом"}
                               }
        self.veh_form = VehicleForm(vehicle_db=self.vehicle_data, valid_params=self.veh_form_valid)

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

        # Установка ширины отдельных колонок таблиц автомобилей и характеристик
        self.ui.veh_table.setColumnWidth(0, 45)
        self.ui.veh_table.setColumnWidth(1, 150)

        self.ui.spec_table.setColumnWidth(0, 200)

        """Установка функционала элементов интерфейса"""
        self.ui.veh_table.cellClicked.connect(self.set_spec_table)
        self.ui.find_btn.clicked.connect(self.find_by_filter)
        self.ui.add_veh_btn.clicked.connect(self.veh_form.show)
        self.veh_form.FormFilled.connect(self.get_veh_form_v)

        """Действия при запуске программы"""
        self.set_veh_table()
        self.fill_combobox()

    # Заполнение таблицы траснпорта
    def set_veh_table(self) -> NoReturn:

        all_veh = self.vehicle_data.get_all_veh(filter=self.veh_filter)
        self.ui.veh_table.setRowCount(0)
        self.ui.veh_table.setRowCount(len(all_veh))

        for i, vehicle in enumerate(all_veh):
            self.ui.veh_table.setItem(i, 0, QTableWidgetItem(str(vehicle['id'])))
            self.ui.veh_table.setItem(i, 1, QTableWidgetItem(str(vehicle['name'])))
            self.ui.veh_table.setItem(i, 2, QTableWidgetItem(str(self.vehicle_data.status_list[vehicle['status']])))

    # Заполнение таблицы с информацией об авто
    def set_spec_table(self) -> NoReturn:

        self.ui.spec_table.setRowCount(0)
        veh_id = self.ui.veh_table.item(self.ui.veh_table.currentItem().row(), 0).text()
        data = self.vehicle_data.get_spec(veh_id=veh_id)
        cols = self.vehicle_data.cols[1:]
        self.ui.spec_table.setRowCount(len(cols))

        # Если существует картинка, до загрузить ее
        self.ui.img_box.clear()
        img_path = f"app/data/img/{veh_id}.jpg"
        if os.path.exists(img_path) and os.path.isfile(img_path):
            veh_img = QPixmap(img_path)
            veh_img = veh_img.scaledToHeight(self.ui.img_box.height())
            self.ui.img_box.setPixmap(veh_img)
        else:
            logging.debug(f"Can't find img file for veh (id ={veh_id})")

        for i, col in enumerate(cols):
            self.ui.spec_table.setItem(i, 0, QTableWidgetItem(self.vehicle_data.spec_dict.get(col, col)))
            item = str(data.get(col, i))
            self.ui.spec_table.setItem(i, 1, QTableWidgetItem(item if col != 'status' else
                                                              self.vehicle_data.status_list[int(item)]))

    # Заполнить опции фильтра
    def fill_combobox(self) -> NoReturn:

        cols = self.vehicle_data.cols[1:]
        for col in cols:
            if hasattr(self.ui, col + '_v'):
                checkbox = self.ui.__getattribute__(col + '_v')
                for item in self.vehicle_data.get_uniq_spec(col):
                    checkbox.addItem(str(item))

    # Поиск по фильтру
    def find_by_filter(self) -> NoReturn:

        cols = self.vehicle_data.cols[1:]
        for col in cols:
            if hasattr(self.ui, col + '_v'):
                checkbox_v = self.ui.__getattribute__(col + '_v').currentText()
                if checkbox_v:
                    self.veh_filter[col] = checkbox_v

        self.set_veh_table()
        self.veh_filter.clear()

    # Получить данные из формы добавления авто
    def get_veh_form_v(self, form: Database.ItemData, valid: bool) -> NoReturn:

        if valid:
            self.vehicle_data.add_veh(form)
            file = self.veh_form.file_name
            if file:
                shutil.copy2(file, f"app/data/img/{self.vehicle_data.db.get_last_added_id()}.{file.split('.')[-1]}")
            self.set_veh_table()
            self.fill_combobox()
