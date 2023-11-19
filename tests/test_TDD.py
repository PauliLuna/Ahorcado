import unittest
from src.ahorcado import Ahorcado
from unittest.mock import patch

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

# Creo una instancia del Ahorcado
juego = Ahorcado()
 

# HISTORIA DE USUARIO 1
class ArriesgarPalabraTest(unittest.TestCase):

     def test_adivino_palabra(self):
        juego.palabraAdivinar = "giacomo"
        esperado = True
        actual = juego.arriesgoPalabra("giacomo")
        self.assertEqual(actual, esperado)

     def test_adivino_palabra_flag(self):
        juego.palabraAdivinar = "giacomo"
        esperado = 1
        juego.arriesgoPalabra("giacomo")
        self.assertEqual(juego.gano, esperado)

     def test_pierdo_palabra(self):
        juego.palabraAdivinar = "giacomo"
        esperado = False 
        actual = juego.arriesgoPalabra("nogiacomo")
        self.assertEqual(actual, esperado)

     def test_pierdo_palabra_flag(self):
        juego.palabraAdivinar = "giacomo"
        esperado = 0
        juego.arriesgoPalabra("nogiacomo")
        self.assertEqual(juego.gano, esperado)
     
     def test_no_repetir_palabras(self):
        juego.palabraAdivinar = "giacomo"
        juego.palabras_incorrectas.append("tirabuzones")
        esperado = False 
        actual = juego.verificar_repeticion("giacomo2")
        self.assertEqual(actual, esperado)

     def test_repetir_palabras(self):
        juego.palabraAdivinar = "giacomo"
        juego.palabras_incorrectas.append("tirabuzones")
        esperado = True 
        actual = juego.verificar_repeticion("tirabuzones")
        self.assertEqual(actual, esperado)

     def test_juega_palabra_correcta(self):
          juego.palabraAdivinar= "giacomo"
          actual = juego.juega("giacomo")
          esperado = True
          self.assertEqual(actual, esperado)

     def test_juega_palabra_incorrecta(self):
          juego.palabraAdivinar= "giacomo"
          actual = juego.juega("zapallito")
          esperado = False
          self.assertEqual(actual, esperado)
      
# HISTORIA DE USUARIO 2
class ArriesgoLetra(unittest.TestCase):
     def test_adivino_letra(self):
          juego.palabraAdivinar = "giacomo"
          esperado = True
          actual = juego.arriesgoLetra("a")
          self.assertEqual(actual, esperado)

     def test_pierdo_letra(self):
        juego.palabraAdivinar = "giacomo"
        esperado = False 
        actual = juego.arriesgoLetra("x")
        self.assertEqual(actual, esperado)

     

     def test_no_repetir_letra(self):
          juego.palabraAdivinar = "giacomo"
          juego.letras_adivinadas = ["g", "a"]
          juego.letras_incorrectas = ["w"]
          esperado = False
          actual = juego.verificar_repeticion_letra("z")
          self.assertEqual(actual, esperado)
    
     def test_repetir_letra_adivinada(self):
          juego.palabraAdivinar = "giacomo"
          juego.letras_adivinadas = ["g", "a"]
          juego.letras_incorrectas = ["w"]
          esperado = True
          actual = juego.verificar_repeticion_letra("a")
          self.assertEqual(actual, esperado)
    
     def test_repetir_letra_incorrecta(self):
          juego.palabraAdivinar = "giacomo"
          juego.letras_adivinadas = ["g", "a"]
          juego.letras_incorrectas = ["w"]
          esperado = True
          actual = juego.verificar_repeticion_letra("w")
          self.assertEqual(actual, esperado)     

class ValidoJuego(unittest.TestCase):
     def test_entrada_letra(self):
          juego.palabraAdivinar = "giacomo"
          entrada = "g"
          esperado = True
          actual = juego.validaEntrada(entrada)
          self.assertEqual(actual, esperado)

     def test_entrada_palabra(self):
          entrada = "hola"
          esperado = True
          actual = juego.validaEntrada(entrada)
          self.assertEqual(actual, esperado)

     def test_entrada_no_valida(self):
          entrada = "#hola"
          esperado = False
          actual = juego.validaEntrada(entrada)
          self.assertEqual(actual, esperado)
     
     # Elegir palabras
      ## Temas
     def test_elegir_palabra_tema_animales(self):
          actual = juego.elegir_palabra(tema='animales', nivel=None)
          self.assertIn(actual,palabras_temas["animales"])
     
     def test_elegir_palabra_tema_comida(self):
          actual = juego.elegir_palabra(tema='comida', nivel=None)
          self.assertIn(actual,palabras_temas["comida"])
     
     def test_elegir_palabra_tema_deportes(self):
          actual = juego.elegir_palabra(tema='deportes', nivel=None)
          self.assertIn(actual,palabras_temas["deportes"])
     
     def test_elegir_palabra_tema_paises(self):
          actual = juego.elegir_palabra(tema='paises', nivel=None)
          self.assertIn(actual,palabras_temas["paises"])
     
     def test_elegir_palabra_tema_profesiones(self):
          actual = juego.elegir_palabra(tema='profesiones', nivel=None)
          self.assertIn(actual,palabras_temas["profesiones"])
     
      ## Niveles
     def test_elegir_palabra_nivel_facil(self):
          actual = juego.elegir_palabra(tema=None, nivel='facil')
          self.assertIn(actual,palabras_niveles["facil"])

     def test_elegir_palabra_nivel_medio(self):
               actual = juego.elegir_palabra(tema=None, nivel='medio')
               self.assertIn(actual,palabras_niveles["medio"])
     
     def test_elegir_palabra_nivel_dificil(self):
          actual = juego.elegir_palabra(tema=None, nivel='dificil')
          self.assertIn(actual,palabras_niveles["dificil"])
     
