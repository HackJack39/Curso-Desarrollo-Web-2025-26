<?php
// procesar.php

// 1. Incluir la clase Database
require_once 'Database.php';

// Comprobar que la petición viene por POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: index.php');
    exit;
}

// 2. Recoger y sanear TODOS los datos del formulario (deben coincidir con la tabla contactos)
$nombre   = trim($_POST['nombre']   ?? '');
$email    = trim($_POST['email']    ?? '');
$telefono = trim($_POST['telefono'] ?? '');
$asunto   = trim($_POST['asunto']   ?? '');
$mensaje  = trim($_POST['mensaje']  ?? '');

// 3. Validaciones básicas
$errores = [];

// Validación de campos obligatorios según la tabla
if ($nombre === '') {
    $errores[] = 'El nombre es obligatorio.';
}
if ($email === '') {
    $errores[] = 'El email es obligatorio.';
} elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errores[] = 'El email no tiene un formato válido.';
}
if ($asunto === '') {
    $errores[] = 'El asunto es obligatorio.';
}
if ($mensaje === '') {
    $errores[] = 'El mensaje es obligatorio.';
}

// Si hay errores, los mostramos de forma sencilla
if (!empty($errores)) {
    echo '<h3>Se han producido errores:</h3>';
    echo '<ul>';
    foreach ($errores as $error) {
        echo '<li>' . htmlspecialchars($error, ENT_QUOTES, 'UTF-8') . '</li>';
    }
    echo '</ul>';
    echo '<p><a href="index.php">Volver al formulario</a></p>';
    exit;
}

// --- ZONA DE CONEXIÓN Y CONSULTAS (CAMBIADA PARA POSTGRESQL/PDO) ---

try {
    // 4. Conectar con la base de datos a través del Singleton Database
    // No necesitamos una variable $conexion, Database::prepare() gestiona la conexión.

    // 5. Insertar el nuevo contacto usando consulta preparada
    $sqlInsert = 'INSERT INTO contactos (nombre, email, telefono, asunto, mensaje) VALUES (?, ?, ?, ?, ?)';
    
    // Usamos el método prepare de nuestra clase Database
    $stmt = Database::prepare($sqlInsert);

    // Ejecutamos la consulta con los parámetros
    $resultado = $stmt->execute([
        $nombre,
        $email,
        $telefono,
        $asunto,
        $mensaje
    ]);

    if ($resultado) {
        // Registro correcto: redirigir a index.php con mensaje
        // Opcional: obtener el ID insertado
        // $id_insertado = Database::getLastInsertId(); 
        
        header('Location: index.php?success=1');
        exit;
    } else {
        // En un entorno de producción, esto debería manejarse con logs más detallados.
        echo 'Error al registrar el contacto.';
        exit;
    }

} catch (PDOException $e) {
    // Manejo de errores de conexión o consulta de PDO
    // En DEBUG_MODE, la clase Database ya lanza o registra el error.
    error_log('Error en procesar.php durante la inserción: ' . $e->getMessage());
    die('Ocurrió un error en el servidor. Inténtalo más tarde.');
}

// --- FIN ZONA DE CONEXIÓN Y CONSULTAS ---

?>