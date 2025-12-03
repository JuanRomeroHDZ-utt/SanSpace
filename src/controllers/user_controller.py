from src.models.user_model import UserModel
from src.utils.security import Security

class UserController:
    def __init__(self):
        self.user_model = UserModel()
        pass

    def get_users(self):
        # Iniciamos la clase UserModel y llamamos al metodo read_users
        return self.user_model.read_users()

    def create_user(self, data:dict):
        try:
            # 1. Validar datos ingresados
            if not data.get('user_name') or not data.get('user_email'):
                return {'success': False, 'message': 'Nombre y Email son obligatorios'}

            # 2. Validar formato de email
            if '@' not in data['user_email']:
                return {'success': False, 'message': 'Email inválido (falta @)'}

            # 3. Validar longitud de la contraseña
            password = data.get('password', '')
            if len(password) < 4:
                return {'success': False, 'message': 'La contraseña debe tener al menos 4 catacteres'}

            # 2. Seguridad
            hashed_password = Security.hash_password(password)

            # 3. Si no hay datos, dejar los de default
            user_photo_url = data.get('user_photo_url', '')
            user_employee_number = data.get('user_employee_number', 'N/A')
            user_emergency_data = data.get('user_emergency_data', {})

            # 4. Llamar al modulo
            # Pasamos los argumentos en el orden que se pide en UserModel.create_users
            new_user = self.user_model.create_users(
                data['user_name'],
                data['user_last_name'],
                data['user_email'],
                hashed_password,
                data['user_cellphone'],
                user_photo_url,
                user_employee_number,
                user_emergency_data,
                int(data['role_id']),
                int(data['department_id']),
                int(data['address_id'])
            )
            if new_user:
                return {'success': True, 'message': f'Usuario creado exitosamente, ID: {new_user}'}
            else:
                return {'success': False, 'message': 'Error al guardar en base de datos'}
        except Exception as e:
            print(f'Error en create_user -> user_controller')
            return {'success': False, 'message': f'Error interno: {e}'}

    def update_user(self, user_id, data:dict):
        try:
            # 1. Validar datos importantes
            if not user_id:
                return {'success': False, 'message': 'El ID es obligatorio'}
            if not data:
                return {'success': False, 'message': 'No se enviaron datos para actualizar'}
            required_fields = ['user_name', 'user_last_name', 'user_cellphone', 'role_id', 'department_id']
            for field in required_fields:
                if not data.get(field):
                    return {'success': False, 'message': f'El campo {field} es obligatorio'}
            update_user = self.user_model.update_users(
                user_id,
                data['user_name'],
                data['user_last_name'],
                data['user_cellphone'],
                int(data['role_id']),
                int(data['department_id'])
            )
            if update_user is True:
                return {'success': True, 'message': f'Usuario actualizado exitosamente: {update_user}'}
            elif update_user is False:
                return {'success': False, 'message': 'El usuario no existe o no hubo cambios'}
            else:
                return {'success': False, 'message': 'Error al guardar en la base de datos'}
        except Exception as e:
            print(f'Error en update_users -> user_controller')
            return {'success': False, 'message': f'Error interno: {e}'}

    def delete_user(self, user_id):
        try:
            if not user_id:
                return {'success': False, 'message': 'El ID es obligatorio'}
            delete_user = self.user_model.delete_users(
                user_id
            )
            if delete_user is True:
                return {'success': True, 'message': f'Usuario eliminado exitosamente: {delete_user}'}
            elif delete_user is False:
                return {'success': False, 'message': 'El usuario no existe o no hubo cambios'}
            else:
                return {'success': False, 'message': 'Error al guardar en la base de datos'}
        except Exception as e:
            print(f'Error en delete_user -> user_controller')
            return {'success': False, 'message': f'Error interno: {e}'}
if __name__ == '__main__':
    # Iniciamos el objeto UserController para poder llamar el metodo get_users -> Si quiero hacer una prueba solo descomentar
    # user_controller = UserController()
    # print(user_controller.get_users())

    pass