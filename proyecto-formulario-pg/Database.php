<?php
require_once 'config.php';

class Database {
    private static $connection = null;

    public static function getInstance(): PDO {
        if (self::$connection === null) {
            self::connect();
        }
        return self::$connection;
    }

    private static function connect(): void {
        try {
            // DSN para PostgreSQL
            // Nota: en PostgreSQL el charset no va siempre en el DSN, se puede ajustar en la BD
            $dsn = sprintf(
                'pgsql:host=%s;port=%d;dbname=%s',
                DB_HOST,
                DB_PORT,
                DB_NAME
            );

            self::$connection = new PDO(
                $dsn,
                DB_USER,
                DB_PASS,
                [
                    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
                    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                    PDO::ATTR_EMULATE_PREPARES   => false,
                ]
            );

            if (DEBUG_MODE) {
                error_log('✅ Conexión PostgreSQL OK: ' . DB_NAME);
            }
        } catch (PDOException $e) {
            error_log('❌ Error conexión PostgreSQL: ' . $e->getMessage());
            if (DEBUG_MODE) {
                throw $e;
            } else {
                die('Error de conexión a la base de datos.');
            }
        }
    }

    public static function prepare(string $sql): PDOStatement {
        return self::getInstance()->prepare($sql);
    }

    public static function getLastInsertId(): ?string {
        try {
            return self::getInstance()->lastInsertId();
        } catch (PDOException $e) {
            error_log('Error lastInsertId: ' . $e->getMessage());
            return null;
        }
    }
}