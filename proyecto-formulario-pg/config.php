<?php
// Tipo de BD: ahora pgsql
define('DB_DRIVER', 'pgsql');

// Servidor PostgreSQL: Usamos el nombre del servicio de Podman
define('DB_HOST', 'db_curso');

// Puerto por defecto PostgreSQL
define('DB_PORT', 5432);

// Nombre de la base de datos
define('DB_NAME', 'mi_base_de_datos'); 

// Usuario y contraseña de PostgreSQL
define('DB_USER', 'usuario_web');     
define('DB_PASS', 'su_contraseña_usuario'); 

// Codificación
define('DB_CHARSET', 'utf8');

// Zona horaria
date_default_timezone_set('Europe/Madrid');

// Modo debug
define('DEBUG_MODE', true);