<?php
/**
 * Archivo: login.php
 * Panel de acceso para usuarios del sistema (TRABAJO_006)
 */

// Iniciar sesión para manejar la autenticación
session_start();

// Si el usuario ya está logueado, lo redirigimos directamente al panel principal.
if (isset($_SESSION['logged_in']) && $_SESSION['logged_in'] === true) {
    header('Location: index.php');
    exit;
}

// Incluir clase de base de datos (ruta correcta desde 'app/')
require_once 'config/Database.php';

$mensaje_error = '';
$db = new Database();

// Obtener la IP del cliente para registrarla en los logs (seguridad)
$ip_cliente = $_SERVER['REMOTE_ADDR'] ?? 'N/A';
$intento_username = '';

// Procesar el formulario de inicio de sesión
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username'] ?? '');
    $password = $_POST['password'] ?? '';
    $intento_username = $username; // Guardamos el username intentado para el log

    // 1. Validaciones básicas
    if (empty($username) || empty($password)) {
        $mensaje_error = "Por favor, introduce el usuario y la contraseña.";
    } else {
        // 2. Obtener el usuario de la BD (tabla 'users')
        $usuario = $db->getUsuarioPanel($username);

        if ($usuario) {
            // 3. Verificar la contraseña hasheada
            if (password_verify($password, $usuario['password_hash'])) {
                
                // --- INICIO DE SESIÓN EXITOSO ---
                
                // Registrar el log de acceso exitoso
                $db->registrarLogAcceso($username, true, $ip_cliente, 'Acceso exitoso');
                
                // Establecer variables de sesión
                $_SESSION['logged_in'] = true;
                $_SESSION['user_id'] = $usuario['id'];
                $_SESSION['username'] = $usuario['username'];
                
                // Redirigir al panel principal
                header('Location: index.php');
                exit;

            } else {
                // Contraseña incorrecta
                $mensaje_error = "Usuario o contraseña incorrectos.";
                // Registrar log de fallo
                $db->registrarLogAcceso($username, false, $ip_cliente, 'Contraseña incorrecta');
            }
        } else {
            // Usuario no encontrado
            $mensaje_error = "Usuario o contraseña incorrectos.";
            // Registrar log de fallo (registramos el username intentado)
            $db->registrarLogAcceso($username, false, $ip_cliente, 'Usuario no encontrado');
        }
    }
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Acceso al Panel</title>
    <link rel="stylesheet" href="CSS/styles.css"> <style>
        /* Estilos específicos para el formulario de login */
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f4f7f6;
        }
        .login-card {
            width: 100%;
            max-width: 400px;
            padding: 40px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            background-color: #fff;
            text-align: center;
        }
        .login-card h2 {
            margin-bottom: 25px;
            color: #4a5568;
        }
        .login-card .form-group {
            text-align: left;
        }
    </style>
</head>
<body>
    <div class="login-card">
        <h2>🔒 Iniciar Sesión</h2>

        <?php if (!empty($mensaje_error)): ?>
            <div class="alert alert-error"><?= htmlspecialchars($mensaje_error) ?></div>
        <?php endif; ?>

        <form method="POST" action="login.php">
            <div class="form-group">
                <label for="username">Usuario</label>
                <input 
                    type="text" 
                    id="username" 
                    name="username" 
                    value="<?= htmlspecialchars($intento_username) ?>"
                    required
                >
            </div>

            <div class="form-group">
                <label for="password">Contraseña</label>
                <input 
                    type="password" 
                    id="password" 
                    name="password" 
                    required
                >
            </div>

            <button type="submit" class="btn" style="width: 100%; margin-top: 20px;">Acceder al Panel</button>
        </form>
    </div>
</body>
</html>