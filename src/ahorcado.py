import random
import re
import os

abecedario = list("abcdefghijklmnopqrstuvwxyz")

#Palabras con tematica
# palabras_animales = ["gato", "perro", "oso" ,"elefante", "jirafa", "tigre", "delfín"]
# palabras_comida = ["pizza", "hamburguesa", "fideos", "ensalada", "helado", "sushi"]
# palabras_paises = ["italia", "españa", "francia", "canada", "japon", "australia"]
# palabras_profesiones = ["doctor", "profesor", "ingeniero", "policia", "bombero", "musico"]
# palabras_deportes = ["futbol", "baloncesto", "tenis", "natacion", "atletismo","ciclismo"]

#Palabra con niveles de dificultad
# palabras_faciles = ["gato", "sol", "flor", "casa", "libro", "rio", "lago","oso","nube"]
# palabras_medias = ["coche", "ciudad", "invierno", "perro", "montaña", "verano"]
# palabras_dificiles = ["anticonstitucionalidad", "anacronismo", "paradigma", "quimera", "efervescente","electroencefalografista", "esternocleidomastoideo"]


class Ahorcado():
    def __init__(self, tema=None, nivel=None):
        self.vidas = 7
        self.letrasAdivinadas = []
        self.letrasIncorrectas = []
        self.palabrasIncorrectas = []
        self.gano = 0
        self.palabraAdivinar = self.elegir_palabra(tema, nivel)
    
    #El siguiente codigo es para que flask pueda mandar  el objeto al navegador
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
    
    def obtener_nombre(self):
        jugador = input("Bienvenido al juego ahorcado, ¿Cuál es tu nombre? ")
        return jugador
    
    def menu_opcion_niveles(self):
        while True:
                #print("Opciones de juego:")
                #print("1- Nivel 1 (Fácil)")
                #print("2- Nivel 2 (Medio)")
                #print("3- Nivel 3 (Difícil)")
                opcion = input("Ingrese opción: ")

                if opcion in ["1", "2", "3"]:
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                    #print("Opción incorrecta. Por favor, ingrese una opción válida (1, 2 o 3).")        

        return opcion

    def menu_opcion_tematicas(self):
        while True:
            #print("Seleccione una temática: ")
            #print("1- Animales")
            #print("2- Comida")
            #print("3- Paises")
            #print("4- Profesionales")
            #print("5- Deportes")
            opcion = input("Ingrese opción: ")
            
            if opcion in ["1", "2", "3", "4", "5"]:
                os.system('cls')
                break
            else:
                os.system('cls')
                #print("Opción incorrecta. Por favor, ingrese una opción válida (1, 2, 3, 4 o 5).")
        
        return opcion
    
    def juega(self,input):
       if self.validaEntrada(input):
            if len(input) == 1:
                self.arriesgoLetra(input)
            else:
                if self.arriesgoPalabra(input):
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
                #print("Letra correcta!")
                if "_" in self.imprimo_palabra():
                    self.gano = 0
                else:
                    self.gano = 1
                return True
            else:
                self.descontar_vida()
                self.letrasIncorrectas.append(letra)
                #print("Letra incorrecta. Perdiste 1 vida")
                return False

    def verificar_repeticion_letra(self,letra):
        if letra in self.letrasIncorrectas or letra in self.letrasAdivinadas:
            #print("La letra {} ya fué ingresada!".format(letra))
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
                #print("La palabra ingresada es incorrecta! Perdiste 1 vida")
                return False

    def descontar_vida(self):
        if not self.vidas==0:
            self.vidas -=1
            return self.vidas
        else:
            return 0

    def verificar_repeticion(self,A):
        if A in self.palabrasIncorrectas:
            #print("La palabra {} ya fue ingresada!".format(A))
            return True
        else:
            return False
        
    def imprimo_palabra(self):
        palabra_mostrar = ""
        for letra in self.palabraAdivinar:
            if letra in self.letrasAdivinadas:
                palabra_mostrar += letra+" "
            else:
                palabra_mostrar += "_ "
        return palabra_mostrar
    
    #PARA MI NO VA ESTE
    def imprimo_palabra_ganadora(self, palabra):
        palabra_mostrar = ""
        for letra in palabra:
            palabra_mostrar += letra+" "
        return palabra_mostrar
    
    def definir_si_gano(self):
        if self.gano==1:
            #print("La palabra ingresada es correcta!")
            #print(juegoActual.imprimo_palabra_ganadora(ingreso))
            #print(" ")
            #print("GANASTE!")
            #print(" ")
            return True
        else:
            #print("Agotaste todas las vidas! La palabra a adivinar era: {}".format(juegoActual.palabraAdivinar))
            #print(" ")
            #print("---GAME OVER----")
            #print(" ")
            return False

        #print("")

