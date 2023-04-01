from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from tqdm import tqdm

def bot_whatsapp():
    # Atualização do navegador
    my_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=my_service)

    # Abre a página do navegador
    browser.get('https://wa.me/5521969873189?text=Ol%C3%A1,%20excelente%20dia!%20%F0%9F%98%83%F0%9F%91%8D%0A%0AMe%20chamo%20Kamylla,%20sou%20consultora%20da%20VIVO%20EMPRESAS%20aqui%20de%20Nova%20Igua%C3%A7u.%0A%0ATemos%20%C3%B3timas%20condi%C3%A7%C3%B5es%20para%20linhas%20novas,%20portabilidade%20e%20muitos%20outros%20servi%C3%A7os%20para%20voc%C3%AA%20e%20sua%20empresa.%0A%0A%F0%9F%93%B2%20Benef%C3%ADcios%20dos%20nossos%20planos:%0A%E2%9C%85%20Liga%C3%A7%C3%B5es%20ilimitadas%20para%20todo%20o%20Brasil;%20para%20fixo%20e%20m%C3%B3vel%20de%20todas%20as%20operadoras;%0A%E2%9C%85%201000%20SMS;%0A%E2%9C%85%20Internet%20ilimitada;%20(quando%20acabar%20a%20franquia%20contratada%20a%20internet%20%C3%A9%20reduzida%20mas%20n%C3%A3o%20bloqueia)%0A%E2%9C%85%20Apps%20que%20n%C3%A3o%20descontam%20da%20franquia%20do%20seu%20plano:%20Easy%20Taxi,%20Waze%20e%20msg.%20Whatsapp;%20Skeelo.%0A%0AE%20muito%20mais...%0A%0AGostaria%20de%20solicitar%20uma%20cota%C3%A7%C3%A3o?%20%0ASer%C3%A1%20um%20prazer%20atende-lo(a)%20%E2%98%BA%EF%B8%8F')
    browser.maximize_window()

