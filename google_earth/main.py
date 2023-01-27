import time
import pyautogui as gui

from tqdm import tqdm
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
from tkinter import filedialog
from pathlib import Path

def mouse_position():
    x, y = gui.position()
    print('Posicao atual do mouse: ' + str(x) + ', ' + str(y))

def search_google_earth():
    path_cep = filedialog.askopenfilename()
    address = open(path_cep, 'r').read().split('\n')

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
    time.sleep(45)

    for add in tqdm(address):
        segments = open('C:\Matheus\www\\automacao-rgm-telecom\google_earth\segmentos.txt', 'r').read().split('\n')
        for segment in tqdm(segments):
            try:
                gui.write(segment + ' ' + add)
                time.sleep(3)
                gui.hotkey('enter')
                time.sleep(3)
                gui.click(45, 649)
                time.sleep(3)
                gui.hotkey('alt', 'tab')
                time.sleep(3)
                gui.click(1353, 473)
                time.sleep(3)
                browser.find_element('xpath', '//*[@id="txt1"]').clear()
                browser.find_element('xpath', '//*[@id="txt1"]').click()
                time.sleep(3)
                gui.hotkey('ctrl', 'v')
                time.sleep(3)
                gui.click(1360, 434)
                time.sleep(3)
                browser.find_element(By.XPATH, "//input[@value=\'KML To Excel\']").click()
                time.sleep(10)
                gui.hotkey('alt', 'tab')
                time.sleep(3)
                gui.hotkey('ctrl', 'a')
                time.sleep(3)
                gui.hotkey('delete')
                time.sleep(3)
                file = open('C:\Matheus\www\\automacao-rgm-telecom\docs\log.txt', 'a')
                file.write(segment + ' ' + add + ' realizado com sucesso! -- ' + str(datetime.now()) + '\n')
                file.close()
            except:
                file = open('C:\Matheus\www\\automacao-rgm-telecom\docs\error.txt', 'a')
                file.write('Não foi possível consultar: ' + segment + ' ' + add + ' -- ' + str(datetime.now()) + '\n')
                file.close()

    gui.hotkey('alt', 'f4')
    print('Programa finalizado com sucesso!')
    gui.hotkey('win', 'r')
    gui.write('shutdown -s -t 3600')
    gui.hotkey('enter')
    gui.hotkey('alt', 'f4')