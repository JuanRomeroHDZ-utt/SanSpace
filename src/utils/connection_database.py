import os
import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row

load_dotenv()

class DatabaseConnection:
    def __init__(self):
        #! Utilizaremos mejor el url que está en el .env
        # _user = os.getenv("DB_USER")
        # _pass = os.getenv("DB_PASS")
        # _host = os.getenv("DB_HOST")
        # _port = os.getenv("DB_PORT")
        # _name = os.getenv("DB_NAME")
        #self.connection_url = f"postgresql://{_user}:{_pass}@{_host}:{_port}/{_name}"
        self.connection_url = os.getenv("DATABASE_URL")

    def get_connection(self):
        try:
            # autocommit=True es útil para evitar bloqueos si no manejas transacciones manuales aún
            return psycopg.connect(self.connection_url, row_factory=dict_row, autocommit=True)
        except Exception as e:
            print(f'❌ Error crítico de conexión: {e}')
            return None

    def test_connection(self):
        conexion = self.get_connection()
        # Validación de seguridad: Si falló la conexión, no seguimos
        if conexion is None:
            return "Fallo al conectar"
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT 1 as Prueba_de_Conexion")
                    resultado = cursor.fetchone()
                    return resultado # Debería devolver {'prueba_de_conexion': 1}
        except Exception as e:
            print(f"Error durante el test: {e}")
            return None

if __name__ == '__main__':
    db = DatabaseConnection()
    print(f"Prueba de conexión: {db.test_connection()}")