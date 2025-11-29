-- =======================
-- 1. Tabla roles
-- =======================
CREATE TABLE IF NOT EXISTS roles(
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(50) UNIQUE NOT NULL,
    role_description TEXT,
    role_level INT NOT NULL CHECK (role_level >= 0),
    -- Auditori
    role_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    role_updated_at TIMESTAMP,
    role_is_active BOOLEAN DEFAULT TRUE
);
-- =======================
-- 2. Tabla users
-- =======================
CREATE TABLE IF NOT EXISTS users(
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    user_last_name VARCHAR(100) NOT NULL,
    user_email VARCHAR(255) UNIQUE NOT NULL,
    user_password_hashed VARCHAR(255) NOT NULL,
    user_cellphone VARCHAR(20) NOT NULL,
    user_photo VARCHAR(255),
    -- Auditoria
    user_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    user_updated_at TIMESTAMP,
    user_is_active BOOLEAN DEFAULT TRUE,
    -- Relación con la tabla roles
    role_id INT NOT NULL REFERENCES roles(role_id)
);
-- =======================
-- 3. Tabla buildings
-- =======================
CREATE TABLE IF NOT EXISTS buildings(
    building_id SERIAL PRIMARY KEY,
    building_name VARCHAR(150) NOT NULL,
    building_address VARCHAR(255) NOT NULL,
    building_city VARCHAR(100) NOT NULL,
    building_state VARCHAR(100) NOT NULL,
    building_postal_code VARCHAR(10) NOT NULL,
    building_emergency_contact VARCHAR(20) NOT NULL,
    -- Auditoria
    building_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    building_updated_at TIMESTAMP,
    building_is_active BOOLEAN DEFAULT TRUE
);

-- =======================
-- 4. Tabla pisos
-- =======================
CREATE TABLE IF NOT EXISTS floors(
    floor_id SERIAL PRIMARY KEY,
    floor_name VARCHAR (150) NOT NULL,
    floor_number INT,
    -- Auditoria
    floor_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    floor_updated_at TIMESTAMP,
    floor_is_active BOOLEAN DEFAULT TRUE,
    -- Relación con la tabla edificios
    building_id INT NOT NULL REFERENCES buildings(building_id)
);
-- =======================
-- 5. Tabla tipos_espacios
-- =======================
CREATE TABLE IF NOT EXISTS space_types(
    space_type_id SERIAL PRIMARY KEY,
    space_type_name VARCHAR(50) NOT NULL,
    space_type_description TEXT,
    -- Auditoria
    space_type_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    space_type_updated_at TIMESTAMP,
    space_type_is_active BOOLEAN DEFAULT TRUE
);
-- =======================
-- 6. Tabla espacios
-- =======================
CREATE TABLE IF NOT EXISTS spaces(
    space_id SERIAL PRIMARY KEY,
    space_name VARCHAR(100) NOT NULL,
    space_code VARCHAR(50) UNIQUE NOT NULL,
    space_capacity INT NOT NULL,
    space_square_meters NUMERIC(10, 2) NOT NULL,
    -- Auditoria
    space_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    space_updated_at TIMESTAMP,
    space_is_active BOOLEAN DEFAULT TRUE,
    -- Relacionado con la tabla pisos
    floor_id INT NOT NULL REFERENCES floors(floor_id),
    -- Relacionado con la tabla tipos_espacios
    space_type_id INT NOT NULL REFERENCES space_types(space_type_id)
);
-- =======================
-- 7. Tabla categorias
-- =======================
CREATE TABLE IF NOT EXISTS categories(
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(150) NOT NULL,
    -- Auto relación (categoria padre)
    category_parent_id INT REFERENCES categories(category_id),
    -- Auditoria
    category_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    category_updated_at TIMESTAMP,
    category_is_active BOOLEAN DEFAULT TRUE
);
-- =======================
-- 8. Tabla proveedores
-- =======================
CREATE TABLE IF NOT EXISTS providers(
    provider_id SERIAL PRIMARY KEY,
    provider_name VARCHAR(100) NOT NULL,
    provider_color VARCHAR(50) NOT NULL,
    -- Auditoria
    provider_created_at TIMESTAMP DEFAULT NOW() NOT NULL,
    provider_updated_at TIMESTAMP,
    provider_is_active BOOLEAN DEFAULT TRUE
);