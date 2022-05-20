
def payroll():

    layout = [
            [sg.Text('Payroll', font=('ariel',25))],
            [sg.Text('Please choose one of the following options:', font=('ariel',19))],
            [sg.Button('Timekeeping', font=('ariel',16))],
            [sg.Button('Employee', font=('ariel',16))],
            [sg.Button('Main', font=('ariel',16))]
    ]

    window = sg.Window('Payroll', layout, size=(450,450), element_justification='c')

    # Event Loop

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Main':
            window.close()
            main()         #This sends me back to the main menu
        if event == 'Timekeeping':
            window.close()
            time()         #This sends me to the timekeeping menu listed once I import it
        if event == 'Employee':
            window.close()
            employee()     #This Sends me to the employee menu once it is imported

    window.close()
