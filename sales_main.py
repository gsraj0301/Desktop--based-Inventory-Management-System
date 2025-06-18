import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from sales_form import Ui_unit_input_2
import sqlite3
from database import create_sales_table

class Sales_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_unit_input_2()
        self.ui.setupUi(self)

        #set higher max rate
        self.ui.rate_input.setMaximum(9999999.99)
        

        create_sales_table()

        self.ui.calc_btn.clicked.connect(self.calculate_total)
        self.ui.clear_btn.clicked.connect(self.pagevanish)

        self.ui.submit_btn.clicked.connect(self.submit_form)

#Calculation code
    def calculate_total(self):
        quantity = self.ui.qty_input.value()
        rate = self.ui.rate_input.value()
        tax = self.ui.tax_input.value()
        subtotal = quantity * rate
        total = subtotal + (subtotal * tax / 100)
        self.ui.totale_rate_label.setText(f"{total:2f}")

#Submit code
    def submit_form(self):
        product = self.ui.product_input.text()
        customer = self.ui.customer_input.text()
        qty = self.ui.qty_input.value()
        unit = self.ui.unit_input.currentText()
        rate = self.ui.rate_input.value()
        tax = self.ui.tax_input.value()
        total = float(self.ui.totale_rate_label.text())

        if not all([product, customer, qty, rate, tax]):
            QMessageBox.warning(self, "Missing Data.", "Please fill all the fields and calculate the total")
        
        try:
            conn = sqlite3.connect("inventory.db")
            c = conn.cursor()
            c.execute('''
                    INSERT INTO sales(
                    customer_name, product_name, quantity, unit, rate_per_unit, tax, total)
                    VALUES (?,?,?,?,?,?,?)
                    
                    ''',(customer, product,  qty, unit, rate, tax, total) )
            conn.commit()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))
        
        QMessageBox.information(self, "Sucess", "Sales Data Saved Sucessfully")
        self.pagevanish()
        print("Product form submitted successfully.")
        


        
    def pagevanish(self):
        self.ui.product_input.clear()
        self.ui.customer_input.clear()
        self.ui.qty_input.setValue(0)
        self.ui.rate_input.setValue(0)
        self.ui.tax_input.setValue(0)
        self.ui.total_label.setText("0.00")

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Sales_Form()
    window.show()
    sys.exit(app.exec())