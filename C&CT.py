import PySimpleGUI as sg

sg.theme('Reddit')
sg.set_options(font=('Arial', 10))

KEYS = {
    'QTD_100': '-QTD100-',     # Quantidade a 100%
    'TEOR1': '-TEOR1-',        # Teor para cálculo com 1 teor
    'QTDF1': '-QTDF1-',        # Quantidade física 1
    'TEORF1': '-TEORF1-',      # Teor da quantidade física 1
    'QTDF2': '-QTDF2-',        # Quantidade física 2
    'TEORF2': '-TEORF2-',      # Teor da quantidade física 2
    'NOVO_TEOR': '-NOVO_TEOR-' # Novo teor desejado
}

def window_menu():
    layout = [
        [sg.Push(), sg.Text('*BEM-VINDO(A)*', font=('Arial', 12, 'bold')), sg.Push()],
        [sg.Push(), sg.Text('*Sistema Cálculos e Correções de Teor*\n', font=('Arial', 12, 'bold')), sg.Push()],
        [sg.VPush()], 
        # Coluna de botões
        [sg.Push(), 
         sg.Column([
            [sg.Button('Correção com 1 Teor', key='-1TEOR-', size=(20, 2))],
            [sg.Button('Correção com 2 Teores', key='-2TEOR-', size=(20, 2))],
            [sg.Button('Correção com 3 Teores', key='-3TEOR-', size=(20, 2))]
         ], element_justification='center'),
         sg.Push()],
        [sg.VPush()] 
    ]
    return sg.Window('C&CT', layout, size=(450, 350), resizable=True, finalize=True)

def window_1teor():
    layout = [
        [sg.Push(), sg.Text('*CORREÇÃO COM 1 TEOR*\n', font=('Arial', 12, 'bold')), sg.Push()],
        [sg.VPush()],
        # Campos de entrada com labels
        [sg.Push(), sg.Text('QTD a 100%:', size=(12, 1)), 
         sg.Input(key=KEYS['QTD_100'], size=(20, 1)), sg.Push()],
        [sg.Push(), sg.Text('Teor:', size=(12, 1)), 
         sg.Input(key=KEYS['TEOR1'], size=(20, 1)), sg.Push()],
        [sg.VPush()],
        # Botões de ação
        [sg.Push(),
         sg.Button('«', key='-MENU-', size=(8, 1)),
         sg.Button('Calcular', key='-1CC-', size=(8, 1)),
         sg.Push()]
    ]
    return sg.Window('Correção com 1 Teor', layout, size=(450, 350), resizable=True, finalize=True)

def window_2teores():
    layout = [
        [sg.Push(), sg.Text('*CORREÇÃO COM 2 TEORES*\n', font=('Arial', 12, 'bold')), sg.Push()],
        [sg.VPush()],
        # Campos de entrada com labels
        [sg.Push(), sg.Text('QTD a 100%:', size=(15, 1)), 
         sg.Input(key=KEYS['QTD_100'], size=(20, 1)), sg.Push()],
        [sg.Push(), sg.Text('Quantidade Física:', size=(15, 1)), 
         sg.Input(key=KEYS['QTDF1'], size=(20, 1)), sg.Push()],
        [sg.Push(), sg.Text('Teor:', size=(15, 1)), 
         sg.Input(key=KEYS['TEORF1'], size=(20, 1)), sg.Push()],
        [sg.Push(), sg.Text('Novo Teor:', size=(15, 1)), 
         sg.Input(key=KEYS['NOVO_TEOR'], size=(20, 1)), sg.Push()],
        [sg.VPush()],
        # Botões de ação
        [sg.Push(),
         sg.Button('«', key='-MENU-', size=(8, 1)),
         sg.Button('Calcular', key='-2CC-', size=(8, 1)),
         sg.Push()]
    ]
    return sg.Window('Correção com 2 Teores', layout, size=(450, 400), resizable=True, finalize=True)

def window_3teores():
    layout = [
        [sg.Push(), sg.Text('*CORREÇÃO COM 3 TEORES*\n', font=('Arial', 12, 'bold')), sg.Push()],
        [sg.VPush()],
        # Campos de entrada com labels
        [sg.Push(), sg.Text('QTD a 100%:', size=(18, 1)), 
         sg.Input(key=KEYS['QTD_100'], size=(20, 1)), sg.Push()],
        [sg.Push(), sg.Text('Primeira Quantidade Fís:', size=(18, 1)), 
         sg.Input(key=KEYS['QTDF1'], size=(20, 1)), sg.Push()],
        [sg.Push(), sg.Text('Primeiro Teor:', size=(18, 1)), 
         sg.Input(key=KEYS['TEORF1'], size=(20, 1)), sg.Push()],
        [sg.Push(), sg.Text('Segunda Quantidade Fís:', size=(18, 1)), 
         sg.Input(key=KEYS['QTDF2'], size=(20, 1)), sg.Push()],
        [sg.Push(), sg.Text('Segundo Teor:', size=(18, 1)), 
         sg.Input(key=KEYS['TEORF2'], size=(20, 1)), sg.Push()],
        [sg.Push(), sg.Text('Novo Teor:', size=(18, 1)), 
         sg.Input(key=KEYS['NOVO_TEOR'], size=(20, 1)), sg.Push()],
        [sg.VPush()],
        # Botões de ação
        [sg.Push(),
         sg.Button('«', key='-MENU-', size=(8, 1)),
         sg.Button('Calcular', key='-3CC-', size=(8, 1)),
         sg.Push()]
    ]
    return sg.Window('Correção com 3 Teores', layout, size=(450, 500), resizable=True, finalize=True)

