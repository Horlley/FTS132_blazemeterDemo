from behave import given, when, then
from selenium.webdriver.common.by import By


@when(u'clico em Register')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[1]/nav[1]/div[1]/div[2]/ul[2]/li[2]").click()

    print()


@then(u'vejo o formulario de cadastro')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "div.panel-heading").text == 'Register'
    print()


@when(u'preencho "{name}" "{empresa}" "{email}" "{senha}"')
def step_impl(context, name, empresa, email, senha):
    context.driver.find_element(By.ID, 'name').send_keys(name)
    context.driver.find_element(By.ID, 'company').send_keys(empresa)
    context.driver.find_element(By.ID, 'email').send_keys(email)
    context.driver.find_element(By.ID, 'password').send_keys(senha)
    context.driver.find_element(By.ID, 'password-confirm').send_keys(senha)

@when(u'clico no botao Register')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    print()
