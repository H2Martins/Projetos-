import webbrowser
import pyautogui
from time import sleep

while True:
    # Navegar ate o site http://www.instagram.com
    webbrowser.open('http://www.instagram.com')
    sleep(3)
    # entar com meu usuarioGostei demais!
    pyautogui.click(880, 292, duration=1)
    sleep(1)
    pyautogui.typewrite('h2robsbot')
    sleep(1)
    # entrar com senha
    pyautogui.press('tab')
    sleep(1)
    pyautogui.typewrite('96536264gael')
    sleep(2)
    pyautogui.click(903, 380, duration=1)
    sleep(3.5)
    # clicar em "agora nao" para nao salvar informacoes
    pyautogui.click(992, 504, duration=1)
    sleep(3.5)
    # pesquisar pela pagina
    pyautogui.click(980, 118, duration=1)
    sleep(2)
    pyautogui.typewrite('nike')
    sleep(1.5)
    pyautogui.move(0, 50, duration=1)
    sleep(1)
    pyautogui.click()
    sleep(5)
    # entrar na ultima publicacao da pagina
    pyautogui.click(812, 628, duration=1)
    sleep(6)
    # verificar se ja curti ou nao aquela postagem
    try:
        coracao_vasio = pyautogui.locateOnScreen('coracaoVasio.png')
        sleep(1)
        # caso nao esteja curtido, curtir e comentar algo
        if coracao_vasio is not None:
            sleep(0.5)
            pyautogui.click(936,556, duration=1)
            sleep(3)
        # adicionar um comentario
            pyautogui.click(975,557, duration=1)
            sleep(2.6)
            pyautogui.click(985,644, duration=1)
            sleep(1.5)
            pyautogui.typewrite('Gostei demais!')
            sleep(3)
            pyautogui.press('enter')
        # pausar 24hrs
            sleep(86400)
        # se tiver curtido, fechar voltar ao inicio e pausar por 24hrs
        elif coracao_vasio == None:
            pyautogui.locateOnScreen('coracao.png')
    except pyautogui.ImageNotFoundException as erro:  # IGNOROU ERRO.
        sleep(2)
        pyautogui.click(799, 260, duration=1)
        sleep(0.5)
        pyautogui.click(757, 109, duration=1)
        # pausar por 24hrs
        sleep(86400)
