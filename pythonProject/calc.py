from tkinter import *
def operations(operation):
    global formula

    if operation == 'C':
        formula = ''
    elif operation == 'DEL':
        formula = formula[0: -1]
    elif operation == 'X^2':
        formula == str((eval(formula)) ** 2)
    elif operation == '=':
        formula == str(eval(formula))
    else:
        if formula == '0':
            formula = ''
        formula += operation
    label_text.configure(text=formula)


