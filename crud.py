# crud.py
from db import connect_db
from psycopg2 import sql

# Crear un destino
def create_travel_destination(name, country, description):
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = sql.SQL("INSERT INTO destinations (name, country, description) VALUES (%s, %s, %s) RETURNING id")
        cur.execute(query, (name, country, description))
        destination_id = cur.fetchone()[0]  # Devuelve el ID del destino insertado
        conn.commit()
        cur.close()
        conn.close()
        return destination_id
        
    except Exception as e:
        print(f"Error creating destination: {e}")
        return None

# Leer todos los destinos
def get_destinations():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT id, name, country, description FROM destinations;")
        destinations = cur.fetchall()  # Devuelve todas las filas de la tabla
        cur.close()
        conn.close()
        
        return [{"id": destination[0], "name": destination[1], "country": destination[2], "description": destination[3]} for destination in destinations]
    except Exception as e:
        print(f"Error retrieving destinations: {e}")
        return []  # En caso de error, devolvemos una lista vacía

# Actualizar un destino
def update_destination(id, name, country, description):
    try:
        conn = connect_db()
        cur = conn.cursor()
        
        cur.execute("SELECT id FROM destinations WHERE id = %s;", (id,))
        destination = cur.fetchone()
    
        if destination:
            query = """
                UPDATE destinations
                SET name = %s, country = %s, description = %s
                WHERE id = %s
                RETURNING id, name, country, description;
            """
            cur.execute(query, (name, country, description, id))
            updated_destination = cur.fetchone()

            conn.commit()
            cur.close()
            conn.close()

            return updated_destination  
        else:
            conn.close()
            return None  
    except Exception as e:
        print(f"Error updating destination: {e}")
        return None
    
    

# Eliminar un destino
def delete_destination(id):
    try:
        conn = connect_db()
        cur = conn.cursor()
        
        cur.execute("SELECT id FROM destinations WHERE id = %s;", (id,))
        destination = cur.fetchone()
        
        if destination:
            query = sql.SQL("DELETE FROM destinations WHERE id = %s")
            cur.execute(query, (id,))
            conn.commit()
            cur.close()
            conn.close()
            return True  
        else:
            conn.close()
            return False
            
    except Exception as e:
        print(f"Error deleting destination: {e}")
        return False
