import PySimpleGUI as sg

def initial_screen():

    sg.theme('DarkBlue4')

    linha = [
        [sg.Text('Boletim', font='arial 18 bold')],
        [sg.Text('Aluno')],
        [sg.Input(key='aluno', size=(35, 1))],
        [sg.Text('Matrícula')],
        [sg.Input(key='matricula', size=(35, 1))],
        [sg.Button('Entrar'), sg.Button('Sair')],
        [sg.Text(key='mensagem')]
    ]

    layout = [
        [sg.Frame('Students App', layout=linha, key='container')],
    ]

    return sg.Window('App', layout=layout, finalize=True)

def second_screen():
    sg.theme('DarkBlue4')

    layout2 = [
        [sg.Text('Dados do Aluno', font='arial 18 bold')],
        [sg.Text('Aluno'), sg.Text('Matricula'), sg.Text('Curso')],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Informações CVTI', layout= layout2,finalize=True)

screen,screen2 = initial_screen(),None

while True:
    window, event, values = sg.read_all_windows()

    if window == screen and event == sg.WIN_CLOSED:
        break

    elif window == screen and event == 'Entrar':
        aluno = values['aluno']
        matricula = values['matricula']

        #Nomes e números de matrículas válidos      
        cadastrados = {'gabriel': '1234', 'joao': '5678', 'maria': '9012'}


        if aluno in cadastrados and matricula == cadastrados[aluno]:
            screen.hide()
            screen2 = second_screen()           
        else:
            screen['mensagem'].update('Nome ou Matrícula incorretos.')

    elif window == screen2 and event == 'Voltar':
        screen2.hide()
        screen.un_hide()

    elif event == 'Sair':
        sg.popup('Até a próxima!')
        break

screen.close()