# robo de postagens no facebook
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
    arguments = ['--lang=pt-BR', '--start-maximized', '--incognito']
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


# ir ate o facebook
driver = iniciar_driver()
driver.get('https://www.facebook.com/')
sleep(2)

# digitar login
login = driver.find_element(By.XPATH, '//input[@type="text"]')
sleep(1)
digitar_naturalmente('', login)
sleep(1)
# digitar senha
senha = driver.find_element(By.XPATH, '//input[@type="password"]')
sleep(1)
digitar_naturalmente('', senha)
sleep(1)
# clicar em fazer login
botao_login = driver.find_element(By.XPATH, '//button[@value="1"]')
botao_login.click()
sleep(5)
# atualizar a pagina
f5 = driver.find_element(By.CLASS_NAME, 'xe3v8dz')
f5.click()
sleep(2)
# encontrar e clicar no campo de postagem
campo_status = driver.find_element(
    By.XPATH, '//div[@class="x1i10hfl x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou"]')
sleep(1)
campo_status.click()
sleep(1.5)
# digitar algo
digitar_status = driver.find_element(
    By.XPATH, '//p[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8"]')
sleep(1)
digitar_naturalmente('Boa noite!', digitar_status)
sleep(2)
# clicar em publicar
botao_publicar = driver.find_element(
    By.XPATH, '//div[@class="x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67"]')
sleep(1)
botao_publicar.click()

# para fechar o bot
input('digite algo para fechar... ')
