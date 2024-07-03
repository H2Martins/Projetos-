# zerar Sulfur-Slipknot.
import pyautogui
import keyboard
import webbrowser
from time import sleep

# abrir o Jogo no navegdor
webbrowser.open(
    'https://guitarflash.com/?lg=pt&_gl=1*l9yksd*_ga*MjEzNDA4MjgzMy4xNzA4NzgyNzY5*_ga_37GXT4VGQK*MTcxNzA3ODIzNS4xMi4xLjE3MTcwNzgyNTEuMC4wLjA.')
sleep(3)
pyautogui.click(600, 381, duration=1)
sleep(2)
# buscar faixa "Sulfur-Slipknot"
pyautogui.click(986, 565, duration=1)
sleep(1)
pyautogui.typewrite('wish you were here')
sleep(1)
pyautogui.click(551, 603, duration=1)
sleep(3)
# descer ate o jogo
pyautogui.scroll(-445)
sleep(4)
# dar play no jogo
pyautogui.press('q')
'''
Verificar se ha um botao com a cor correspodente dentro do circulo daquela cor
e pressionar o botao correspondente a ela.
'''
while keyboard.is_pressed('1') == False:
    # verde(a)
    if pyautogui.pixelMatchesColor(643, 582, (0, 152, 0)):
        pyautogui.press('a')
        sleep(0.01)
    elif pyautogui.pixelMatchesColor(646, 608, (0, 152, 0)):
        pyautogui.press('a')
        sleep(0.01)
    elif pyautogui.pixelMatchesColor(643, 622, (0, 152, 0)):
        pyautogui.press('a')
        sleep(0.01)
# vermelho(s)
    if pyautogui.pixelMatchesColor(731, 583, (255, 0, 0)):
        pyautogui.press('s')
        sleep(0.01)
    elif pyautogui.pixelMatchesColor(734, 608, (255, 0, 0)):
        pyautogui.press('s')
        sleep(0.01)
    elif pyautogui.pixelMatchesColor(735, 622, (255, 0, 0)):
        pyautogui.press('s')
        sleep(0.01)
# amarelo(j)
    if pyautogui.pixelMatchesColor(823, 582, (244, 244, 2)):
        pyautogui.press('j')
        sleep(0.01)
    elif pyautogui.pixelMatchesColor(823, 609, (244, 244, 2)):
        pyautogui.press('j')
        sleep(0.01)
    elif pyautogui.pixelMatchesColor(824, 624, (244, 244, 2)):
        pyautogui.press('j')
        sleep(0.01)

# azul(k)
    if pyautogui.pixelMatchesColor(912, 582, (0, 152, 255)):
        pyautogui.press('k')
        sleep(0.01)
