# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehicle_form.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

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
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.img = QLabel(self.formLayoutWidget)
        self.img.setObjectName(u"img")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.img)

        self.add_btn = QPushButton(veh_form)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(180, 430, 111, 28))

        self.retranslateUi(veh_form)

        QMetaObject.connectSlotsByName(veh_form)
    # setupUi

    def retranslateUi(self, veh_form):
        veh_form.setWindowTitle(QCoreApplication.translate("veh_form", u"Form", None))
        self.img.setText(QCoreApplication.translate("veh_form", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.add_btn.setText(QCoreApplication.translate("veh_form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

