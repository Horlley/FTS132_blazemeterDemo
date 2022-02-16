Feature: Compra de passagem Aerea
  # Descreve uma compra pelo site Blazedemo

  Scenario: De Sao Paulo a Roma
    Given que acesso o site Blazedemo
    When seleciona a cidade de origem como "São Paolo"
    And seleciono a cidade de destino como "Roma"
    And clico no Find Flights
    Then sou direcionado para a pagina de selecao de voos
    When seleciono o primeiro voo
    Then sou direcionada para a pagina de pagamento
    When preencho os dados para o pagamento
    And clico no botao Purchase Flight
    Then sou direcionado para a pagina de confirmacao

  Scenario: De Sao Paulo a Roma Compacto
    Given que acesso o site Blazedemo
    When seleciona de "São Paolo" para "Roma"
    Then sou direcionado para a pagina de selecao de voos
    When seleciono o primeiro voo
    Then sou direcionada para a pagina de pagamento
    When preencho os dados para o pagamento
    And clico no botao Purchase Flight
    Then sou direcionado para a pagina de confirmacao

  # 5.FTS132 - Aula 19
  # pip install behave