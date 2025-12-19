from flask import (
    Flask, 
    render_template, 
    request, 
    redirect, 
    url_for, 
    send_file, 
    flash
) 

# Importamos las funciones de base de datos desde tu archivo de la PARTE 1
from repaso_008 import (
    init_db,
    cursos_df,
    listar_alumnos_por_curso_df,
    estadisticas_por_curso_df,
    buscar_alumno_df,
    exportar_informe_csv
) 

# Configuración de la aplicación
# Si tu carpeta se llama 'statics', lo indicamos aquí:
app = Flask(__name__, static_folder='static') 

# Clave secreta necesaria para usar la función flash()
app.secret_key = "clave_super_secreta_para_sesiones" 

# --- INICIALIZACIÓN DE LA BASE DE DATOS ---
# Esta es la corrección para Flask 3.0+ (sustituye a before_first_request)
with app.app_context():
    init_db() 

# --- RUTAS DE LA APLICACIÓN ---

@app.route("/")
def index():
    """Ruta principal que muestra el formulario y los cursos disponibles"""
    cursos = cursos_df().to_dict(orient="records") 
    return render_template("index.html", cursos=cursos) 

@app.route("/alumnos", methods=["POST"])
def alumnos_por_curso():
    """Muestra la lista de alumnos filtrada por el curso seleccionado"""
    id_curso = request.form.get("id_curso") 
    df = listar_alumnos_por_curso_df(id_curso) 
    alumnos = df.to_dict(orient="records") 
    cursos = cursos_df().to_dict(orient="records") 
    return render_template("index.html", cursos=cursos, alumnos=alumnos) 

@app.route("/estadisticas")
def estadisticas():
    """Muestra cálculos de medias, máximos y mínimos"""
    df = estadisticas_por_curso_df() 
    stats = df.to_dict(orient="records")
    cursos = cursos_df().to_dict(orient="records")
    return render_template("index.html", cursos=cursos, stats=stats) 

@app.route("/buscar", methods=["POST"])
def buscar():
    """Busca alumnos por coincidencia de nombre"""
    nombre = request.form.get("nombre") 
    df = buscar_alumno_df(nombre) 
    resultados = df.to_dict(orient="records") 
    
    if not resultados:
        flash(f"No se encontraron alumnos con el nombre: {nombre}") 
        
    cursos = cursos_df().to_dict(orient="records") 
    return render_template("index.html", cursos=cursos, resultados=resultados) 

@app.route("/exportar")
def exportar():
    """Genera el archivo CSV y fuerza la descarga en el navegador"""
    exportar_informe_csv() 
    # El archivo se genera en la raíz del proyecto
    return send_file("informe_alumnos_cursos.csv", as_attachment=True) 

# --- EJECUCIÓN ---
if __name__ == "__main__":
    # debug=True permite ver errores en el navegador y recarga cambios automáticamente
    app.run(debug=True)