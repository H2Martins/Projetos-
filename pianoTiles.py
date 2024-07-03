import pyautogui as pg
import webbrowser
from time import sleep
import keyboard
import win32api
import win32con

# abrir o Piano tiles
webbrowser.open('https://www.gamesgames.com/game/magic-piano-tiles')
sleep(5)

# dar play
pg.click(845, 395, duration=1)
sleep(5.5)
pg.click(850, 419, duration=1)
sleep(3.5)

# funcao do click
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# clicar em cada posicao que apresentar uma "tecla"
while keyboard.is_pressed('1') == False:
    if pg.pixelMatchesColor(729, 336, (0, 0, 0)):
        click(729, 336)
        sleep(0.05)
    if pg.pixelMatchesColor(806, 345, (0, 0, 0)):
        click(806, 345)
        sleep(0.05)
    if pg.pixelMatchesColor(885, 335, (0, 0, 0)):
        click(885, 335)
        sleep(0.05)
    if pg.pixelMatchesColor(964, 343, (0, 0, 0)):
        click(964, 343)
        sleep(0.05)
