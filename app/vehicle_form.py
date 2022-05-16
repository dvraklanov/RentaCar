import logging
from typing import NoReturn, List, Dict, Callable, Union

from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QFormLayout, QDialogButtonBox, QDialog, \
    QFileDialog, QComboBox
from .ui.ui_vehicle_form import Ui_veh_form

# Форма добавления нового авто
from .vehicles import Vehicles


class VehicleForm(QWidget):
    FormFilled = QtCore.Signal(dict, bool)

    # Диалог при добавлении нового авто
    class AddDialog(QDialog):
        def __init__(self):
            super().__init__()

        # Показать диалоговое окно
        def show_(self, err_msg: str, is_err=False) -> int:

            message = "Проверьте правильность введенных данных и "
            if is_err:
                win_title = "Ошибка!"
                message += "попробуйте еще раз."
                if err_msg:
                    message = err_msg + "\n" + message
                button_box = QDialogButtonBox(QDialogButtonBox.Cancel)
                button_box.rejected.connect(self.reject)
            else:
                win_title = "Проверьте данные!"
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

    def __init__(self, vehicle_db: Vehicles, valid_params=None):
        super(VehicleForm, self).__init__()
        if valid_params is None:
            valid_params = {}
        self.valid_params = valid_params
        self.ui = Ui_veh_form()
        self.ui.setupUi(self)

        self.vehicle_db = vehicle_db

        self.form_values = dict()
        self.form_is_valid = False

        self.file_name = ""

        self.ui.add_btn.clicked.connect(self.get_form_fields)
        self.ui.find_img_btn.clicked.connect(self.show_file_dialog)
        # Добавить класс валидатора и регулярные выражения для остальных полей

    # Получить значения полей формы
    def get_form_fields(self) -> NoReturn:

        cols = self.vehicle_db.cols[1:]
        err = False
        err_msg = ""
        for col in cols:
            if hasattr(self.ui, col + '_v'):
                field = self.ui.__getattribute__(col + '_v')
                if type(field) == QComboBox:
                    txt = field.currentText()
                else:
                    txt = field.text()
                    validator = self.valid_params[col]['func'] if col in self.valid_params else lambda x: True
                    if txt:
                        if not validator(txt):
                            err = True
                            err_msg = self.valid_params[col].get('msg', 'Ошибка!')
                            break
                    else:
                        err = True
                        err_msg = "Все поля должны быть заполнены!"
                        break
                self.form_values[col] = txt

        dlg = self.AddDialog()

        if dlg.show_(err_msg=err_msg, is_err=err):
            logging.debug(f"Add new data in db.\n{self.form_values}")
            self.form_is_valid = True
            self.close()
        else:
            logging.debug(f"Retry input data.\n{self.form_values}")

    def show_file_dialog(self):

        self.file_name, _ = QFileDialog.getOpenFileName(self, 'Open file',
                                                        None, 'Image (*.jpg)')

        self.ui.find_img_btn.setText(self.file_name.split("/")[-1])

    # Перегрузка метода, вызывающемся при закрытии формы
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:

        self.FormFilled.emit(self.form_values, self.form_is_valid)
        cols = self.vehicle_db.cols[1:]

        for col in cols:
            if hasattr(self.ui, col + '_v'):
                self.ui.__getattribute__(col + '_v').clear()

        self.form_is_valid = False
        event.accept()
