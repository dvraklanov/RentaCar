from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit
from .ui.ui_vehicle_form import Ui_veh_form


class VehicleForm(QWidget):

    def __init__(self):
        super(VehicleForm, self).__init__()
        self.ui = Ui_veh_form()
        self.ui.setupUi(self)
        self.form_values = dict()
        self.ui.add_btn.clicked.connect(self.get_form_fields)

    def add_form_fields(self, spec):
        for label in spec.values():
            self.ui.formLayout.addRow(QLabel(label), QLineEdit(""))

    def get_form_fields(self):
        print("field")
        print(self.ui.formLayout.rowCount())

        for i in range(1, self.ui.formLayout.rowCount()):
            print(self.ui.formLayout.layout())
