Creación de proyecto

docker-compose.yml
app /
    index.php
    api.php
    / config
        Database.php
CSS /
    styles.css
config
    / apache.conf


// Modificaciones en el archivo docker-compose.yml en el contenedor de PostgreSQL
// Usuario: admin
// Contraseña: 123456789
// Nombre de base de datos: formulario_db

// Creación del archivo Database.php
// Actualización de los campos user, pass y db a los introducidos en docker-compose.yml

// Creación del index.php y styles.css. El archivo de estilos se ubica en la carpeta CSS

// Creación de una carpeta config para depositar el archivo apache.conf

// Creación de la carpeta init-db y dentro el archivo init.sql