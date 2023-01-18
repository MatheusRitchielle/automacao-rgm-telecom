import time
import pyautogui as gui
import pandas as pd

from tqdm import tqdm
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from tkinter import filedialog
from selenium.common.exceptions import NoSuchElementException

def synergy_client():
    # path_cnpj = filedialog.askopenfilename()
    # file_cnpj = open(path_cnpj, 'r')
    # cnpjs = file_cnpj.readlines()
    client_type = ''
    my_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=my_service)

    browser.get('https://pd.simplifiquevivoemp.com.br/Simulacoes.aspx')
    browser.maximize_window()
    time.sleep(20)

    browser.find_element('xpath', '//*[@id="username"]').send_keys('80842561')
    browser.find_element('xpath', '//*[@id="password"]').send_keys('Tel@123456')
    time.sleep(20)

    browser.find_element('xpath', '//*[@id="form"]/fieldset/input[4]').click()
    browser.find_element('xpath', '//*[@id="email"]').click()
    browser.find_element('xpath', '//*[@id="form"]/fieldset/input').click()
    time.sleep(45)
    browser.find_element('xpath', '//*[@id="form"]/fieldset/input').click()

    browser.find_element('xpath', '//*[@id="spn-simuladores"]').click()
    browser.find_element('xpath', '//*[@id="btnMovelOfertasPreAprovadas"]').click()

    browser.find_element('xpath', '//*[@id="MainContent_lbNovaSimulacao"]').click()
#                      sim                nao                    nao                     sim                sim                 sim
    cnpjs = ['26.619.437/0001-00', '00.000.036/9316-32', '11.091.215/0001-81', '04.073.818/0001-95', '12.945.474/0001-95', '36.345.663/0001-95', '01.046.360/0001-97', '00.131.738/0001-98', '11.067.093/0001-98', '01.273.914/0001-99', '04.430.111/0001-99', '24.158.383/0001-99', '39.505.136/0001-99']

    time.sleep(35)
    for cnpj in tqdm(cnpjs):
        try:
            time.sleep(2)
            browser.find_element('xpath', '//*[@id="ucPesquisarCliente_txtPesquisarDocumento"]').clear()
            browser.find_element('xpath', '//*[@id="ucPesquisarCliente_txtPesquisarDocumento"]').send_keys(cnpj)
            browser.find_element('xpath', '//*[@id="ucPesquisarCliente_lbPesquisar"]').click()

            time.sleep(5)
            if browser.find_element(By.CSS_SELECTOR, ".text-primary > span"):
                client_type = 'Planta'
            elif browser.find_element(By.CSS_SELECTOR, ".text-success > span"):
                client_type = 'Fresh'
            elif browser.find_element(By.CSS_SELECTOR, ".text-info > span"):
                client_type = 'Sinergia'
            elif browser.find_element(By.CSS_SELECTOR, ".text-warning > span"):
                client_type = 'Prioritario'
            elif browser.find_element(By.CSS_SELECTOR, ".text-danger > span"):
                client_type = 'PorOut'

            customer_table = browser.find_element(by=By.ID, value='ucPesquisarCliente_gvClientes').get_attribute('outerHTML')
            soup_customer = BeautifulSoup(customer_table, 'html.parser')
            empresas = soup_customer.find(name='table')
            df_table = pd.read_html(str(empresas))[0]
            df_table.to_csv('sinergia.csv', encoding='UTF-8', header=False, sep=';', index=False)

            time.sleep(4)
            gui.click(1083, 609)

            time.sleep(2)
            gui.click(1049, 467)
            time.sleep(4)

            browser.find_element('xpath', '//*[@id="MainContent_lkbAbrirCreditoC1"]').click()
            time.sleep(2)
            htmlContent_situation_detail = browser.find_element(by=By.ID, value='MainContent_UC_CreditoC1_lblCreditoC1').get_attribute('outerHTML')
            soup_credit = BeautifulSoup(htmlContent_situation_detail, 'html.parser').getText()

            df_table = pd.read_html(str(empresas))[0]
            df_table['Crédito'] = soup_credit
            df_table['Cliente'] = client_type

            file = open('C:\Matheus\www\\automacao-rgm-receita\simplifique\simplifique.csv', 'a')
            file.write(df_table)
            file.close()
            df_table.to_csv('sinergia.csv', encoding='UTF-8', header=False, sep=';', index=False)

            print(df_table)
            browser.back()
        except:
            print('CNPJ não encontrado')

    time.sleep(2)
    print('Ocorreu um erro inesperado!')