from flask import Flask, render_template, request, redirect, url_for
from afd import *
app = Flask(__name__)

# Lista para almacenar los estados
estados = []
alfabeto = []
estados_finales = []
estado_inicial = None
transiciones = {}
mensaje = 'Creá tu autómata finito determínistico para ver si reconoce una cadena'
log = ''

# Ruta principal para mostrar los estados
@app.route('/')
def home():
    automata_armado = estados and alfabeto and estados_finales and estado_inicial
    return render_template('index.html', estados=estados, alfabeto=alfabeto, estados_finales=estados_finales, transiciones = transiciones, automata_armado= automata_armado,
                           estado_inicial = estado_inicial,
                           mensaje = mensaje,
                           log = log)

# Ruta para agregar un estado
@app.route('/agregar_estado', methods=['POST'])
def agregar_estado():
    # Obtenemos el estado desde el formulario
    nuevo_estado = request.form.get('estado')
    if nuevo_estado:
        estados.append(nuevo_estado)  # Agregamos el estado a la lista
    return redirect(url_for('home'))  # Redirigimos a la página principal para ver los cambios


@app.route('/seleccionar_estado_inicial', methods=['POST'])
def seleccionar_estado_inicial():
    # Obtener el estado seleccionado desde el formulario
    estado = request.form.get('estado_inicial')
    
    # Verificar si se seleccionó un estado
    if estado:
        # Aquí puedes hacer algo con el estado inicial, por ejemplo, guardarlo en alguna estructura
        # Puedes asignarlo a una variable global, o actualizar el estado de tu autómata
        global estado_inicial
        estado_inicial = estado

    # Redirigir al usuario con un mensaje de éxito o error
    return redirect(url_for('home'))



# Ruta para eliminar un estado
@app.route('/eliminar_estado/<estado>')
def eliminar_estado(estado):
    if estado in estados:
        estados.remove(estado)  # Eliminamos el estado de la lista
    return redirect(url_for('home'))  # Redirigimos a la página principal

@app.route('/modificar_alfabeto', methods=['POST'])
def modificar_alfabeto():
    global alfabeto
    alfabeto = set(request.form['alfabeto'])
    return redirect(url_for('home'))
    

@app.route('/agregar_estado_final', methods=['POST'])
def agregar_estado_final():
    global estados_finales
    # Obtenemos los estados seleccionados
    estados_finales_seleccionados = request.form.getlist('estado_final')
    # Actualizamos los estados finales
    estados_finales = set(estados_finales_seleccionados)
    return redirect(url_for('home'))


@app.route('/agregar_transicion', methods=['POST'])
def agregar_transicion():
    # Obtener las transiciones del formulario
    for estado in estados:
        for simbolo in alfabeto:
            siguiente_estado = request.form.get(f"transicion_{estado}_{simbolo}")
            if siguiente_estado:
                # Guardamos la transición
                transiciones[(estado, simbolo)] = siguiente_estado
    return redirect('/')

@app.route('/eliminar_transicion/<estado>/<simbolo>')
def eliminar_transicion(estado, simbolo):
    k = (estado, simbolo)
    if k in transiciones:
        del transiciones[k]

    return redirect(url_for('home'))

@app.route('/chequear_cadena', methods=['POST'])
def chequear_cadena():
    global mensaje
    cadena = request.form.get('cadena')
    if cadena:
        automata = t_automata(estados=estados, alfabeto = alfabeto, transicion=transiciones,estados_finales=estados_finales, estado_inicial=estado_inicial)
    if automata.leer_cadena(cadena):
        mensaje = 'La cadena es reconocida por el autómata'
    else:
        mensaje = 'La cadena no es reconocida por el autóamata'

    global log
    log = automata.ver_log()
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True, port=8080)
