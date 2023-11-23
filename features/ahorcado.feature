Feature: Juego del Ahorcado

  # Scenario Outline: Elegir opcion elegir por tematica o por nivel
  #   Given Que estoy en la página del Juego del Ahorcado
  #   When Eligo "<opcion>"
  #   And Hago clic en el boton Continuar
  #   Then Deberia ser redirigido a la proxima pagina
  #   And Deberia ver el label "<eleccion>"

  #   Examples: Opciones
  #     | opcion                         | eleccion         |
  #     | Jugar por temáticas            | Elegir temática: |
  #     | Jugar por nivel de dificultad  | Elegir nivel:    |

  # Scenario Outline: Elegir diferentes tematicas o niveles
  #   Given Que estoy en la página del Juego del Ahorcado
  #   When Eligo "<opcion>"
  #   And Hago clic en el boton Continuar
  #   Then Deberia ser redirigido a la proxima pagina
  #   And Deberia ver la opcion "<seleccion>"

  #   Examples: Tematicas
  #     | opcion                         | seleccion   |
  #     | Jugar por temáticas            | Animales    |
  #     | Jugar por temáticas            | Comida      |
  #     | Jugar por temáticas            | Paises      |
  #     | Jugar por temáticas            | Profesiones |
  #     | Jugar por temáticas            | Deportes    |
  #     | Jugar por nivel de dificultad  | Fácil       |
  #     | Jugar por nivel de dificultad  | Medio       |
  #     | Jugar por nivel de dificultad  | Difícil     |

  Scenario: Ingresar letra incorrecta
    Given Que estoy en la página del Juego del Ahorcado
    When Eligo "Jugar por temáticas"
    And Hago clic en el botón Continuar
    Then Debería ser redirigido a la próxima página
    And Debería ver el label "Elegir temática:"

    Given Que estoy en la página Elegir opcion
    When Selecciono la temática "Animales"
    And Hago clic en el botón Comenzar Juego
    Then Debería ser redirigido a la próxima página de juego
    And Debería ver el label "Ingresar letra o palabra:"

    Given Que estoy en la página Jugar
    When Ingreso la letra "X"
    And Hago clic en el botón Adivinar
    Then Debería ver el mensaje de letra incorrecta
    And Debería ver que las vidas disminuyen en 1