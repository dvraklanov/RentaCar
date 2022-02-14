# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.veh_table = QTableWidget(self.centralwidget)
        if (self.veh_table.columnCount() < 3):
            self.veh_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.veh_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.veh_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.veh_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.veh_table.setObjectName(u"veh_table")
        self.veh_table.setGeometry(QRect(280, 60, 555, 601))
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
        self.spec_table = QTableWidget(self.centralwidget)
        if (self.spec_table.columnCount() < 2):
            self.spec_table.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.spec_table.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.spec_table.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        self.spec_table.setObjectName(u"spec_table")
        self.spec_table.setGeometry(QRect(860, 260, 400, 291))
        self.spec_table.horizontalHeader().setVisible(False)
        self.spec_table.horizontalHeader().setDefaultSectionSize(199)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 30, 551, 21))
        self.label.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(866, 30, 401, 21))
        self.label_2.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignCenter)
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
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.veh_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None));
        ___qtablewidgetitem2 = self.veh_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem3 = self.spec_table.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem4 = self.spec_table.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"value", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043f\u0430\u0440\u043a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
    # retranslateUi

