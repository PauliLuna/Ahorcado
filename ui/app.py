import sys
sys.path.append('src')

from flask import Flask, redirect, url_for,render_template, request, jsonify, session
from ahorcado import Ahorcado

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'
juegoActual= Ahorcado()

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/elegir_opcion', methods=['POST'])
def elegir_opcion():
    opcion = request.form['opcion']

    if opcion == '1':
        return render_template('elegir_tematica.html')
    elif opcion == '2':
        return render_template('elegir_nivel.html')
    else:
        return redirect('/')

@app.route('/jugar', methods=['POST'])
def jugar():
    opcion = request.form['opcion']
    seleccion = request.form['seleccion']

    if opcion == '1':
        tema = obtener_tema(seleccion)
        juego_actual = Ahorcado(tema=tema)
    elif opcion == '2':
        nivel = obtener_nivel(seleccion)
        juego_actual = Ahorcado(nivel=nivel)
    else:
        return redirect('/')

    session['juego_actual'] = juego_actual.to_dict()  # Guardar el juego en la sesión

    resultado = {
        'vidas_restantes': juego_actual.vidas,
        'palabra_oculta': juego_actual.imprimo_palabra()
    }

    return render_template('juego.html', resultado=resultado)

@app.route('/jugar_letra', methods=['POST'])
def jugar_letra():
    letra = request.form['letra']
    juego_actual = session.get('juego_actual')

    if juego_actual:
        juego_actual_obj = Ahorcado()
        juego_actual_obj.__dict__.update(juego_actual)  # Restaurar el objeto Ahorcado
        juego_actual_obj.juega(letra)
        session['juego_actual'] = juego_actual_obj.to_dict()  # Actualizar el juego en la sesión

        resultado = {
            'vidas_restantes': juego_actual_obj.vidas,
            'palabra_oculta': juego_actual_obj.imprimo_palabra(),
            'mensaje': juego_actual_obj.obtener_mensaje_actual(letra),
            'gano': juego_actual_obj.gano
        }

        return render_template('juego.html', resultado=resultado)

    return redirect('/')

@app.route('/jugar_nuevamente', methods=['GET'])
def jugar_nuevamente():
    juego_anterior = session.get('juego_actual')
    
    if juego_anterior:
        # Crea un nuevo objeto Ahorcado con la configuración anterior
        juego_nuevo = Ahorcado(
            tema=None,
            nivel=None
        )

        # Reinicia el juego con una palabra aleatoria
        juego_nuevo.palabraAdivinar = juego_nuevo.elegir_palabra(juego_anterior.get('tema'), juego_anterior.get('nivel'))

        # Actualiza la sesión con el nuevo juego
        session['juego_actual'] = juego_nuevo.to_dict()

        resultado = {
            'vidas_restantes': juego_nuevo.vidas,
            'palabra_oculta': juego_nuevo.imprimo_palabra()
        }

        return render_template('juego.html', resultado=resultado)

    return redirect('/')

def obtener_tema(seleccion):
    temas = {
        'a': 'animales',
        'b': 'comida',
        'c': 'paises',
        'd': 'profesiones',
        'e': 'deportes'
    }
    return temas.get(seleccion, 'animales')  # Valor predeterminado 'animales' si no se encuentra la selección

def obtener_nivel(seleccion):
    niveles = {
        'a': 'facil',
        'b': 'medio',
        'c': 'dificil'
    }
    return niveles.get(seleccion, 'facil')  # Valor predeterminado 'facil' si no se encuentra la selección


if __name__ == "__main__":
    app.run(debug=True)