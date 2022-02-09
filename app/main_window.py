import sys
import random
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


# главное окно приложения расширяет класс QWidget
class MainWindow(QWidget):

    # список предложений
    strings = ["Раз два три", "Четыре пять  шесть", "Семь восемь девять", "Просто тест", "Как так это"]

    # конструктор
    def __init__(self):
        super().__init__()

        # создаем кнопку
        self.button = QPushButton("Нажмите на меня!")
        # создаем текстовую метку отцентиророванную посередине контейнера
        self.text = QLabel("Привет, меня зовут PyQt.", alignment=Qt.AlignCenter)

        # вертикальная разметка
        self.layout = QVBoxLayout(self)
        # добавляем виджеты в разметку
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        # назначаем обработчки для копки на событие клика
        self.button.clicked.connect(self.randomSentence)

    # сам обработчик
    @Slot()
    def randomSentence(self):
        self.text.setText(random.choice(self.strings))