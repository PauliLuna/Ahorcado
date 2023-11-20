import sys
sys.path.append('src')

from flask import Flask, redirect, url_for,render_template, request, jsonify, session, send_from_directory
from ahorcado import Ahorcado

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta' #Sino da error
juego_html = 'juego.html'

# Ruta para servir archivos estáticos (CSS en este caso)
@app.route('/ui/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

#Cargar pagina de inicio
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

    return render_template(juego_html, resultado=resultado)

@app.route('/jugar_letra', methods=['POST'])
def jugar_letra():
    entrada = request.form['entrada']
    juego_actual = session.get('juego_actual')

    if juego_actual:
        juego_actual_obj = Ahorcado()
        juego_actual_obj.__dict__.update(juego_actual)  # Restaurar el objeto Ahorcado

        if juego_actual_obj.vidas > 0 and '_' in juego_actual_obj.imprimo_palabra():
            if not juego_actual_obj.valida_entrada(entrada):
                mensaje = juego_actual_obj.mensaje_solo_letras()
                resultado = {
                    'vidas_restantes': juego_actual_obj.vidas,
                    'palabra_oculta': juego_actual_obj.imprimo_palabra(),
                    'mensaje': mensaje,
                    'gano': juego_actual_obj.gano
                }
                return render_template(juego_html, resultado=resultado)

            juego_actual_obj.juega(entrada.lower())

            session['juego_actual'] = juego_actual_obj.to_dict()  # Actualizar el juego en la sesión

            resultado = {
                'vidas_restantes': juego_actual_obj.vidas,
                'palabra_oculta': juego_actual_obj.imprimo_palabra(),
                'mensaje': juego_actual_obj.obtener_mensaje_actual(entrada),
                'gano': juego_actual_obj.gano
            }

            if juego_actual_obj.gano == 1 or juego_actual_obj.vidas == 0:
                # Redirigir a la página de juego nuevamente al ganar o perder
                return render_template(juego_html, resultado=resultado)

    return render_template(juego_html, resultado=resultado)  # Renderizar la plantilla nuevamente

@app.route('/jugar_nuevamente', methods=['GET'])
def jugar_nuevamente():
    juego_anterior = session.get('juego_actual')
    
    if juego_anterior:
        # Crea un nuevo objeto Ahorcado con la configuración anterior
        juego_nuevo = Ahorcado(
            tema=juego_anterior.get('tema'),
            nivel=juego_anterior.get('nivel')
        )

        # Reinicia el juego con una palabra aleatoria
        juego_nuevo.palabra_adivinar = juego_nuevo.elegir_palabra(juego_anterior.get('tema'), juego_anterior.get('nivel'))

        # Actualiza la sesión con el nuevo juego
        session['juego_actual'] = juego_nuevo.to_dict()

        resultado = {
            'vidas_restantes': juego_nuevo.vidas,
            'palabra_oculta': juego_nuevo.imprimo_palabra()
        }

        return render_template(juego_html, resultado=resultado)

    return redirect('/')

#hacer que el diccionario de elecciones este en ahorcado.py, aca se realice la selecion
def obtener_tema(seleccion):
    temas = {
        'a': 'animales',
        'b': 'comida',
        'c': 'paises',
        'd': 'profesiones',
        'e': 'deportes'
    }
    return temas.get(seleccion, 'animales')  # Valor predeterminado 'animales' si no se encuentra la selección

#hacer que el diccionario de elecciones este en ahorcado.py, aca se realice la selecion
def obtener_nivel(seleccion):
    niveles = {
        'a': 'facil',
        'b': 'medio',
        'c': 'dificil'
    }
    return niveles.get(seleccion, 'facil')  # Valor predeterminado 'facil' si no se encuentra la selección


if __name__ == "__main__":
    app.run(debug=True)