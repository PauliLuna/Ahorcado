import random

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

class Ahorcado():
    def __init__(self, tema=None, nivel=None):
        self.vidas = 7
        self.letras_adivinadas = []
        self.letras_incorrectas = []
        self.palabras_incorrectas = []
        self.gano = 0
        self.tema = tema
        self.nivel = nivel
        self.palabra_adivinar = self.elegir_palabra(tema, nivel)
        self.mensaje = ""
    
    #El siguiente codigo es para que flask pueda mandar el objeto al navegador
    def to_dict(self):
        return {
            'vidas': self.vidas,
            'letras_adivinadas': self.letras_adivinadas,
            'letras_incorrectas': self.letras_incorrectas,
            'palabras_incorrectas': self.palabras_incorrectas,
            'gano': self.gano,
            'tema': self.tema,
            'nivel': self.nivel,
            'palabra_adivinar': self.palabra_adivinar,
            'mensaje': self.mensaje
        }

    def elegir_palabra(self, tema, nivel):
        if tema:
            return random.choice(palabras_temas.get(tema, []))
        elif nivel:
            return random.choice(palabras_niveles.get(nivel, []))
        else:
            return "ahorcado"  # Palabra predeterminada para el ejemplo
    
    def imprimo_palabra(self):
        palabra_mostrar = ""
        if self.vidas > 0:
            if self.gano == 1:
                palabra_mostrar = " ".join(self.palabra_adivinar)
            else:
                for letra in self.palabra_adivinar:
                    if letra in self.letras_adivinadas:
                        palabra_mostrar += letra+" "
                    else:
                        palabra_mostrar += "_ "
            palabra_mostrar = palabra_mostrar.rstrip()
        else:
            palabra_mostrar = " ".join(self.palabra_adivinar)  
        return palabra_mostrar

    def juega(self,input):
        if self.valida_entrada(input):
            if len(input) == 1:
                if self.arriesgo_letra(input.lower()):
                    return True
                else:
                    return False
            else:
                if self.arriesgo_palabra(input.lower()):
                    return True
                else:
                    return False
        else:
            return False

    def valida_entrada(self,input):
        return False
        #return input.isalpha()
    
    def arriesgo_letra(self, letra):
        repite = self.verificar_repeticion_letra(letra)
        if not repite:
            if letra in self.palabra_adivinar:
                self.letras_adivinadas.append(letra)
                self.mensaje = self.obtener_mensaje_actual(letra)
                if all(letra in self.letras_adivinadas for letra in self.palabra_adivinar):
                # Todas las letras han sido adivinadas, el jugador ha ganado
                    self.gano = 1
                    self.mensaje = self.obtener_mensaje_actual(letra)
                return True
            else:
                self.descontar_vida()
                self.letras_incorrectas.append(letra)
                self.mensaje = self.obtener_mensaje_actual(letra)
                return False
        else:
        # La letra ya fue ingresada
            self.mensaje = self.mensaje_letra_repetida(letra)
            return False

    def verificar_repeticion_letra(self, letra):
        return letra in self.letras_incorrectas or letra in self.letras_adivinadas

    def arriesgo_palabra(self, word):
        repite = self.verificar_repeticion(word)
        if not repite:
            if word == self.palabra_adivinar:
                self.gano= 1
                self.mensaje = self.obtener_mensaje_actual(word)
                return True
            else:
                self.descontar_vida()
                self.gano= 0
                self.palabras_incorrectas.append(word)
                self.mensaje = self.obtener_mensaje_actual(word)
                return False
        self.mensaje = self.mensaje_palabra_repetida(word)

    def descontar_vida(self):
        if self.vidas!=0:
            self.vidas -=1
            return self.vidas
        else:
            return 0

    def verificar_repeticion(self,a):
        return a in self.palabras_incorrectas
    
    def definir_si_gano(self):
        if self.gano==1:
            return True
        else:
            return False

#Los siguientes metodos son para mostrar mensajes que flask consuma:
    def mensaje_palabra_incorrecta(self, palabra):
        return f"La palabra '{palabra}' es incorrecta. Perdiste 1 vida."
    
    def mensaje_palabra_repetida(self, palabra):
        return f"La palabra {palabra} ya fue ingresada anteriormente."

    def mensaje_letra_incorrecta(self, letra):
        return f"La letra {letra} es incorrecta. Perdiste 1 vida."

    def mensaje_letra_repetida(self, letra):
        return f"La letra {letra} ya fue ingresada anteriormente."
    
    def mensaje_solo_letras(self):
        return "Advertencia: La entrada debe contener solo letras"

    def mensaje_perdio(self):
        return "Agotaste todas las vidas. La palabra a adivinar era: {}".format(self.palabra_adivinar)

    def mensaje_gano(self):
        return "¡Felicidades! Ganaste."
    
    def mensaje_letra_correcta(self, letra):
        return f"La entrada {letra} es acertada."

    def obtener_mensaje_actual(self, entrada):
        entrada = entrada.lower()

        if entrada in self.palabras_incorrectas:
            return self.mensaje_palabra_incorrecta(entrada)
        elif entrada in self.letras_incorrectas:
            return self.mensaje_letra_incorrecta(entrada)
        elif entrada in self.palabra_adivinar:
            return self.mensaje_letra_correcta(entrada)
        elif self.vidas == 0:
            return self.mensaje_perdio()
        elif self.gano == 1:
            return self.mensaje_gano()
        else:
            return ""