#Los siguientes metodos son para mostrar mejs que flask consuma:
    def mensaje_letra_incorrecta(self, letra):
        return f"La letra {letra} es incorrecta. Perdiste 1 vida."

    def mensaje_letra_repetida(self, letra):
        return f"La letra {letra} ya fue ingresada anteriormente."

    def mensaje_perdio(self):
        return "Agotaste todas las vidas. La palabra a adivinar era: {}".format(self.palabraAdivinar)

    def mensaje_gano(self):
        return "¡Felicidades! Ganaste."

    def obtener_mensaje_actual(self, letra):
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

# if __name__ == '__main__':
#     while True:
#         juegoActual = Ahorcado()
#         juegoActual.jugador = juegoActual.obtener_nombre()
#         print("¡Bienvenido {}! --> Vamos a jugar!".format(juegoActual.jugador))
#         print("--------------------------------------------------------")
#         print("Seleccione un tipo de juego: ")
#         print("1- Jugar por nivel de dificultad")
#         print("2- Jugar por temática")
#         opcion = input("Ingrese opción: ")
#         if opcion == "1":
#             op = juegoActual.menu_opcion_niveles()
#             if op == "1":
#                 juegoActual.palabraAdivinar = random.choice(palabras_faciles)
#                 print("-----Bienvenido al nivel FACIL-----")
#                 print ("           Mucha suerte!")
#                 print("Vidas: {}".format(juegoActual.vidas))
#                 print("La palabra a adivinar tiene {} letras".format(len(juegoActual.palabraAdivinar)))
#                 print(juegoActual.imprimo_palabra())
#                 print("")
#                 while juegoActual.vidas > 0 and juegoActual.gano !=1:
#                     ingreso = input("Ingresa una letra o palabra: ").lower()
#                     juegoActual.juega(ingreso)
#                     print("Vidas: {}".format(juegoActual.vidas))
#                     print("")
#                     print(juegoActual.imprimo_palabra())

#                 juegoActual.definir_si_gano()

#             if op == "2":
#                 juegoActual.palabraAdivinar = random.choice(palabras_medias)
#                 print("-----Bienvenido al nivel MEDIO-----")
#                 print ("           Mucha suerte!")
#                 print("Vidas: {}".format(juegoActual.vidas))
#                 print("La palabra a adivinar tiene {} letras".format(len(juegoActual.palabraAdivinar)))
#                 print(juegoActual.imprimo_palabra())
#                 print("")
#                 while juegoActual.vidas > 0 and juegoActual.gano !=1:
#                     ingreso = input("Ingresa una letra o palabra: ").lower()
#                     juegoActual.juega(ingreso)
#                     print("Vidas: {}".format(juegoActual.vidas))
#                     print("")
#                     print(juegoActual.imprimo_palabra())

#                 juegoActual.definir_si_gano()

#             if op == "3":
#                 juegoActual.palabraAdivinar = random.choice(palabras_dificiles)
#                 print("-----Bienvenido al nivel DIFICIL-----")
#                 print ("           Mucha suerte!")
#                 print("Vidas: {}".format(juegoActual.vidas))
#                 print("La palabra a adivinar tiene {} letras".format(len(juegoActual.palabraAdivinar)))
#                 print(juegoActual.imprimo_palabra())
#                 print("")
#                 while juegoActual.vidas > 0 and juegoActual.gano !=1:
#                     ingreso = input("Ingresa una letra o palabra: ").lower()
#                     juegoActual.juega(ingreso)
#                     print("Vidas: {}".format(juegoActual.vidas))
#                     print("")
#                     print(juegoActual.imprimo_palabra())

#                 juegoActual.definir_si_gano()
        