# HISTORIA DE USUARIO 3
class ImprimoPalabra(unittest.TestCase):
     def test_imprimo(self):
            juego.palabraAdivinar = "giacomo"
            juego.letras_adivinadas = ["a", "o"]
            esperado = "_ _ a _ o _ o "
            actual = juego.imprimo_palabra()
            self.assertEqual(actual, esperado)
     
     # Mensajes para UI
     def test_mensaje_letra_incorrecta(self):
          letra = "w"
          juego.gano = 0
          juego.letras_incorrectas = ["a", "w"]
          esperado = f"La letra {letra} es incorrecta. Perdiste 1 vida."
          actual = juego.obtener_mensaje_actual(letra)
          self.assertEqual(actual, esperado)
     
     def test_mensaje_letra_repetida(self):
          letra = "w"
          juego.gano = 0
          juego.letras_incorrectas = ["m"]
          juego.letras_adivinadas = ["a", "w"]
          esperado = f"La letra {letra} ya fue ingresada anteriormente."
          actual = juego.obtener_mensaje_actual(letra)
          self.assertEqual(actual, esperado)
     
     def test_mensaje_perdio(self):
          letra = "n"
          juego.palabraAdivinar = "prueba"
          juego.letras_incorrectas = ["m"]
          juego.letras_adivinadas = ["a", "w"]
          juego.vidas = 0
          esperado = f"Agotaste todas las vidas. La palabra a adivinar era: {juego.palabraAdivinar}"
          actual = juego.obtener_mensaje_actual(letra)
          self.assertEqual(actual, esperado)
     
     def test_mensaje_gano(self):
          letra = "w"
          juego.letras_incorrectas = ["m"]
          juego.letras_adivinadas = ["a"]
          juego.gano = 1
          esperado = "¡Felicidades! Ganaste."
          actual = juego.obtener_mensaje_actual(letra)
          self.assertEqual(actual, esperado)


# HISTORIA DE USUARIO 4
class Menu(unittest.TestCase):

     def test_entrada_valida(self): 
          entrada = "hola"
          esperado = True
          actual = juego.validaEntrada(entrada)
          self.assertEqual(actual, esperado)

     def test_entrada_no_valida(self):
          entrada = "?hola%123!"
          esperado = False
          actual = juego.validaEntrada(entrada)
          self.assertEqual(actual, esperado)


# HISTORIA DE USUARIO 5
class Vidas(unittest.TestCase):
     def test_pierdo_primer_vida(self):
            juego.vidas=7
            esperado = 6 
            actual = juego.descontar_vida()
            self.assertEqual(actual, esperado)
    
     def test_pierdo_segunda_vida(self):
            juego.vidas=6
            esperado = 5
            actual = juego.descontar_vida()
            self.assertEqual(actual, esperado)

     def test_pierdo_tercera_vida(self):
            juego.vidas=5
            esperado = 4
            actual = juego.descontar_vida()
            self.assertEqual(actual, esperado)
     
     def test_pierdo_cuarta_vida(self):
            juego.vidas=4
            esperado = 3
            actual = juego.descontar_vida()
            self.assertEqual(actual, esperado)

     def test_pierdo_quinta_vida(self):
            juego.vidas=3
            esperado = 2
            actual = juego.descontar_vida()
            self.assertEqual(actual, esperado)

     def test_pierdo_sexta_vida(self):
            juego.vidas=2
            esperado = 1
            actual = juego.descontar_vida()
            self.assertEqual(actual, esperado)

     def test_pierdo_septima_vida(self):     
            juego.vidas=1
            esperado = 0
            actual = juego.descontar_vida()
            self.assertEqual(actual, esperado)

     def test_sin_vida(self):
            juego.vidas=0
            esperado = 0
            actual = juego.descontar_vida()
            self.assertEqual(actual, esperado)

     def test_si_gano(self):
          juego.gano=1
          esperado = True
          actual = juego.definir_si_gano()
          self.assertEqual(actual, esperado)

     def test_no_gano(self):
          juego.gano= 0
          esperado = False
          actual = juego.definir_si_gano()
          self.assertEqual(actual, esperado)

if __name__ == '__main__':
     unittest.main()