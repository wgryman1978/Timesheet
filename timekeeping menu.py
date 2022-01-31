import pandas as pd
import PySimpleGUI as sg
import openpyxl as op

# TimeKeeping Menu

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
            #main() Main menu
        if event == 'Back':
            window.close()
            #payroll() Payroll Menu
        if event == 'Weekly Timesheet':
            window.close()
            #timesheet() Launch Timesheet Data entry form
        if event == 'Weekly Wages Report':
            window.close()
            #weekly_wages() Launch search weekly gross wage
        if event == 'Q-Leave Totals':
            window.close()
            #q_leave() Launce search widow for report labelled QLeave

    window.close()
time()
