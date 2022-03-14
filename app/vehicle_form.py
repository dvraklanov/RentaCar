import logging

from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QFormLayout, QDialogButtonBox, QDialog
from .ui.ui_vehicle_form import Ui_veh_form


# Форма добавления нового авто
class VehicleForm(QWidget):
    form_filled = QtCore.Signal(dict, bool)

    # Диалог при добавлении нового авто
    class AddVehDialog(QDialog):
        def __init__(self):
            super().__init__()

        # Показать диалоговое окно
        def show_(self, is_err=False) -> int:

            message = "Проверьте правильность введенных данных и "
            if is_err:
                win_title = "Ошибка"
                message += "попробуйте еще раз."
                button_box = QDialogButtonBox(QDialogButtonBox.Cancel)
                button_box.rejected.connect(self.reject)
            else:
                win_title = "Проверьте данные"
                message += "подвердите действие"
                button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
                button_box.accepted.connect(self.accept)
                button_box.rejected.connect(self.reject)
            self.setWindowTitle(win_title)
            layout = QVBoxLayout()
            layout.addWidget(QLabel(message))
            layout.addWidget(button_box)
            self.setLayout(layout)
            return self.exec_()

    def __init__(self, vehicle_db):
        super(VehicleForm, self).__init__()
        self.ui = Ui_veh_form()
        self.ui.setupUi(self)

        self.vehicle_db = vehicle_db
        self.form_values = dict()
        self.form_valid = False

        self.ui.add_btn.clicked.connect(self.get_form_fields)
        self.valid_func = {"n_seat": lambda x: x.isdigit(),
                           "power_hp": lambda x: x.isdigit()}
        # Добавить класс валидатора и регулярные выражения для остальных полей

    # Получить значения полей формы
    def get_form_fields(self) -> None:

        cols = self.vehicle_db.cols[1:]
        err = False
        for col in cols:
            if hasattr(self.ui, col + '_v'):
                txt = self.ui.__getattribute__(col + '_v').text()
                if txt and self.valid_func.get(col, lambda x: True)(txt):
                    self.form_values[col] = txt
                    # Валидация говна, поправить!!!
                else:
                    err = True
                    break
        dlg = self.AddVehDialog()
        if dlg.show_(is_err=err):
            logging.debug(f"Add new data in db.\n{self.form_values}")
            self.form_valid = True
            self.close()
        else:
            logging.debug(f"Retry input data.\n{self.form_values}")

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.form_filled.emit(self.form_values, self.form_valid)
        cols = self.vehicle_db.cols[1:]
        for col in cols:
            if hasattr(self.ui, col + '_v'):
                self.ui.__getattribute__(col + '_v').clear()
        self.form_valid = False
        event.accept()

