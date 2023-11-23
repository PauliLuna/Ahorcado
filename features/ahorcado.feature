Feature: Juego del Ahorcado

  Scenario Outline: Elegir opcion elegir por tematica o por nivel
    Given Que estoy en la página del Juego del Ahorcado
    When Eligo "<opcion>"
    And Hago clic en el boton Continuar
    Then Deberia ser redirigido a la proxima pagina
    And Deberia ver el label "<eleccion>"

    Examples: Opciones
      | opcion                         | eleccion         |
      | Jugar por temáticas            | Elegir temática: |
      | Jugar por nivel de dificultad  | Elegir nivel:    |

  Scenario Outline: Elegir diferentes tematicas o niveles
    Given Que estoy en la página del Juego del Ahorcado
    When Eligo "<opcion>"
    And Hago clic en el boton Continuar
    Then Deberia ser redirigido a la proxima pagina
    And Deberia ver la opcion "<seleccion>"

    Examples: Tematicas
      | opcion                         | seleccion   |
      | Jugar por temáticas            | Animales    |
      | Jugar por temáticas            | Comida      |
      | Jugar por temáticas            | Paises      |
      | Jugar por temáticas            | Profesiones |
      | Jugar por temáticas            | Deportes    |
      | Jugar por nivel de dificultad  | Fácil       |
      | Jugar por nivel de dificultad  | Medio       |
      | Jugar por nivel de dificultad  | Difícil     |