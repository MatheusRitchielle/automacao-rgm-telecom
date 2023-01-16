import time
import pyautogui as gui

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime

file_segments = open('google_earth/segmentos.txt', 'r')

def mouse_position():
    x, y = gui.position()
    print('Posicao atual do mouse: ' + str(x) + ', ' + str(y))

def search_google_earth():
    address = ['Teresopolis, Rj', 'Guapi, Rj', 'Friburgo, Rj', 'Magé, Rj']

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

    for add in address:
        segments = file_segments.readlines()
        for segment in segments:
            try:
                gui.write(segment + ' ' + add)
                time.sleep(1)
                gui.hotkey('enter')
                time.sleep(2)
                gui.click(45, 759)
                time.sleep(2)
                gui.hotkey('alt', 'tab')
                time.sleep(2)
                gui.click(1911, 693)
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
                time.sleep(10)
                gui.hotkey('alt', 'tab')
                time.sleep(2)
                gui.hotkey('ctrl', 'a')
                time.sleep(2)
                gui.hotkey('delete')
                time.sleep(2)
                file = open('C:\Matheus\www\\automacao-rgm-receita\docs\log.txt', 'a')
                file.write(segment + ' ' + add + ' realizado com sucesso! -- ' + str(datetime.now()))
                file.close()
            except:
                file = open('C:\Matheus\www\\automacao-rgm-receita\docs\error.txt', 'a')
                file.write('Não foi possível consultar: ' + segment + ' ' + add + ' -- ' + str(datetime.now()))
                file.close()

    gui.hotkey('alt', 'f4')
    print('Programa finalizado com sucesso!')