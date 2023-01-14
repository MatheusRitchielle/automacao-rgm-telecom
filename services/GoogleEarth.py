import time
import pyautogui as gui

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def position_mouse():
    x, y = gui.position()
    print('Posicao atual do mouse: x = ' + str(x) + ' y = ' + str(y))

def find_google_earth():
    ceps = ['25957005', '25975005', '25975550']
    seg = ['profissionais', 'mecanica', 'padaria']

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

    for cep in ceps:
        for segmento in seg:
            gui.write(segmento + ' ' + cep)
            time.sleep(2)
            gui.hotkey('enter')
            time.sleep(5)
            gui.click(44, 754)
            time.sleep(3)
            gui.hotkey('alt', 'tab')
            time.sleep(3)
            browser.find_element('xpath', '//*[@id="txt1"]').click()
            gui.hotkey('ctrl', 'a')
            time.sleep(2)
            gui.hotkey('delete')
            time.sleep(2)
            gui.hotkey('ctrl', 'v')
            time.sleep(2)
            gui.click(1912, 653)
            time.sleep(2)
            browser.find_element(By.XPATH, "//input[@value=\'KML To Excel\']").click()
            time.sleep(15)
            gui.hotkey('alt', 'tab')
            time.sleep(3)
            gui.hotkey('ctrl', 'a')
            time.sleep(2)
            gui.hotkey('delete')
            time.sleep(2)
    gui.hotkey('alt', 'f4')
    print('Programa finalizado com sucesso!')