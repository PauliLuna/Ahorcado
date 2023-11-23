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

  Scenario: Ingresar letra incorrecta
    Given Que estoy en la página del Juego del Ahorcado
    When Eligo "Jugar por temáticas"
    And Hago clic en el boton Continuar
    Then Deberia ser redirigido a la proxima pagina
    And Deberia ver el label "Elegir temática:"

    Given Que estoy en la pagina Elegir opcion
    When Selecciono la tematica "Animales"
    And Hago clic en el boton Comenzar Juego
    Then Deberia ser redirigido a la proxima pagina de juego
    And Deberia ver el label "Ingresar letra o palabra:"

    Given Que estoy en la pagina Jugar
    When Ingreso la letra "X"
    And Hago clic en el boton Adivinar
    Then Deberia ver el mensaje de letra incorrecta
    And Deberia ver que las vidas disminuyen en 1
  
  Scenario: Ingresar letra repetida
    Given Que estoy en la página del Juego del Ahorcado
    When Eligo "Jugar por temáticas"
    And Hago clic en el boton Continuar
    Then Deberia ser redirigido a la proxima pagina
    And Deberia ver el label "Elegir temática:"

    Given Que estoy en la pagina Elegir opcion
    When Selecciono la tematica "Animales"
    And Hago clic en el boton Comenzar Juego
    Then Deberia ser redirigido a la proxima pagina de juego
    And Deberia ver el label "Ingresar letra o palabra:"

    Given Que estoy en la pagina Jugar
    When Ingreso la letra "X"
    And Hago clic en el boton Adivinar
    Then Deberia ver el mensaje de letra incorrecta
    And Deberia ver que las vidas es 6

    Given Que estoy en la pagina Jugar
    When Ingreso la letra "X"
    And Hago clic en el boton Adivinar
    #Then Deberia ver el mensaje de letra repetida
    Then Deberia ver que las vidas es 6