--
-- 1. Países
--
CREATE TABLE IF NOT EXISTS countries(
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR(100) UNIQUE,
    country_code VARCHAR(3),
    country_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    country_updated_at TIMESTAMP NULL,
    country_is_active BOOLEAN DEFAULT TRUE
);

--
-- 2. Estados/Provincias
--
CREATE TABLE IF NOT EXISTS states(
    state_id SERIAL PRIMARY KEY,
    state_name VARCHAR(100),
    state_code VARCHAR(10),
    state_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    state_updated_at TIMESTAMP NULL,
    state_is_active BOOLEAN DEFAULT TRUE
);

--
-- 3. Ciudades
--
CREATE TABLE IF NOT EXISTS cities(
    city_id SERIAL PRIMARY KEY,
    city_name VARCHAR(100),
    city_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    city_updated_at TIMESTAMP NULL,
    city_is_active BOOLEAN DEFAULT TRUE
);

--
-- 4. Codigos postales
--
CREATE TABLE IF NOT EXISTS postal_codes(
    postal_code_id SERIAL PRIMARY KEY,
    postal_code_number VARCHAR(10) UNIQUE,
    postal_code_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    postal_code_updated_at TIMESTAMP NULL,
    postal_code_is_active BOOLEAN DEFAULT TRUE
);

--
-- 5. Direcciones fisicas
--
CREATE TABLE IF NOT EXISTS addresses(
    address_id SERIAL PRIMARY KEY,
    address_street VARCHAR(255),
    address_exterior_num VARCHAR(20),
    address_interior_num VARCHAR(20) NULL,
    address_colonia VARCHAR(100),
    address_references TEXT,
    address_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    address_updated_at TIMESTAMP NULL,
    address_is_active BOOLEAN DEFAULT TRUE
);

--
-- 6. Reglas de uso
--
CREATE TABLE IF NOT EXISTS rules(
    rule_id SERIAL PRIMARY KEY,
    rule_name VARCHAR(100),
    rule_description TEXT,
    rule_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    rule_updated_at TIMESTAMP NULL,
    rule_is_active BOOLEAN DEFAULT TRUE
);

--
-- 7. Roles
--
CREATE TABLE IF NOT EXISTS roles(
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(50) UNIQUE,
    role_description TEXT,
    role_level INT,
    role_permissions JSON,
    role_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    role_updated_at TIMESTAMP NULL,
    role_is_active BOOLEAN DEFAULT TRUE
);

--
-- 8. Departamentos
--
CREATE TABLE IF NOT EXISTS departments(
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR (100),
    department_manager_name VARCHAR(150),
    department_notes TEXT,
    department_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    department_updated_at TIMESTAMP NULL,
    department_is_active BOOLEAN DEFAULT TRUE
);

--
-- 9. Marcas
--
CREATE TABLE IF NOT EXISTS brands(
    brand_id SERIAL PRIMARY KEY,
    brand_name VARCHAR(100),
    brand_website VARCHAR(255),
    brand_support_phone VARCHAR(20),
    brand_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    brand_updated_at TIMESTAMP NULL,
    brand_is_active BOOLEAN DEFAULT TRUE
);

--
-- 10. Estado del activo
--
CREATE TABLE IF NOT EXISTS active_statuses(
    active_status_id SERIAL PRIMARY KEY,
    active_status_name VARCHAR(50),
    active_status_color_hex VARCHAR(7),
    active_status_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    active_status_updated_at TIMESTAMP NULL,
    active_status_is_active BOOLEAN DEFAULT TRUE
);

--
-- 11. Tipos de espacio
--
CREATE TABLE IF NOT EXISTS space_types(
    space_type_id SERIAL PRIMARY KEY,
    space_type_name VARCHAR (50),
    space_type_description TEXT,
    space_type_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    space_type_updated_at TIMESTAMP NULL,
    space_type_is_active BOOLEAN DEFAULT TRUE
);

--
-- 12. Protocolos de IOT
--
CREATE TABLE IF NOT EXISTS iot_protocols(
    iot_protocol_id SERIAL PRIMARY KEY,
    iot_protocol_name VARCHAR(50) UNIQUE,
    iot_protocol_description TEXT,
    iot_protocol_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    iot_protocol_updated_at TIMESTAMP NULL,
    iot_protocol_is_active BOOLEAN DEFAULT TRUE
);

