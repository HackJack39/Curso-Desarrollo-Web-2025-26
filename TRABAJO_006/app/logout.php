<?php
// Destructor de sesión para cerrar sesión del usuario
session_start();

// Vaciamos datos y destruimos la sesión
$_SESSION = [];
session_destroy();

// Re-iniciamos la sesión rápidamente para pasar un mensaje de éxito
session_start();
$_SESSION['success'] = 'Has cerrado sesión correctamente.';
header('Location: index.php');
exit;