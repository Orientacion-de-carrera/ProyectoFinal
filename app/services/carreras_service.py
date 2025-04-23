from app.models import Carrera

class CarrerasService:
    def __init__(self):
        # Catálogo de carreras
        self._carreras_catalogo = [
            Carrera(
                nombre="Licenciatura en Psicología",
                facultad="Ciencias de la Salud",
                descripcion="Forma profesionales capaces de comprender y abordar el comportamiento humano, aplicando técnicas de evaluación e intervención en contextos clínicos, educativos y organizacionales.",
                url="https://uip.edu.pa/licenciaturas/ciencias-de-la-salud-2/lic-en-psicologia/"
            ),
            Carrera(
                nombre="Licenciatura en Farmacia",
                facultad="Ciencias de la Salud",
                descripcion="Prepara expertos en medicamentos, enfocados en la investigación, producción, distribución y asesoramiento sobre el uso adecuado de productos farmacéuticos.",
                url="https://uip.edu.pa/licenciaturas/ciencias-de-la-salud-2/lic-en-farmacia/"
            ),
            Carrera(
                nombre="Licenciatura en Enfermería",
                facultad="Ciencias de la Salud",
                descripcion="Capacita profesionales en el cuidado integral de la salud, promoviendo la prevención, tratamiento y rehabilitación de pacientes en diversos entornos clínicos.",
                url="https://uip.edu.pa/licenciaturas/ciencias-de-la-salud-2/lic-en-enfermeria/"
            ),
            Carrera(
                nombre="Doctor en Medicina",
                facultad="Ciencias de la Salud",
                descripcion="Forma médicos generales con sólidos conocimientos científicos y éticos para diagnosticar, tratar y prevenir enfermedades, contribuyendo al bienestar de la sociedad.",
                url="https://uip.edu.pa/licenciaturas/ciencias-de-la-salud-2/doctor-en-medicina-3/"
            ),
            Carrera(
                nombre="Licenciatura en Nutrición y Dietética",
                facultad="Ciencias de la Salud",
                descripcion="Prepara especialistas en alimentación y nutrición, capaces de diseñar planes dietéticos que mejoren la salud y calidad de vida de las personas.",
                url="https://uip.edu.pa/licenciaturas/ciencias-de-la-salud-2/lic-en-nutricion-y-dietetica/"
            ),
            Carrera(
                nombre="Doctor en Cirugía Dental",
                facultad="Ciencias de la Salud",
                descripcion="Forma odontólogos competentes en la prevención, diagnóstico y tratamiento de enfermedades bucales, promoviendo la salud oral de la población.",
                url="https://uip.edu.pa/licenciaturas/ciencias-de-la-salud-2/doctor-en-cirugia-dental/"
            ),
            Carrera(
                nombre="Licenciatura en Administración de Negocios",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Desarrolla líderes empresariales con habilidades estratégicas para gestionar y optimizar organizaciones en un entorno globalizado.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-administracion-de-negocios-2/"
            ),
            Carrera(
                nombre="Licenciatura en Administración de Recursos Humanos",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Capacita profesionales en la gestión del talento humano, enfocándose en el desarrollo organizacional y bienestar laboral.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-administracion-de-recursos-humanos/"
            ),
            Carrera(
                nombre="Licenciatura en Contabilidad",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Forma contadores expertos en el análisis financiero y cumplimiento de normativas fiscales, esenciales para la toma de decisiones empresariales.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-contabilidad/"
            ),
            Carrera(
                nombre="Licenciatura en Contabilidad (A Distancia)",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Ofrece formación contable flexible, combinando teoría y práctica para adaptarse a las necesidades del estudiante moderno.",
                url="https://uip.edu.pa/modalidad-virtual/lic-en-contabilidad-a-distancia/"
            ),
            Carrera(
                nombre="Licenciatura en Comercio Internacional",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Prepara profesionales para gestionar operaciones comerciales globales, entendiendo tratados, logística y mercados internacionales.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-comercio-internacional/"
            ),
            Carrera(
                nombre="Licenciatura en Negocios Internacionales",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Forma expertos en estrategias empresariales globales, capaces de liderar en entornos multiculturales y dinámicos.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-negocios-internacionales/"
            ),
            Carrera(
                nombre="Licenciatura en Negocios Internacionales (A Distancia)",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Ofrece una formación integral en negocios globales, adaptada a la modalidad virtual para mayor flexibilidad.",
                url="https://uip.edu.pa/lic-en-negocios-internacionales-modalidad-a-distancia-virtual/"
            ),
            Carrera(
                nombre="Licenciatura en Comportamiento Organizacional y Desarrollo Humano",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Capacita en la comprensión y mejora del comportamiento humano dentro de las organizaciones, promoviendo entornos laborales saludables.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-comportamiento-organizacional-y-desarrollo-humano/"
            ),
            Carrera(
                nombre="Licenciatura en Administración de Empresas Turísticas",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Forma profesionales capaces de gestionar y promover destinos turísticos, impulsando el desarrollo sostenible del sector.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-administracion-de-empresas-turisticas/"
            ),
            Carrera(
                nombre="Lic. en Marketing Digital y Gerencia de Marca",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Prepara especialistas en estrategias de marketing digital y construcción de marcas sólidas en el entorno online.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/marketing-digital-y-gerencia-de-marca/"
            ),
            Carrera(
                nombre="Lic. en Marketing Digital y Gerencia de Marca - virtual",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Ofrece formación en marketing digital y branding, adaptada a la modalidad virtual para mayor accesibilidad.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/marketing-digital-y-gerencia-de-marca-virtual/"
            ),
        Carrera(
                nombre="Lic. en Administración Marítima y Portuaria",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Forma profesionales capaces de planear, organizar, dirigir y controlar procesos de operaciones en importación, exportación, trasbordo de mercancía y otros.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-administracion-maritima-y-portuaria/"
            ),
            Carrera(
                nombre="Lic. en Gestión Marítima con énfasis en Operaciones Portuarias",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Enfocada en la planificación de operaciones de buques, verificación de carga y control de tráfico marítimo.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-gestion-maritima-con-enfasis-en-operaciones-portuarias/"
            ),
            Carrera(
                nombre="Lic. en Gestión Marítima con énfasis en Operaciones Portuarias – Modalidad a Distancia Virtual",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Especialízate en operaciones portuarias desde cualquier lugar, con un enfoque en la planificación de operaciones de buques, verificación de carga y control de tráfico marítimo.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-gestion-maritima-con-enfasis-en-operaciones-portuarias-virtual/"
            ),
            Carrera(
                nombre="Lic. en Gestión Logística del Transporte Internacional de Mercancías",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Enfocada en la administración de los procesos asociados al transporte de mercancía por vía terrestre, aérea o marítima, garantizando el registro correcto de cada operación.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-ingenieria-de-transporte-y-logistica-2/"
            ),
            Carrera(
                nombre="Lic. en Gestión Marítima con énfasis en Transporte Multimodal",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Forma profesionales capaces de contribuir al desarrollo sostenido del país, a través del estudio y formación científica tecnológica basados en propuestas para la solución de situaciones de los problemas locales, nacionales e internacionales relativos al transporte marítimo y de movimiento de carga. ",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-gestion-maritima-con-enfasis-en-transporte-multimodal/"
            ),
            Carrera(
                nombre="Lic. en Administración de la Cadena de Suministro",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Forma profesionales capaces de diseñar, planificar, gestionar y controlar sistemas de suministro sostenible y los recursos logísticos de la empresa, a través de la planificación de compras, transporte, almacenaje y distribución de información, bienes y servicios.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-administracion-de-la-cadena-de-suministro/"
            ),
            Carrera(
                nombre="Lic. en Ingeniería de Transporte y Logística",
                facultad="Ciencias Administrativas, Marítima y Portuaria",
                descripcion="Forma a los futuros líderes de transporte marítimo, aéreo, terrestre y urbano, enfocados en procesos logísticos y gestión de carga comercial.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-ciencias-administrativas/lic-en-ingenieria-de-transporte-y-logistica/"
            ),
            Carrera(
                nombre="Lic. en Ing. de Redes y Datos con énfasis en Sis. Inalámbricos",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Enfocada en el diseño y administración de redes de comunicación y soluciones de conectividad de larga distancia, garantizando la transmisión efectiva de datos y la seguridad de la información.",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-ingenieria-de-redes-y-datos-con-enfasis-en-sistemas-inalambricos/"
            ),
            Carrera(
                nombre="Lic. en Ingeniería en Sistemas Computacionales",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Enfocada en el desarrollo de soluciones para sistemas de información y desarrollo de software, mediante el empleo de distintos lenguajes de programación y tecnologías actuales.",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-ingenieria-en-sistemas-computacionales/"
            ),
            Carrera(
                nombre="Lic. en Ingeniería en Sistemas Computacionales (VIRTUAL)",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Ofrece la misma formación que la modalidad presencial, enfocándose en el desarrollo de sistemas de información y software, utilizando lenguajes de programación y herramientas tecnológicas modernas.",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-ingenieria-en-sistemas-computacionales-virtual/"
            ),
            Carrera(
                nombre="Lic. en Sis. Comp. con énfasis en Desarrollo de Sis. Avanzados de Redes y Software",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Capacita para desarrollar e implementar software tanto para aplicaciones de escritorio como para aplicaciones web, administrar sistemas operativos y gestionar redes avanzadas.",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-sistemas-computacionales-con-enfasis-en-desarrollo-de-sistemas-avanzados-de-redes-y-software/"
            ),
            Carrera(
                nombre="Lic. en Sis. Comp. con énfasis en Desarrollo de Sis. Avanzados de Redes y Software (VIRTUAL)",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Ofrece formación en desarrollo e implementación de software para diversas plataformas, administración de sistemas operativos y gestión de redes, todo en modalidad virtual.",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-sistemas-computacionales-con-enfasis-en-desarrollo-de-sistemas-avanzados-de-redes-y-software-virtual/"
            ),
            Carrera(
                nombre="Lic. en Ingeniería Electrónica y de Comunicaciones",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Forma profesionales competentes para analizar, diseñar y desarrollar sistemas electrónicos analógicos, digitales y de comunicaciones fijas e inalámbricas. ",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-ingenieria-electronica-y-de-comunicaciones/"
            ),
            Carrera(
                nombre="Lic. en Ingeniería Industrial y de Sistemas",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Enfocada en la planificación, diseño, evaluación, mejoramiento e instalación de sistemas integrados por personas, materiales y equipos, utilizando técnicas y herramientas modernas.",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-ingenieria-industrial-y-de-sistemas/"
            ),
            Carrera(
                nombre="Lic. en Ingeniería Industrial con énfasis en Gestión de Calidad",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Enfocada en la planificación, diseño, evaluación, mejoramiento e instalación de sistemas integrados por personas, materiales y equipos, utilizando técnicas y herramientas modernas",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-ingenieria-industrial-con-enfasis-en-gestion-de-calidad/"
            ),
            Carrera(
                nombre="Lic. en Ingeniería Industrial con énfasis en Gestión de Operaciones",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Enfocada en la administración de los sistemas de producción de bienes y servicios, para garantizar la eficiencia operativa y maximizar la productividad de las organizaciones.",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-ingenieria-industrial-con-enfasis-en-gestion-de-operaciones/"
            ),
            Carrera(
                nombre="Licenciatura en Arquitectura",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Enfocada en el diseño y desarrollo de proyectos constructivos, desde su conceptualización hasta la ejecución, considerando aspectos técnicos, estéticos y funcionales.",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-arquitectura/"
            ),
            Carrera(
                nombre="Licenciatura en Arquitectura a Distancia",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Ofrece formación en diseño arquitectónico y planificación urbana, adaptada a una modalidad virtual que permite flexibilidad en el aprendizaje.",
                url="https://uip.edu.pa/modalidad-virtual/lic-en-arquitectura-a-distancia/"
            ),
            Carrera(
                nombre="Licenciatura en Periodismo",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Forma profesionales competentes en la búsqueda, recolección, redacción, interpretación y difusión de noticias, con un enfoque ético y crítico. ",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/licenciatura-en-periodismo/"
            ),
            Carrera(
                nombre="Licenciatura en Comunicación con énfasis en Producción Digital",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Se centra en la generación de propuestas gráficas y visuales para satisfacer las demandas comunicacionales de las empresas, utilizando herramientas digitales.",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-comunciacion-con-enfasis-en-produccion-digital/"
            ),
            Carrera(
                nombre="Licenciatura en Diseño de Interiores",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Enfocada en el diseño de espacios creativos y estéticos, tanto comerciales como residenciales, para brindar experiencias funcionales y armoniosas.",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-diseno-de-interiores/"
            ),
            Carrera(
                nombre="Licenciatura en Diseño de Interiores (VIRTUAL)",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Ofrece los mismos contenidos que la modalidad presencial, adaptados a una plataforma virtual que facilita el aprendizaje a distancia.",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-diseno-de-interiores-2/"
            ),
            Carrera(
                nombre="Licenciatura en Diseño Gráfico",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Enfocada en el desarrollo de proyectos de comunicación visual mediante técnicas de expresión gráfica y el dominio de software de diseño. ",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-diseno-grafico-original/"
            ),
            Carrera(
                nombre="Licenciatura en Diseño Gráfico con énfasis en Publicidad y Mercadeo",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Prepara profesionales capaces de diseñar y crear imágenes de comunicación visual, integrando estrategias de mercadeo y publicidad.",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-diseno-grafico-2/"
            ),
            Carrera(
                nombre="Licenciatura en Comunicación con énfasis en Producción de Radio y Televisión",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Se enfoca en el desarrollo de contenido visual y auditivo en distintos formatos y lenguajes, garantizando una comunicación efectiva al espectador.",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-comunicacion-con-enfasis-en-radio-y-television/"
            ),
            Carrera(
                nombre="Licenciatura en Publicidad y Mercadeo con énfasis en Imagen Corporativa",
                facultad="Ingeniería, Arquitectura y Diseño",
                descripcion="Enfocada en el desarrollo de estrategias de comunicación creativa para posicionar la identidad corporativa de las empresas frente a sus públicos. ",
                url="https://uip.edu.pa/licenciaturas/descripcion-ingenieria-y-sistemas/lic-en-publicidad-y-mercadeo-con-enfasis-en-imagen-corporativa/"
            ),
            Carrera(
                nombre="Licenciatura Internacional en Artes Culinarias",
                facultad="Hotelería, Gastronomía y Turismo",
                descripcion="Enfocada en la creación de platillos originales y creativos, estudiando su origen cultural y preservando técnicas y recetas de cocina tradicionales. ",
                url="https://www.uip.edu.pa/licenciaturas/facultad-de-gastronomia-hoteleria-y-turismo-2/lic-internacional-en-artes-culinarias/"
            ),
            Carrera(
                nombre="Licenciatura Internacional en Artes Culinarias (Semipresencial)",
                facultad="Hotelería, Gastronomía y Turismo",
                descripcion="Combina estudios teóricos con práctica profesional en alimentos, permitiendo una experiencia culinaria completa a través de una modalidad semipresencial.",
                url="https://uip.edu.pa/licenciaturas/facultad-de-gastronomia-hoteleria-y-turismo-2/lic-internacional-en-artes-culinarias-2/"
            ),
            Carrera(
                nombre="Licenciatura Internacional en Administración de Empresas Hoteleras",
                facultad="Hotelería, Gastronomía y Turismo",
                descripcion="Enfocada en la gerencia de las distintas áreas y servicios de la industria hotelera, garantizando la excelencia operativa y estándares de servicio internacional. ",
                url="https://uip.edu.pa/licenciaturas/facultad-de-gastronomia-hoteleria-y-turismo-2/lic-internacional-en-administracion-de-empresas-hoteleras/"
            ),
            Carrera(
                nombre="Licenciatura en Derecho y Ciencias Políticas",
                facultad="Derecho y Ciencias Políticas",
                descripcion="Enfocada en el diseño e implementación de estrategias legales para la solución de diversos problemas a nivel social y empresarial, con una sólida formación jurídica. ",
                url="https://www.uip.edu.pa/licenciaturas/derecho/lic-en-derecho-y-ciencias-politicas/"
            ),
            Carrera(
                nombre="Licenciatura en Criminología",
                facultad="Derecho y Ciencias Políticas",
                descripcion="Enfocada en el diseño de estrategias de prevención del acto criminal a nivel público y privado, mediante la investigación y análisis del comportamiento delictivo. ",
                url="https://www.uip.edu.pa/licenciaturas/derecho/lic-en-derecho-y-ciencias-politicas/"
            )
        ]

        # Mapeo de intereses a palabras clave para mejor detalle
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
        Retorna todas las carreras disponibles.

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

        #Expandir el interés a palabras clave relacionadas
        keywords = self._expandir_interes_a_keywords(interes_lower)

        #Buscar carreras que coincidan con las palabras clave
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

            # Si no hay coincidencias, usar las palabras originales
            if not keywords:
                keywords = palabras_interes

        # Eliminar duplicados manteniendo el orden
        keywords_sin_duplicados = []
        for kw in keywords:
            if kw not in keywords_sin_duplicados:
                keywords_sin_duplicados.append(kw)

        return keywords_sin_duplicados

