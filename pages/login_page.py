#1 - bibliotecas

#2 - classe
from selenium.webdriver.common.by import By


class LoginPage():
# 2.1 - mapeamento dos elemento da pagina
    _username_input = {'by': By.ID, 'value': 'username'}
    _password_input = {'by': By.ID, 'value': 'password'}
    _login_button = {'by': By.CSS_SELECTOR, 'value': 'button.radius'}
    _success_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.success'}
    _failure_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.error'}



#2.2 Inicializador/Construtor(Java)
    def __init__(self, driver):
        self.driver.get('https://the-internet.herokuapp.com/login')

    def com_(self, username, password):
        self.driver.find_element(self._username_input['by'],
                                 self._username_input['value']).send_keys(username)
        self.driver.find_element(self._password_input['by'],
                                 self._password_input['value']).send_keys(password)
        self.driver.find_element(self._login_button['by'],
                                 self._login_button['value']).click()



#2.3 - açoes realizaveis
    def vejo_mensagem_de_sucesso(self):
        return self.driver.find_element(self._success_message['by'],
                                 self._success_message['value']).is_displayed()


    def vejo_mensagem_de_falha(self):
        return self.driver.find_element(self._failure_message['by'],
                                    self._failure_message['value']).is_displayed()



