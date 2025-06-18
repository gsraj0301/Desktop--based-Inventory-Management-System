import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from goods_form import Ui_Form
import sqlite3
from database import create_goods_table
class GoodsForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #set higher max rate
        self.ui.rate_input.setMaximum(9999999.99)
       

        create_goods_table()

        self.ui.calcbtn.clicked.connect(self.calculate_total)
        self.ui.clear_btn.clicked.connect(self.pagevanish)

        self.ui.pushButton.clicked.connect(self.submit_form)

    def pagevanish(self):
        self.ui.product_name.clear()
        self.ui.supplier_name.clear()
        self.ui.quantity_input.setValue(0)
        self.ui.rate_input.setValue(0)
        self.ui.tax_input.setValue(0)
        self.ui.total_label.setText("0.00")

            
        

    def calculate_total(self):
        quantity = self.ui.quantity_input.value()
        rate = self.ui.rate_input.value()
        tax = self.ui.tax_input.value()
        subtotal = quantity * rate
        total = subtotal + (subtotal * tax / 100)
        self.ui.total_label.setText(f"{total:2f}")

    def submit_form(self):
        name = self.ui.product_name.text()
        supplier = self.ui.supplier_name.text()
        qty = self.ui.quantity_input.value()
        unit = self.ui.comboBox_2.currentText()
        rate = self.ui.rate_input.value()
        tax = self.ui.tax_input.value()
        total = float(self.ui.total_label.text())

        if not all([name, supplier, qty, rate, tax]):
            QMessageBox.warning(self, "Missing Data.", "Please fill all the fields and calculate the total")

        try:
            conn = sqlite3.connect("inventory.db")
            c = conn.cursor()
            c.execute('''
                    INSERT INTO goods_receiving(
                    supplier_name, product_name, quantity, unit, rate_per_unit, tax, total)
                    VALUES (?,?,?,?,?,?,?)
                    
                    ''',(name, supplier,  qty, unit, rate, tax, total) )
            conn.commit()
            conn.close()
            
        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

        QMessageBox.information(self, "Sucess", "Goods Receiving Data Saved Sucessfully")
        self.pagevanish()
        print("Product form submitted successfully.")

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = GoodsForm()
    window.show()
    sys.exit(app.exec())