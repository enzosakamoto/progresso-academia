# Importações
import PySimpleGUI as sg

# Abre/cria e lê arquivo txt
arquivo = open("progresso_acad.txt", "a")

# Criação de Layout
sg.theme('Reddit')
layout = [
    [sg.Text("Data [DD/MM/AA]: "), sg.Input(key='data', size=(11,1))],
    [sg.Text("Massa Gorda/Body Fat [%]: "), sg.Input(key='bodyfat', size=(5,1))],
    [sg.Text("Massa Magra/Muscle [Kg]: "), sg.Input(key='muscle', size=(5,1))],
    [sg.Text("Peso [Kg]: "), sg.Input(key='peso', size=(5,1))],
    [sg.Text("IMC/BMI [Kg/m^2]: "), sg.Input(key='imc', size=(5,1))],
    [sg.Push(), sg.Button('Enviar!'), sg.Button('Limpar tudo!'), sg.Button('Sair!'), sg.Push()]
]

# Inicialização da janela
janela = sg.Window('Progresso na Academia', layout=layout, size=(300,180))

# Leitura de eventos da janela
while True:
    eventos, valores = janela.read()

    if eventos in [sg.WIN_CLOSED, 'Sair!']:
        break

    if eventos == 'Enviar!':
        arquivo.write("%s\n" %(valores['data']))
        arquivo.write("Massa Gorda: {} %\n".format(valores['bodyfat']))
        arquivo.write("Massa Magra: %s Kg\n" %(valores['muscle']))
        arquivo.write("Peso: %s Kg\n" %(valores['peso']))
        arquivo.write("IMC: %s Kg/m^2\n" %(valores['imc']))
        arquivo.write("\n")
        sg.popup('Progresso gravado!')
    
    if eventos == 'Limpar tudo!':
        janela['data'].update('')
        janela['bodyfat'].update('')
        janela['muscle'].update('')
        janela['peso'].update('')
        janela['imc'].update('')

# Fecha janela e arquivo
arquivo.close()
janela.close()