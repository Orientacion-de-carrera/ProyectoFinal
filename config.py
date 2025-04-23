import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Configuración general de la aplicación
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True

    # Configuración de OpenAI API
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')  # Ahora carga

