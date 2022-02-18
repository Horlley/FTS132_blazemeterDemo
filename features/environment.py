from selenium import webdriver

# Inicio
def before_all(context):
    # Declarar selenium e instanciar como navegador e apontar o driver
    context.driver = webdriver.Chrome('drivers/chrome/98/chromedriver.exe')
    # Maximinar janela do navegador
    context.driver.maximize_window()
    # Define uma espera para todos os elementos do script
    context.driver.implicitly_wait(10)

# fim
def after_all(context):
    # Desligar/Destruir o objeto do Selenium
    context.driver.quit()

def after_step(context, step):
    print()
