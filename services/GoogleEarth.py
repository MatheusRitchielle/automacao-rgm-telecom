import time
import pyautogui as gui

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime

def position_mouse():
    x, y = gui.position()
    print('Posicao atual do mouse: x = ' + str(x) + ' y = ' + str(y))
    print(datetime.now())
def find_google_earth():

    ceps = ['Teresópolis, Rj', 'Guapimirim, Rj', 'Niterói, Rj']
    file_segments = open('C:\Matheus\www\\automacao-rgm-receita\docs\segmentos.txt', 'r')

    my_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=my_service)

    browser.get('https://www.convertcsv.com/kml-to-csv.htm')
    browser.maximize_window()
    gui.hotkey('win', 'r')
    time.sleep(2)
    gui.hotkey('ctrl', 'a')
    time.sleep(2)
    gui.hotkey('delete')
    time.sleep(2)
    gui.write('C:\Program Files\Google\Google Earth Pro\client\googleearth.exe')
    time.sleep(2)
    gui.hotkey('enter')
    time.sleep(15)

    try:
        for cep in ceps:
            segments = file_segments.readlines()
            for seg in segments:
                gui.write(seg + ' ' + cep)
                time.sleep(2)
                gui.hotkey('enter')
                time.sleep(5)
                gui.click(45, 647)
                time.sleep(3)
                gui.hotkey('alt', 'tab')
                time.sleep(3)
                gui.click(1360, 434)
                time.sleep(1)
                browser.find_element('xpath', '//*[@id="txt1"]').click()
                gui.hotkey('ctrl', 'a')
                time.sleep(2)
                gui.hotkey('delete')
                time.sleep(2)
                gui.hotkey('ctrl', 'v')
                time.sleep(2)
                gui.click(1360, 434)
                time.sleep(2)
                browser.find_element(By.XPATH, "//input[@value=\'KML To Excel\']").click()
                time.sleep(15)
                gui.hotkey('alt', 'tab')
                time.sleep(3)
                gui.hotkey('ctrl', 'a')
                time.sleep(2)
                gui.hotkey('delete')
                time.sleep(2)
                try:
                    file = open('C:\Matheus\www\\automacao-rgm-receita\docs\log.txt', 'a')
                    file.write(seg + ' ' + cep + ' realizado com sucesso! -- ' + str(datetime.now()))
                    file.close()
                except:
                    file = open('C:\Matheus\www\\automacao-rgm-receita\docs\error.txt', 'a')
                    file.write('Não foi possível consultar: ' + seg + ' ' + cep + ' -- ' + str(datetime.now()))
                    file.close()

    except:
        file = open('C:\Matheus\www\\automacao-rgm-receita\docs\error.txt', 'a')
        file.write('Não foi possível consultar: ' + seg + ' ' + cep + ' -- ' + str(datetime.now()))
        file.close()
    gui.hotkey('alt', 'f4')
    print('Programa finalizado com sucesso!')