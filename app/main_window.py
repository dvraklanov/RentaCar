import os
from datetime import datetime
import logging
import shutil

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView, QMessageBox, QHeaderView
from .ui.ui_main_window import Ui_MainWindow

from .database import Database
from .vehicles import Vehicles
from .customers import Customers
from .forms.vehicle_form import VehicleForm
from .forms.rent_form import RentForm


# Главное окно приложения расширяет класс QWidget
class MainWindow(QMainWindow):

    # Конструктор
    def __init__(self):
        # Инициализация родительского класса
        super(MainWindow, self).__init__()

        """Установка интерфейса"""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        """Объекты для работы с данными"""

        self.db = Database("app/data/RentaCar")  # Объкет базы данных
        self.vehicle_data = Vehicles(self.db)  # Класс для работы с авто
        self.customers_data = Customers(self.db)  # Класс для работы с клиентами
        self.veh_filter = dict()  # Фильтр для поиска авто в базе
        self.cur_item = None  # Текущий выбранная запись авто

        # Функции-валидаторы для полей формы добавления авто
        self.veh_form_valid = {
            "number_plate": {"func": lambda x: x not in self.vehicle_data.get_uniq_spec("number_plate"),
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

        # Форма добавления авто
        self.veh_form = VehicleForm(vehicle_db=self.vehicle_data, valid_params=self.veh_form_valid)
        # Форма оформления аренды
        self.rent_form = RentForm(vehicle_db=self.vehicle_data, customer_db=self.customers_data)

        """Установка доп. параметров интерфейса"""

        # Запрет на редактирование данных в таблицах
        self.ui.veh_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.spec_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Запрет на редактирование размеров колонок таблиц
        self.ui.veh_table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.spec_table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        # Выбор всей строки при нажатии
        self.ui.veh_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.spec_table.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Установка ширины отдельных колонок таблиц автомобилей и характеристик
        self.ui.veh_table.setColumnWidth(0, 45)
        self.ui.veh_table.setColumnWidth(1, 150)

        self.ui.spec_table.setColumnWidth(0, 200)

        """Установка функционала элементов интерфейса"""
        self.ui.veh_table.cellClicked.connect(self.set_spec_table)  # Отображения информации о выбранном авто
        self.ui.find_btn.clicked.connect(self.find_by_filter)  # Поиск авто в бд по текущему фильтру
        self.ui.add_veh_btn.clicked.connect(self.veh_form.show)  # Отображение формы добавления авто
        self.ui.new_rent_btn.clicked.connect(self.rent_form_show)  # Отображение формы оформления аренды
        self.ui.delete_btn.clicked.connect(self.del_veh)  # Удаления выбранного авто из бд
        self.ui.close_rent_btn.clicked.connect(self.close_rent)  # Закрытие аренды выбранного авто
        self.veh_form.VehicleFormFilled.connect(self.get_veh_form_v)  # Получение данных из формы добавления авто
        self.rent_form.RentFormFilled.connect(self.rent_form_close)  # Действия после закрытия формы аренды

        """Действия при запуске программы"""
        self.reset_ui()

    # Заполнение таблицы траснпорта
    def set_veh_table(self):

        all_veh = self.vehicle_data.get_all_veh(filter=self.veh_filter)
        self.ui.veh_table.setRowCount(0)
        self.ui.veh_table.setRowCount(len(all_veh))

        for i, vehicle in enumerate(all_veh):
            self.ui.veh_table.setItem(i, 0, QTableWidgetItem(str(vehicle['id'])))
            self.ui.veh_table.setItem(i, 1, QTableWidgetItem(str(vehicle['name'])))
            self.ui.veh_table.setItem(i, 2, QTableWidgetItem(str(self.vehicle_data.status_list[vehicle['status']])))

    # Заполнение таблицы с информацией об авто
    def set_spec_table(self):

        self.ui.spec_table.setRowCount(0)
        # Получчение данных из бд
        self.cur_item = self.ui.veh_table.currentItem()
        veh_id = self.ui.veh_table.item(self.cur_item.row(), 0).text()
        veh_data = self.vehicle_data.get_spec(veh_id=veh_id)
        cols = self.vehicle_data.cols[1:]
        self.ui.spec_table.setRowCount(len(cols))

        # Если существует картинка, то загрузить ее
        self.ui.img_box.clear()
        img_path = f"app/data/img/{veh_id}.jpg"
        if os.path.exists(img_path) and os.path.isfile(img_path):
            veh_img = QPixmap(img_path)
            veh_img = veh_img.scaledToHeight(self.ui.img_box.height())
            self.ui.img_box.setPixmap(veh_img)
        else:
            logging.debug(f"Can't find img file for veh ({veh_id=})")

        # Заполнение таблицы информации
        for i, col in enumerate(cols):
            self.ui.spec_table.setItem(i, 0, QTableWidgetItem(self.vehicle_data.spec_dict.get(col, col)))
            item = str(veh_data.get(col, i))
            self.ui.spec_table.setItem(i, 1, QTableWidgetItem(item if col != 'status' else
                                                              self.vehicle_data.status_list[int(item)]))

        # Проверка аренды авто
        date_val = veh_data.get("end_date")
        rent_flag = False
        rent_end_flag = False
        msg = ""
        if date_val:
            rent_date = datetime.strptime(date_val, self.rent_form.datetime_format)
            rent_flag = True
            if rent_date < datetime.now():
                rent_end_flag = True
                msg = "Внимание! У данного автомобиля закончилась аренда!"

        # Активация кнопок меню
        self.ui.close_rent_btn.setEnabled(rent_end_flag)
        self.ui.msg_box.setText(msg)
        self.ui.delete_btn.setEnabled(not rent_flag)
        self.ui.new_rent_btn.setEnabled(not rent_flag)

    # Заполнить опции фильтра
    def fill_filter_combobox(self):

        cols = self.vehicle_data.cols[1:]
        for col in cols:
            if hasattr(self.ui, col + '_v'):
                checkbox = self.ui.__getattribute__(col + '_v')
                checkbox.clear()
                checkbox.addItem("")
                for item in self.vehicle_data.get_uniq_spec(col):
                    checkbox.addItem(str(item))

    # Поиск по фильтру
    def find_by_filter(self):

        cols = self.vehicle_data.cols[1:]
        for col in cols:
            if hasattr(self.ui, col + '_v'):
                checkbox_v = self.ui.__getattribute__(col + '_v').currentText()
                if checkbox_v:
                    self.veh_filter[col] = checkbox_v

        self.set_veh_table()
        self.veh_filter.clear()

    # Получить данные из формы добавления авто
    def get_veh_form_v(self, form: Database.ItemData, valid: bool):

        if valid:
            self.vehicle_data.add_veh(form)
            # Если в форме указан файл, скопировать картинку
            file = self.veh_form.file_name
            if file:
                shutil.copy2(file, f"app/data/img/{self.vehicle_data.db.get_last_added_id()}.{file.split('.')[-1]}")

            self.reset_ui()

    # Сборосить интерфейс (обновить таблицу авто, фильтр, сбросить окно данных об авто)
    def reset_ui(self):

        # Сброс окна выбора ав т
        self.set_veh_table()
        self.fill_filter_combobox()

        # Сброс окна информации об авто
        self.ui.spec_table.setRowCount(0)
        self.ui.img_box.clear()
        self.ui.msg_box.clear()

        # Сброс кнопок
        self.ui.delete_btn.setEnabled(False)
        self.ui.new_rent_btn.setEnabled(False)
        self.ui.close_rent_btn.setEnabled(False)

    # Удалить автомобиль из бд
    def del_veh(self):

        if self.cur_item:
            veh_id = self.ui.veh_table.item(self.cur_item.row(), 0).text()
            is_del = QMessageBox.question(self, "Удаление авто",
                                          "Вы действительно хотите удалить автомобиль из базы данных?")

            if is_del == QMessageBox.Yes:
                self.vehicle_data.del_veh(veh_id=veh_id)
                self.reset_ui()

    # Закрыть аренду авто
    def close_rent(self):
        if self.cur_item:
            veh_id = self.ui.veh_table.item(self.cur_item.row(), 0).text()
            is_close = QMessageBox.question(self, "Закрыть аренду",
                                            "Вы действительно хотите закрыть аренду?")
            if is_close == QMessageBox.Yes:
                self.vehicle_data.edit_spec(veh_id=veh_id, new_values={"start_date": "",
                                                                       "end_date": "",
                                                                       "cust_id": "",
                                                                       "status": 1})
                logging.debug(f"Close rent ({veh_id=})")
                self.reset_ui()

    # Показать форму аренды
    def rent_form_show(self):
        if self.cur_item:
            self.rent_form.veh_id = self.ui.veh_table.item(self.ui.veh_table.currentItem().row(), 0).text()
            self.rent_form.show()
            self.rent_form.set_cust_table()

    # Сброс после закрытия формы аренды
    def rent_form_close(self, is_valid: bool):
        if is_valid:
            self.reset_ui()
