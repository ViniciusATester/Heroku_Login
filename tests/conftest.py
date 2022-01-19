import os

import pytest
from selenium import webdriver
from selenium.webdriver import firefox

from . import config


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
        defualt='saucelabs',
        help='Onde vamos executar nossos testes: localhost ou saucelabs'
    )
    parser.addoption(
        '--browser',
        action='store',
        defualt='chrome',
        help='O nome do navegador utilizado nos testes'
    )
    parser.addoption(
        '--browserversion',
        action='store',
        defualt='96.0',
        help='Versao do browser'
    )
    parser.addoption(
        '--platform',
        action='store',
        defualt='Windows 10',
        help='Sistema Operacional a ser utilizado durante os testes(apenas no saucelabs)'
    )

@pytest.fixture
def driver(request):
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
            'sauce:options':{
                'name': test_name
            }
        }
        _credentials = os.environ['oauth-viniciusat.13-31538'] + ':' + os.environ['eed6ea3a-8178-45ce-9ce8-c2229d1c6458']
        _url = 'https//' + _credentials + '@ondemand.us-west-1.saucelabs.com:443/wd/hub'
        driver_ = webdriver.Remote(_url, capabilities)
    else: # execução local/ localhost
        if config.browser == 'chrome':
            _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')
            if os.path.isfile(_chromedriver):
                driver_ = webdriver.Chrome(_chromedriver)
            else:
                driver_ = webdriver.Chrome()
        elif config.browser == firefox:
            _geckodriver = os.path.join(os.getcwd(), 'vendor', 'geckodriver.exe')
            if os.path.isfile(_geckodriver):
                driver_ = webdriver.Firefox(_geckodriver)
            else:
                driver_ = webdriver.Firefox()