--
-- 13. Unidades de medida
--
CREATE TABLE IF NOT EXISTS measurement_units(
    measurement_unit_id SERIAL PRIMARY KEY,
    measurement_unit_name VARCHAR(50),
    measurement_unit_symbol VARCHAR(10),
    measurement_unit_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    measurement_unit_updated_at TIMESTAMP NULL,
    measurement_unit_is_active BOOLEAN DEFAULT TRUE
);

--
-- 14. Categorias
--
CREATE TABLE IF NOT EXISTS categories(
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100),
    category_code VARCHAR(20),
    category_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    category_updated_at TIMESTAMP NULL,
    category_is_active BOOLEAN DEFAULT TRUE,
    category_parent_id INT NULL REFERENCES categories(category_id)
);

--
-- 15. Proveedores
--
CREATE TABLE IF NOT EXISTS providers(
    provider_id SERIAL PRIMARY KEY,
    provider_name VARCHAR(150),
    provider_rfc VARCHAR(20),
    provider_contact_name VARCHAR(150),
    provider_email VARCHAR(150),
    provider_phone VARCHAR(20),
    provider_website VARCHAR(255),
    provider_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    provider_updated_at TIMESTAMP NULL,
    provider_is_active BOOLEAN DEFAULT TRUE,
    -- Tabla relacionada: addresses
    address_id INT NOT NULL REFERENCES addresses(address_id)
);

--
-- 16. Edificios
--
CREATE TABLE IF NOT EXISTS buildings(
    building_id SERIAL PRIMARY KEY,
    building_name VARCHAR(150),
    building_emergency_contact VARCHAR(20),
    building_latitude DECIMAL(10, 8),
    building_longitude DECIMAL(11, 8),
    building_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    building_updated_at TIMESTAMP NULL,
    building_is_active BOOLEAN DEFAULT TRUE,
    -- Tabla relacionada: addresses
    address_id INT NOT NULL REFERENCES addresses(address_id)
);

--
-- 17. Usuarios
--
CREATE TABLE IF NOT EXISTS users(
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(100),
    user_last_name VARCHAR(100),
    user_email VARCHAR(150) UNIQUE,
    user_password_hashed VARCHAR(255),
    user_cellphone VARCHAR(20),
    user_photo_url VARCHAR(255),
    user_employee_number VARCHAR(50),
    user_emergency_data JSON,
    user_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    user_updated_at TIMESTAMP NULL,
    user_is_active BOOLEAN DEFAULT TRUE,
    -- Tabla relacionada: roles
    role_id INT NOT NULL REFERENCES roles(role_id),
    -- Tabla relacionada: departments
    department_id INT NOT NULL REFERENCES departments(department_id),
    -- Tabla relacionada: addresses
    address_id INT NOT NULL REFERENCES addresses(address_id)
);

--
-- 18. Tipos de sensores IOT
--
CREATE TABLE IF NOT EXISTS iot_sensor_types(
    iot_sensor_type_id SERIAL PRIMARY KEY,
    iot_sensor_type_name VARCHAR(100),
    iot_sensor_type_datasheet_url VARCHAR(255),
    iot_sensor_type_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    iot_sensor_type_updated_at TIMESTAMP NULL,
    iot_sensor_type_is_active BOOLEAN DEFAULT TRUE,
    -- Tabla relacionada: protocols
    iot_protocol_id INT NOT NULL REFERENCES iot_protocols(iot_protocol_id),
    -- Tabla relacionada: unidades
    measurement_unit_id INT NOT NULL REFERENCES measurement_units(measurement_unit_id)
);

--
-- 19. Modelos
--
CREATE TABLE IF NOT EXISTS models(
    model_id SERIAL PRIMARY KEY,
    model_name VARCHAR(100),
    model_release_year INT,
    model_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    model_updated_at TIMESTAMP NULL,
    model_is_active BOOLEAN DEFAULT TRUE,
    -- Tabla relacionada: brands
    brand_id INT NOT NULL REFERENCES brands(brand_id)
);

--
-- 20. Pisos
--
CREATE TABLE IF NOT EXISTS floors(
    floor_id SERIAL PRIMARY KEY,
    floor_name VARCHAR(50),
    floor_number INT,
    floor_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    floor_updated_at TIMESTAMP NULL,
    floor_is_active BOOLEAN DEFAULT TRUE,
    -- Tabla relacionada: buildings
    building_id INT NOT NULL REFERENCES buildings(building_id)
);

