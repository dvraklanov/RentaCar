import logging
import datetime as dt

from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QMessageBox
from app.ui.ui_rent_form import Ui_rent_form

# Форма добавления нового авто
from app.vehicles import Vehicles
from app.customers import Customers


class RentForm(QWidget):
    RentFormFilled = QtCore.Signal(bool)

    def __init__(self, vehicle_db: Vehicles, customer_db: Customers):
        super(RentForm, self).__init__()
        self.ui = Ui_rent_form()
        self.ui.setupUi(self)

        """Объекты для работы с данными"""
        self.vehicle_db = vehicle_db  # Бд для авто
        self.customer_db = customer_db  # Бд для клиентов
        self.veh_id = None  # ID выбранного авто
        self.form_is_valid = False  # Заполнена ли форма
        self.cur_cust_id = None  # ID выбранного клиента
        self.form_values = dict()  # Значения полей формы
        self.datetime_format = "%d.%m.%Y"  # Формат отображения даты

        """Начальные значения полей"""
        self.ui.start_date_v.setDate(dt.datetime.now())
        self.ui.end_date_v.setDate(dt.datetime.now() + dt.timedelta(days=1))

        """Установление функционала элементов формы"""
        self.ui.new_cust_v.toggled.connect(self.new_cust_enable)  # Выбор: новый клиент или из бд
        self.ui.cust_table.cellClicked.connect(self.choice_cust)  # Выбор клиента в таблице
        self.ui.add_rent_btn.clicked.connect(self.check_rent_form)  # Проверка формы

        """Запрет на редактирование таблицы и выбора несколько строк"""
        self.ui.cust_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.cust_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.ui.cust_table.setSelectionBehavior(QAbstractItemView.SelectRows)

    # Заполнение таблицы клиентов
    def set_cust_table(self):
        all_cust = self.customer_db.get_all_cust()
        self.ui.cust_table.setRowCount(0)
        self.ui.cust_table.setRowCount(len(all_cust))

        for i, cust in enumerate(all_cust):

            self.ui.cust_table.setItem(i, 0, QTableWidgetItem(str(cust['id'])))
            self.ui.cust_table.setItem(i, 1, QTableWidgetItem(str(" ".join([cust['name'],
                                                                           cust['lastname'],
                                                                           cust['surname']]))))

    # Включение или отключение добавление нового клиента
    def new_cust_enable(self):
        is_new_cust = False
        if self.ui.new_cust_v.isChecked():
            is_new_cust = True

        # Очистка формы
        self.ui.name_v.clear()
        self.ui.lastname_v.clear()
        self.ui.surname_v.clear()
        self.ui.pass_id_v.clear()

        # Переключение режима (активно или нет)
        self.ui.name_v.setEnabled(is_new_cust)
        self.ui.lastname_v.setEnabled(is_new_cust)
        self.ui.surname_v.setEnabled(is_new_cust)
        self.ui.pass_id_v.setEnabled(is_new_cust)
        self.ui.cust_table.setEnabled(not is_new_cust)

    # Выбор клиента из таблицы
    def choice_cust(self):

        self.cur_cust_id = self.ui.cust_table.item(self.ui.cust_table.currentItem().row(), 0).text()
        cur_data = self.customer_db.get_cust(cust_id=self.cur_cust_id)

        self.ui.name_v.setText(cur_data.get('name', ''))
        self.ui.lastname_v.setText(cur_data.get('lastname', ''))
        self.ui.surname_v.setText(cur_data.get('surname', ''))
        self.ui.pass_id_v.setText(str(cur_data.get('pass_id', '')))

    # Проверка формы договора
    def check_rent_form(self):
        valid_flag = True

        # Все поля должны быть заполнены
        msg = "Проверьте правильность введенных данных:\n"
        for field_name in self.customer_db.fields_labels:
            if not self.ui.__getattribute__(field_name + '_v').text():
                valid_flag = False
                msg += "\nВсе поля должны быть заполнены."
                break

        # Оконачение не должно быть раньше начала аренды
        end_dt = dt.datetime.strptime(self.ui.end_date_v.text(), self.datetime_format)
        start_dt = dt.datetime.strptime(self.ui.start_date_v.text(), self.datetime_format)
        if start_dt > end_dt:
            valid_flag = False
            msg += "\nДата начала аренды не может быть больше даты окончания."

        if valid_flag:
            self.add_rent()
        else:
            is_check = QMessageBox.warning(self, "Некоректный ввод", msg)

    # Добавить договор аренды
    def add_rent(self):

        veh_data = self.vehicle_db.get_spec(veh_id=self.veh_id)
        start_dt = dt.datetime.strptime(self.ui.start_date_v.text(), self.datetime_format)
        start_dt_f = start_dt.strftime(self.datetime_format)
        end_dt = dt.datetime.strptime(self.ui.end_date_v.text(), self.datetime_format)
        end_dt_f = end_dt.strftime(self.datetime_format)
        dt_range = (end_dt - start_dt).days

        rent_data = \
            f"Подвердите правильность данных договора:\n" \
            f"ФИО: {self.ui.name_v.text()} {self.ui.lastname_v.text()} {self.ui.surname_v.text()}\n" \
            f"Номер паспорта: {self.ui.pass_id_v.text()}\n" \
            f"Период аренды: {start_dt_f} -> {end_dt_f} ({dt_range} дн.)\n" \
            f"Автомобиль: {veh_data.get('name', '')} {veh_data.get('number_plate', '')}\n" \
            f"К оплате: {dt_range * veh_data['rental_price']} руб."
        is_add = QMessageBox.question(self, "Новый договор аренды", rent_data)

        if is_add == QMessageBox.Yes:
            self.vehicle_db.edit_spec(veh_id=self.veh_id, new_values={"start_date": start_dt_f,
                                                                      "end_date": end_dt_f,
                                                                      "cust_id": self.cur_cust_id,
                                                                      "status": 2})
            logging.debug(f"New rent: {self.cur_cust_id} -> {veh_data['id']}")
            self.form_is_valid = True
            self.close()

    # Перегрузка метода, вызывающемся при закрытии формы
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.RentFormFilled.emit(self.form_is_valid)
        self.form_is_valid = False
        event.accept()
