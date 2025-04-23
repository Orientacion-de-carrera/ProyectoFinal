class Carrera:
    def __init__(self, nombre, facultad, descripcion, url, perfil_profesional=None, plan_estudio=None):
        self.nombre = nombre
        self.facultad = facultad
        self.descripcion = descripcion
        self.url = url
        self.perfil_profesional = perfil_profesional
        self.plan_estudio = plan_estudio

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'facultad': self.facultad,
            'descripcion': self.descripcion,
            'url': self.url,
            'perfil_profesional': self.perfil_profesional,
            'plan_estudio': self.plan_estudio
        }

class Recomendacion:
    def __init__(self, carrera, puntuacion, explicacion):
        self.carrera = carrera
        self.puntuacion = puntuacion
        self.explicacion = explicacion

    def to_dict(self):
        return {
            'carrera': self.carrera.to_dict() if hasattr(self.carrera, 'to_dict') else self.carrera,
            'puntuacion': self.puntuacion,
            'explicacion': self.explicacion
        }