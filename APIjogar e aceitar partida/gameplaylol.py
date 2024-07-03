import pyautogui
from time import sleep

# blitz
# pyautogui.press('win')
# sleep(1)
# pyautogui.typewrite('blitz')
# sleep(1)
# pyautogui.press('enter')
# sleep(5)

# # Discord
# pyautogui.press('win')
# sleep(1)
# pyautogui.typewrite('discord')
# sleep(1)
# pyautogui.press('enter')
# sleep(20)
# # entrar no server
# pyautogui.click(33, 274, duration=1)
# sleep(2)
# # entrar na sala
# pyautogui.click(154, 354, duration=1)
# sleep(3)

# # lol
# pyautogui.press('win')
# sleep(1)
# pyautogui.typewrite('League of legends')
# sleep(1)
# pyautogui.press('enter')
# sleep(60)
# # dar queue
# pyautogui.click(237, 86, duration=1)
# sleep(3)
# pyautogui.click(195, 514, duration=1)
# sleep(2)
# pyautogui.click(546, 601, duration=1)
# sleep(3)
# pyautogui.click(562, 594, duration=1)

# aceitar partida
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
 