#         if opcion == "2":
#             op = juegoActual.menu_opcion_tematicas()
#             if op == "1":
#                 juegoActual.palabraAdivinar = random.choice(palabras_animales)
#                 print("-----Bienvenido a la temática ANIMALES-----")
#                 print ("           Mucha suerte!")
#                 print("Vidas: {}".format(juegoActual.vidas))
#                 print("La palabra a adivinar tiene {} letras".format(len(juegoActual.palabraAdivinar)))
#                 print(juegoActual.imprimo_palabra())
#                 print("")
#                 while juegoActual.vidas > 0 and juegoActual.gano !=1:
#                     ingreso = input("Ingresa una letra o palabra: ").lower()
#                     juegoActual.juega(ingreso)
#                     print("Vidas: {}".format(juegoActual.vidas))
#                     print("")
#                     print(juegoActual.imprimo_palabra())

#                 juegoActual.definir_si_gano()
                
#             if op == "2":
#                 juegoActual.palabraAdivinar = random.choice(palabras_comida)
#                 print("-----Bienvenido a la temática COMIDA-----")
#                 print ("           Mucha suerte!")
#                 print("Vidas: {}".format(juegoActual.vidas))
#                 print("La palabra a adivinar tiene {} letras".format(len(juegoActual.palabraAdivinar)))
#                 print(juegoActual.imprimo_palabra())
#                 print("")
#                 while juegoActual.vidas > 0 and juegoActual.gano !=1:
#                     ingreso = input("Ingresa una letra o palabra: ").lower()
#                     juegoActual.juega(ingreso)
#                     print("Vidas: {}".format(juegoActual.vidas))
#                     print("")
#                     print(juegoActual.imprimo_palabra())

#                 juegoActual.definir_si_gano()

#             if op == "3":
#                 juegoActual.palabraAdivinar = random.choice(palabras_paises)
#                 print("-----Bienvenido a la temática PAISES-----")
#                 print ("           Mucha suerte!")
#                 print("Vidas: {}".format(juegoActual.vidas))
#                 print("La palabra a adivinar tiene {} letras".format(len(juegoActual.palabraAdivinar)))
#                 print(juegoActual.imprimo_palabra())
#                 print("")
#                 while juegoActual.vidas > 0 and juegoActual.gano !=1:
#                     ingreso = input("Ingresa una letra o palabra: ").lower()
#                     juegoActual.juega(ingreso)
#                     print("Vidas: {}".format(juegoActual.vidas))
#                     print("")
#                     print(juegoActual.imprimo_palabra())

#                 juegoActual.definir_si_gano()

#             if op == "4":
#                 juegoActual.palabraAdivinar = random.choice(palabras_profesiones)
#                 print("-----Bienvenido a la temática PROFESIONES-----")
#                 print ("           Mucha suerte!")
#                 print("Vidas: {}".format(juegoActual.vidas))
#                 print("La palabra a adivinar tiene {} letras".format(len(juegoActual.palabraAdivinar)))
#                 print(juegoActual.imprimo_palabra())
#                 print("")
#                 while juegoActual.vidas > 0 and juegoActual.gano !=1:
#                     ingreso = input("Ingresa una letra o palabra: ").lower()
#                     juegoActual.juega(ingreso)
#                     print("Vidas: {}".format(juegoActual.vidas))
#                     print("")
#                     print(juegoActual.imprimo_palabra())

#                 juegoActual.definir_si_gano()

#             if op == "5":
#                 juegoActual.palabraAdivinar = random.choice(palabras_deportes)
#                 print("-----Bienvenido a la temática DEPORTES-----")
#                 print ("           Mucha suerte!")
#                 print("Vidas: {}".format(juegoActual.vidas))
#                 print("La palabra a adivinar tiene {} letras".format(len(juegoActual.palabraAdivinar)))
#                 print(juegoActual.imprimo_palabra())
#                 print("")
#                 while juegoActual.vidas > 0 and juegoActual.gano !=1:
#                     ingreso = input("Ingresa una letra o palabra: ").lower()
#                     juegoActual.juega(ingreso)
#                     print("Vidas: {}".format(juegoActual.vidas))
#                     print("")
#                     print(juegoActual.imprimo_palabra())

#                 juegoActual.definir_si_gano()



## NOTAS:
# En Python, cuando importas un módulo, todas las declaraciones en ese módulo se ejecutan una vez,
#  incluyendo las declaraciones que no están dentro de funciones o clases.
#  En este caso, la línea juegoActual.obtener_nombre() se ejecuta inmediatamente cuando se importa el módulo
#  ahorcado.py, antes de que se ejecuten las pruebas en el archivo test_TDD.py.
# Para solucionar esto, puedes mover la línea juegoActual.obtener_nombre()
#  dentro de una función o un bloque if __name__ == '__main__':
