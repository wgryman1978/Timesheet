def time():

    layout = [
        [sg.Text('Please choose one of the following options:', font=('ariel',19))],
        [sg.Button('Weekly Timesheet', font=('ariel',16))],
        [sg.Button('Weekly Wages Report', font=('ariel',16))],
        [sg.Button('Q-Leave Totals', font=('ariel',16))],
        [sg.Button('Back', font=('ariel',16))],
        [sg.Button('Main', font=('ariel',16))]
    ]

    window = sg.Window('Timekeeping', layout, size=(450,450), element_justification='c')

    # Event Loop

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Main':
            window.close()
            main()
        if event == 'Back':
            window.close()
            payroll()
        if event == 'Weekly Timesheet':
            window.close()
            timesheet() #Launch data entry form for timesheets
        if event == 'Q-Leave Totals':
            window.close()
            q_leave() #Launch search widow for report labelled QLeave

    window.close()
time()
