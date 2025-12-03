-- Tabla para formulario de contacto/registros
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20),
    mensaje TEXT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla para ejemplo adicional: cursos
CREATE TABLE IF NOT EXISTS cursos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    duracion_horas INT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ----------------------------------------------------
-- TABLAS PARA TRABAJO_006: ACCESO Y LOGS
-- ----------------------------------------------------

-- 1. Tabla para el registro de usuarios del panel de acceso (Autenticación - Tabla 'users')
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL, -- Contraseña cifrada (PHP password_hash)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Tabla para registrar logs de intentos de acceso (Seguridad)
CREATE TABLE IF NOT EXISTS logs_acceso (
    id SERIAL PRIMARY KEY,
    email_intentado VARCHAR(100) NOT NULL, -- Usaremos esta columna para guardar el 'username' intentado
    fecha_intento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    es_exitoso BOOLEAN NOT NULL,
    direccion_ip VARCHAR(45),
    detalles TEXT
);

-- Insertar datos de ejemplo
INSERT INTO cursos (nombre, descripcion, duracion_horas) VALUES
    ('PHP Avanzado', 'Curso completo de PHP con patrones de diseño', 40),
    ('PostgreSQL Mastery', 'Domina las bases de datos relacionales', 35),
    ('Docker for Developers', 'Containerización profesional de aplicaciones', 30)
ON CONFLICT DO NOTHING;

-- Usuario administrador INICIAL (contraseña: admin123)
INSERT INTO users (username, password_hash) 
    VALUES(
        'admin',
        '$2y$10$aOWNlaGS7w5v/Uz4JQ8vlez.LzzeHBvoal7dGRNfjwkyASKEf6LMK'  
    )
ON CONFLICT (username) DO NOTHING;