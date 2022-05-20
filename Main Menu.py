import PySimpleGUI as sg

# Main Menu

def main():

    sg.theme('BlueMono')#program display theme

    #define the layout

    layout = [
        [sg.Text('Welcome to POOL RESURFACING', font=('ariel',25))],
        [sg.Text('NQ ACCOUNTING PACKAGE', font=('ariel',25))],
        [sg.Text('Please choose one of the following options:', font=('ariel',19))],
        [sg.Button('Payroll', font=('ariel',16))],
        [sg.Button('Income', font=('ariel',16))],
        [sg.Button('Expences', font=('ariel',16))],
        [sg.Button('Taxation', font=('ariel',16))],
        [sg.Exit(font=('ariel',16))]
    ]

    window = sg.Window('Accounting', layout, size=(450, 450), element_justification='c')

    # Event Loop

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Payroll':
            window.close()
            #payroll()  Goto payroll menu
        if event == 'Income':
            window.close()
            #income() Goto income menu
        if event == 'Expences':
            window.close()
            #expences() Goto expences menu
        if event == 'Taxation':
            window.close()
            #taxation() Goto taxation menu
        
    window.close()
main()
