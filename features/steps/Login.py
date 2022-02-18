
from behave import when, then
from selenium.webdriver.common.by import By


@when(u'clico em home')
def step_impl(context):

    context.driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
    # assert context.driver.find_element(By.XPATH, "//div[@class='panel-heading']").text() == 'Login'

@when(u'preencho "{email}" "{password}" e clico no botao Login')
def step_impl(context, email, password):
    context.driver.find_element(By.ID, 'email').send_keys(email)
    context.driver.find_element(By.ID, 'password').send_keys(password)

    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()

@then(u'Visualizo a mensagem de cofirmacao')
def step_impl(context):

    assert context.driver.find_element(By.CSS_SELECTOR, 'div.code').text == '419'
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.message').text == 'Page Expired'