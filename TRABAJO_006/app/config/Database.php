<?php
/**
 * Archivo: config/Database.php
 * Clase para gestionar conexión a PostgreSQL usando PDO
 */

class Database {
    private $host = 'db';
    private $db = 'formulario_db';
    private $user = 'admin';
    private $password = '123456789';
    private $port = '5432';
    
    private $pdo;

    // Constructor: establece la conexión
    public function __construct() {
        try {
            $dsn = "pgsql:host={$this->host};port={$this->port};dbname={$this->db}";
            
            $this->pdo = new PDO(
                $dsn,
                $this->user,
                $this->password,
                [
                    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                    PDO::ATTR_EMULATE_PREPARES => false,
                ]
            );
        } catch (PDOException $e) {
            die("Error de conexión a la base de datos: " . $e->getMessage());
        }
    }

    // Retorna la conexión PDO
    public function getConnection() {
        return $this->pdo;
    }

    // ----------------------------------------------------
    // MÉTODOS TRABAJO_005 (Formulario de Registros)
    // ----------------------------------------------------
    
    // Método para obtener todos los usuarios del formulario
    public function getUsuarios() {
        $sql = "SELECT * FROM usuarios ORDER BY fecha_registro DESC";
        $stmt = $this->pdo->query($sql);
        return $stmt->fetchAll();
    }

    // Método para insertar usuario del formulario
    public function crearUsuario($nombre, $email, $telefono, $mensaje) {
        $sql = "INSERT INTO usuarios (nombre, email, telefono, mensaje) 
                VALUES (:nombre, :email, :telefono, :mensaje)";
        
        $stmt = $this->pdo->prepare($sql);
        
        return $stmt->execute([
            ':nombre' => $nombre,
            ':email' => $email,
            ':telefono' => $telefono,
            ':mensaje' => $mensaje
        ]);
    }

    // Método para obtener cursos
    public function getCursos() {
        $sql = "SELECT * FROM cursos ORDER BY fecha_creacion DESC";
        $stmt = $this->pdo->query($sql);
        return $stmt->fetchAll();
    }


    // ----------------------------------------------------
    // MÉTODOS TRABAJO_006 (Autenticación y Logs)
    // ----------------------------------------------------

    /**
     * Obtiene un usuario del panel por username (para el proceso de Login).
     * Adaptado a la tabla 'users'.
     * @param string $username
     * @return array|false
     */
    public function getUsuarioPanel($username) {
        // Busca en la tabla 'users' por la columna 'username'
        $sql = "SELECT * FROM users WHERE username = :username"; 
        $stmt = $this->pdo->prepare($sql);
        $stmt->execute([':username' => $username]); 
        return $stmt->fetch();
    }

    /**
     * Registra un intento de acceso en la tabla logs_acceso.
     * @param string $username_intentado (Se registra en la columna 'email_intentado' de la BD)
     * @param bool $es_exitoso
     * @param string|null $ip
     * @param string|null $detalles
     * @return bool
     */
    public function registrarLogAcceso($username_intentado, $es_exitoso, $ip, $detalles = null) {
        $sql = "INSERT INTO logs_acceso (email_intentado, es_exitoso, direccion_ip, detalles) 
                VALUES (:username, :exito, :ip, :detalles)";
        
        $stmt = $this->pdo->prepare($sql);
        
        if ($ip === null) {
            $ip = $_SERVER['REMOTE_ADDR'] ?? 'N/A';
        }

        return $stmt->execute([
            ':username' => $username_intentado, 
            ':exito' => $es_exitoso,
            ':ip' => $ip,
            ':detalles' => $detalles
        ]);
    }
}
?>