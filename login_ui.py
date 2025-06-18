# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(787, 598)
        self.oper_label = QLabel(Dialog)
        self.oper_label.setObjectName(u"oper_label")
        self.oper_label.setGeometry(QRect(140, 230, 201, 31))
        font = QFont()
        font.setFamilies([u"Courier"])
        font.setPointSize(28)
        self.oper_label.setFont(font)
        self.login_btn = QPushButton(Dialog)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(310, 430, 171, 41))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.login_btn.setFont(font1)
        self.login_btn.setAutoFillBackground(False)
        self.login_btn.setStyleSheet(u"QPushButton{ background-color: white;\n"
"color:black;\n"
"border-radius:8px;\n"
"padding:6px 12px;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: blue;\n"
"}")
        self.login_label = QLabel(Dialog)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setGeometry(QRect(290, 40, 181, 81))
        font2 = QFont()
        font2.setPointSize(44)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(True)
        font2.setStrikeOut(False)
        self.login_label.setFont(font2)
        self.operator_input = QLineEdit(Dialog)
        self.operator_input.setObjectName(u"operator_input")
        self.operator_input.setGeometry(QRect(420, 230, 181, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.operator_input.setFont(font3)
        self.pass_label = QLabel(Dialog)
        self.pass_label.setObjectName(u"pass_label")
        self.pass_label.setGeometry(QRect(140, 300, 181, 31))
        self.pass_label.setFont(font)
        self.password_input = QLineEdit(Dialog)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(420, 300, 181, 31))
        self.password_input.setFont(font3)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setClearButtonEnabled(False)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Login Form", None))
        self.oper_label.setText(QCoreApplication.translate("Dialog", u"Operator :", None))
        self.login_btn.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.login_label.setText(QCoreApplication.translate("Dialog", u"LOGIN ", None))
        self.pass_label.setText(QCoreApplication.translate("Dialog", u"Password", None))
    # retranslateUi

