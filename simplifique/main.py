import time
import pandas as pd

from pathlib import Path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from tkinter import filedialog
from docs.credentials import credentials

def synergy_client():
    client_type = ''

    user = credentials.get('user')
    password = credentials.get('password')

    path_cnpj = filedialog.askopenfilename()
    cnpjs = open(path_cnpj, 'r').read().split('\n')

    my_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=my_service)
    browser.get('https://pd.simplifiquevivoemp.com.br/Simulacoes.aspx')
    browser.maximize_window()
    try:
        time.sleep(20)
        browser.find_element('xpath', '//*[@id="username"]').send_keys(user)
        browser.find_element('xpath', '//*[@id="password"]').send_keys(password)
        time.sleep(20)
        browser.find_element('xpath', '//*[@id="form"]/fieldset/input[4]').click()

        browser.find_element('xpath', '//*[@id="email"]').click()
        browser.find_element('xpath', '//*[@id="form"]/fieldset/input').click()

        time.sleep(45)
        browser.find_element('xpath', '//*[@id="form"]/fieldset/input').click()
        browser.find_element('xpath', '//*[@id="spn-simuladores"]').click()
        browser.find_element('xpath', '//*[@id="btnMovelOfertasPreAprovadas"]').click()
        browser.find_element('xpath', '//*[@id="MainContent_lbNovaSimulacao"]').click()
    except:
        pass

    time.sleep(35)
    i = 0
    for cnpj in cnpjs:
        i += 1
        if i % 15 == 0:
            time.sleep(300)
        try:
            time.sleep(2)
            browser.find_element('xpath', '//*[@id="ucPesquisarCliente_txtPesquisarDocumento"]').clear()
            browser.find_element('xpath', '//*[@id="ucPesquisarCliente_txtPesquisarDocumento"]').send_keys(cnpj)
            browser.find_element('xpath', '//*[@id="ucPesquisarCliente_lbPesquisar"]').click()

            time.sleep(5)
            try:
               if browser.find_element(By.CSS_SELECTOR, ".text-info > span"):
                client_type = 'Sinergia'
            except:
                pass
            try:
               if browser.find_element(By.CSS_SELECTOR, ".text-success > span"):
                client_type = 'Fresh'
            except:
                pass
            try:
                if browser.find_element(By.CSS_SELECTOR, ".text-primary > span"):
                    client_type = 'Planta'
            except:
                pass
            try:
                if browser.find_element(By.CSS_SELECTOR, ".text-warning > span"):
                    client_type = 'Prioritario'
            except:
                pass
            try:
                if browser.find_element(By.CSS_SELECTOR, ".text-danger > span"):
                    client_type = 'PorOut'
            except:
                pass

            filepath = Path(f'C:\Matheus\www\\automacao-rgm-telecom\simplifique\consulta\\{i}.csv')
            filepath.parent.mkdir(parents=True, exist_ok=True)

            customer_table = browser.find_element(by=By.ID, value='ucPesquisarCliente_gvClientes').get_attribute('outerHTML')
            soup_customer = BeautifulSoup(customer_table, 'html.parser')
            empresas = soup_customer.find(name='table')
            df_table = pd.read_html(str(empresas))[0]
            df_table.to_csv(filepath, encoding='UTF-8', header=False, sep=';', index=False)

            time.sleep(2)
            browser.find_element('xpath',  '//*[@id="ucPesquisarCliente_gvClientes_lbSelecionarCliente_0"]').click()

            time.sleep(4)
            browser.find_element('xpath', '//*[@id="ucPesquisarCliente_lbConfirmarCliente"]').click()

            time.sleep(4)
            browser.find_element('xpath', '//*[@id="MainContent_lkbAbrirCreditoC1"]').click()

            time.sleep(4)
            htmlContent_situation_detail = browser.find_element(by=By.ID, value='MainContent_UC_CreditoC1_lblCreditoC1').get_attribute('outerHTML')
            soup_credit = BeautifulSoup(htmlContent_situation_detail, 'html.parser').getText()

            df_table['Cliente'] = client_type
            df_table['Crédito'] = soup_credit

            df_table.to_csv(filepath, encoding='UTF-8', header=False, sep=';', index=False)
            browser.back()
        except:
            file = open('C:\Matheus\www\\automacao-rgm-telecom\simplifique\consulta\error.txt', 'a')
            file.write('\n' + cnpj)
            file.close()

    print('Programa finalizado')
