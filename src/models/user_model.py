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
#? Prueba de read
a = UserModel()
print(a.read_users())
