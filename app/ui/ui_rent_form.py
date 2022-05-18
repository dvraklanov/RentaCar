# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rent_form.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_rent_form(object):
    def setupUi(self, rent_form):
        if not rent_form.objectName():
            rent_form.setObjectName(u"rent_form")
        rent_form.resize(864, 486)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(rent_form.sizePolicy().hasHeightForWidth())
        rent_form.setSizePolicy(sizePolicy)
        rent_form.setMinimumSize(QSize(864, 486))
        rent_form.setMaximumSize(QSize(864, 486))
        self.horizontalLayoutWidget = QWidget(rent_form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 20, 821, 441))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.rent_label = QLabel(self.horizontalLayoutWidget)
        self.rent_label.setObjectName(u"rent_label")
        self.rent_label.setStyleSheet(u"font: 14pt \"Segoe UI\";\n"
"")
        self.rent_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.rent_label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(20)
        self.new_cust_l = QLabel(self.horizontalLayoutWidget)
        self.new_cust_l.setObjectName(u"new_cust_l")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.new_cust_l)

        self.new_cust_v = QRadioButton(self.horizontalLayoutWidget)
        self.new_cust_v.setObjectName(u"new_cust_v")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.new_cust_v)

        self.name_l = QLabel(self.horizontalLayoutWidget)
        self.name_l.setObjectName(u"name_l")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.name_l)

        self.name_v = QLineEdit(self.horizontalLayoutWidget)
        self.name_v.setObjectName(u"name_v")
        self.name_v.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name_v)

        self.lastname_l = QLabel(self.horizontalLayoutWidget)
        self.lastname_l.setObjectName(u"lastname_l")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lastname_l)

        self.lastname_v = QLineEdit(self.horizontalLayoutWidget)
        self.lastname_v.setObjectName(u"lastname_v")
        self.lastname_v.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lastname_v)

        self.surname_l = QLabel(self.horizontalLayoutWidget)
        self.surname_l.setObjectName(u"surname_l")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.surname_l)

        self.surname_v = QLineEdit(self.horizontalLayoutWidget)
        self.surname_v.setObjectName(u"surname_v")
        self.surname_v.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.surname_v)

        self.pass_l = QLabel(self.horizontalLayoutWidget)
        self.pass_l.setObjectName(u"pass_l")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.pass_l)

        self.pass_v = QLineEdit(self.horizontalLayoutWidget)
        self.pass_v.setObjectName(u"pass_v")
        self.pass_v.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.pass_v)

        self.start_date_l = QLabel(self.horizontalLayoutWidget)
        self.start_date_l.setObjectName(u"start_date_l")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.start_date_l)

        self.start_date_v = QDateEdit(self.horizontalLayoutWidget)
        self.start_date_v.setObjectName(u"start_date_v")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.start_date_v)

        self.end_date_l = QLabel(self.horizontalLayoutWidget)
        self.end_date_l.setObjectName(u"end_date_l")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.end_date_l)

        self.end_date_v = QDateEdit(self.horizontalLayoutWidget)
        self.end_date_v.setObjectName(u"end_date_v")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.end_date_v)

        self.add_rent_btn = QPushButton(self.horizontalLayoutWidget)
        self.add_rent_btn.setObjectName(u"add_rent_btn")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.add_rent_btn)


        self.verticalLayout.addLayout(self.formLayout)

        self.msg_box = QLabel(self.horizontalLayoutWidget)
        self.msg_box.setObjectName(u"msg_box")

        self.verticalLayout.addWidget(self.msg_box)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 22)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cust_table_lable = QLabel(self.horizontalLayoutWidget)
        self.cust_table_lable.setObjectName(u"cust_table_lable")
        self.cust_table_lable.setStyleSheet(u"font: 14pt \"Segoe UI\";\n"
"\n"
"")
        self.cust_table_lable.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.cust_table_lable)

        self.cust_table = QTableWidget(self.horizontalLayoutWidget)
        if (self.cust_table.columnCount() < 2):
            self.cust_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.cust_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.cust_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.cust_table.setObjectName(u"cust_table")
        self.cust_table.horizontalHeader().setVisible(True)
        self.cust_table.horizontalHeader().setDefaultSectionSize(60)
        self.cust_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.cust_table)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(rent_form)

        QMetaObject.connectSlotsByName(rent_form)
    # setupUi

    def retranslateUi(self, rent_form):
        rent_form.setWindowTitle(QCoreApplication.translate("rent_form", u"Form", None))
        self.rent_label.setText(QCoreApplication.translate("rent_form", u"\u0424\u043e\u0440\u043c\u0430 \u043d\u043e\u0432\u043e\u0433\u043e \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430 \u0430\u0440\u0435\u043d\u0434\u044b", None))
        self.new_cust_l.setText(QCoreApplication.translate("rent_form", u"\u041d\u043e\u0432\u044b\u0439 \u043a\u043b\u0438\u0435\u043d\u0442?", None))
        self.new_cust_v.setText("")
        self.name_l.setText(QCoreApplication.translate("rent_form", u"\u0418\u043c\u044f", None))
        self.lastname_l.setText(QCoreApplication.translate("rent_form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.surname_l.setText(QCoreApplication.translate("rent_form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.pass_l.setText(QCoreApplication.translate("rent_form", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.start_date_l.setText(QCoreApplication.translate("rent_form", u"\u041d\u0430\u0447\u0430\u043b\u043e \u0430\u0440\u0435\u043d\u0434\u044b", None))
        self.end_date_l.setText(QCoreApplication.translate("rent_form", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435 \u0430\u0440\u0435\u043d\u0434\u044b", None))
        self.add_rent_btn.setText(QCoreApplication.translate("rent_form", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
        self.msg_box.setText("")
