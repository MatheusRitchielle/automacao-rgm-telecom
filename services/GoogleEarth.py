import time

import pyautogui as gui

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def position_mouse():
    x, y = gui.position()
    print('Posicao atual do mouse: x = ' + str(x) + ' y = ' + str(y))

def find_google_earth():
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
    gui.write('profissionais 25957005')
    time.sleep(2)
    gui.hotkey('enter')
    time.sleep(5)
    gui.click(44, 754)
    time.sleep(3)
    gui.hotkey('alt', 'tab')
    time.sleep(3)
    browser.find_element('xpath',  '//*[@id="txt1"]').click()
    # gui.click(1229, 546)
    gui.hotkey('ctrl', 'a')
    time.sleep(2)
    gui.hotkey('delete')
    time.sleep(2)
    gui.hotkey('ctrl', 'v')
    time.sleep(2)
    browser.find_element('xpath', '//*[@id="frm1"]/div/input[2]').click()
    time.sleep(5)
    # gui.hotkey('enter')
    # time.sleep(3)
    gui.hotkey('alt', 'tab')
    time.sleep(3)
    gui.hotkey('ctrl', 'a')
    time.sleep(2)
    gui.hotkey('delete')
    time.sleep(2)