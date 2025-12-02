CREATE TABLE contactos (
id SERIAL PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
email VARCHAR(150) NOT NULL,
telefono VARCHAR(20),
asunto VARCHAR(150) NOT NULL,
mensaje TEXT NOT NULL,
fecha_creacion TIMESTAMP DEFAULT NOW(),
estado VARCHAR(20) DEFAULT 'pendiente'
);
