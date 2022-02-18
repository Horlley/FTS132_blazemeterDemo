@compra_passagem
Feature: Compra de passagem Aerea
  # Descreve uma compra pelo site Blazedemo

  Scenario: De Sao Paulo a Roma
    Given que acesso o site Blazedemo
    When seleciona a cidade de origem como "São Paolo"
    And seleciono a cidade de destino como "Rome"
    And clico no Find Flights
    Then sou direcionado para a pagina de selecao de voos de "São Paolo" para "Rome"
    When seleciono o primeiro voo
    Then sou direcionada para a pagina de pagamento
    When preencho os dados para o pagamento
    And clico no botao Purchase Flight
    Then sou direcionado para a pagina de confirmacao

  Scenario: De Boston a Berlin Compacto
    Given que acesso o site Blazedemo
    When seleciona de "Boston" para "Berlin"
    Then sou direcionado para a pagina de selecao de voos de "Boston" para "Berlin"
    When seleciono o primeiro voo
    Then sou direcionada para a pagina de pagamento
    When preencho os dados para o pagamento
    And clico no botao Purchase Flight
    Then sou direcionado para a pagina de confirmacao

  Scenario Outline: De origem a destino
    Given que acesso o site Blazedemo
    When seleciona de "<origem>" para "<destino>"
    Then sou direcionado para a pagina de selecao de voos de "<origem>" para "<destino>"
    When seleciono o primeiro voo
    Then sou direcionada para a pagina de pagamento
    When preencho os dados para o pagamento
    And clico no botao Purchase Flight
    Then sou direcionado para a pagina de confirmacao

    Examples:
      | origem        | destino     |
      | Philadelphia  | Buenos Aires|
      | Paris         | New York    |
      | San Diego     | Cairo       |

  # 7 - FTS132 - Aula 21 =



  # 5.FTS132 - Aula 19
  # pip install behave