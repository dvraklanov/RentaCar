import logging
from typing import NoReturn, List, Dict, Callable, Union

from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import QWidget, QFileDialog, QComboBox, QMessageBox
from app.ui.ui_vehicle_form import Ui_veh_form

# Форма добавления нового авто
from app.vehicles import Vehicles


class VehicleForm(QWidget):
    VehicleFormFilled = QtCore.Signal(dict, bool)

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
    def get_form_fields(self):

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

        resp = self.show_msg(err_msg=err_msg, is_err=err)
        if resp == QMessageBox.Save:
            logging.debug(f"Add new data in db.\n{self.form_values}")
            self.form_is_valid = True
            self.close()
        else:
            logging.debug(f"Retry input data.\n{self.form_values}")

    # Показать диалог выбора фото авто
    def show_file_dialog(self):

        self.file_name, _ = QFileDialog.getOpenFileName(self, 'Open file',
                                                        None, 'Image (*.jpg)')

        self.ui.find_img_btn.setText(self.file_name.split("/")[-1])

    # Показать сообщение о заполнении формы
    def show_msg(self, is_err=False, err_msg=None) -> int:

        if err_msg is None:
            err_msg = ""

        msg_box = QMessageBox(self)
        message = "Проверьте правильность введенных данных и "
        if is_err:
            win_title = "Ошибка!"
            message += "попробуйте еще раз."
            if err_msg:
                message = err_msg + "\n" + message

            msg_box.setStandardButtons(QMessageBox.Cancel)
        else:
            win_title = "Проверьте данные!"
            message += "подвердите действие."
            msg_box.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)
        msg_box.setWindowTitle(win_title)
        msg_box.setText(message)
        return msg_box.exec_()

    # Перегрузка метода, вызывающемся при закрытии формы
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:

        self.VehicleFormFilled.emit(self.form_values, self.form_is_valid)
        cols = self.vehicle_db.cols[1:]

        for col in cols:
            if hasattr(self.ui, col + '_v'):
                self.ui.__getattribute__(col + '_v').clear()

        self.form_is_valid = False
        event.accept()
