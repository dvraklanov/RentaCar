import sys

from PySide6.QtWidgets import QApplication
from app.main_window import MainWindow


if __name__ == "__main__":
    # главный класс приложения принимает строку - заголовок окна
    app = QApplication(['Пример прииложения на PyQT'])

    # создаем главный виджет размером 800x600 и отображаем его
    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
