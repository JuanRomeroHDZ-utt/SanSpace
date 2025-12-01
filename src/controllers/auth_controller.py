from src.models.user_model import UserModel
from src.utils.security import Security

class AuthController:
    def __init__(self):
        # El controlador no necesita conexión directa, usa el Modelo
        self.user_model = UserModel()

    def login(self, email, password):
        try:
            # 1. Obtener el usuario por email (El modelo ya hace el SELECT y los JOINS)
            # Esto devuelve un diccionario con: user_id, user_name, user_password_hashed, etc.
            user = self.user_model.get_user_by_email(email)
            if not user:
                return None # Usuario no encontrado
            # 2. Extraer el hash que ya vino de la base de datos
            hashed_password_from_db = user['user_password_hashed']

            # 3. Verificar password usando la utilidad
            if Security.verify_password(password, hashed_password_from_db):
                return user # Retornamos los datos del usuario para que la interfaz sepa quién es (Admin/Staff)
            else:
                return None # Contraseña incorrecta

        except Exception as e:
            print(f'Error en login controller: {e}')
            return None

if __name__ == '__main__':
    # Prueba
    # auth = AuthController()

    # resultado = auth.login('admin@sanspace.com', '1234')
    # if resultado:
    #     print(f"✅ Login Exitoso: Bienvenido {resultado['user_name']}")
    # else:
    #     print("❌ Login Fallido")
    pass