def validate_input(values, keys):
    try:
        return {k: float(values[k]) for k in keys if values[k]}
    except ValueError:
        sg.popup_error('Por favor, insira apenas números válidos')
        return None

def main():
    window = window_menu()

    while True:
        event, values = window.read()

        if event in (None, 'Exit'):
            break

        # Gerencia a navegação entre janelas
        if event in ('-1TEOR-', '-2TEOR-', '-3TEOR-', '-MENU-'):
            window.close()
            
            # Abre a janela correspondente ao botão clicado
            match event:
                case '-1TEOR-':
                    window = window_1teor()
                case '-2TEOR-':
                    window = window_2teores()
                case '-3TEOR-':
                    window = window_3teores()
                case '-MENU-':
                    window = window_menu()

        # Processamento do cálculo com 1 teor
        if event == '-1CC-':
            keys_needed = [KEYS['QTD_100'], KEYS['TEOR1']]
            validated = validate_input(values, keys_needed)
            if validated:
                # Extração dos valores validados
                qtd100 = validated[KEYS['QTD_100']]
                teor = validated[KEYS['TEOR1']]

                # Validação dos valores críticos
                if qtd100 == 0 or teor == 0:
                    sg.popup_error("Os valores não podem ser zero!")
                    continue
                    
                # Cálculo para 1 teor
                divisao = qtd100 / teor
                res = round((divisao * 100), 3)
                sg.popup(f'Quantidade a ser usada é: {res}')

        # Processamento do cálculo com 2 teores
        elif event == '-2CC-':
            keys_needed = [KEYS['QTD_100'], KEYS['QTDF1'], KEYS['TEORF1'], KEYS['NOVO_TEOR']]
            validated = validate_input(values, keys_needed)
            if validated:
                # Extração dos valores validados
                qtd100 = validated[KEYS['QTD_100']]
                qtdFr = validated[KEYS['QTDF1']]
                teorFr = validated[KEYS['TEORF1']]
                nTeor = validated[KEYS['NOVO_TEOR']]
                
                # Validação dos valores críticos
                if qtd100 == 0 or qtdFr == 0:
                    sg.popup_error("Os valores não podem ser zero!")
                    continue
                elif teorFr == 0 or nTeor == 0:
                    sg.popup_error("Os valores não podem ser zero!")
                    continue
                    
                # Cálculo para 2 teores
                mult = round(((qtdFr * teorFr) / 100), 3)
                res0 = round((qtd100 - mult), 3)
                res1 = round((res0 / nTeor * 100 + qtdFr), 3)
                sg.popup(f'Quantidade a ser utilizada é: {res1}')

        # Processamento do cálculo com 3 teores
        elif event == '-3CC-':
            keys_needed = [KEYS['QTD_100'], KEYS['QTDF1'], KEYS['TEORF1'], 
                          KEYS['QTDF2'], KEYS['TEORF2'], KEYS['NOVO_TEOR']]
            validated = validate_input(values, keys_needed)
            if validated:
                # Extração dos valores validados
                qtd100 = validated[KEYS['QTD_100']]
                qtdFr1 = validated[KEYS['QTDF1']]
                teorFr1 = validated[KEYS['TEORF1']]
                qtdFr2 = validated[KEYS['QTDF2']]
                teorFr2 = validated[KEYS['TEORF2']]
                nTeor = validated[KEYS['NOVO_TEOR']]
                
                # Validação dos valores críticos
                if qtd100 == 0:
                    sg.popup_error("Os valores não podem ser zero!")
                    continue
                elif qtdFr1 == 0 or teorFr1 == 0:
                    sg.popup_error("Os valores não podem ser zero!")
                    continue
                elif qtdFr2 == 0 or teorFr2 == 0:
                    sg.popup_error("Os valores não podem ser zero!")
                    continue
                elif nTeor == 0:
                    sg.popup_error("Os valores não podem ser zero!")
                    continue

                # Cálculo para 3 teores
                mult = round(((qtdFr1 * teorFr1) / 100), 3)
                mult2 = round(((qtdFr2 * teorFr2) / 100), 3)
                res0 = round((qtd100 - mult - mult2), 3)
                res1 = round((res0 / nTeor * 100 + qtdFr1 + qtdFr2), 3)
                sg.popup(f'Quantidade a ser utilizada é: {res1}')


    window.close()

if __name__ == '__main__':
    main()