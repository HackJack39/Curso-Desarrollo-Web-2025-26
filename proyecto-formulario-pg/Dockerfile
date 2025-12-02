# Usamos la imagen base para PHP 8.3 con el servidor Apache
FROM php:8.3-apache

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /var/www/html

# Copia todos tus archivos de la carpeta local TRABAJO_004 al directorio web del contenedor
COPY . /var/www/html/

# 💡 AÑADIDO CLAVE: Instala el driver de PostgreSQL (libpq-dev y pdo_pgsql)
# También se incluyen comandos para limpiar la caché después de la instalación.
RUN apt-get update && apt-get install -y \
    libpq-dev \
    libzip-dev \
    && docker-php-ext-install pdo pdo_pgsql \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# El servidor Apache se inicia automáticamente.