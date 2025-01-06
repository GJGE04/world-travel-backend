# db.py
import os
from dotenv import load_dotenv
import psycopg2
from urllib.parse import urlparse

load_dotenv()  # Cargar las variables de entorno del archivo .env


def connect_db():
    
    # Obtener la URL de la base de datos desde la variable de entorno
    database_url = os.getenv('DATABASE_URL')
    print(f"Conectando ........")
    print(f"Database URL: {database_url}")
    
    # Depurar todas las variables de entorno
    print("Variables de entorno cargadas:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")
    
    if database_url is None:
        raise ValueError("La variable de entorno DATABASE_URL no está definida")
        
    print(f"Conectando a la base de datos: {database_url}")

    # Analizar la URL de la base de datos usando urllib.parse
    result = urlparse(database_url)
    
    # Verificar si el path contiene el nombre de la base de datos correctamente
    dbname = result.path[1:] if result.path.startswith('/') else result.path
    
    # Conectar a la base de datos usando los valores obtenidos de la URL
    conn = psycopg2.connect(
        dbname=dbname,  # El nombre de la base de datos
        user=result.username,     # El usuario de la base de datos
        password=result.password, # La contraseña de la base de datos
        host=result.hostname,     # El host de la base de datos
        port=result.port          # El puerto de la base de datos
    )
    return conn
