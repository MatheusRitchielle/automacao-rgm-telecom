import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from tkinter import filedialog

def find_cnpjs():
    my_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=my_service)
    browser.get('https://www.procep.com.br')
    browser.maximize_window()

    path_cep = filedialog.askopenfilename()
    file_cep = open(path_cep, 'r')
    lines = file_cep.readlines()

    for line in lines:
        cep = str(line)
        time.sleep(3)
        try:
            browser.find_element('xpath', '//*[@id="navbarSupportedContent"]/form/input[2]').send_keys(cep)
            time.sleep(3)
            browser.find_element(By.XPATH, "//input[@name=\'search\']").send_keys(Keys.ENTER)
            time.sleep(3)
            htmlContent = browser.find_element(By.CSS_SELECTOR, '.col-md-8 > .mt-4').get_attribute('outerHTML')
            soup = BeautifulSoup(htmlContent, 'html.parser').getText()
        except:
            print('Não encontramos o CEP: ' + cep)

        try:
            file = open('/download/pasta cnpjs/cnpjs.csv', 'a')
            file.write(soup)
            file.close()
        except:
            print('Não foi possível salvar o CEP: ' + cep)
    print('Consulta realizada com sucesso!')