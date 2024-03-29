import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from tkinter import filedialog
from tqdm import tqdm

def find_cnpjs():
    link = 'https://www.procep.com.br'
    my_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=my_service)
    browser.get(link)
    browser.maximize_window()

    path_cep = filedialog.askopenfilename()
    ceps = open(path_cep, 'r').read().split('\n')

    for cep in tqdm(ceps):
        cep = str(cep)
        time.sleep(3)
        try:
            browser.find_element('xpath', '//*[@id="navbarSupportedContent"]/form/input[2]').send_keys(cep)
            time.sleep(3)
            browser.find_element(By.XPATH, "//input[@name=\'search\']").send_keys(Keys.ENTER)
            time.sleep(3)
            htmlContent = browser.find_element(By.CSS_SELECTOR, '.col-md-8 > .mt-4').get_attribute('outerHTML')
            soup = BeautifulSoup(htmlContent, 'html.parser').getText()
            file = open('consulta-cnpjs-procep.txt', 'a')
            file.write(soup)
            file.close()
        except:
            print('Erro ao consultar o CEP: ' + cep)

    print('Consulta realizada com sucesso!')