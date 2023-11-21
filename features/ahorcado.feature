Feature: Juego del Ahorcado

  Scenario: Elegir opcion elegir por tematica
    Given Que estoy en la página del Juego del Ahorcado
    When Hago clic en el boton Continuar
    Then Deberia ser redirigido a la proxima pagina
    And Deberia ver el label Elegir por temática
