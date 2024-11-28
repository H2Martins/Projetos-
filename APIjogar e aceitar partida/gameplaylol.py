import pyautogui
from time import sleep
while True:
    try:
        aceitar_partida = pyautogui.locateCenterOnScreen('aceitar.png')

        if aceitar_partida is not None:
            pyautogui.click(aceitar_partida[0],
                            aceitar_partida[1], duration=0.5)

        elif aceitar_partida == None:
            sleep(0)
    except pyautogui.ImageNotFoundException as erro:
        sleep(0.1)
 
