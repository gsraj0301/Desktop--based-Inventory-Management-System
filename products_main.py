import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
import os
from PySide6.QtGui import QPixmap
from product_master import Ui_product_label
import sqlite3
from database import create_product_table

class Product_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_product_label()
        self.ui.setupUi(self)
        
        self.image_file_path = ""

        create_product_table()

        self.ui.clear_btn.clicked.connect(self.pagevanish)
        self.ui.upl_img.clicked.connect(self.upload_image)

        self.ui.submit_btn.clicked.connect(self.submit_form)

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.xpm *.jpg *.bmp)" )  
        if file_path:
            self.image_file_path = file_path
            pixmap = QPixmap(file_path).scaled(150, 150)
            self.ui.img_pre.setPixmap(pixmap)


    
    def pagevanish(self):
        self.ui.bar_input.clear()
        self.ui.sku_input.clear()
        self.ui.cat_input.clear()
        self.ui.subcat_input.clear()
        self.ui.product_input.clear()
        self.ui.desc_input.clear()
        self.ui.tax_input.setValue(0)
        self.ui.doubleSpinBox.clear()
        self.ui.unit_input.setCurrentIndex(0)
        self.ui.img_pre.clear()

    def submit_form(self):
        product = self.ui.product_input.text()
        barcode = self.ui.bar_input.text()
        sku_id = self.ui.sku_input.text()
        unit = self.ui.unit_input.currentText()
        price = self.ui.doubleSpinBox.value()
        tax = self.ui.tax_input.value()
        description = self.ui.desc_input.toPlainText()
        category = self.ui.cat_input.text()
        subcategory = self.ui.subcat_input.text()
        image_path = self.image_file_path

        if not product or price <= 0:
            QMessageBox.warning(self, "Missing Data", "Please enter product name and a valid price.")
            return

        try:
            conn = sqlite3.connect("inventory.db")
            c = conn.cursor()
            c.execute('''
                INSERT INTO product_master (
                    product_name, barcode, sku_id, category, subcategory,
                    description, image_path, unit, tax, price
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (product, barcode, sku_id, category, subcategory,
                description, image_path, unit, tax, price))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Success", "Product saved successfully!")
            self.pagevanish()
            print("Product form submitted successfully.")

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

        self.image_file_path = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Product_Form()
    window.show()
    sys.exit(app.exec())


        