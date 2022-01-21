# 1 - bibliotecas
from selenium.webdriver.common.by import By
from pages.base_page import BasePage  # recebe as funções da base_page


# 2 - classe


class LoginPage(BasePage):
    # 2.1 - mapeamento dos elemento da pagina
    _username_input = {'by': By.ID, 'value': 'username'}
    _password_input = {'by': By.ID, 'value': 'password'}
    _login_button = {'by': By.CSS_SELECTOR, 'value': 'button.radius'}
    _success_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.success'}
    _failure_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.error'}
    _login_form = {'by': By.ID, 'value': 'login'}

    # 2.2 Inicializador/Construtor(Java)
    def __init__(self, driver):
        self.driver = driver  # instanciando o selenium
        self._entrar('/login')  # abrindo a pagina alvo
        assert self._aparecer(self._login_form)  # validando se o formulpario de login esta visivel

    def com_(self, username, password):
        '''
        #Programação comum - sem PageObjects
        self.driver.find_element(self._username_input['by'],
                                 self._username_input['value']).send_keys(username)
        self.driver.find_element(self._password_input['by'],
                                 self._password_input['value']).send_keys(password)
        self.driver.find_element(self._login_button['by'],
                                 self._login_button['value']).click()'''

        self._escrever(self._username_input, username)
        self._escrever(self._password_input, password)
        self._clicar(self._login_button)

    # 2.3 - açoes realizaveis
    def vejo_mensagem_de_sucesso(self):
        '''
        return self.driver.find_element(self._success_message['by'],
                                 self._success_message['value']).is_displayed()
        '''
        return self._aparecer(self._success_message, 10)


    def vejo_mensagem_de_falha(self):
        '''
        return self.driver.find_element(self._failure_message['by'],
                                    self._failure_message['value']).is_displayed()
        '''
        return self._aparecer(self._failure_message, 10)


    def testar_login_com_sucesso(self, login):
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
