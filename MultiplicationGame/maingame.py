import PySimpleGUI as sg
import helperfile

# Ensure the db is created
helperfile.createTable()

sg.theme('SandyBeach')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Welcome', key='-TITLE-')],
          [sg.Text('EXPRESSION', key='-HASEXPRESSION-'),
           sg.InputText(key='-ANSWER-', do_not_clear=False)],
          [sg.Button('End Game', key='-END-')]]

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
    if event == sg.WIN_CLOSED or event == '-END-':
        break

    # print(f"{event=}")
    # print(f"{values=}")
    if event == '-ANSWER-' + '_Enter' and len(values['-ANSWER-']) > 0:
        # print(values['-ANSWER-'])
        result = values['-ANSWER-']
        # print(f"{left_op=}")
        # print(f"{right_op=}")

        # print(f"{left_op*right_op}")
        if left_op * right_op != int(result):
            print('Incorrect')
            numIncorrect += 1
        else:
            print('Correct')
            numCorrect += 1

    ExpressionResults = helperfile.buildExpression()
    left_op, right_op, mathExpression = ExpressionResults
    window['-HASEXPRESSION-'].update(mathExpression)

helperfile.insertValue(numCorrect, numIncorrect)

window.close()
