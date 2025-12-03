<?php
/**
 * Archivo: logout.php
 * Cierra la sesión del usuario
 */

// 1. Iniciar la sesión
session_start();

// 2. Destruir todas las variables de sesión
// Desestablece todas las variables de sesión
$_SESSION = array();

// Si se desea destruir la sesión completamente, borre también la cookie de sesión.
// Nota: ¡Esto destruirá la sesión, y no solo los datos de la sesión!
if (ini_get("session.use_cookies")) {
    $params = session_get_cookie_params();
    setcookie(session_name(), '', time() - 42000,
        $params["path"], $params["domain"],
        $params["secure"], $params["httponly"]
    );
}

// Finalmente, destruir la sesión
session_destroy();

// 3. Redirigir al usuario a la página de inicio de sesión
header('Location: login.php');
exit;
?>