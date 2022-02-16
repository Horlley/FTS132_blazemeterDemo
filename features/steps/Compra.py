from behave import given, when, then

@given(u'que acesso o site Blazedemo')
def step_impl(context):
    print('Passo-01 - que acesso o site Blazedemo')


@when(u'seleciona a cidade de origem como "São Paolo"')
def step_impl(context):
    print('Passo-02 - seleciona a cidade de origem como "São Paolo')


@when(u'seleciono a cidade de destino como "Roma"')
def step_impl(context):
    print('Passo-03 - seleciono a cidade de destino como "Roma')


@when(u'clico no Find Flights')
def step_impl(context):
    print('Passo-04 - clico no Find Flights')


@then(u'sou direcionado para a pagina de selecao de voos')
def step_impl(context):
    print('Passo-05 - sou direcionado para a pagina de selecao de voos')


@when(u'seleciono o primeiro voo')
def step_impl(context):
    print('Passo-06 - seleciono o primeiro voo')


@then(u'sou direcionada para a pagina de pagamento')
def step_impl(context):
    print('Passo-07 - sou direcionada para a pagina de pagamento')


@when(u'preencho os dados para o pagamento')
def step_impl(context):
    print('Passo-08 - preencho os dados para o pagamento')


@when(u'clico no botao Purchase Flight')
def step_impl(context):
    print('Passo-09 - clico no botao Purchase Flight')


@then(u'sou direcionado para a pagina de confirmacao')
def step_impl(context):
    print('Passo-10 - sou direcionado para a pagina de confirmacao')


@when(u'seleciona de "São Paolo" para "Roma"')
def step_impl(context):
    print('Passo-02C - seleciona de Origem e Destino')