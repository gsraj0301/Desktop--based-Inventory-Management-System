from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from login_ui import Ui_Dialog
from menu_form import MainMenu
import sys


class LoginApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    
        self.ui.login_btn.clicked.connect(self.handle_login)
    def handle_login(self):
        username = self.ui.operator_input.text()
        password = self.ui.password_input.text()

        if (username == "admin1" and password == "1234") or (username == "admin2" and password == "4321"):
            QMessageBox.information(self,"Success", "Login Sucessfull")
            self.open_main_menu()
        else:
            QMessageBox.warning(self,"Error", "Invalid Username or Password ")

    def open_main_menu(self):
        self.main_menu = MainMenu()
        self.main_menu.show()
        self.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())