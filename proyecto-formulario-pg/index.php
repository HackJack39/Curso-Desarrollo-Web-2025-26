<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Formulario de Contacto</title>
</head>

<body>
    <div class="contenedor">
        <h1>📧 Formulario de Contacto</h1>

        <?php
        // ************************************************
        // Bloque para mostrar el mensaje de éxito (AÑADIDO)
        // ************************************************
        if (isset($_GET['success']) && $_GET['success'] == 1) {
            echo '<p style="color: green; font-weight: bold; padding: 10px; border: 1px solid green; background-color: #e6ffe6; border-radius: 5px;">✅ ¡Mensaje enviado y guardado correctamente en PostgreSQL!</p>';
        }
        ?>

        <form action="procesar.php" method="POST">
            <div class="grupo-formulario">
                <label for="nombre">Nombre completo *</label>
                <input type="text" id="nombre" name="nombre" required placeholder="Juan García" minlength="3"
                    maxlength="50">
            </div>

            <div class="grupo-formulario">
                <label for="email">Correo electrónico *</label>
                <input type="email" id="email" name="email" required placeholder="tu@email.com">
            </div>

            <div class="grupo-formulario">
                <label for="telefono">Teléfono (opcional)</label>
                <input type="tel" id="telefono" name="telefono" placeholder="+34 612 345 678" pattern="[0-9+\s\-]{7,}">
            </div>

            <div class="grupo-formulario">
                <label for="asunto">Asunto *</label>
                <input type="text" id="asunto" name="asunto" required placeholder="Consulta sobre..." minlength="5"
                    maxlength="100">
            </div>

            <div class="grupo-formulario">
                <label for="mensaje">Mensaje *</label>
                <textarea id="mensaje" name="mensaje" required placeholder="Escribe tu mensaje aquí..." minlength="10"
                    maxlength="1000"></textarea>
            </div>

            <p class="campo-requerido">* Campos obligatorios</p>

            <div class="botones">
                <button type="submit" class="btn-enviar">Enviar</button>
                <button type="reset" class="btn-limpiar">Limpiar</button>
            </div>
        </form>
    </div>
</body>

</html>