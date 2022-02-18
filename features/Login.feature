@Login
Feature: Efetuar login na pagina Blazemeter

  Scenario: Login com sucesso
    Given que acesso o site Blazedemo
    When clico em home
    And preencho "vamos@mail.com" "123456" e clico no botao Login
    Then Visualizo a mensagem de cofirmacao

  Scenario Outline: Login com sucesso
    Given que acesso o site Blazedemo
    When clico em home
    And preencho "<email>" "<senha>" e clico no botao Login
    Then Visualizo a mensagem de cofirmacao
    Examples:

      | email          | senha  |
      | teste@mail.com | 123456 |
      | mais1@mail.com | 789555 |
      | outro@mail.com | 741553 |
