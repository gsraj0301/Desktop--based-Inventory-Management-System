from PySide6.QtWidgets import QApplication, QMainWindow,QDialog
from main_menu_ui import Ui_MainWindow
from goods_main import GoodsForm
from sales_main import Sales_Form
from products_main import Product_Form


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.goods_btn.clicked.connect(self.open_goods_form)
        self.ui.sales_btn.clicked.connect(self.open_sales_form)
        self.ui.product_btn.clicked.connect(self.open_product_form)
        self.good_window = None
        self.sales_window = None
        self.product_window = None

    def open_goods_form(self):
        self.goods_window = GoodsForm()
        self.goods_window.show()
    def open_sales_form(self):
        self.sales_window = Sales_Form()
        self.sales_window.show()
    def open_product_form(self):
        self.product_window = Product_Form()
        self.product_window.show()

if __name__=="__main__":
    app = QApplication([])
    window = MainMenu()
    window.show()
    app.exec()