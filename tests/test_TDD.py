import unittest
from src.ahorcado import Ahorcado
from unittest.mock import patch

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
        juego.palabrasIncorrectas.append("tirabuzones")
        esperado = False 
        actual = juego.verificar_repeticion("giacomo2")
        self.assertEqual(actual, esperado)

     def test_repetir_palabras(self):
        juego.palabraAdivinar = "giacomo"
        juego.palabrasIncorrectas.append("tirabuzones")
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
          juego.letrasAdivinadas = ["g", "a"]
          juego.letrasIncorrectas = ["w"]
          esperado = False
          actual = juego.verificar_repeticion_letra("z")
          self.assertEqual(actual, esperado)
    
     def test_repetir_letra_adivinada(self):
          juego.palabraAdivinar = "giacomo"
          juego.letrasAdivinadas = ["g", "a"]
          juego.letrasIncorrectas = ["w"]
          esperado = True
          actual = juego.verificar_repeticion_letra("a")
          self.assertEqual(actual, esperado)
    
     def test_repetir_letra_incorrecta(self):
          juego.palabraAdivinar = "giacomo"
          juego.letrasAdivinadas = ["g", "a"]
          juego.letrasIncorrectas = ["w"]
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

   
# HISTORIA DE USUARIO 3 -- agregar tests
class ImprimoPalabra(unittest.TestCase):
     def test_imprimo(self):
            juego.palabraAdivinar = "giacomo"
            juego.letrasAdivinadas = ["a", "o"]
            esperado = "_ _ a _ o _ o "
            actual = juego.imprimo_palabra()
            self.assertEqual(actual, esperado)
     
     # Mensajes para UI
     def test_mensaje_letra_incorrecta(self):
          letra = "w"
          juego.gano = 0
          juego.letrasIncorrectas = ["a", "w"]
          esperado = f"La letra {letra} es incorrecta. Perdiste 1 vida."
          actual = juego.obtener_mensaje_actual(letra)
          self.assertEqual(actual, esperado)
     
     def test_mensaje_letra_repetida(self):
          letra = "w"
          juego.gano = 0
          juego.letrasIncorrectas = ["m"]
          juego.letrasAdivinadas = ["a", "w"]
          esperado = f"La letra {letra} ya fue ingresada anteriormente."
          actual = juego.obtener_mensaje_actual(letra)
          self.assertEqual(actual, esperado)
     
     def test_mensaje_perdio(self):
          letra = "n"
          juego.palabraAdivinar = "prueba"
          juego.letrasIncorrectas = ["m"]
          juego.letrasAdivinadas = ["a", "w"]
          juego.vidas = 0
          esperado = f"Agotaste todas las vidas. La palabra a adivinar era: {juego.palabraAdivinar}"
          actual = juego.obtener_mensaje_actual(letra)
          self.assertEqual(actual, esperado)
     
     def test_mensaje_gano(self):
          letra = "w"
          juego.letrasIncorrectas = ["m"]
          juego.letrasAdivinadas = ["a"]
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