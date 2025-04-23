from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash, session
from app.services.carreras_service import CarrerasService
from app.services.openai_service import OpenAIService

# Crear blueprint
main_bp = Blueprint('main', __name__)

# Servicios
carreras_service = CarrerasService()
openai_service = OpenAIService()

@main_bp.route('/')
def index():
    """Ruta principal que muestra el formulario de orientación vocacional"""
    return render_template('index.html')

@main_bp.route('/carreras')
def listar_carreras():
    """Ruta que muestra todas las carreras disponibles"""
    carreras = carreras_service.obtener_carreras()
    return render_template('carreras.html', carreras=carreras)

@main_bp.route('/carrera/<string:nombre>')
def detalle_carrera(nombre):
    """Ruta que muestra el detalle de una carrera específica"""
    carrera = carreras_service.buscar_carrera_por_nombre(nombre)
    if not carrera:
        flash('Carrera no encontrada', 'error')
        return redirect(url_for('main.listar_carreras'))

    return render_template('detalle_carrera.html', carrera=carrera)

@main_bp.route('/recomendar', methods=['POST'])
def recomendar():
    """Procesa el formulario y genera recomendaciones de carreras"""
    # Obtener datos del formulario
    datos_usuario = {
        'intereses': request.form.get('intereses', ''),
        'habilidades': request.form.get('habilidades', ''),
        'metas': request.form.get('metas', ''),
        'materia_favorita': request.form.get('materia_favorita', ''),
        'valores': request.form.get('valores', '')
    }

    # Filtrar carreras según los intereses del usuario
    interes_usuario = datos_usuario.get('intereses', '')
    carreras = carreras_service.buscar_carreras_por_interes(interes_usuario)

    # Generar recomendaciones
    recomendaciones = openai_service.generar_recomendaciones(datos_usuario, carreras)

    # Guardar en sesión para mostrar en la página de resultados
    session['datos_usuario'] = datos_usuario
    session['recomendaciones'] = [r.to_dict() for r in recomendaciones]

    return redirect(url_for('main.resultados'))

@main_bp.route('/resultados')
def resultados():
    """Muestra los resultados de la recomendación"""
    datos_usuario = session.get('datos_usuario', {})
    recomendaciones_dict = session.get('recomendaciones', [])

    # Convertir las recomendaciones de vuelta a objetos
    from app.models import Recomendacion, Carrera
    recomendaciones = []

    for rec_dict in recomendaciones_dict:
        carrera_dict = rec_dict.get('carrera', {})
        carrera = Carrera(
            nombre=carrera_dict.get('nombre', ''),
            facultad=carrera_dict.get('facultad', ''),
            descripcion=carrera_dict.get('descripcion', ''),
            url=carrera_dict.get('url', ''),
            perfil_profesional=carrera_dict.get('perfil_profesional', '')
        )

        recomendacion = Recomendacion(
            carrera=carrera,
            puntuacion=rec_dict.get('puntuacion', 0),
            explicacion=rec_dict.get('explicacion', '')
        )

        recomendaciones.append(recomendacion)

    return render_template('resultados.html',
                           datos_usuario=datos_usuario,
                           recomendaciones=recomendaciones)
