import time
import pyautogui as gui

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def synergy_client():
    cnpj = '29.217.055/0001-30'
    my_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=my_service)

    browser.get('https://pd.simplifiquevivoemp.com.br/Simulacoes.aspx')
    browser.maximize_window()
    time.sleep(20)

    browser.find_element('xpath', '//*[@id="username"]').send_keys('80842561')
    browser.find_element('xpath', '//*[@id="password"]').send_keys('y5RHwA@f')
    time.sleep(20)

    browser.find_element('xpath', '//*[@id="form"]/fieldset/input[4]').click()
    browser.find_element('xpath', '//*[@id="email"]').click()
    browser.find_element('xpath', '//*[@id="form"]/fieldset/input').click()
    time.sleep(45)
    browser.find_element('xpath', '//*[@id="form"]/fieldset/input').click()

    browser.find_element('xpath', '//*[@id="spn-simuladores"]').click()
    browser.find_element('xpath', '//*[@id="btnMovelOfertasPreAprovadas"]').click()

    browser.find_element('xpath', '//*[@id="MainContent_lbNovaSimulacao"]').click()

    time.sleep(3)
    gui.hotkey('tab', 'tab')
    gui.hotkey('space')
    time.sleep(3)
    browser.find_element('xpath', '//*[@id="MainContent_lbValidaCriarSimulacao"]').click()

    browser.find_element('xpath', '//*[@id="ucPesquisarCliente_txtPesquisarDocumento"]').send_keys(cnpj)
    browser.find_element('xpath', '//*[@id="ucPesquisarCliente_lbPesquisar"]').click()

    browser.find_element('xpath', '//*[@id="ucPesquisarCliente_gvClientes"]/tbody/tr/td[1]/a/span/span').click()
    # browser.find_element('xpath', '//*[@id="ucPesquisarCliente_gvClientes_lbSelecionarCliente_0"]').click()

    browser.find_element('xpath', '//*[@id="ucPesquisarCliente_lbConfirmarCliente"]').click()

    htmlContent = browser.find_element('xpath', '//*[@id="MainContent_lblSemaforo"]').get_attribute('outerHTML')
    soup = BeautifulSoup(htmlContent, 'html.parser').getText()
    browser.find_element('xpath', '//*[@id="pnlBotaoSimplifique"]/a/img').click()
    print(cnpj + ';' + soup)


