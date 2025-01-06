# db.py
import psycopg2

def connect_db():
    # Configura la conexión a tu base de datos
    conn = psycopg2.connect(
        dbname="world_travel_db",  # Nombre de tu base de datos
        user="postgres",           # Tu usuario de PostgreSQL
        password="1234",   # Tu contraseña de PostgreSQL
        host="localhost",           # Si estás en producción, usa la IP de tu servidor
        port="5432"                 # Puerto de PostgreSQL (5432 por defecto)
    )
    return conn
