import PySimpleGUI as sg
import pandas as pd
import openpyxl as op

def weekly_wage():

    filename = 'Payroll.xlsx'

    wb = op.load_workbook(filename, data_only=True)

    ws = wb.worksheets[0]

    ws_tables = []


    layout = [
        [sg.Text('Employee Name', size=(15,1), font=('ariel', 16)), sg.InputText(key='-Name-', font=('ariel',16))],
        [sg.Text('Week Ending', size=(15,1), font=('ariel',16)), sg.InputText(key='-Date-', font=('ariel',16))],
        [sg.Submit(font=('ariel', 16))],
        [sg.Text('The Weekly Wage is:', font=('ariel', 16))],
        [sg.Output(size=(10, 1))]
    ]

    window = sg.Window('Gross Wages Search', layout, size=(450,250))

    # Event Loop
            
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Submit':
            key1 = window['-Name-']      # this gives a callable object to the Input keys
            key2 = window['-Date-']
            for row in ws.iter_rows():
                if row[1].value == key1 and row[2].value == key2:   # filter on first column with value 16
                    ws.cell(row=cell.row, column=49).value
                    print(value, font=('ariel',16))
                    break
                else:
                    print('Check Your Search Parameters and Try Again', font=('ariel', 16))
                    break

    window.close()

weekly_wage()
