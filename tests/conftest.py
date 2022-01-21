import os

import pytest
from selenium import webdriver
from selenium.webdriver import firefox

from . import config, credentials


def pytest_addoption(parser):
    parser.addoption(
        '--baseurl',
        action='store',
        default='https://the-internet.herokuapp.com',
        help='url base da aplicacao alvo do teste'
    )
    parser.addoption(
        '--host',
        action='store',
        default='saucelabs',
        help='Onde vamos executar nossos testes: localhost ou saucelabs'
    )
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='O nome do navegador utilizado nos testes'
    )
    parser.addoption(
        '--browserversion',
        action='store',
        default='96.0',
        help='Versao do browser'
    )
    parser.addoption(
        '--platform',
        action='store',
        default='Windows 10',
        help='Sistema Operacional a ser utilizado durante os testes(apenas no saucelabs)'
    )

@pytest.fixture
def driver(request): #Inicialização dos testte - similar a um before / Setup
    config.baseurl = request.config.getoption('--baseurl')
    config.host = request.config.getoption('--host')
    config.browser = request.config.getoption('--browser')
    config.browserversion = request.config.getoption('--browserversion')
    config.platform = request.config.getoption('--platform')

    if config.host == 'saucelabs':
        test_name = request.node.name #nome do teste
        capabilities = {
            'browserName': config.browser,
            'browserVersion': config.browserversion,
            'platformName': config.platform,
            'sauce:options': {
                'name': test_name
            }
        }
       # _credentials = os.environ['oauth-viniciusat.13-31538'] + ':' + os.environ['eed6ea3a-8178-45ce-9ce8-c2229d1c6458']

       # _credentials = credentials.SAUCE_USERNAME + ':' + credentials.SAUCE_ACCESS_KEY
       # _url = 'https//' + _credentials + '@ondemand.us-west-1.saucelabs.com:443/wd/hub'
        #outra forma de usar as credenciais chamendo por um arquivo


        _url = 'https://oauth-viniciusat.13-31538:eed6ea3a-8178-45ce-9ce8-c2229d1c6458@ondemand.us-west-1.saucelabs.com:443/wd/hub' #primeiro modo de execução
        driver_ = webdriver.Remote(_url, capabilities)
    else: # execução local/ localhost
        if config.browser == 'chrome':
            _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')
            if os.path.isfile(_chromedriver):
                driver_ = webdriver.Chrome(_chromedriver)
            else:
                driver_ = webdriver.Chrome()
        elif config.browser == 'firefox':
            _geckodriver = os.path.join(os.getcwd(), 'vendor', 'geckodriver.exe')
            if os.path.isfile(_geckodriver):
                driver_ = webdriver.Firefox(_geckodriver)
            else:
                driver_ = webdriver.Firefox()

    def quit(): # Finalização dos testes - similar ap After ou TearDown
        # sinalização de passou ou falhou conforme o retorno da requisição
        sauce_result = 'failed' if request.node.rep_call.failed else 'passed'
        driver_.execute_script('sauce:job-result={}'.format(sauce_result))
        driver_.quit()

    request.addfinalizer(quit)
    return driver_

@pytest.hookimpl(hookwrapper=True, tryfirst=True) # Implementação do gatilho de comunicação com SL
def pytest_runtest_makereport(item, call):
    # parametors para fereação do relatorio / informçoes dos resultados
    outcome = yield
    rep = outcome.get_result()

    #definir atributos para o relatorio
    setattr(item, 'rep_' + rep.when, rep)