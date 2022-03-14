# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehicle_form.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_veh_form(object):
    def setupUi(self, veh_form):
        if not veh_form.objectName():
            veh_form.setObjectName(u"veh_form")
        veh_form.resize(460, 500)
        veh_form.setMinimumSize(QSize(460, 500))
        veh_form.setMaximumSize(QSize(460, 500))
        self.formLayoutWidget = QWidget(veh_form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 30, 381, 394))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.name_l = QLabel(self.formLayoutWidget)
        self.name_l.setObjectName(u"name_l")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.name_l)

        self.number_plate_l = QLabel(self.formLayoutWidget)
        self.number_plate_l.setObjectName(u"number_plate_l")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.number_plate_l)

        self.body_type_l = QLabel(self.formLayoutWidget)
        self.body_type_l.setObjectName(u"body_type_l")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.body_type_l)

        self.wheel_drive_l = QLabel(self.formLayoutWidget)
        self.wheel_drive_l.setObjectName(u"wheel_drive_l")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.wheel_drive_l)

        self.fuel_type_l = QLabel(self.formLayoutWidget)
        self.fuel_type_l.setObjectName(u"fuel_type_l")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.fuel_type_l)

        self.powet_hp_l = QLabel(self.formLayoutWidget)
        self.powet_hp_l.setObjectName(u"powet_hp_l")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.powet_hp_l)

        self.n_seat_l = QLabel(self.formLayoutWidget)
        self.n_seat_l.setObjectName(u"n_seat_l")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.n_seat_l)

        self.gearbox_type_l = QLabel(self.formLayoutWidget)
        self.gearbox_type_l.setObjectName(u"gearbox_type_l")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.gearbox_type_l)

        self.rental_price_l = QLabel(self.formLayoutWidget)
        self.rental_price_l.setObjectName(u"rental_price_l")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.rental_price_l)

        self.img_2 = QLabel(self.formLayoutWidget)
        self.img_2.setObjectName(u"img_2")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.img_2)

        self.name_v = QLineEdit(self.formLayoutWidget)
        self.name_v.setObjectName(u"name_v")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_v)

        self.number_plate_v = QLineEdit(self.formLayoutWidget)
        self.number_plate_v.setObjectName(u"number_plate_v")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.number_plate_v)

        self.body_type_v = QLineEdit(self.formLayoutWidget)
        self.body_type_v.setObjectName(u"body_type_v")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.body_type_v)

        self.wheel_drive_v = QLineEdit(self.formLayoutWidget)
        self.wheel_drive_v.setObjectName(u"wheel_drive_v")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.wheel_drive_v)

        self.fuel_type_v = QLineEdit(self.formLayoutWidget)
        self.fuel_type_v.setObjectName(u"fuel_type_v")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.fuel_type_v)

        self.power_hp_v = QLineEdit(self.formLayoutWidget)
        self.power_hp_v.setObjectName(u"power_hp_v")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.power_hp_v)

        self.n_seat_v = QLineEdit(self.formLayoutWidget)
        self.n_seat_v.setObjectName(u"n_seat_v")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.n_seat_v)

        self.gearbox_type_v = QLineEdit(self.formLayoutWidget)
        self.gearbox_type_v.setObjectName(u"gearbox_type_v")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.gearbox_type_v)

        self.rental_price_v = QLineEdit(self.formLayoutWidget)
        self.rental_price_v.setObjectName(u"rental_price_v")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.rental_price_v)

        self.add_btn = QPushButton(veh_form)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(180, 430, 111, 28))

        self.retranslateUi(veh_form)

        QMetaObject.connectSlotsByName(veh_form)
    # setupUi

    def retranslateUi(self, veh_form):
        veh_form.setWindowTitle(QCoreApplication.translate("veh_form", u"Form", None))
        self.name_l.setText(QCoreApplication.translate("veh_form", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.number_plate_l.setText(QCoreApplication.translate("veh_form", u"\u0413\u043e\u0441. \u043d\u043e\u043c\u0435\u0440", None))
        self.body_type_l.setText(QCoreApplication.translate("veh_form", u"\u0422\u0438\u043f \u043a\u0443\u0437\u043e\u0432\u0430", None))
        self.wheel_drive_l.setText(QCoreApplication.translate("veh_form", u"\u0422\u0438\u043f \u043f\u0440\u0438\u0432\u043e\u0434\u0430", None))
        self.fuel_type_l.setText(QCoreApplication.translate("veh_form", u"\u0422\u0438\u043f \u0442\u043e\u043f\u043b\u0438\u0432\u0430", None))
        self.powet_hp_l.setText(QCoreApplication.translate("veh_form", u"\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c (\u043b.\u0441.)", None))
        self.n_seat_l.setText(QCoreApplication.translate("veh_form", u"\u041a\u043e\u043b-\u0432\u043e \u043c\u0435\u0441\u0442", None))
        self.gearbox_type_l.setText(QCoreApplication.translate("veh_form", u"\u0422\u0438\u043f \u041a\u041f\u041f", None))
        self.rental_price_l.setText(QCoreApplication.translate("veh_form", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c (\u0440\u0443\u0431./\u0441\u0443\u0442.)", None))
        self.img_2.setText(QCoreApplication.translate("veh_form", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.add_btn.setText(QCoreApplication.translate("veh_form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

