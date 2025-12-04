import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from src.views.ui.login_ui import Ui_MainWindow
from src.controllers.auth_controller import AuthController

class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        # 1. Configuración de la UI generada de Qt
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 2. Instancia del controlador
        self.auth_controller = AuthController()

        # 3. Conectamos eventos  (signals and slots)
        self.ui.button_login.clicked.connect(self.handle_login)

    def handle_login(self):
        email = self.ui.input_email.text().strip()
        password = self.ui.input_password.text().strip()

        if not email or not password:
            QMessageBox.warning(self, 'Faltan datos', 'Faltan datos')
            return
        user = self.auth_controller.login(email, password)

        if user:
            QMessageBox.information(self, "Bienvenido", f"Bienvenido {user['user_name']}")
        else:
            QMessageBox.critical(self, "Error", "Error: Credenciales incorrectas")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginView()
    window.show()
    sys.exit(app.exec())

