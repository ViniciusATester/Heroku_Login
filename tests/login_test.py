import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    # è uma variavel local para armazenar o caminho do chromedriver
    # '_' antes da variavel significa que ela so existe aqui
    # _chromedriver = 'vendor/chromedriver.exe'
    _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')

    if os.path.isfile(_chromedriver):
        # '_' depois da variavel driver , significa que qur não quero que ela
        # se confunda com outro driver que possa aparecer
        # If- Se existe um chromedrivr dentro do projeto, instancie com ele
        driver_ = webdriver.Chrome(_chromedriver)
    else:
        # Else - se não existe, tente usar um chromedriver publico no ambiente
        driver_ = webdriver.Chrome()

    def quit():
        driver_.quit()

    # sinalizando o fim da execução do ambiente
    request.addfinalizer(quit)
    return driver_


# Comoera os passos do jeio simples
'''    
    def old_test_login_valido(driver):
    driver.get('https://the-internet.herokuapp.com/login')
    driver.find_element(By.ID, 'username').send_keys('tomsmith')
    driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
    driver.find_element(By.CSS_SELECTOR, 'button.radius').click()
    assert driver.find_element(By.CSS_SELECTOR, 'div.flash.success').is_displayed()
   '''


def testar_login_com_sucesso(login):
    # Preencher o usuario, senha e clicar no botao
    login.com_('tomsmith', 'SuperSecretPassword!')
    # validar message
    assert login.vejo_mensagem_de_sucesso()


def testar_login_com_usuario_invalido(self, login):
    # Preencher o usuario, senha e clicar no botao
    login.com_('asdedasdead', 'SuperSecretPassword!')
    # validar message
    assert login.vejo_mensagem_de_falha()


def testar_login_com_senha_invalida(self, login):
    # Preencher o usuario, senha e clicar no botao
    login.com_('tomsmith', 'xpto3456')
    # validar message
    assert login.vejo_mensagem_de_falha()
