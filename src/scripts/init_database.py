import os
import psycopg
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# -------------------------
#  Rutas del proyecto
# -------------------------

# Subir 2 niveles para llegar a la carpeta raíz "sanspace/"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ruta completa a /database/schema.sql
SCHEMA_PATH = os.path.join(BASE_DIR, "database", "schema.sql")

def create_database_structure():
    print('🚀 Iniciando configuración de SanSpace DB...\n')
    # Obtener contraseña local de postgres
    password_postgres = input("Ingresa la contraseña de tu usuario 'postgres' local: ")
    # Conexión al sistema postgres principal
    postgres_conexion_url = f"postgresql://postgres:{password_postgres}@localhost:5432/postgres"

    # -------------------------------------------------
    # Paso 1 → Crear usuario y base de datos
    # -------------------------------------------------
    try:
        with psycopg.connect(postgres_conexion_url, autocommit=True) as conexion:
            with conexion.cursor() as cursor:
                print("1️⃣  Creando usuario: 'sanspace_dev'")
                try:
                    cursor.execute("CREATE USER sanspace_dev WITH PASSWORD 'sanspace_dev';")
                    cursor.execute("ALTER USER sanspace_dev WITH LOGIN;")
                    cursor.execute("ALTER USER sanspace_dev WITH CREATEDB;")
                except Exception as e:
                    print(f"⚠️  Usuario ya existe → {e}")
                print("2️⃣  Creando base de datos 'sanspace_db'")
                try:
                    cursor.execute("CREATE DATABASE sanspace_db OWNER sanspace_dev;")
                except Exception as e:
                    print(f"⚠️  Base de datos ya existe → {e}")
    except Exception as e:
        print(f"❌ Error en paso administrativo: {e}")
        return

    # -------------------------------------------------
    # Paso 2 → Crear tablas desde schema.sql
    # -------------------------------------------------
    sanspace_conexion_url = "postgresql://sanspace_dev:sanspace_dev@localhost:5432/sanspace_db"
    try:
        with psycopg.connect(sanspace_conexion_url) as conexion:
            with conexion.cursor() as cursor:
                print(f"\n📄 Leyendo archivo SQL desde:\n{SCHEMA_PATH}")
                with open(SCHEMA_PATH, "r", encoding="utf-8") as schema_file:
                    schema_sql = schema_file.read()
                print("\n🛠️  Ejecutando creación de tablas...")
                cursor.execute(schema_sql)
                print("✅ Tablas creadas exitosamente")
    except Exception as e:
        print(f"❌ Error al crear tablas: {e}")

if __name__ == "__main__":
    create_database_structure()