
from behave import when, then
from selenium.webdriver.common.by import By

@when(u'clico no link destination of the week the Beach')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[contains(text(),'destination of the week! The Beach!')]").click()


@then(u'vejo a promocao da semana')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div.container').text == 'Destination of the week: Hawaii !'
    context.driver.find_element(By.XPATH, "//img[@class='img-rounded']").get_attribute('src') == 'assets/vacation.jpg'
