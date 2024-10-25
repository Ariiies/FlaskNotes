import mysql.connector
from mysql.connector import Error
from models.entities.user import User

# Connecting to the database with exception handling
def get_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            port='3306',
            user="root",
            password="mypassword",
            database="reviews"
        )
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Helper function to handle read queries
def execute_query(query, params=None):
    try:
        connection = get_connection()
        if connection:
            with connection.cursor(buffered=True) as cursor:
                cursor.execute(query, params)
                result = cursor.fetchall()
            connection.close()
            return result
    except Error as e:
        print(f"Error ejecutando la consulta: {e}")
        return []

# Auxiliary function to handle DB modifications (INSERT, UPDATE, DELETE)
def execute_update(query, params=None):
    try:
        connection = get_connection()
        if connection:
            with connection.cursor(buffered=True) as cursor:
                cursor.execute(query, params)
                connection.commit()
            connection.close()
    except Error as e:
        print(f"Error ejecutando la modificación: {e}")

# search by title
def search_by_title(titulo):
    query = "SELECT * FROM review WHERE titulo = %s"
    return execute_query(query, (titulo,))

# Show all notes
def show_all():
    query = "SELECT * FROM review"
    return execute_query(query)

# Show a note by ID
def show_note(id):
    query = "SELECT * FROM review WHERE id = %s"
    return execute_query(query, (id,))

# Execute a order
def execute_order(instruccion):
    return execute_query(instruccion)

# Crete a new note
def create_note(id, titulo, contenido):
    query = "INSERT INTO review (id_usuario, titulo, contenido, fecha) VALUES (%s, %s, %s, NOW())"
    execute_update(query, (id, titulo, contenido))

# Edit a note
def edit_note(id, titulo, contenido):
    query = "UPDATE review SET titulo = %s, contenido = %s WHERE id = %s"
    execute_update(query, (titulo, contenido, id))

# Delete note by ID
def delete_note(id):
    query = "DELETE FROM review WHERE id = %s"
    execute_update(query, (id,))

# Swho notes with selected fields
def show_all4():
    query = "SELECT id, titulo, contenido, fecha FROM review"
    return execute_query(query)
