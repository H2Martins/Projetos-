import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from random import randint
# funcao de inicializacao e configuracoes


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver

# funcao para digitar naturlmente


def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(randint(1, 6)/30)


# abrir site
driver = iniciar_driver()
driver.get('https://web.whatsapp.com/')
sleep(35)
driver.maximize_window()

sleep(2)
# contatos
contatos = ['so um teste', 'teste 2', 'teste 3']

# repetir o processo
for item in contatos:
    # encontrar barra de pesquisa e procurar os contatos
    barra_pesquisa = driver.find_element(
        By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
    digitar_naturalmente(item, barra_pesquisa)
    sleep(randint(2, 5))
    pyautogui.press('enter')
    sleep(randint(2, 5))

# escrever msg aos contatos e enviar imagens
    anexar = driver.find_element(
        By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span')
    anexar.click()
    sleep(randint(1, 4))
    imagem = driver.find_element(
        By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/span')
    sleep(1)
    imagem.click()
    sleep(randint(3, 5))
    pyautogui.typewrite(
        'C:\\Users\\H2MT.H2DESKTOP\\Desktop\\PrintsST\\img.avif')
    sleep(1.5)
    pyautogui.press('enter')
    sleep(randint(2, 5))
# DIGITAR MSG
    msg = driver.find_element(By.XPATH,
                              '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')
    digitar_naturalmente('Ola, boa tarde!', msg)
    sleep(randint(1, 3))
    pyautogui.press('enter')
    sleep(randint(15, 30))


# para fechar o bot
input('digite algo para fechar... ')
