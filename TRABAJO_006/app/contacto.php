<?php
session_start();

// Si se envía el formulario, validar y guardar mensaje en sesión (demo)
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name'] ?? '');
    $email = trim($_POST['email'] ?? '');
    $message = trim($_POST['message'] ?? '');

    if ($name === '' || $email === '' || $message === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $_SESSION['error'] = 'Por favor, rellena todos los campos con datos válidos.';
        header('Location: contacto.php');
        exit;
    }

    if (!isset($_SESSION['messages'])) {
        $_SESSION['messages'] = [];
    }
    $_SESSION['messages'][] = [
        'name' => $name,
        'email' => $email,
        'message' => $message,
        'created' => date('c')
    ];

    $_SESSION['success'] = 'Mensaje enviado correctamente. Gracias por contactar.';
    header('Location: contacto.php');
    exit;
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Contacto</title>
    <link rel="stylesheet" href="css/style.css?v=20251210">
</head>
<body>
<div class="container">
    <h2>Formulario de contacto</h2>

    <?php if (!empty($_SESSION['error'])): ?>
        <div class="message error"><?= htmlspecialchars($_SESSION['error']) ?></div>
        <?php unset($_SESSION['error']); ?>
    <?php endif; ?>

    <?php if (!empty($_SESSION['success'])): ?>
        <div class="message success"><?= htmlspecialchars($_SESSION['success']) ?></div>
        <?php unset($_SESSION['success']); ?>
    <?php endif; ?>

    <form action="contacto.php" method="post">
        <label for="name">Nombre:</label>
        <input id="name" name="name" type="text" required>
        <label for="email">Email:</label>
        <input id="email" name="email" type="email" required>
        <label for="message">Mensaje:</label>
        <textarea id="message" name="message" required></textarea>
        <button class="btn" type="submit">Enviar</button>
    </form>

    <p><a href="index.php">Volver</a></p>

    <!-- Mostrar mensajes guardados (solo demo) -->
    <?php if (!empty($_SESSION['messages'])): ?>
        <h3>Mensajes enviados (demo)</h3>
        <ul>
            <?php foreach ($_SESSION['messages'] as $m): ?>
                <li>
                    <strong><?= htmlspecialchars($m['name']) ?></strong>
                    (<?= htmlspecialchars($m['email']) ?>) en <?= htmlspecialchars($m['created']) ?>:
                    <div><?= nl2br(htmlspecialchars($m['message'])) ?></div>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>
</div>
</body>
</html>