--
-- 21. Sensores IOT
--
CREATE TABLE IF NOT EXISTS iot_sensors(
    iot_sensor_id SERIAL PRIMARY KEY,
    iot_sensor_name VARCHAR(100),
    iot_sensor_serial VARCHAR(100) UNIQUE,
    iot_sensor_ip VARCHAR(45),
    iot_sensor_mac VARCHAR(17),
    iot_sensor_api_endpoint VARCHAR(255),
    iot_sensor_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    iot_sensor_updated_at TIMESTAMP NULL,
    iot_sensor_is_active BOOLEAN DEFAULT TRUE,
    -- Tabla relacionada: iot_sensor_types
    iot_sensor_type_id INT NOT NULL REFERENCES iot_sensor_types(iot_sensor_type_id)
);

--
-- 22. Tipo de espacio y sus reglas -> Intermedia
--
CREATE TABLE IF NOT EXISTS space_type_rules(
    space_type_rule_id SERIAL PRIMARY KEY,
    space_type_rule_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    space_type_rule_updated_at TIMESTAMP NULL,
    space_type_rule_is_active BOOLEAN DEFAULT TRUE,
    -- Tabla relacionada: space_types
    space_type_id INT NOT NULL REFERENCES space_types(space_type_id),
    -- Tabla relacionada: rules
    rule_id INT NOT NULL REFERENCES rules(rule_id)
);

--
-- 23. Espacios
--
CREATE TABLE IF NOT EXISTS spaces(
    space_id SERIAL PRIMARY KEY,
    space_name VARCHAR(100),
    space_code VARCHAR(20) UNIQUE,
    space_capacity INT,
    space_square_meters DECIMAL(10, 2),
    space_has_access_control BOOLEAN DEFAULT TRUE,
    space_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    space_updated_at TIMESTAMP NULL,
    space_is_active BOOLEAN DEFAULT TRUE,
    -- Tabla relacionada: space_types
    space_type_id INT NOT NULL REFERENCES space_types(space_type_id),
    -- Tabla relacionada: floors
    floor_id INT NOT NULL REFERENCES floors(floor_id),
    -- Tabla relacionada: iot_sensors
    iot_sensor_id INT NULL REFERENCES iot_sensors(iot_sensor_id)
);

--
-- 24. Activos
--
CREATE TABLE IF NOT EXISTS actives(
    active_id SERIAL PRIMARY KEY,
    active_serial_number VARCHAR(100) UNIQUE,
    active_cost DECIMAL(15, 2),
    active_purchase_date DATE,
    active_warranty_expiration DATE,
    active_notes TEXT,
    active_barcode VARCHAR(100),
    active_lifespan_years INT,
    active_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    active_updated_at TIMESTAMP NULL,
    active_is_active BOOLEAN DEFAULT TRUE,
    -- Tabla relacionada: categories
    category_id INT NOT NULL REFERENCES categories(category_id),
    -- Tabla relacionada: models
    model_id INT NOT NULL REFERENCES models(model_id),
    -- Tabla relacionada: providers
    provider_id INT NOT NULL REFERENCES providers(provider_id),
    -- Tabla relacionada: active_statuses
    active_status_id INT NOT NULL REFERENCES active_statuses(active_status_id),
    -- Tabla relacionada: spaces
    space_id INT NOT NULL REFERENCES spaces(space_id),
    -- Tabla relacionada: users
    user_id INT REFERENCES users(user_id)
);

--
-- 25. Movimientos de activos
--
CREATE TABLE IF NOT EXISTS asset_movements(
    asset_movement_id SERIAL PRIMARY KEY,
    asset_movement_date TIMESTAMP,
    asset_movement_reason TEXT,
    asset_movement_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    asset_movement_updated_at TIMESTAMP NULL,
    asset_movement_is_active BOOLEAN DEFAULT TRUE,
    -- Tabla relacionada: actives
    active_id INT NOT NULL REFERENCES actives(active_id),
    -- Tabla relacionada: spaces
    asset_movement_from_space_id INT REFERENCES spaces(space_id),
    -- Tabla relacionada: spaces
    asset_movement_to_space_id INT REFERENCES spaces(space_id),
    -- Tabla relacionada: users
    user_id INT NOT NULL REFERENCES users(user_id)
);

--
-- 26. Archivos ASSET
--
CREATE TABLE IF NOT EXISTS asset_files(
    asset_file_id SERIAL PRIMARY KEY,
    asset_file_path VARCHAR(255),
    asset_file_type VARCHAR(10),
    asset_file_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    asset_file_updated_at TIMESTAMP NULL,
    asset_file_is_active BOOLEAN DEFAULT TRUE,
    -- Tabla relacionada: actives
    active_id INT NOT NULL REFERENCES actives(active_id)
);