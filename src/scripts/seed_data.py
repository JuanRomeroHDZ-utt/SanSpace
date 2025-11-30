from src.utils.connection_database import DatabaseConnection

class SanSpaceSeeder:
    def __init__(self):
        self.db = DatabaseConnection()

    def run(self):
        #* Se rellenan todas las tablas con información, si no da error entonces se llenaron con éxito
        print("🌱 Iniciando siembra de datos (Seeding)...")
        if self.seed_level_cero_geografia():
            pass
    def _execute_batch(self, query, data, level_name):
        #* Ayuda a ejecutar inserts masivos.
        try:
            with self.db.get_connection() as conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(query,data)
                    print(f"✅ {level_name} insertado.")
                    return True
        except Exception as e:
            print(f'Error en {level_name}: {e}')

    #! ---------------------------------------------------
    #! NIVEL 0 -> Geografia y reglas (base)
    #! ---------------------------------------------------
    def seed_level_cero_geografia(self):
        # 1. Paises
        query_countries = "INSERT INTO countries (country_name, country_code) VALUES (%s, %s)"
        data_countries = "[('México', 'MEX'), ('Estados Unidos', 'USA')]"

        # 2. Estados
        query_states = "INSERT INTO states(state_name, state_code) VALUES (%s, %s)"
        data_states = [('Baja California', 'BC'), ('California', 'CA')]

        # 3. Ciudades
        query_cities = "INSERT INTO cities (city_name) VALUES(%s)"
        data_cities = [('Tijuana'), ('San Diego')]

        # 4. Codigos Postales
        query_postal_codes = "INSERT INTO postal_codes (postal_code_number) VALUES(%s)"
        data_postal_codes = [('22000'), ('22100'), ('92101')]

        # 5. Direcciones fisicas
        query_addresses = "INSERT INTO addresses (address_street, address_exterior_num, address_colonia, address_references)"
        data_addresses = [('Av. Revolución', '1234', 'Centro', 'Frente al arco'), ('Calle 5ta', '500', 'Zona Rio', 'Bodega trasera'), ('Blvd. Agua Caliente', '90', 'Cacho', 'Casa color azul')]

        # 6. Reglas de uso
        query_rules = "INSERT INTO rules (rule_name, rule_description) VALUES (%s, %s)"
        data_rules = [('Prohibido Fumar', 'No se permite humo en áreas cerradas'), ('Casco Obligatorio', 'Zona de construcción o riesgo'), ('Solo Personal', 'Área restringida a empleados')]

        success = (
            self._execute_batch(query_addresses, data_addresses, "Paises") and
            self._execute_batch(query_states, data_states, "Estados") and
            self._execute_batch(query_cities, data_cities, "Ciudades") and
            self._execute_batch(query_postal_codes, data_postal_codes, "CPs") and
            self._execute_batch(query_addresses, data_addresses, "Direcciones") and
            self._execute_batch(query_rules, data_rules, "Reglas")
        )
        return success