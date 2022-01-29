# Payroll Data Entry Forms go here
import PySimpleGUI as sg
import pandas as pd
import openpyxl as op
# Timesheet

def timesheet():
    
    filename = 'Payroll.xlsx'

    wb = op.load_workbook(filename)

    ws = wb.worksheets[0]

    ws_tables = []

    layout = [
            [sg.Text('Please complete the form below:', font=('ariel',19))],
            [sg.Text('Employee Name', size=(15,1)), sg.InputText(key='Name')],
            [sg.Text('Week Ending', size=(15,1)), sg.InputText(key='WeekEnding')],
            [sg.Text('Employee Level', size=(15,1)), sg.Spin(values=('0', '1', '2'), initial_value='0', key='EmpLev')],
            [sg.Text('Saturday Start Time', size=(15,1)), sg.InputText(key='SaSTime')],
            [sg.Text('Saturday Finish Time', size=(15,1)), sg.InputText(key='SaFTime')],
            [sg.Text('Saturday Break', size=(15,1)), sg.Spin(values=('0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5'), initial_value='0', key='SaBreak')],
            [sg.Text('Sunday Start Time', size=(15,1)), sg.InputText(key='SuSTime')],
            [sg.Text('Sunday Finish Time', size=(15,1)), sg.InputText(key='SuFTime')],
            [sg.Text('Sunday Break', size=(15,1)), sg.Spin(values=('0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5'), initial_value='0', key='SuBreak')],    
            [sg.Text('Monday Start Time', size=(15,1)), sg.InputText(key='MSTime')],
            [sg.Text('Monday Finish Time', size=(15,1)), sg.InputText(key='MFTime')],
            [sg.Text('Monday Break', size=(15,1)), sg.Spin(values=('0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5'), initial_value='0', key='MBreak')],
            [sg.Text('Tuesday Start Time', size=(15,1)), sg.InputText(key='TuSTime')],
            [sg.Text('Tuesday Finish Time', size=(15,1)), sg.InputText(key='TuFTime')],
            [sg.Text('Tuesday Break', size=(15,1)), sg.Spin(values=('0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5'), initial_value='0', key='TuBreak')],
            [sg.Text('Wednesday Start Time', size=(15,1)), sg.InputText(key='WSTime')],
            [sg.Text('Wednesday Finish Time', size=(15,1)), sg.InputText(key='WFTime')],
            [sg.Text('Wednesday Break', size=(15,1)), sg.Spin(values=('0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5'), initial_value='0', key='WBreak')],
            [sg.Text('Thursday Start Time', size=(15,1)), sg.InputText(key='ThSTime')],
            [sg.Text('Thursday Finish Time', size=(15,1)), sg.InputText(key='ThFTime')],
            [sg.Text('Thursday Break', size=(15,1)), sg.Spin(values=('0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5'), initial_value='0', key='ThBreak')],
            [sg.Text('Friday Start Time', size=(15,1)), sg.InputText(key='FSTime')],
            [sg.Text('Friday Finish Time', size=(15,1)), sg.InputText(key='FFTime')],
            [sg.Text('Friday Break', size=(15,1)), sg.Spin(values=('0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5'), initial_value='0', key='FBreak')],
            [sg.Submit(font=('ariel',16)), sg.Button('Clear', font=('ariel',16)), sg.Button('Back', font=('ariel',16)), sg.Button('Main', font=('ariel',16))]
    ]

    window = sg.Window('Timesheet Entry Form', layout, size=(450, 600), element_justification='c')


    # Nested Event Loop

    def clear_input():
        for key in values:
            window[key]('')
        return None

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Main':
            window.close()
            main()
        if event == 'Back':
            window.close()
            time()
        if event == 'Clear':
            clear_input()
        if event == 'Submit':
            for table in ws_tables:
                ws_tables.append(table)
            sg.popup('Data saved!')
            wb.save(filename)
            clear_input()

    window.close()

timesheet()
