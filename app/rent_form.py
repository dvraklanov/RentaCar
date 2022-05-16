import logging

from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from .ui.ui_rent_form import Ui_rent_form

# Форма добавления нового авто
from .vehicles import Vehicles
from .customers import Customers


class RentForm(QWidget):
    RentFormFilled = QtCore.Signal(dict, bool)

    def __init__(self, vehicle_db: Vehicles, customer_db: Customers):
        super(RentForm, self).__init__()
        self.ui = Ui_rent_form()
        self.ui.setupUi(self)
        self.form_values = dict()

        self.vehicle_db = vehicle_db
        self.customer_db = customer_db
        self.veh_id = None
        self.form_is_valid = False

        self.ui.new_cust_v.toggled.connect(self.new_cust_enable)

    def set_cust_table(self):
        all_cust = self.customer_db.get_all_cust()
        self.ui.cust_table.setRowCount(0)
        self.ui.cust_table.setRowCount(len(all_cust))

        for i, cust in enumerate(all_cust):
            self.ui.cust_table.setItem(i, 0, QTableWidgetItem(str(cust['id'])))
            self.ui.cust_table.setItem(i, 1, QTableWidgetItem(str("".join([cust['name'],
                                                                           cust['lastname'],
                                                                           cust['surname']]))))

    # Включение или отключение добавление нового клиента
    def new_cust_enable(self):
        flag = False
        if self.ui.new_cust_v.isChecked():
            flag = True
        self.ui.name_v.setEnabled(flag)
        self.ui.lastname_v.setEnabled(flag)
        self.ui.surname_v.setEnabled(flag)
        self.ui.pass_v.setEnabled(flag)
        self.ui.cust_table.setEnabled(not flag)

    # Перегрузка метода, вызывающемся при закрытии формы
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.RentFormFilled.emit(self.form_values, self.form_is_valid)
        self.form_is_valid = False
        event.accept()
