"""
Servicio que gestiona el catálogo de carreras universitarias disponibles.

Este módulo proporciona funcionalidades para acceder y filtrar el catálogo
de carreras de la Universidad Interamericana de Panamá (UIP), permitiendo
búsquedas por nombre o por intereses del usuario.
"""

from app.models import Carrera

class CarrerasService:
    """
    Servicio para gestionar el catálogo de carreras universitarias.
    
    Proporciona métodos para:
    - Acceder a todas las carreras disponibles
    - Buscar carreras por nombre específico
    - Buscar carreras relacionadas con intereses del usuario
    
    Mantiene un catálogo interno de objetos Carrera y un mapeo de intereses
    a palabras clave relacionadas para mejorar las búsquedas.
    """
    
    def __init__(self):
        """
        Inicializa el servicio con un catálogo predefinido de carreras y un
        mapeo de intereses a palabras clave.
        """
        # Catálogo de carreras - contiene información sobre todas las carreras disponibles
        # Cada carrera incluye: nombre, facultad, descripción y URL
        self._carreras_catalogo = [
            Carrera(
                nombre="Licenciatura en Psicología",
                facultad="Ciencias de la Salud",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/ciencias-de-la-salud-2/lic-en-psicologia/"
            ),
            Carrera(
                nombre="Licenciatura en Farmacia",
                facultad="Ciencias de la Salud",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/ciencias-de-la-salud-2/lic-en-farmacia/"
            ),
            Carrera(
                nombre="Licenciatura en Enfermería",
                facultad="Ciencias de la Salud",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/ciencias-de-la-salud-2/lic-en-enfermeria/"
            ),
            Carrera(
                nombre="Doctor en Medicina",
                facultad="Ciencias de la Salud",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/ciencias-de-la-salud-2/doctor-en-medicina-3/"
            ),
            Carrera(
                nombre="Licenciatura en Nutrición y Dietética",
                facultad="Ciencias de la Salud",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/ciencias-de-la-salud-2/lic-en-nutricion-y-dietetica/"
            ),
            Carrera(
                nombre="Doctor en Cirugía Dental",
                facultad="Ciencias de la Salud",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/ciencias-de-la-salud-2/doctor-en-cirugia-dental/"
            ),
            Carrera(
                nombre="Licenciatura en Administración de Negocios",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-administracion-de-negocios-2/"
            ),
            Carrera(
                nombre="Licenciatura en Administración de Recursos Humanos",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-administracion-de-recursos-humanos/"
            ),
            Carrera(
                nombre="Licenciatura en Contabilidad",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-contabilidad/"
            ),
            Carrera(
                nombre="Licenciatura en Contabilidad (A Distancia)",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/modalidad-virtual/lic-en-contabilidad-a-distancia/"
            ),
            Carrera(
                nombre="Licenciatura en Comercio Internacional",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-comercio-internacional/"
            ),
            Carrera(
                nombre="Licenciatura en Negocios Internacionales",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-negocios-internacionales/"
            ),
            Carrera(
                nombre="Licenciatura en Negocios Internacionales (A Distancia)",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/lic-en-negocios-internacionales-modalidad-a-distancia-virtual/"
            ),
            Carrera(
                nombre="Licenciatura en Comportamiento Organizacional y Desarrollo Humano",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-comportamiento-organizacional-y-desarrollo-humano/"
            ),
            Carrera(
                nombre="Licenciatura en Administración de Empresas Turísticas",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-administracion-de-empresas-turisticas/"
            ),
            Carrera(
                nombre="Lic. en Marketing Digital y Gerencia de Marca",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/marketing-digital-y-gerencia-de-marca/"
            ),
            Carrera(
                nombre="Lic. en Marketing Digital y Gerencia de Marca - virtual",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/marketing-digital-y-gerencia-de-marca-virtual/"
            ),
            Carrera(
                nombre="Lic. en Administración Marítima y Portuaria",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-administracion-maritima-y-portuaria/"
            ),
            Carrera(
                nombre="Lic. en Gestión Marítima con énfasis en Operaciones Portuarias",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-gestion-maritima-con-enfasis-en-operaciones-portuarias/"
            ),
            Carrera(
                nombre="Lic. en Gestión Marítima con énfasis en Operaciones Portuarias – Modalidad a Distancia Virtual",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-gestion-maritima-con-enfasis-en-operaciones-portuarias-virtual/"
            ),
            Carrera(
                nombre="Lic. en Gestión Logística del Transporte Internacional de Mercancías",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-ingenieria-de-transporte-y-logistica-2/"
            ),
            Carrera(
                nombre="Lic. en Gestión Marítima con énfasis en Transporte Multimodal",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-gestion-maritima-con-enfasis-en-transporte-multimodal/"
            ),
            Carrera(
                nombre="Lic. en Administración de la Cadena de Suministro",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-administracion-de-la-cadena-de-suministro/"
            ),
            Carrera(
                nombre="Lic. en Ingeniería de Transporte y Logística",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-ingenieria-de-transporte-y-logistica/"
            ),
            Carrera(
                nombre="Lic. en Ing. de Redes y Datos con énfasis en Sis. Inalámbricos",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-ingenieria-de-redes-y-datos-con-enfasis-en-sistemas-inalambricos/"
            ),
            Carrera(
                nombre="Lic. en Ingeniería en Sistemas Computacionales",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-ingenieria-en-sistemas-computacionales/"
            ),
            Carrera(
                nombre="Lic. en Ingeniería en Sistemas Computacionales (VIRTUAL)",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-ingenieria-en-sistemas-computacionales-virtual/"
            ),
            Carrera(
                nombre="Lic. en Sis. Comp. con énfasis en Desarrollo de Sis. Avanzados de Redes y Software",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-sistemas-computacionales-con-enfasis-en-desarrollo-de-sistemas-avanzados-de-redes-y-software/"
            ),
            Carrera(
                nombre="Lic. en Sis. Comp. con énfasis en Desarrollo de Sis. Avanzados de Redes y Software (VIRTUAL)",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-sistemas-computacionales-con-enfasis-en-desarrollo-de-sistemas-avanzados-de-redes-y-software-virtual/"
            ),
            Carrera(
                nombre="Lic. en Ingeniería Electrónica y de Comunicaciones",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-ingenieria-electronica-y-de-comunicaciones/"
            ),
            Carrera(
                nombre="Lic. en Ingeniería Industrial y de Sistemas",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-ingenieria-industrial-y-de-sistemas/"
            ),
            Carrera(
                nombre="Lic. en Ingeniería Industrial con énfasis en Gestión de Calidad",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-ingenieria-industrial-con-enfasis-en-gestion-de-calidad/"
            ),
            Carrera(
                nombre="Lic. en Ingeniería Industrial con énfasis en Gestión de Operaciones",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-ingenieria-industrial-con-enfasis-en-gestion-de-operaciones/"
            ),
            Carrera(
                nombre="Licenciatura en Arquitectura",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-arquitectura/"
            ),
            Carrera(
                nombre="Licenciatura en Arquitectura a Distancia",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/modalidad-virtual/lic-en-arquitectura-a-distancia/"
            ),
            Carrera(
                nombre="Licenciatura en Periodismo",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/licenciatura-en-periodismo/"
            ),
            Carrera(
                nombre="Licenciatura en Comunicación con énfasis en Producción Digital",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-comunciacion-con-enfasis-en-produccion-digital/"
            ),
            Carrera(
                nombre="Licenciatura en Diseño de Interiores",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-diseno-de-interiores/"
            ),
            Carrera(
                nombre="Licenciatura en Diseño de Interiores (VIRTUAL)",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-diseno-de-interiores-2/"
            ),
            Carrera(
                nombre="Licenciatura en Diseño Gráfico",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-diseno-grafico-original/"
            ),
            Carrera(
                nombre="Licenciatura en Diseño Gráfico con énfasis en Publicidad y Mercadeo",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-diseno-grafico-2/"
            ),
            Carrera(
                nombre="Licenciatura en Comunicación con énfasis en Producción de Radio y Televisión",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-comunicacion-con-enfasis-en-radio-y-television/"
            ),
            Carrera(
                nombre="Licenciatura en Publicidad y Mercadeo con énfasis en Imagen Corporativa",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-publicidad-y-mercadeo-con-enfasis-en-imagen-corporativa/"
            ),
            Carrera(
                nombre="Licenciatura Internacional en Artes Culinarias",
                facultad="Hotelería, Gastronomía y Turismo",
                descripcion="Descripción no disponible",
                url="https://www.uip.edu.pa/licenciaturas/facultad-de-gastronomia-hoteleria-y-turismo-2/lic-internacional-en-artes-culinarias/"
            ),
            Carrera(
                nombre="Licenciatura Internacional en Artes Culinarias (Semipresencial)",
                facultad="Hotelería, Gastronomía y Turismo",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-gastronomia-hoteleria-y-turismo-2/lic-internacional-en-artes-culinarias-2/"
            ),
            Carrera(
                nombre="Licenciatura Internacional en Administración de Empresas Hoteleras",
                facultad="Hotelería, Gastronomía y Turismo",
                descripcion="Descripción no disponible",
                url="https://uip.edu.pa/licenciaturas/facultad-de-gastronomia-hoteleria-y-turismo-2/lic-internacional-en-administracion-de-empresas-hoteleras/"
            ),
            Carrera(
                nombre="Licenciatura en Derecho y Ciencias Políticas",
                facultad="Derecho y Ciencias Políticas",
                descripcion="Descripción no disponible",
                url="https://www.uip.edu.pa/licenciaturas/derecho/lic-en-derecho-y-ciencias-politicas/"
            ),
            Carrera(
                nombre="Licenciatura en Criminología",
                facultad="Derecho y Ciencias Políticas",
                descripcion="Descripción no disponible",
                url="https://www.uip.edu.pa/licenciaturas/derecho/lic-en-derecho-y-ciencias-politicas/"
            )
        ]

        # Mapeo de intereses a palabras clave relacionadas para mejorar las búsquedas
        self._mapeo_intereses = {
           "cocinar": ["culinarias", "gastronomía", "chef", "alimentación", "comida", "restaurantes", "nutrición"],
            "hotel": ["hotelera", "turismo", "hospitalidad", "recepción", "gestión hotelera"],
            "viajes": ["turismo", "hotelería", "viajar", "aerolínea", "cruceros"],
            "programación": ["sistemas", "software", "ingeniería", "algoritmos", "código", "desarrollo", "inteligencia artificial"],
            "computadora": ["sistemas", "tecnología", "hardware", "informática", "datos", "redes"],
            "diseño": ["diseño", "creativo", "interiores", "gráfico", "moda", "ilustración", "digital"],
            "arte": ["arte", "creativo", "audiovisual", "pintura", "escultura", "expresión", "fotografía"],
            "negocios": ["negocios", "comercio", "empresa", "marketing", "ventas", "finanzas", "economía"],
            "empresa": ["administración", "gerencia", "negocios", "dirección", "estrategia"],
            "comunicación": ["comunicación", "periodismo", "publicidad", "medios", "marketing digital", "relaciones públicas"],
            "derecho": ["derecho", "criminología", "leyes", "justicia", "tribunal", "jurídico"],
            "salud": ["salud", "medicina", "enfermería", "nutrición", "hospital", "clínica", "pacientes"],
            "psicología": ["psicología", "comportamiento", "mente", "emociones", "terapia", "salud mental"],
            "educación": ["educación", "enseñanza", "docencia", "pedagogía", "maestro", "formación"],
            "construcción": ["arquitectura", "ingeniería civil", "edificación", "estructuras", "planos", "urbanismo"],
            "industria": ["ingeniería industrial", "logística", "producción", "procesos", "calidad", "gestión de operaciones"]
        }

    def obtener_carreras(self):
        """
        Retorna todas las carreras disponibles en el catálogo.

        Returns:
            list: Lista de todas las carreras
        """
        return self._carreras_catalogo

    def buscar_carrera_por_nombre(self, nombre):
        """
        Busca una carrera específica por nombre.

        Args:
            nombre (str): Nombre de la carrera a buscar

        Returns:
            Carrera: Objeto carrera encontrado o None si no se encuentra
        """
        nombre_lower = nombre.lower()
        for carrera in self._carreras_catalogo:
            if nombre_lower in carrera.nombre.lower():
                return carrera
        return None

    def buscar_carreras_por_interes(self, interes):
        """
        Busca carreras relacionadas con el interés del usuario.

        Args:
            interes (str): El interés del usuario

        Returns:
            list: Lista de objetos Carrera relacionados con el interés
        """
        if not interes:
            return []

        interes_lower = interes.lower()
        carreras_relacionadas = []

        # Paso 1: Expandir el interés a palabras clave relacionadas
        keywords = self._expandir_interes_a_keywords(interes_lower)

        # Paso 2: Buscar carreras que coincidan con las palabras clave
        for carrera in self._carreras_catalogo:
            for keyword in keywords:
                # Verificar si la palabra clave está en el nombre, descripción o facultad
                if (keyword in carrera.nombre.lower() or
                        keyword in carrera.facultad.lower() or
                        (carrera.descripcion and keyword in carrera.descripcion.lower())):
                    if carrera not in carreras_relacionadas:
                        carreras_relacionadas.append(carrera)
                        break  # Una vez encontrada, pasamos a la siguiente carrera

        return carreras_relacionadas

    def _expandir_interes_a_keywords(self, interes):
        """
        Expande un interés a palabras clave relacionadas.

        Args:
            interes (str): El interés del usuario

        Returns:
            list: Lista de palabras clave relacionadas
        """
        keywords = []

        # Verificar si el interés exacto está en nuestro mapeo
        for key, values in self._mapeo_intereses.items():
            if key in interes:
                keywords.extend(values)

        # Si no se encontraron keywords en el mapeo, usar palabras del interés original
        if not keywords:
            # Dividir el interés en palabras individuales
            palabras_interes = interes.split()

            # Revisar si alguna palabra coincide con nuestras categorías
            for palabra in palabras_interes:
                for key, values in self._mapeo_intereses.items():
                    if palabra == key or palabra in values:
                        keywords.extend(values)

            # Si aún no hay coincidencias, usar las palabras originales
            if not keywords:
                keywords = palabras_interes

        # Eliminar duplicados manteniendo el orden
        keywords_sin_duplicados = []
        for kw in keywords:
            if kw not in keywords_sin_duplicados:
                keywords_sin_duplicados.append(kw)

        return keywords_sin_duplicados

        return keywords_sin_duplicados

