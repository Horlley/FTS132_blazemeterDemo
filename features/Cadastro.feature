@Cadastro
Feature: Cadastra Usuario

  Scenario: Cadastro com Sucesso
    Given que acesso o site Blazedemo
    When clico em home
    And clico em Register
    Then vejo o formulario de cadastro
    When preencho "Horley" "Illymisystem" "contato@illumi.com.br" "123456"
    And clico no botao Register
    Then Visualizo a mensagem de cofirmacao

  Scenario Outline: Cadastro com Sucesso 02
    Given que acesso o site Blazedemo
    When clico em home
    And clico em Register
    Then vejo o formulario de cadastro
    When preencho "<name>" "<empresa>" "<email>" "<senha>"
    And clico no botao Register
    Then Visualizo a mensagem de cofirmacao
    Examples:
      | name     | empresa      | email         | senha  |
      | JaoM     | System       | mail01@com.br | 123456 |
      | AMaria   | IllumySystem | mail02@com.br | 456887 |
      | LoboMalv | Melhor       | mail03@com.br | 654987 |

#FTS132 - Aula 22 01:00:00