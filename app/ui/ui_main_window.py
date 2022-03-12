# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(280, 20, 561, 641))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.veh_table = QTableWidget(self.verticalLayoutWidget_2)
        if (self.veh_table.columnCount() < 3):
            self.veh_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.veh_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.veh_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.veh_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.veh_table.setObjectName(u"veh_table")
        self.veh_table.setTabletTracking(False)
        self.veh_table.setContextMenuPolicy(Qt.NoContextMenu)
        self.veh_table.setAutoScroll(True)
        self.veh_table.setDragEnabled(False)
        self.veh_table.setShowGrid(True)
        self.veh_table.setWordWrap(False)
        self.veh_table.horizontalHeader().setDefaultSectionSize(149)
        self.veh_table.horizontalHeader().setHighlightSections(False)
        self.veh_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.veh_table.horizontalHeader().setStretchLastSection(True)
        self.veh_table.verticalHeader().setVisible(False)
        self.veh_table.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_2.addWidget(self.veh_table)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(870, 20, 391, 641))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.widget = QWidget(self.verticalLayoutWidget_3)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_3.addWidget(self.widget)

        self.spec_table = QTableWidget(self.verticalLayoutWidget_3)
        if (self.spec_table.columnCount() < 2):
            self.spec_table.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.spec_table.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.spec_table.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        self.spec_table.setObjectName(u"spec_table")
        self.spec_table.horizontalHeader().setVisible(False)
        self.spec_table.horizontalHeader().setDefaultSectionSize(190)
        self.spec_table.horizontalHeader().setStretchLastSection(True)
        self.spec_table.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.spec_table)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 15)
        self.verticalLayout_3.setStretch(2, 30)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 50, 249, 25))
        self.label_10.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 80, 251, 241))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.wheel_drive_l = QLabel(self.verticalLayoutWidget)
        self.wheel_drive_l.setObjectName(u"wheel_drive_l")
        self.wheel_drive_l.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.wheel_drive_l, 1, 0, 1, 1)

        self.gearbox_type_l = QLabel(self.verticalLayoutWidget)
        self.gearbox_type_l.setObjectName(u"gearbox_type_l")
        self.gearbox_type_l.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.gearbox_type_l, 4, 0, 1, 1)

        self.n_seat_l = QLabel(self.verticalLayoutWidget)
        self.n_seat_l.setObjectName(u"n_seat_l")
        self.n_seat_l.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.n_seat_l, 3, 0, 1, 1)

        self.gearbox_type_v = QComboBox(self.verticalLayoutWidget)
        self.gearbox_type_v.addItem("")
        self.gearbox_type_v.setObjectName(u"gearbox_type_v")

        self.gridLayout.addWidget(self.gearbox_type_v, 4, 1, 1, 1)

        self.body_type_v = QComboBox(self.verticalLayoutWidget)
        self.body_type_v.addItem("")
        self.body_type_v.setObjectName(u"body_type_v")

        self.gridLayout.addWidget(self.body_type_v, 0, 1, 1, 1)

        self.n_seat_v = QComboBox(self.verticalLayoutWidget)
        self.n_seat_v.addItem("")
        self.n_seat_v.setObjectName(u"n_seat_v")

        self.gridLayout.addWidget(self.n_seat_v, 3, 1, 1, 1)

        self.body_type_l = QLabel(self.verticalLayoutWidget)
        self.body_type_l.setObjectName(u"body_type_l")
        self.body_type_l.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.body_type_l, 0, 0, 1, 1)

        self.fuel_type_v = QComboBox(self.verticalLayoutWidget)
        self.fuel_type_v.addItem("")
        self.fuel_type_v.setObjectName(u"fuel_type_v")

        self.gridLayout.addWidget(self.fuel_type_v, 2, 1, 1, 1)

        self.fuel_type_l = QLabel(self.verticalLayoutWidget)
        self.fuel_type_l.setObjectName(u"fuel_type_l")
        self.fuel_type_l.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.fuel_type_l, 2, 0, 1, 1)

        self.wheel_drive_v = QComboBox(self.verticalLayoutWidget)
        self.wheel_drive_v.addItem("")
        self.wheel_drive_v.setObjectName(u"wheel_drive_v")

        self.gridLayout.addWidget(self.wheel_drive_v, 1, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)

        self.verticalLayout.addLayout(self.gridLayout)

        self.find_btn = QPushButton(self.verticalLayoutWidget)
        self.find_btn.setObjectName(u"find_btn")

        self.verticalLayout.addWidget(self.find_btn)

        self.add_veh_btn = QPushButton(self.centralwidget)
        self.add_veh_btn.setObjectName(u"add_veh_btn")
        self.add_veh_btn.setGeometry(QRect(20, 630, 251, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043f\u0430\u0440\u043a", None))
        ___qtablewidgetitem = self.veh_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.veh_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None));
        ___qtablewidgetitem2 = self.veh_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        ___qtablewidgetitem3 = self.spec_table.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem4 = self.spec_table.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"value", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.wheel_drive_l.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043f\u0440\u0438\u0432\u043e\u0434\u0430", None))
        self.gearbox_type_l.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041f\u041f", None))
        self.n_seat_l.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u043c\u0435\u0441\u0442", None))
        self.gearbox_type_v.setItemText(0, "")

        self.body_type_v.setItemText(0, "")

        self.n_seat_v.setItemText(0, "")

        self.body_type_l.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043a\u0443\u0437\u043e\u0432\u0430", None))
        self.fuel_type_v.setItemText(0, "")

        self.fuel_type_l.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0442\u043e\u043f\u043b\u0438\u0432\u0430", None))
        self.wheel_drive_v.setItemText(0, "")

        self.find_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.add_veh_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0430\u0432\u0442\u043e\u043f\u0430\u0440\u043a", None))
    # retranslateUi

