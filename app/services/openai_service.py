# app/services/openai_service.py
import json
import re
from openai import OpenAI
from config import Config
from app.models import Recomendacion

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def generar_recomendaciones(self, datos_usuario, carreras_disponibles):
        try:
            # Verificar que el usuario ha proporcionado suficientes datos
            if not datos_usuario.get('intereses') or not carreras_disponibles:
                raise ValueError("Datos insuficientes para generar recomendaciones adecuadas")

            carreras_info = ""
            for carrera in carreras_disponibles:
                carreras_info += f"Nombre: {carrera.nombre}\n"
                carreras_info += f"Facultad: {carrera.facultad}\n"
                carreras_info += f"Descripción: {carrera.descripcion}\n"
                if hasattr(carrera, 'perfil_profesional') and carrera.perfil_profesional:
                    carreras_info += f"Perfil profesional: {carrera.perfil_profesional}\n"
                carreras_info += "---\n"

            # Lista de nombres exactos para validación posterior
            nombres_exactos = [carrera.nombre for carrera in carreras_disponibles]
            nombres_exactos_lower = [nombre.lower() for nombre in nombres_exactos]

            prompt = f"""
Eres un consejero profesional experto en orientación vocacional para la Universidad Interamericana de Panamá (UIP).

Tu misión es analizar DETALLADAMENTE los intereses, habilidades y metas del estudiante para recomendar las carreras que mejor se adapten a su perfil.

Información del estudiante:
- Intereses: {datos_usuario.get('intereses', '')}
- Habilidades: {datos_usuario.get('habilidades', '')}
- Metas profesionales: {datos_usuario.get('metas', '')}
- Materia favorita: {datos_usuario.get('materia_favorita', '')}
- Valores personales: {datos_usuario.get('valores', '')}

Carreras disponibles en la UIP:
{carreras_info}

INSTRUCCIONES CRÍTICAS:
1. EVALÚA RIGUROSAMENTE la compatibilidad entre el perfil del estudiante y cada carrera.
2. NO recomiendes carreras que no se alineen claramente con los intereses y habilidades del estudiante.
3. PRIORIZA las carreras que mejor correspondan a los intereses específicos mencionados.
4. USA EXACTAMENTE los nombres de carreras proporcionados en la lista.
5. Si no hay suficiente compatibilidad con 3 carreras, recomienda solo las que realmente encajen.
6. Asegúrate de que las puntuaciones reflejen genuinamente el nivel de compatibilidad.
7. Cada explicación debe ser ÚNICA y destacar aspectos específicos de compatibilidad entre el perfil del estudiante y la carrera.

Formato de respuesta (JSON):
{{
  "recomendaciones": [
    {{
      "nombre_carrera": "Nombre exacto de la carrera",
      "puntuacion": número entre 1 y 100 basado en compatibilidad real,
      "explicacion": "Explicación detallada que conecte específicamente los intereses/habilidades del estudiante con esta carrera"
    }}
  ]
}}
"""

            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Eres un consejero experto en orientación vocacional con alta capacidad analítica. Tu objetivo es proporcionar recomendaciones precisas y personalizadas."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,  # Reducido para mayor consistencia
                max_tokens=1500
            )

            resultado = response.choices[0].message.content

            # Extraer el JSON, incluso si hay texto adicional
            json_match = re.search(r'\{[\s\S]*\}', resultado)
            if json_match:
                resultado_json = json_match.group(0)
                recomendaciones_json = json.loads(resultado_json)
            else:
                recomendaciones_json = json.loads(resultado)

            if "recomendaciones" not in recomendaciones_json:
                print("Formato inesperado de respuesta de OpenAI")
                return self._generar_recomendaciones_fallback(carreras_disponibles, datos_usuario)

            nombres_usados = set()
            recomendaciones = []

            # Validar cada recomendación para asegurar que sea relevante
            for rec in recomendaciones_json["recomendaciones"]:
                nombre = rec.get("nombre_carrera", "").strip()
                puntuacion = rec.get("puntuacion", 0)
                explicacion = rec.get("explicacion", "")

                # Validar que la carrera existe y no se ha recomendado antes
                nombre_lower = nombre.lower()
                if nombre_lower in nombres_usados:
                    continue

                # Buscar coincidencia exacta
                carrera_recomendada = None
                for i, nombre_exacto in enumerate(nombres_exactos_lower):
                    if nombre_lower == nombre_exacto:
                        carrera_recomendada = carreras_disponibles[i]
                        break

                # Si no hay coincidencia exacta, buscar coincidencia parcial
                if not carrera_recomendada:
                    for i, nombre_exacto in enumerate(nombres_exactos_lower):
                        if nombre_lower in nombre_exacto or nombre_exacto in nombre_lower:
                            carrera_recomendada = carreras_disponibles[i]
                            break

                # Si no se encontró la carrera, saltarla en lugar de usar una por defecto
                if not carrera_recomendada:
                    print(f"No se encontró coincidencia para '{nombre}', se omitirá esta recomendación")
                    continue

                # Validar que la explicación menciona los intereses del usuario
                intereses_usuario = datos_usuario.get('intereses', '').lower()
                if len(intereses_usuario) > 0 and not any(interes in explicacion.lower() for interes in intereses_usuario.split()):
                    # Mejorar la explicación para incluir intereses si la puntuación es alta
                    if puntuacion > 70:
                        explicacion += f" Esta carrera se alinea con tus intereses en {intereses_usuario}."

                nombres_usados.add(nombre_lower)

                recomendaciones.append(
                    Recomendacion(
                        carrera=carrera_recomendada,
                        puntuacion=puntuacion,
                        explicacion=explicacion
                    )
                )

            # Si no se generaron recomendaciones válidas, usar el fallback
            if not recomendaciones:
                print("No se generaron recomendaciones válidas, usando método de respaldo")
                return self._generar_recomendaciones_fallback(carreras_disponibles, datos_usuario)

            return recomendaciones

        except Exception as e:
            print(f"Error al generar recomendaciones con OpenAI: {str(e)}")
            return self._generar_recomendaciones_fallback(carreras_disponibles, datos_usuario)

    def _generar_recomendaciones_fallback(self, carreras_disponibles, datos_usuario):
        """Método de respaldo para generar recomendaciones cuando el método principal falla"""
        intereses = datos_usuario.get('intereses', '').lower()
        recomendaciones = []

        # Intentar encontrar carreras que coincidan con los intereses del usuario
        carreras_coincidentes = []
        for carrera in carreras_disponibles:
            # Buscar coincidencias entre intereses y descripción/nombre de carrera
            descripcion = getattr(carrera, 'descripcion', '').lower()
            if (intereses and (
                    any(interes in descripcion for interes in intereses.split()) or
                    any(interes in carrera.nombre.lower() for interes in intereses.split())
            )):
                carreras_coincidentes.append(carrera)

        # Si encontramos carreras coincidentes, usarlas
        carreras_a_recomendar = carreras_coincidentes[:3] if carreras_coincidentes else carreras_disponibles[:3]

        for i, carrera in enumerate(carreras_a_recomendar):
            puntuacion = 95 - (i * 10)

            # Crear una explicación más personalizada
            explicacion = f"Esta carrera se alinea con tu interés en {intereses if intereses else 'el área'} y "
            if i == 0:
                explicacion += f"ofrece excelentes oportunidades para desarrollar tus habilidades en {carrera.nombre}."
            elif i == 1:
                explicacion += f"te permitirá explorar temas relacionados con {carrera.facultad}."
            else:
                explicacion += f"representa una opción sólida basada en tu perfil profesional."

            recomendaciones.append(
                Recomendacion(
                    carrera=carrera,
                    puntuacion=puntuacion,
                    explicacion=explicacion
                )
            )

        return recomendaciones

