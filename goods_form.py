# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'goods_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(828, 538)
        self.goods_receive_label = QLabel(Form)
        self.goods_receive_label.setObjectName(u"goods_receive_label")
        self.goods_receive_label.setGeometry(QRect(220, 20, 411, 61))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(32)
        font.setUnderline(True)
        self.goods_receive_label.setFont(font)
        self.product_label = QLabel(Form)
        self.product_label.setObjectName(u"product_label")
        self.product_label.setGeometry(QRect(20, 200, 221, 31))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(24)
        self.product_label.setFont(font1)
        self.supplier_label = QLabel(Form)
        self.supplier_label.setObjectName(u"supplier_label")
        self.supplier_label.setGeometry(QRect(20, 110, 241, 41))
        self.supplier_label.setFont(font1)
        self.quantity_label = QLabel(Form)
        self.quantity_label.setObjectName(u"quantity_label")
        self.quantity_label.setGeometry(QRect(20, 290, 141, 41))
        self.quantity_label.setFont(font1)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 160, 821, 16))
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.unit_label = QLabel(Form)
        self.unit_label.setObjectName(u"unit_label")
        self.unit_label.setGeometry(QRect(60, 400, 81, 41))
        self.unit_label.setFont(font1)
        self.Rate_label = QLabel(Form)
        self.Rate_label.setObjectName(u"Rate_label")
        self.Rate_label.setGeometry(QRect(520, 230, 171, 51))
        self.Rate_label.setFont(font1)
        self.tax_label = QLabel(Form)
        self.tax_label.setObjectName(u"tax_label")
        self.tax_label.setGeometry(QRect(590, 320, 111, 41))
        self.tax_label.setFont(font1)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(700, 420, 121, 20))
        self.line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.total_rate_label = QLabel(Form)
        self.total_rate_label.setObjectName(u"total_rate_label")
        self.total_rate_label.setGeometry(QRect(490, 450, 191, 41))
        self.total_rate_label.setFont(font1)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 490, 121, 41))
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton{ background-color: white;\\n\"\n"
"\"color:white;\\n\"\n"
"\"border-radius:8px;\\n\"\n"
"\"padding:6px 12px;\\n\"\n"
"\"font-weight:bold;\\n\"\n"
"\"}\\n\"\n"
"\"\\n\"\n"
"\"QPushButton:hover{\\n\"\n"
"\"background-color: #0078D7;\\n\"\n"
"}")
        self.supplier_name = QLineEdit(Form)
        self.supplier_name.setObjectName(u"supplier_name")
        self.supplier_name.setGeometry(QRect(280, 110, 251, 31))
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(18)
        self.supplier_name.setFont(font3)
        self.product_name = QLineEdit(Form)
        self.product_name.setObjectName(u"product_name")
        self.product_name.setGeometry(QRect(260, 200, 221, 31))
        self.product_name.setFont(font3)
        self.quantity_input = QSpinBox(Form)
        self.quantity_input.setObjectName(u"quantity_input")
        self.quantity_input.setGeometry(QRect(210, 300, 61, 31))
        font4 = QFont()
        font4.setFamilies([u"Consolas"])
        font4.setPointSize(12)
        self.quantity_input.setFont(font4)
        self.rate_input = QDoubleSpinBox(Form)
        self.rate_input.setObjectName(u"rate_input")
        self.rate_input.setGeometry(QRect(720, 230, 71, 41))
        self.rate_input.setFont(font4)
        self.tax_input = QDoubleSpinBox(Form)
        self.tax_input.setObjectName(u"tax_input")
        self.tax_input.setGeometry(QRect(730, 320, 61, 31))
        font5 = QFont()
        font5.setFamilies([u"Comic Sans MS"])
        font5.setPointSize(12)
        self.tax_input.setFont(font5)
        self.total_label = QLabel(Form)
        self.total_label.setObjectName(u"total_label")
        self.total_label.setGeometry(QRect(710, 460, 91, 31))
        self.total_label.setFont(font4)
        self.calcbtn = QPushButton(Form)
        self.calcbtn.setObjectName(u"calcbtn")
        self.calcbtn.setGeometry(QRect(710, 380, 101, 31))
        font6 = QFont()
        font6.setPointSize(12)
        self.calcbtn.setFont(font6)
        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(170, 400, 61, 41))
        self.comboBox_2.setEditable(True)
        self.clear_btn = QPushButton(Form)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setGeometry(QRect(20, 490, 81, 41))
        font7 = QFont()
        font7.setPointSize(18)
        font7.setUnderline(False)
        self.clear_btn.setFont(font7)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Goods Receiving ", None))
        self.goods_receive_label.setText(QCoreApplication.translate("Form", u"Goods Receiving list", None))
        self.product_label.setText(QCoreApplication.translate("Form", u"Product Name", None))
        self.supplier_label.setText(QCoreApplication.translate("Form", u"Supplier Name", None))
        self.quantity_label.setText(QCoreApplication.translate("Form", u"Quantity", None))
        self.unit_label.setText(QCoreApplication.translate("Form", u"Unit", None))
        self.Rate_label.setText(QCoreApplication.translate("Form", u"Rate/Unit", None))
        self.tax_label.setText(QCoreApplication.translate("Form", u"Tax %", None))
        self.total_rate_label.setText(QCoreApplication.translate("Form", u"Total Rate", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.total_label.setText("")
        self.calcbtn.setText(QCoreApplication.translate("Form", u"Calculate", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"Kg", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"meter", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form", u"L", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form", u"pcs", None))
        self.clear_btn.setText(QCoreApplication.translate("Form", u"Clear", None))
    # retranslateUi

