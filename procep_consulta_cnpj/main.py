import pandas as pd

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from tkinter import filedialog
from tqdm import tqdm

def find_cnpj():

    path_cnpj = filedialog.askopenfilename()

    data = pd.read_excel(
        path_cnpj,
        header=None,
        names=['CNPJ', 'RAZÃO SOCIAL', 'MATRIZ || FILIAL', 'TELEFONE', 'EMAIL',
               'SITUAÇÃO CADASTRAL', 'DATA DE ABERTURA', 'ULTIMA ATUALIZAÇÃO',
               'ENDEREÇO', 'CIDADE | UF', 'CEP'],
        converters={'CNPJ': '{:0>14}'.format})

    df = pd.DataFrame(data)
    cnpjs = df.CNPJ.to_list()

    my_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=my_service)

    # Abre a página do navegador
    browser.get('https://www.informecadastral.com.br/')
    browser.maximize_window()

    i = 0
    for cnpj_lista in tqdm(cnpjs):
        try:
            browser.find_element('xpath', '//*[@id="cnpj"]').send_keys(cnpj_lista)
            browser.find_element('xpath', '// *[ @ id = "formSearch"] / div / button / span[1]').click()
            try:
                html_cnpj = browser.find_element('xpath', '/html/body/div/div[2]/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/p').get_attribute('outerHTML')
                cnpj = BeautifulSoup(html_cnpj, 'html.parser').getText()
            except:
                cnpj = ''
            try:
                html_razao = browser.find_element('xpath', '/html/body/div/div[2]/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/p').get_attribute('outerHTML')
                razao = BeautifulSoup(html_razao, 'html.parser').getText()
            except:
                razao = ''
            try:
                html_matriz_filial = browser.find_element('xpath', '/html/body/div/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[1]/p').get_attribute('outerHTML')
                matriz_filial = BeautifulSoup(html_matriz_filial, 'html.parser').getText()
            except:
                matriz_filial = ''
            try:
                html_situa = browser.find_element('xpath', '/html/body/div/div[2]/div/div/div[3]/div[1]/div[2]/div[3]/div[1]/p/span').get_attribute('outerHTML')
                situa = BeautifulSoup(html_situa, 'html.parser').getText()
            except:
                situa = ''
            try:
                html_dt_abertura = browser.find_element('xpath', '/html/body/div/div[2]/div/div/div[3]/div[1]/div[2]/div[5]/div[1]/p').get_attribute('outerHTML')
                dt_abertura = BeautifulSoup(html_dt_abertura, 'html.parser').getText()
            except:
                dt_abertura = ''
            try:
                html_dt_ult_atualizacao = browser.find_element('xpath', '/html/body/div/div[2]/div/div/div[3]/div[1]/div[2]/div[6]/div[2]/p').get_attribute('outerHTML')
                dt_ult_atualizacao = BeautifulSoup(html_dt_ult_atualizacao, 'html.parser').getText()
            except:
                dt_ult_atualizacao = ''
            try:
                html_endereco = browser.find_element('xpath', '/html/body/div/div[2]/div/div/div[3]/div[2]/div[2]/div[1]/div/p').get_attribute('outerHTML')
                endereco = BeautifulSoup(html_endereco, 'html.parser').getText()
            except:
                endereco = ''
            try:
                html_cep = browser.find_element('xpath',  '/html/body/div/div[2]/div/div/div[3]/div[2]/div[2]/div[2]/div[2]/p').get_attribute('outerHTML')
                cep = BeautifulSoup(html_cep, 'html.parser').getText()
            except:
                cep = ''
            try:
                html_cidade_estado = browser.find_element('xpath', '/html/body/div/div[2]/div/div/div[3]/div[2]/div[2]/div[2]/div[1]/p').get_attribute('outerHTML')
                cidade_estado = BeautifulSoup(html_cidade_estado, 'html.parser').getText()
            except:
                cidade_estado = ''
            try:
                html_tel = browser.find_element('xpath', '/html/body/div/div[2]/div/div/div[3]/div[3]/div[2]/p/a').get_attribute('outerHTML')
                tel = BeautifulSoup(html_tel, 'html.parser').getText()
            except:
                tel = ''
            try:
                html_email = browser.find_element('xpath', '/html/body/div/div[2]/div/div/div[3]/div[4]/div[2]/p/a').get_attribute('outerHTML')
                email = BeautifulSoup(html_email, 'html.parser').getText()
            except:
                email = ''
            df.loc[i] = [cnpj, razao, matriz_filial, tel, email, situa, dt_abertura, dt_ult_atualizacao, endereco, cidade_estado, cep]
            i += 1
            print(df)
        except:
            pass

