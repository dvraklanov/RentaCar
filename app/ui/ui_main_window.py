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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.veh_table = QTableWidget(self.centralwidget)
        if (self.veh_table.columnCount() < 2):
            self.veh_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.veh_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.veh_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.veh_table.rowCount() < 1):
            self.veh_table.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.veh_table.setVerticalHeaderItem(0, __qtablewidgetitem2)
        self.veh_table.setObjectName(u"veh_table")
        self.veh_table.setGeometry(QRect(280, 60, 551, 551))
        self.veh_table.horizontalHeader().setDefaultSectionSize(250)
        self.veh_table.horizontalHeader().setStretchLastSection(True)
        self.veh_table.verticalHeader().setVisible(False)
        self.veh_table.verticalHeader().setProperty("showSortIndicator", False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.veh_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None));
        ___qtablewidgetitem1 = self.veh_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem2 = self.veh_table.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"123", None));
    # retranslateUi

