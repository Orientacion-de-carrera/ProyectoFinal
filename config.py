import os

class Config:
    # Configuración general de la aplicación
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-por-defecto'
    DEBUG = True

    # Configuración de OpenAI API
    OPENAI_API_KEY = "OPENAI_API_KEY"  


    # Configuración de archivos estáticos (si necesario)
    STATIC_FOLDER = 'static'
    TEMPLATE_FOLDER = 'templates'
