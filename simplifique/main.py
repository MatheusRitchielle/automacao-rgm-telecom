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

def synergy_client():
    # Declaração de variáveis
    client_type = ''
    user = credentials.get('user')
    password = credentials.get('password')

    # Abre a tela para selecionar o arquivo com os CNPJs
    path_cnpj = filedialog.askopenfilename()

    data = pd.read_excel(path_cnpj, header=None, names=['cnpj', 'Razão Social', 'Voz', 'Dados', 'Segmento', 'Tipo de Cliente', 'Crédito'], converters={'cnpj': '{:0>14}'.format})
    df = pd.DataFrame(data)
    cnpjs = df.cnpj.to_list()

    # Atualização do navegador
    my_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=my_service)

    # Abre a página do navegador
    browser.get('https://pd.simplifiquevivoemp.com.br/Simulacoes.aspx')
    browser.maximize_window()
    try:
        # Toda a parte de login.
        time.sleep(20)
        browser.find_element('xpath', '//*[@id="username"]').send_keys(user)
        browser.find_element('xpath', '//*[@id="password"]').send_keys(password)
        time.sleep(20)
        browser.find_element('xpath', '//*[@id="form"]/fieldset/input[4]').click()

        browser.find_element('xpath', '//*[@id="email"]').click()
        browser.find_element('xpath', '//*[@id="form"]/fieldset/input').click()

        # Na tela principal acessa simuladores até a tela de validação de captcha
        time.sleep(45)
        browser.find_element('xpath', '//*[@id="form"]/fieldset/input').click()
        browser.find_element('xpath', '//*[@id="spn-simuladores"]').click()
        browser.find_element('xpath', '//*[@id="btnMovelOfertasPreAprovadas"]').click()
        browser.find_element('xpath', '//*[@id="MainContent_lbNovaSimulacao"]').click()
    except:
        pass

    # Tempo para validação do captcha
    time.sleep(35)
    # Inicia a pesquisa da lista de CNPJs
    i = 0
    for cnpj in tqdm(cnpjs):
        # if i % 15 == 0:
        #     time.sleep(300)
        try:
            # Limpa o campo de pesquisa, informa o cnpj e pesquisa
            time.sleep(2)
            browser.find_element('xpath', '//*[@id="ucPesquisarCliente_txtPesquisarDocumento"]').clear()
            browser.find_element('xpath', '//*[@id="ucPesquisarCliente_txtPesquisarDocumento"]').send_keys(cnpj)
            browser.find_element('xpath', '//*[@id="ucPesquisarCliente_lbPesquisar"]').click()

            # Verifica o tipo de cliente
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

            # Pegando o texto de cada elemento antes de criar a simulação
            time.sleep(4)
            htmlContent_razao = browser.find_element('xpath', '//*[@id="ucPesquisarCliente_gvClientes"]/tbody/tr[1]/td[2]').get_attribute('outerHTML')
            razao = BeautifulSoup(htmlContent_razao, 'html.parser').getText()

            htmlContent_voz = browser.find_element('xpath', '//*[@id="ucPesquisarCliente_gvClientes"]/tbody/tr[1]/td[4]').get_attribute('outerHTML')
            voz = BeautifulSoup(htmlContent_voz, 'html.parser').getText()

            htmlContent_dados = browser.find_element('xpath', '//*[@id="ucPesquisarCliente_gvClientes"]/tbody/tr[1]/td[5]').get_attribute('outerHTML')
            dados = BeautifulSoup(htmlContent_dados, 'html.parser').getText()

            htmlContent_seg = browser.find_element('xpath', '//*[@id="ucPesquisarCliente_gvClientes"]/tbody/tr[1]/td[6]').get_attribute('outerHTML')
            seg = BeautifulSoup(htmlContent_seg, 'html.parser').getText()

            # Cria uma nova simulação para o cliente e acessa as informações de crédito
            time.sleep(2)
            browser.find_element('xpath',  '//*[@id="ucPesquisarCliente_gvClientes_lbSelecionarCliente_0"]').click()
            time.sleep(4)
            browser.find_element('xpath', '//*[@id="ucPesquisarCliente_lbConfirmarCliente"]').click()
            time.sleep(4)
            browser.find_element('xpath', '//*[@id="MainContent_lkbAbrirCreditoC1"]').click()

            # Pega e salva as informações de crédito na variavel soup_credit
            time.sleep(4)
            htmlContent_situation_detail = browser.find_element(by=By.ID, value='MainContent_UC_CreditoC1_lblCreditoC1').get_attribute('outerHTML')
            soup_credit = BeautifulSoup(htmlContent_situation_detail, 'html.parser').getText()

            df.loc[i]=[cnpj, razao, voz, dados, seg, client_type, soup_credit]
            print(df)

            browser.back()
            i += 1

        # Quando ocorre algum erro no meio do processo o CNPJ é salvo no arquivo error.txt
        except:
            file = open('C:\Matheus\www\\automacao-rgm-telecom\simplifique\consulta\error.txt', 'a')
            file.write('\n' + cnpj)
            file.close()

    df.to_excel(f"C:\Matheus\www\\rgm\\teste2.xlsx", index=False, header=True)

    print('Programa finalizado')

