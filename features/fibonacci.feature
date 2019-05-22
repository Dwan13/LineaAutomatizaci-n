Feature: User-Defined Datatype as Step Parameter

  Scenario Outline: Calcular valor de valores par e impar
    Given Yo tengo una serie de fibonacci
    When Agregando "{x:g}"
    Then La serie de fibonacci retorna"<fibo>"

    Examples:
        |  x    | fibo   |
        |  5    |  5     |
        |  8    |  21    |
