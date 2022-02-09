from PySide6.QtWidgets import QMainWindow

from .ui.ui_main_window import Ui_MainWindow


# главное окно приложения расширяет класс QWidget
class MainWindow(QMainWindow):

    # конструктор
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

