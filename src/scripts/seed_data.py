from src.utils.connection_database import DatabaseConnection
from src.utils.security import Security
class SanSpaceSeeder:
    def __init__(self):
        self.db = DatabaseConnection()

    def run(self):
        #* Se rellenan todas las tablas con información, si no da error entonces se llenaron con éxito
        print("🌱 Iniciando siembra de datos (Seeding)...")
        if self.seed_level_cero_geografia():
            if self.seed_level_one_catalogs():
                if self.seed_level_two_users_and_providers():
                    if self.seed_level_three_sensors_and_floors():
                        if self.seed_level_four_spaces_and_actives():
                            if self.seed_level_five_movements_and_files():
                                print("🌳 ¡Base de datos poblada exitosamente!")
    def _execute_batch(self, query, data, level_name):
        #* Ayuda a ejecutar inserts masivos.
        try:
            with self.db.get_connection() as conexion:
                with conexion.cursor() as cursor:
                    cursor.executemany(query,data)
                    print(f"✅ {level_name} insertado.")
                    return True
        except Exception as e:
            print(f'Error en {level_name}: {e}')

    #! ---------------------------------------------------------
    #! NIVEL 0 -> Geografia y reglas (base)
    #! ---------------------------------------------------------
    def seed_level_cero_geografia(self):
        # 1. Paises
        query_countries = "INSERT INTO countries (country_name, country_code) VALUES (%s, %s)"
        data_countries = [('México', 'MEX'), ('Estados Unidos', 'USA')]

        # 2. Estados
        query_states = "INSERT INTO states(state_name, state_code) VALUES (%s, %s)"
        data_states = [('Baja California', 'BC'), ('California', 'CA')]

        # 3. Ciudades
        query_cities = "INSERT INTO cities (city_name) VALUES(%s)"
        data_cities = [('Tijuana', ), ('San Diego', )]

        # 4. Codigos Postales
        query_postal_codes = "INSERT INTO postal_codes (postal_code_number) VALUES(%s)"
        data_postal_codes = [('22000', ), ('22100', ), ('92101', )]

        # 5. Direcciones fisicas
        query_addresses = "INSERT INTO addresses (address_street, address_exterior_num, address_colonia, address_references) VALUES (%s,%s,%s,%s)"
        data_addresses = [('Av. Revolución', '1234', 'Centro', 'Frente al arco'), ('Calle 5ta', '500', 'Zona Rio', 'Bodega trasera'), ('Blvd. Agua Caliente', '90', 'Cacho', 'Casa color azul')]

        # 6. Reglas de uso
        query_rules = "INSERT INTO rules (rule_name, rule_description) VALUES (%s, %s)"
        data_rules = [('Prohibido Fumar', 'No se permite humo en áreas cerradas'), ('Casco Obligatorio', 'Zona de construcción o riesgo'), ('Solo Personal', 'Área restringida a empleados')]

        success = (
            self._execute_batch(query_countries, data_countries, "Paises") and
            self._execute_batch(query_states, data_states, "Estados") and
            self._execute_batch(query_cities, data_cities, "Ciudades") and
            self._execute_batch(query_postal_codes, data_postal_codes, "CPs") and
            self._execute_batch(query_addresses, data_addresses, "Direcciones") and
            self._execute_batch(query_rules, data_rules, "Reglas")
        )
        return success

    #! ---------------------------------------------------------
    #! NIVEL 1: CATÁLOGOS (La base de la operación)
    #! ---------------------------------------------------------
    def seed_level_one_catalogs(self):
        # 7. Roles
        query_roles = """ INSERT INTO roles (role_name, role_description, role_level, role_permissions) VALUES (%s,%s,%s,%s)"""
        data_roles = [('Admin', 'Acceso Total', 100, '{}'), ('Gerente', 'Reportes y Supervisión', 80, '{}'), ('Operador', 'Uso diario del sistema', 50, '{}'), ('Intendente', 'Personal de limpieza y mantenimiento', 20, '{}'), ('Becario', 'Solo lectura limitada', 10, '{}')]

        # 8. Departamentos
        query_departments = """INSERT INTO departments (department_name, department_manager_name, department_notes) VALUES (%s,%s,%s)"""
        data_deparments = [('Dirección', 'Jefe Patrón', 'Oficina principal'), ('TI', 'Ing. Sistemas', 'Soporte técnico'), ('Limpieza', 'Doña Mari', 'Mantenimiento general'), ('Almacén', 'El encargado', 'Logística')]

        # 9. Marcas
        query_brands =  """INSERT INTO brands (brand_name, brand_website, brand_support_phone) VALUES (%s,%s,%s)"""
        data_brands = [('Cisco', 'www.cisco.com', '01-800-CISCO'), ('Dell', 'www.dell.com', '01-800-DELL'), ('Truper', 'www.truper.com', 'N/A'), ('Herman Miller', 'www.hm.com', 'N/A')]

        # 10. Estatus del activo
        query_active_statuses = """INSERT INTO active_statuses (active_status_name, active_status_color_hex) VALUES (%s,%s)"""
        data_active_statuses = [('Nuevo', '#00FF00'), ('Asignado', '#0000FF'), ('En Reparación', '#FFA500'), ('Dañado/Roto', '#FF0000'), ('Perdido', '#000000')]

        # 11. Tipos de espacios
        query_space_types = """INSERT INTO space_types (space_type_name, space_type_description) VALUES (%s,%s)"""
        data_space_types = [('Oficina', 'Trabajo administrativo'), ('Site de Red', 'Servidores y cableado'), ('Cuarto de Limpieza', 'Artículos de aseo'), ('Baño', 'Servicios sanitarios')]

        # 12. Protocolos de IOT
        query_iot_protocols = """INSERT INTO iot_protocols (iot_protocol_name, iot_protocol_description) VALUES (%s,%s)"""
        data_iot_protocols = [('HTTP', 'Web'), ('MQTT', 'Lightweight')]

        # 13. Unidades de Medida
        query_measurement_units = """INSERT INTO measurement_units (measurement_unit_name, measurement_unit_symbol) VALUES (%s,%s)"""
        data_measurement_units = [('Celsius', '°C'), ('Boolean', 'T/F')]

        # 14. Categorías
        query_categories = """INSERT INTO categories (category_name, category_code, category_parent_id) VALUES (%s,%s,%s)"""
        data_categories = [('Electrónica', 'CMP', None), ('Mobiliario', 'MOB', None), ('Herramientas', 'HER', None)]

        success_one = (
            self._execute_batch(query_roles, data_roles, "Roles") and
            self._execute_batch(query_departments, data_deparments, "Departamentos") and
            self._execute_batch(query_brands, data_brands, "Marcas") and
            self._execute_batch(query_active_statuses, data_active_statuses, "Estados") and
            self._execute_batch(query_space_types, data_space_types, "Tipos de espacio") and
            self._execute_batch(query_iot_protocols, data_iot_protocols, "Protocolos") and
            self._execute_batch(query_measurement_units, data_measurement_units, "Unidades") and
            self._execute_batch(query_categories, data_categories, "Categorías")
        )
        return success_one

    #! ---------------------------------------------------------
    #! NIVEL 2: ENTIDADES PRINCIPALES (Usuarios y Proveedores)
    #! ---------------------------------------------------------
    def seed_level_two_users_and_providers(self):
        # 15. Proveedores
        query_providers = """INSERT INTO providers (provider_name, provider_rfc, provider_contact_name, provider_email, provider_phone, provider_website, address_id) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        data_providers = [('Office Depot', 'RFC123', 'Ventas Corp', 'ventas@od.com', '555-1234', 'www.od.com', 2), ('Ferretería El Clavo', 'RFC999', 'Don Pepe', 'pepe@clavo.com', '664-0000', 'N/A', 2)]

        # 16. Edificios
        query_buildings = """INSERT INTO buildings (building_name, building_emergency_contact, building_latitude, building_longitude, address_id) VALUES (%s,%s,%s,%s,%s)"""
        data_buildings = [('Torre SanSpace', 'Juan Velador', 10.0, 10.0, 1)]

        password_real_uno = Security.hash_password('1234')
        password_real_two = Security.hash_password('4321')
        password_real_three = Security.hash_password('1423')
        # 17. Usuarios
        query_users = """INSERT INTO users (user_name, user_last_name, user_email, user_password_hashed, user_cellphone, user_photo_url, user_employee_number, user_emergency_data, role_id, department_id, address_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        data_users = [('Admin', 'Supremo', 'admin@sanspace.com', password_real_uno, '664111', 'url', '001', '{}', 1, 1, 3),('Pedro', 'Pérez', 'pedro@sanspace.com', password_real_two, '664222', 'url', '002', '{}', 4, 3, 3),('Maria', 'López', 'maria@sanspace.com', password_real_three, '664333', 'url', '003', '{}', 3, 2, 3)]

        # 18. Tipos de sensores IOT
        query_iot_sensor_types = """INSERT INTO iot_sensor_types(iot_sensor_type_name, iot_sensor_type_datasheet_url, iot_protocol_id, measurement_unit_id) VALUES (%s,%s,%s,%s)"""
        data_iot_sensor_types = [('Sensor Puerta', 'url_pdf', 2, 2)]

        # 19. Modelos
        query_models = """INSERT INTO models (model_name, model_release_year, brand_id) VALUES (%s,%s,%s)"""
        data_models = [('Latitude 5420', 2021, 2), ('Martillo Goma', 2020, 3), ('Silla Aeron', 2019, 4)]

        success_two =(
            self._execute_batch(query_providers, data_providers, "Proveedores") and
            self._execute_batch(query_buildings, data_buildings, "Edificios") and
            self._execute_batch(query_users, data_users, "Usuarios") and
            self._execute_batch(query_iot_sensor_types, data_iot_sensor_types, "Tipos de sensores") and
            self._execute_batch(query_models, data_models, "Modelos")
        )
        return success_two

    #! ---------------------------------------------------------
    #! NIVEL 3: ESTRUCTURA (Pisos y Sensores)
    #! ---------------------------------------------------------
    def seed_level_three_sensors_and_floors(self):
        # 20. Pisos
        query_floors = """INSERT INTO floors (floor_name, floor_number, building_id) VALUES (%s,%s,%s)"""
        data_floors = [('Planta Baja', 0, 1), ('Nivel 1', 1, 1)]

        # 21. Sensores fisicos IOT
        query_iot_sensors = """INSERT INTO iot_sensors(iot_sensor_name, iot_sensor_serial, iot_sensor_ip, iot_sensor_mac, iot_sensor_api_endpoint, iot_sensor_type_id) VALUES (%s,%s,%s,%s,%s,%s)"""
        data_iot_sensors = [('Sensor Puerta Principal', 'SN-001', '192.168.1.50', 'AA:BB:CC', '/api/v1', 1)]

        success_three = (
            self._execute_batch(query_floors, data_floors, "Pisos") and
            self._execute_batch(query_iot_sensors, data_iot_sensors, "Sensores")
        )
        return success_three

    #! ---------------------------------------------------------
    #! NIVEL 4: CORE (Espacios y Activos)
    #! ---------------------------------------------------------
    def seed_level_four_spaces_and_actives(self):
        # 22. Tipos de reglas de los espacios
        query_space_type_rules = """INSERT INTO space_type_rules(space_type_id, rule_id) VALUES (%s,%s)"""
        data_space_type_rules = [(2, 3), (1, 1)]

        # 23. Espacios
        query_spaces = """INSERT INTO spaces (space_name, space_code, space_capacity, space_square_meters, space_has_access_control, space_type_id, floor_id, iot_sensor_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        data_spaces = [('Cuarto de Aseo', 'ASEO-01', 2, 5.0, False, 1, 1, None), ('Recepción', 'REC-01', 5, 20.0, True, 1, 1, 1)]

        # 24. Activos
        query_actives = """INSERT INTO actives (active_serial_number, active_cost, active_purchase_date, active_warranty_expiration, active_notes, active_barcode, active_lifespan_years, category_id, model_id, provider_id, active_status_id, space_id, user_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        data_actives = [('SN-DELL-001', 15000.0, '2023-01-01', '2025-01-01', 'Laptop Principal', 'BAR-001', 3, 1, 1, 1, 2, 2, 1), ('SN-ESC-999', 50.0, '2023-05-01', '2023-06-01', 'Escoba uso rudo', 'BAR-002', 1, 3, 2, 2, 2, 1, 2)]

        success_five = (
            self._execute_batch(query_space_type_rules, data_space_type_rules, "Reglas de espacios") and
            self._execute_batch(query_spaces, data_spaces, "Espacios") and
            self._execute_batch(query_actives, data_actives, "Activos")
        )
        return success_five

    #! ---------------------------------------------------------
    #! NIVEL 5: TRANSACCIONAL (Movimientos y Archivos)
    #! ---------------------------------------------------------
    def seed_level_five_movements_and_files(self):
        # 25. Movimientos de activos
        query_asset_movements = """INSERT INTO asset_movements(asset_movement_date, asset_movement_reason, active_id, asset_movement_from_space_id, asset_movement_to_space_id, user_id) VALUES (%s,%s,%s,%s,%s,%s)"""
        data_asset_movements = [('2023-10-25 10:00:00', 'Limpieza programada', 2, 1, 2, 2)]

        # 26. Archivos ASSET
        query_asset_files = """INSERT INTO asset_files(asset_file_path, asset_file_type, active_id) VALUES (%s,%s,%s)"""
        data_asset_files = [('/uploads/facturas/factura_dell.pdf', 'PDF', 1)]

        success_six = (
            self._execute_batch(query_asset_movements, data_asset_movements, "Movimientos") and
            self._execute_batch(query_asset_files, data_asset_files, "Archivos")
        )

        return success_six

#! Se crea en el archivo init_database.py
# if __name__ == '__main__':
#     seed = SanSpaceSeeder()
#     seed.run()