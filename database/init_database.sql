-- Crear el usuario dueño del proyecto (No usar postgres root por seguridad)
CREATE USER sanspace_dev WITH PASSWORD 'sanspace_dev';

ALTER USER sanspace_dev WITH LOGIN;
ALTER USER sanspace_dev WITH CREATEDB;

-- Crear la base de datos
CREATE DATABASE sanspace_db OWNER sanspace_dev;

-- Esto se crea automaticamente en src/scripts/init_database.py
-- Solamente es para ver lo que se hizo ahí