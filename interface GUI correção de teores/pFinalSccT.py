from PySimpleGUI import (Window, Text, Button, Image,
                         Input, Push, popup, theme)

theme('Reddit')
# variaves
QTD_1001 = '-1QTD_100-'
teor1 = '-TEOR-'
n = 100
# Janela inicial(Menu)


def window_A():
    layout0 = [
        [Text('*BEM-VINDO(A)*')],
        [Image(filename='coffee-cup.png', key='-IMAGE-')],
        [Text('*SCCT*\n')],
        [Button('Correção com 1 Teor', key='-1TEOR-', size=(10, 0)), Button('Correção com 2 Teores', key='-2TEOR-', size=(10, 0)),
         Button('Correção com 3 Teores', key='-3TEOR-',  size=(10, 0))]
    ]
    return Window('Sc&Correção de Teor',
                  layout=layout0, resizable=True, element_justification='c')

# Janela de CC 1TEOR


def window_B():
    layout1 = [
        [Text('*CORREÇÃO COM 1 TEOR*\n')],
        [Text('QTD a 100% :'), Push(), Text('Teor :'), Push()],
        [Input(key='-1QTD_100-', size=(13, 0)),
         Input(key='-1Teor-', size=(14, 0))],
        [Button('«', key='-MENU-'), Push(), Push(),
         Button('CC', key='-1CC-', size=(10, 0)), Push(), Push(), Push()]
    ]
    return Window(
        'Correção com 1 Teor', layout=layout1, resizable=True, element_justification='c'
    )
# Janela de CC 2 TEORES


def window_C():
    layout2 = [
        [Text('*CORREÇÃO COM 2 TEORES*\n')],
        [Text('QTD a 100% :'), Push(), Text('QTD F 1 :'), Push()],
        [Input(size=(14, 0)), Input(size=(14, 0))],
        [Text('Teor QTD F 1 :'), Push(), Text('Novo Teor :'), Push()],
        [Input(size=(14, 0)), Input(size=(14, 0))],
        [Button('«', key='-MENU-'), Push(), Push(),
         Button('CC', key='-2CC-', size=(10, 0)), Push(), Push(), Push()]
    ]
    return Window('Correção com 2 Teores',
                  layout=layout2, resizable=True, element_justification='c')

# Janela de CC 3 Teores


def window_D():
    layout3 = [
        [Text('*CORREÇÃO COM 3 TEORES*\n')],
        [Text('QTD a 100% :')],
        [Input(size=(14, 0))],
        [Text('QTD F 1 :'), Push(), Push(), Text('Teor QTD F 1 :'), Push()],
        [Input(size=(14, 0)), Input(size=(15, 0))],
        [Text('QTD F 2 :'), Push(), Push(), Text('Teor QTD F 2 :'), Push()],
        [Input(size=(14, 0)), Input(size=(15, 0))],
        [Text('Novo Teor :')],
        [Input(size=(14, 0))],
        [Button('«', key='-MENU-'), Push(), Push(),
         Button('CC', key='-3CC-', size=(10, 0)), Push(), Push(), Push()]
    ]
    return Window('Correção com 3 Teores',
                  layout=layout3, resizable=True, element_justification='c'
                  )


    # EventosA
window = window_A()
# Menu.
while True:
    event, values = window.read()
# Fecha janela menu apos uma opcao selecionada
    match(event):
        case '-1TEOR-' | '-2TEOR-' | '-3TEOR-' | '-MENU-':
            window.close()

    match(event):

        # Evento botao1
        case '-1TEOR-':
            window = window_B()
        case '-1CC-':
            popup('oi')


# Evento botao2
        case '-2TEOR-':
            window = window_C()
        case '-2CC-':
            popup('oi')

# Evento botao3
        case '-3TEOR-':
            window = window_D()
        case '-3CC-':
            popup('oi')

# Evento para retornar ao menu
        case '-MENU-':
            window = window_A()

            # EVENTOS DE OPERAÇÕES!

        case None:
            break

window.close()
