import random
import re
import os

class Ahorcado():
    def __init__(self, tema=None, nivel=None):
        self.vidas = 7
        self.letrasAdivinadas = []
        self.letrasIncorrectas = []
        self.palabrasIncorrectas = []
        self.gano = 0
        self.palabraAdivinar = self.elegir_palabra(tema, nivel)
    
    #El siguiente codigo es para que flask pueda mandar el objeto al navegador
    def to_dict(self):
        return {
            'vidas': self.vidas,
            'letrasAdivinadas': self.letrasAdivinadas,
            'letrasIncorrectas': self.letrasIncorrectas,
            'palabrasIncorrectas': self.palabrasIncorrectas,
            'gano': self.gano,
            'palabraAdivinar': self.palabraAdivinar
        }

    def elegir_palabra(self, tema, nivel):
        palabras_temas = {
            'animales': ["gato", "perro", "oso", "elefante", "jirafa", "tigre", "delfin"],
            'comida': ["pizza", "hamburguesa", "fideos", "ensalada", "helado", "sushi"],
            'paises': ["italia", "españa", "francia", "canada", "japon", "australia"],
            'profesiones': ["doctor", "profesor", "ingeniero", "policia", "bombero", "musico"],
            'deportes': ["futbol", "baloncesto", "tenis", "natacion", "atletismo", "ciclismo"]
        }

        palabras_niveles = {
            'facil': ["gato", "sol", "flor", "casa", "libro", "rio", "lago", "oso", "nube"],
            'medio': ["coche", "ciudad", "invierno", "perro", "montaña", "verano"],
            'dificil': ["anticonstitucionalidad", "anacronismo", "paradigma", "quimera", "efervescente", "electroencefalografista", "esternocleidomastoideo"]
        }

        if tema:
            return random.choice(palabras_temas.get(tema, []))
        elif nivel:
            return random.choice(palabras_niveles.get(nivel, []))
        else:
            return "ahorcado"  # Palabra predeterminada para el ejemplo
    
    #Las siguientes 3 funciones era para probar desde consola
    def obtener_nombre(self):
        jugador = input("Bienvenido al juego ahorcado, ¿Cuál es tu nombre? ")
        return jugador
    
    def menu_opcion_niveles(self):
        while True:
                opcion = input("Ingrese opción: ")

                if opcion in ["1", "2", "3"]:
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                   
        return opcion

    def menu_opcion_tematicas(self):
        while True:
            opcion = input("Ingrese opción: ")
            
            if opcion in ["1", "2", "3", "4", "5"]:
                os.system('cls')
                break
            else:
                os.system('cls')
                
        return opcion
    
    def juega(self,input):
       if self.validaEntrada(input):
            if len(input) == 1:
                self.arriesgoLetra(input.lower())
            else:
                if self.arriesgoPalabra(input.lower()):
                    return True
                else:
                    return False

    def validaEntrada(self,input):
    # Usamos una expresión regular para verificar si la cadena contiene solo letras
        patron = r'^[a-zA-Z]+$'
        return bool(re.match(patron,input))
    
    def arriesgoLetra(self, letra):
        repite = self.verificar_repeticion_letra(letra)
        if not repite:
            if letra in self.palabraAdivinar:
                self.letrasAdivinadas.append(letra)
                if "_" in self.imprimo_palabra():
                    self.gano = 0
                else:
                    self.gano = 1
                return True
            else:
                self.descontar_vida()
                self.letrasIncorrectas.append(letra)
                return False

    def verificar_repeticion_letra(self,letra):
        if letra in self.letrasIncorrectas or letra in self.letrasAdivinadas:
            return True
        else:
            return False

    def arriesgoPalabra(self, word):
        repite = self.verificar_repeticion(word)
        if not repite:
            if word == self.palabraAdivinar:
                self.gano= 1
                return True
            else:
                self.descontar_vida()
                self.gano= 0
                self.palabrasIncorrectas.append(word)
                return False

    def descontar_vida(self):
        if not self.vidas==0:
            self.vidas -=1
            return self.vidas
        else:
            return 0

    def verificar_repeticion(self,A):
        if A in self.palabrasIncorrectas:
            return True
        else:
            return False
        
    def imprimo_palabra(self):
        if self.vidas > 0:
            palabra_mostrar = ""
            for letra in self.palabraAdivinar:
                if letra in self.letrasAdivinadas:
                    palabra_mostrar += letra+" "
                else:
                    palabra_mostrar += "_ "
            return palabra_mostrar
        else:
            return self.palabraAdivinar
    
    def definir_si_gano(self):
        if self.gano==1:
            return True
        else:
            return False

#Los siguientes metodos son para mostrar mensajes que flask consuma:
    def mensaje_letra_incorrecta(self, letra):
        return f"La letra {letra} es incorrecta. Perdiste 1 vida."

    def mensaje_letra_repetida(self, letra):
        return f"La letra {letra} ya fue ingresada anteriormente."

    def mensaje_perdio(self):
        return "Agotaste todas las vidas. La palabra a adivinar era: {}".format(self.palabraAdivinar)

    def mensaje_gano(self):
        return "¡Felicidades! Ganaste."

    def obtener_mensaje_actual(self, letraU):
        letra = letraU.lower()
        if letra in self.letrasIncorrectas:
            return self.mensaje_letra_incorrecta(letra)
        elif letra in self.letrasAdivinadas:
            return self.mensaje_letra_repetida(letra)
        elif self.vidas == 0:
            return self.mensaje_perdio()
        elif self.gano == 1:
            return self.mensaje_gano()
        else:
            return ""


# JUEGO
# Comentar: Ctrl + K + Ctrl + C
# Descomentar: Ctrl + K + Ctrl + U


## NOTAS:
# En Python, cuando importas un módulo, todas las declaraciones en ese módulo se ejecutan una vez,
#  incluyendo las declaraciones que no están dentro de funciones o clases.
#  En este caso, la línea juegoActual.obtener_nombre() se ejecuta inmediatamente cuando se importa el módulo
#  ahorcado.py, antes de que se ejecuten las pruebas en el archivo test_TDD.py.
# Para solucionar esto, puedes mover la línea juegoActual.obtener_nombre()
#  dentro de una función o un bloque if __name__ == '__main__':
