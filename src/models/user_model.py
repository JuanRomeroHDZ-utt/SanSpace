from src.utils.connection_database import DatabaseConnection
import json

class UserModel:
    def __init__(self):
        self.db = DatabaseConnection()

    def read_users(self):
        try:
            with self.db.get_connection() as conexion:
                with conexion.cursor() as cursor:
                    query_read_users = """
                    SELECT *
                    FROM users
                    WHERE user_is_active = TRUE
                    ORDER BY user_id
                    """
                    cursor.execute(query_read_users)
                    return cursor.fetchall()
        except Exception as e:
            print(f'Error en read_users: {e}')

    def create_users(self, user_name, user_last_name, user_email, user_password_hashed, user_cellphone, user_photo_url, user_employee_number, user_emergency_data, role_id, department_id, address_id):
        try:
            with self.db.get_connection() as conexion:
                with conexion.cursor() as cursor:
                    query_create_users = """
                    INSERT INTO users(
                    user_name,
                    user_last_name,
                    user_email,
                    user_password_hashed,
                    user_cellphone,
                    user_photo_url,
                    user_employee_number,
                    user_emergency_data,
                    role_id,
                    department_id,
                    address_id
                    )
                    VALUES(
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                    )
                    RETURNING user_id;
                    """
                    values = (
                            user_name,
                            user_last_name,
                            user_email,
                            user_password_hashed,
                            user_cellphone,
                            user_photo_url,
                            user_employee_number,
                            json.dumps(user_emergency_data),
                            role_id,
                            department_id,
                            address_id)
                    cursor.execute(query_create_users, values)
                    user_id = cursor.fetchone()
                    if not user_id:
                        raise Exception('Error en user_id')
                    return user_id['user_id']
        except Exception as e:
            print(f'Error en create_users: {e}')
            return None

    def get_user_by_email(self, email):
        try:
            with self.db.get_connection() as conexion:
                with conexion.cursor() as cursor:
                    query_get_user_by_email = """
                    SELECT users.user_id, users.user_name, users.user_last_name, users.user_email, users.user_password_hashed, users.user_cellphone, users.user_employee_number, users.user_emergency_data, roles.role_name, departments.department_name, addresses.address_street
                    FROM users
                    INNER JOIN roles ON users.role_id = roles.role_id
                    INNER JOIN departments ON users.department_id = departments.department_id
                    INNER JOIN addresses ON users.address_id = addresses.address_id
                    WHERE users.user_email = %s;
                    """
                    cursor.execute(query_get_user_by_email, (email, ))
                    return cursor.fetchone()
        except Exception as e:
            print(f'Error en get_user_by_email: {e}')
            return None

if __name__ == '__main__':
    #! Descomentar si se quiere hacer algo
    # a = UserModel()
    #? Prueba de read
    # print(a.read_users())

    #? Ejemplo de crear usuario -> Ya en la base de datos, cambiar valores
    # user_data = (
    #     'Maria',  # user_name
    #     'López',  # user_last_name
    #     'maria.lopez@sanspace.com',  # user_email
    #     'hash456',  # user_password_hashed
    #     '664-234-5678',  # user_cellphone
    #     'https://sanspace.com/photos/maria.jpg',  # user_photo_url
    #     'EMP-002',  # user_employee_number
    #     json.dumps({"emergency_contact": "Carlos López", "emergency_phone": "664-876-5432"}),  # user_emergency_data
    #     2,  # role_id
    #     2,  # department_id
    #     2   # address_id
    # )

    #? Prueba de busqueda por email
    # user = a.get_user_by_email('maria.lopez@sanspace.com')
    # if user:
    #     print(f"Usuario encontrado: {user['user_name']} {user['user_last_name']}")
    # else:
    #     print("Usuario no encontrado")
    pass