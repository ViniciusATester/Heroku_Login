#import os
import pytest
#from selenium import webdriver
from pages import login_page



@pytest.fixture
def login(driver): # deixou de receber requests e passou receber diretamente o driver
    return login_page.LoginPage(driver)  # instanciando a classe LoginPage e passando o Selenium



# Como era os passos do jeio simples
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


def testar_login_com_usuario_invalido(login):
    # Preencher o usuario, senha e clicar no botao
    login.com_('asdedasdead', 'SuperSecretPassword!')
    # validar message
    assert login.vejo_mensagem_de_falha()


def testar_login_com_senha_invalida(login):
    # Preencher o usuario, senha e clicar no botao
    login.com_('tomsmith', 'xpto3456')
    # validar message
    assert login.vejo_mensagem_de_falha()
