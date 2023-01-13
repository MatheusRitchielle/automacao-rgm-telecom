import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://www.procep.com.br')
navegador.maximize_window()

arq = open('C:\Matheus\www\\automacao-rgm-receita\download\pasta ceps\ceps.txt', 'r')
linhas = arq.readlines()

for linha in linhas:
    cep = str(linha)
    print('Iniciando CEP: ' + cep)
    time.sleep(3)
    navegador.find_element('xpath',  '//*[@id="navbarSupportedContent"]/form/input[2]').send_keys(cep)
    time.sleep(3)
    navegador.find_element(By.XPATH, "//input[@name=\'search\']").send_keys(Keys.ENTER)
    time.sleep(3)
    htmlContent = navegador.find_element(By.CSS_SELECTOR, '.col-md-8 > .mt-4').get_attribute('outerHTML')
    soup = BeautifulSoup(htmlContent, 'html.parser').getText()

    file = open('C:\Matheus\www\\automacao-rgm-receita\download\pasta cnpjs\cnpjs.csv', 'a')
    file.write(soup)
    file.close()

    print('Fim CEP: ' + cep)

print('Fim do programa:')