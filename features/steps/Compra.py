import time

from behave import given, when, then
from selenium import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Precisa sempre importar a classe environment
from features import environment

# Método executado antes da feature e serve para chamar passor seguintes
def before_feature(context, feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(
            # Pode incluir outras ações
        )


@given(u'que acesso o site Blazedemo')
def step_impl(context):
    context.driver.get('https://blazedemo.com/')


@when(u'seleciona a cidade de origem como "{origem}"')
def step_impl(context, origem):
    # Mapeia o elemento com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'fromPort')
    # Criar um objeto para permitir selecionar as opções do combo
    objeto_origem = Select(combo_origem)
    # Seleciona o elemento no Combo
    objeto_origem.select_by_visible_text(origem)


@when(u'seleciono a cidade de destino como "{destino}"')
def step_impl(context, destino):
    combo_destino = context.driver.find_element(By.NAME, 'toPort')
    objeto_destino = Select(combo_destino)
    objeto_destino.select_by_visible_text(destino)


@when(u'clico no Find Flights')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()

@then(u'sou direcionado para a pagina de selecao de voos de "{origem}" para "{destino}"')
def step_impl(context, origem, destino):

    resultado_esperado = f'Flights from {origem} to {destino}:'
    assert context.driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/h3[1]').text == resultado_esperado

@when(u'seleciono o primeiro voo')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//div[2]/table/tbody/tr[1]/td[1]/input').click()

@then(u'sou direcionada para a pagina de pagamento')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/p[6]').text == 'Please submit the form below to purchase the flight.'

    print('Passo-07 - sou direcionada para a pagina de pagamento')


@when(u'preencho os dados para o pagamento')
def step_impl(context):
    context.driver.find_element(By.ID, 'inputName').send_keys('Teste')
    print('Passo-08 - preencho os dados para o pagamento')


@when(u'clico no botao Purchase Flight')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn').click()
    print('Passo-09 - clico no botao Purchase Flight')


@then(u'sou direcionado para a pagina de confirmacao')
def step_impl(context):
    assert context.driver.find_element(By.TAG_NAME, 'h1').text == 'Thank you for your purchase today!'
#
@when(u'seleciona de "{origem}" para "{destino}"')
def step_impl(context, origem, destino):
    # Mapeia o elemento com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'fromPort')
    # Criar um objeto para permitir selecionar as opções do combo
    objeto_origem = Select(combo_origem)
    # Seleciona o elemento no Combo
    objeto_origem.select_by_visible_text(origem)

    # Seleciona o Destino
    combo_destino = context.driver.find_element(By.NAME, 'toPort')
    objeto_destino = Select(combo_destino)
    objeto_destino.select_by_visible_text(destino)

    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # 5 - FTS132 - Aula19 1:10:00
