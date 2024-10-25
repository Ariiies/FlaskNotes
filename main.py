from flask import Flask, render_template, url_for, request, redirect, flash, session
from datetime import datetime
from config import config
from flask_session import Session
from tools.search import forSearch as fs
from tools.order import busquedaordenada as bus
from tools.datapage import datapage as dp
from models.usermodel import ModelUser  # Models
import DataBaseManager as dbm           # Database manager
from models.entities.user import User   # Entities
import logging

# logging configuration
logging.basicConfig(level=logging.INFO)

# Initializes the app
App = Flask(__name__)
App.secret_key = "clave_secreta_flask"

App.config["SESSION_PERMANENT"] = False
App.config["SESSION_TYPE"] = "filesystem"
Session(App)

# Context processor for the date
@App.context_processor
def Date_Now():
    return {'now': datetime.utcnow()}

# Main rute
@App.route('/', methods=['GET', 'POST'])
def index():
    logging.info(f"Usuario en sesión: {session.get('name')}")

    return render_template('index.html')

# Auxiliar function to process the search
def procesar_busqueda(buscar, pagina):
    resu = dbm.show_all4()
    datos = bus(buscar, resu)
    size = len(datos)
    contador, subcontador = dp(size, pagina)
    return datos, size, contador, subcontador

# search route
@App.route('/buscar')
@App.route('/buscar/<texto>', methods=['GET', 'POST'])
def buscar(buscar=""):
    return render_template('buscar.html', buscar=buscar)

# Redirigir a la página de resultados
# Redirect to the results page
@App.route('/page/<buscar>', methods=['GET', 'POST'])
def page(buscar="No results"):
    try:
        if request.args:
            buscar = request.args.get("buscar", "")
            logging.info(f"Búsqueda recibida: {buscar}")
            return redirect(url_for('results', buscar=buscar, pagina=1))
    except KeyError as e:
        logging.error(f"Key Error: {e}")
    return redirect(url_for('buscar'))

# Show results
@App.route('/results/<buscar>/<pagina>', methods=['GET', 'POST'])
def results(buscar="sin resultado", pagina=1):
    datos = []  # Iitilizes in a default value
    size = 0    # Initializes default size
    try:
        # Validate if 'page' is convertible to integer, if not, assign 1
        if not pagina.isdigit():
            pagina = 1
        else:
            pagina = int(pagina)
        if request.args:
            buscar = request.args.get("buscar", "")
            resu = dbm.show_all4()
            datos = bus(buscar, resu)
            size = len(datos)
            if pagina == 0:
                pagina = 1
            contador, subcontador = dp(size, pagina)
            if len(datos) == 0:
                datos = []
    except Exception as e:
        print(f"ha habido un error: {type(e).__name__}")
    return render_template('results.html', 
                           result=datos,
                           busqueda=buscar,
                           res=size,
                           pagina=pagina, 
                           contador=int(contador) if 'contador' in locals() else 0,
                           subcontador=int(subcontador) if 'subcontador' in locals() else 0)



# Notes
@App.route('/notes/<pagina>', methods=['GET', 'POST'])
def Notes(pagina=1):
    try:
        notes = dbm.show_all()
        num = len(notes)
        contador, subcontador = dp(num, pagina)
    except Exception as e:
        logging.error(f"Error obteniendo las notas: {e}")
        return render_template('notes.html', notes=[], pagina=pagina, contador=0, subcontador=0)
    return render_template('notes.html', 
                           notes=notes, 
                           pagina=int(pagina), 
                           contador=contador, 
                           subcontador=int(subcontador))

# Show one note
@App.route('/note/<note_id>')
def note(note_id):
    try:
        result = dbm.show_note(note_id)
        return render_template('note.html', note=result[0])
    except Exception as e:
        logging.error(f"Error mostrando la nota: {e}")
        return redirect(url_for('index'))

# Login user
@App.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            user = request.form["user"] 
            pase = request.form["password"]
            if not user or not pase:
                flash("User or Password no valid")
                return render_template('login.html')
            
            logging.info(f"Intento de login: {user}")
            user_obj = User(0, user, password=pase)
            logged_user = ModelUser.login(dbm.execute_order, user_obj)
            
            if logged_user and logged_user.password:
                session.update({
                    'id': logged_user.id,
                    'name': logged_user.name,
                    'lastname': logged_user.lastname,
                    'correo': logged_user.correo,
                    'username': logged_user.username
                })
                logging.info(f"Login exitoso para el usuario: {user}")
                return redirect(url_for('index'))
            else:
                flash("Incorrect username or password")
                return render_template('login.html')
        else:
            return render_template('login.html')
    except Exception as e:
        logging.error(f"Error en el login: {e}")
        return render_template('login.html')

# Logout user
@App.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# Create a new note
@App.route('/crear-nota', methods=['GET', 'POST'])
def Crear_Nota():
    if session.get("name"):
        if request.method == 'POST':
            titulo = request.form['titulo']
            contenido = request.form['contenido']
            try:
                dbm.create_note(session.get('id'), titulo, contenido)
                flash('You have successfully created a note!')
                return redirect(url_for('index'))
            except Exception as e:
                logging.error(f"Error creando la nota: {e}")
        return render_template('crear-nota.html')
    else:
        return redirect(url_for('index'))

# Edit note
@App.route('/edit_note/<note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    try:
        result = dbm.show_note(note_id)
        if request.method == 'POST':
            titulo = request.form["titulo"]
            contenido = request.form["contenido"]
            dbm.edit_note(note_id, titulo, contenido)
            flash('The note has been edited successfully!')
            return redirect(url_for('index'))
        return render_template('edit.html', note=result[0])
    except Exception as e:
        logging.error(f"Error editando la nota: {e}")
        return redirect(url_for('index'))

# Delete note
@App.route('/delete_note/<note_id>')
def delete_note(note_id):
    try:
        dbm.delete_note(note_id)
        flash('The note has been successfully deleted!')
        return redirect(url_for('index'))
    except Exception as e:
        logging.error(f"Error eliminando la nota: {e}")
        flash('Could not delete note.')
        return redirect(url_for('index'))

# User profile
@App.route("/profile")
def profile():
    return render_template("profile.html")

# Config and running app
if __name__ == '__main__':
    App.config.from_object(config['development'])
    App.run()
