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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 70, 1221, 621))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_10 = QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gearbox_type_l = QLabel(self.horizontalLayoutWidget)
        self.gearbox_type_l.setObjectName(u"gearbox_type_l")
        self.gearbox_type_l.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.gearbox_type_l, 7, 0, 1, 1)

        self.wheel_drive_l = QLabel(self.horizontalLayoutWidget)
        self.wheel_drive_l.setObjectName(u"wheel_drive_l")
        self.wheel_drive_l.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.wheel_drive_l, 4, 0, 1, 1)

        self.gearbox_type_v = QComboBox(self.horizontalLayoutWidget)
        self.gearbox_type_v.addItem("")
        self.gearbox_type_v.setObjectName(u"gearbox_type_v")

        self.gridLayout.addWidget(self.gearbox_type_v, 7, 1, 1, 1)

        self.body_type_l = QLabel(self.horizontalLayoutWidget)
        self.body_type_l.setObjectName(u"body_type_l")
        self.body_type_l.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.body_type_l, 3, 0, 1, 1)

        self.n_seat_l = QLabel(self.horizontalLayoutWidget)
        self.n_seat_l.setObjectName(u"n_seat_l")
        self.n_seat_l.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.n_seat_l, 6, 0, 1, 1)

        self.n_seat_v = QComboBox(self.horizontalLayoutWidget)
        self.n_seat_v.addItem("")
        self.n_seat_v.setObjectName(u"n_seat_v")

        self.gridLayout.addWidget(self.n_seat_v, 6, 1, 1, 1)

        self.body_type_v = QComboBox(self.horizontalLayoutWidget)
        self.body_type_v.addItem("")
        self.body_type_v.setObjectName(u"body_type_v")

        self.gridLayout.addWidget(self.body_type_v, 3, 1, 1, 1)

        self.fuel_type_v = QComboBox(self.horizontalLayoutWidget)
        self.fuel_type_v.addItem("")
        self.fuel_type_v.setObjectName(u"fuel_type_v")

        self.gridLayout.addWidget(self.fuel_type_v, 5, 1, 1, 1)

        self.wheel_drive_v = QComboBox(self.horizontalLayoutWidget)
        self.wheel_drive_v.addItem("")
        self.wheel_drive_v.setObjectName(u"wheel_drive_v")

        self.gridLayout.addWidget(self.wheel_drive_v, 4, 1, 1, 1)

        self.fuel_type_l = QLabel(self.horizontalLayoutWidget)
        self.fuel_type_l.setObjectName(u"fuel_type_l")
        self.fuel_type_l.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.fuel_type_l, 5, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 4)

        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.veh_table = QTableWidget(self.horizontalLayoutWidget)
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

        self.gridLayout_2.addWidget(self.veh_table, 4, 0, 1, 1)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.add_veh_btn = QPushButton(self.horizontalLayoutWidget)
        self.add_veh_btn.setObjectName(u"add_veh_btn")

        self.gridLayout_2.addWidget(self.add_veh_btn, 5, 0, 1, 1)

        self.find_btn = QPushButton(self.horizontalLayoutWidget)
        self.find_btn.setObjectName(u"find_btn")

        self.gridLayout_2.addWidget(self.find_btn, 2, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_11 = QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.img_box = QLabel(self.horizontalLayoutWidget)
        self.img_box.setObjectName(u"img_box")

        self.horizontalLayout_2.addWidget(self.img_box)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.spec_table = QTableWidget(self.horizontalLayoutWidget)
        if (self.spec_table.columnCount() < 2):
            self.spec_table.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.spec_table.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.spec_table.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        if (self.spec_table.rowCount() < 1):
            self.spec_table.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.spec_table.setVerticalHeaderItem(0, __qtablewidgetitem5)
        self.spec_table.setObjectName(u"spec_table")
        self.spec_table.horizontalHeader().setVisible(False)
        self.spec_table.horizontalHeader().setDefaultSectionSize(200)
        self.spec_table.horizontalHeader().setStretchLastSection(True)
        self.spec_table.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.spec_table)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.msg_box = QLabel(self.horizontalLayoutWidget)
        self.msg_box.setObjectName(u"msg_box")

        self.horizontalLayout_3.addWidget(self.msg_box)

        self.delete_btn = QPushButton(self.horizontalLayoutWidget)
        self.delete_btn.setObjectName(u"delete_btn")

        self.horizontalLayout_3.addWidget(self.delete_btn)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 6)
        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.gearbox_type_l.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041f\u041f", None))
        self.wheel_drive_l.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043f\u0440\u0438\u0432\u043e\u0434\u0430", None))
        self.gearbox_type_v.setItemText(0, "")

        self.body_type_l.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043a\u0443\u0437\u043e\u0432\u0430", None))
        self.n_seat_l.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u043c\u0435\u0441\u0442", None))
        self.n_seat_v.setItemText(0, "")

        self.body_type_v.setItemText(0, "")

        self.fuel_type_v.setItemText(0, "")

        self.wheel_drive_v.setItemText(0, "")

        self.fuel_type_l.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0442\u043e\u043f\u043b\u0438\u0432\u0430", None))
        ___qtablewidgetitem = self.veh_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.veh_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None));
        ___qtablewidgetitem2 = self.veh_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043f\u0430\u0440\u043a", None))
        self.add_veh_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0430\u0432\u0442\u043e\u043f\u0430\u0440\u043a", None))
        self.find_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u" \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.img_box.setText("")
        ___qtablewidgetitem3 = self.spec_table.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem4 = self.spec_table.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"value", None));
        ___qtablewidgetitem5 = self.spec_table.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.msg_box.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

