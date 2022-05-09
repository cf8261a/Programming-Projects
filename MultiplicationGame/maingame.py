import PySimpleGUI as sg
import helperfile
import time

gameDB = helperfile.BackendDB()
# Ensure the db is created
gameDB.invokeSQLite(how='CREATETABLE')

sg.theme('SandyBeach')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Welcome', key='-TITLE-')],
          [sg.Text('EXPRESSION', key='-HASEXPRESSION-'),
           sg.InputText(key='-ANSWER-', do_not_clear=False)],
          [sg.Button('Finish', key='-FINISH-'), sg.Button('Close', key='-END-')]]

# Default font
defaultfont = ('Helvetica', 24)
# Create the Window
window = sg.Window('Multiplication Game', layout,
                   margins=(100, 100), finalize=True, font=defaultfont)
# Binding the input box to the keyboard button 'Enter'
window['-ANSWER-'].bind("<Return>", "_Enter")

ExpressionResults = helperfile.buildExpression()
left_op, right_op, mathExpression = ExpressionResults
window['-HASEXPRESSION-'].update(mathExpression)

numCorrect = 0
numIncorrect = 0


# Event Loop to process "events" and get the "values" of the inputs
while True:

    event, values = window.read()

    if event == '-FINISH-':
        window['-ANSWER-'].update(visible=False)
        window['-HASEXPRESSION-'].update(visible=False)
        highestscore = gameDB.invokeSQLite(how='HIGHSCORE')
        avgscore = gameDB.invokeSQLite(how='AVGSCORE')
        finalMsg = f'Game Over! \n {numCorrect} correct \n {numIncorrect} incorrect.\n Highest Score All Time: {highestscore} \n Average All Time Score {avgscore} \n Thanks for Playing!'
        sg.Popup(finalMsg)
        break

    if event == sg.WIN_CLOSED or event == '-END-':
        break

    if event == '-ANSWER-' + '_Enter' and len(values['-ANSWER-']) > 0:

        result = values['-ANSWER-']

        if left_op * right_op != int(result):
            print('Incorrect')
            numIncorrect += 1
        else:
            print('Correct')
            numCorrect += 1

    ExpressionResults = helperfile.buildExpression()
    left_op, right_op, mathExpression = ExpressionResults
    window['-HASEXPRESSION-'].update(mathExpression)

gameDB.invokeSQLite(cCount=numCorrect, iCount=numIncorrect, how='INSERTVALUE')

window.close()
