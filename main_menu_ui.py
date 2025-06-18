# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(692, 510)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 20, 301, 61))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(44)
        self.label.setFont(font)
        self.goods_btn = QPushButton(self.centralwidget)
        self.goods_btn.setObjectName(u"goods_btn")
        self.goods_btn.setGeometry(QRect(200, 120, 271, 51))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(24)
        self.goods_btn.setFont(font1)
        self.sales_btn = QPushButton(self.centralwidget)
        self.sales_btn.setObjectName(u"sales_btn")
        self.sales_btn.setGeometry(QRect(200, 190, 271, 51))
        self.sales_btn.setFont(font1)
        self.product_btn = QPushButton(self.centralwidget)
        self.product_btn.setObjectName(u"product_btn")
        self.product_btn.setGeometry(QRect(120, 260, 441, 61))
        self.product_btn.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 692, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main Menu", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Main Menu", None))
        self.goods_btn.setText(QCoreApplication.translate("MainWindow", u"Goods Received", None))
        self.sales_btn.setText(QCoreApplication.translate("MainWindow", u"Sales ", None))
        self.product_btn.setText(QCoreApplication.translate("MainWindow", u"Product Master Creation", None))
    # retranslateUi

