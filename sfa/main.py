import time
import pandas as pd

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from tkinter import filedialog
from docs.credentials import credentials
from tqdm import tqdm

def sfa():
    my_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=my_service)
    
    #Recebe login e senha
    user = credentials.get('user')
    password = credentials.get('password')
    
    # Recebe e trata o arquivo de pesquisa
    # path_cnpj = filedialog.askopenfilename()
    # data = pd.read_excel(path_cnpj, header=None, names=['cnpj', 'Razão Social', 'Adabas'], converters={'cnpj': '{:0>14}'.format})
    # df = pd.DataFrame(data)
    # cnpjs = df.cnpj.to_list()

    # Abre a página do navegador
    browser.get('https://vivo-parceiro-my.force.com/sfa/s/')
    browser.maximize_window()


    try:
        # Toda a parte de login.
        time.sleep(20)
        browser.find_element('xpath', '//*[@id="username"]').send_keys(user)
        browser.find_element('xpath', '//*[@id="password"]').send_keys(password)
        browser.find_element('xpath', '//*[@id="form"]/fieldset/input[4]').click()
        time.sleep(5)
        browser.find_element('xpath', '//*[@id="thePage:j_id2:i:f:pb:pbb:nextAjax"]').click()
        time.sleep(5)
    except:
        pass

    try:
        browser.get('https://vivo-parceiro-my.force.com/sfa/s/clientes')
    except:
        pass

    time.sleep(5)
    cnpjs = ['546546546000155', '00884334000152', '36099905000108']
    for cnpj in tqdm(cnpjs):
        try:
            try:
                time.sleep(5)
                print(cnpj)
                # browser.find_element(By.ID, 'input-14').send_keys(cnpj)
                browser.find_element('xpath', '/html/body/div[3]/div[2]/div/div[1]/div/div/div/div/div/div/div[1]/lightning-input/div/div').click()
                browser.find_element('xpath', '//*[@id="input-48"]').click()
                browser.find_element('xpath', '//*[@id="input-48"]').send_keys(cnpj)

                browser.find_element('xpath', '/html/body/div[3]/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/button').click()
                html_razao = browser.find_element('xpath', 'v/html/body/div[3]/div[2]/div/div[1]/div/div/div/div/div/div[2]/article/div/div/div[1]/div[2]').get_attribute('outerHTML')
                razao = BeautifulSoup(html_razao, 'html.parser').getText()
            except:
                razao = ''

            time.sleep(5)
            for i in range(1, 201):
                try:
                    html_adabas = browser.find_element('xpath', f'/html/body/div[3]/div[2]/div/div[1]/div/div/div/div/div/div[2]/article/div/div/div[4]/div/table/tbody/tr[{i}]/th[2]/div').get_attribute('outerHTML')
                    adabas = BeautifulSoup(html_adabas, 'html.parser').getText()
                    print(i, ' ', adabas, ' ', razao)
                except:
                    print(i, ' deu erro')

        except:
            pass