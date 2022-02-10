import logging

from PySide6.QtWidgets import QMainWindow, QTableWidgetItem

from .ui.ui_main_window import Ui_MainWindow
from .vehicles import Vehicles
from .database import Database

# главное окно приложения расширяет класс QWidget
class MainWindow(QMainWindow):

    # конструктор
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Database("app/data/test_db")
        self.vehicle_data = Vehicles(self.db)
        self.set_veh_table()

    def set_veh_table(self):

        all_veh = self.vehicle_data.get_all_veh()
        logging.info(all_veh)

        for i, vehicle in enumerate(all_veh):

            self.ui.veh_table.insertRow(i)
            self.ui.veh_table.setItem(i, 0, QTableWidgetItem(str(vehicle[1])))
            self.ui.veh_table.setItem(i, 1, QTableWidgetItem(str(self.vehicle_data.status_list[vehicle[2]])))



