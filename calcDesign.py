import tkinter as tk

window = tk.Tk()
window.title('calculator')
window.geometry('500x550')
window.resizable(False, False)
window.configure(bg='black')

def calculate(operation):
    pass

# Создаем кнопки
buttons = ['C', 'del', '+', '=', '1', '2', '3', '/', '4', '5', '6', '+', '7', '8', '9', '-', '+/-', '0', '%', 'X^2']
x = 18
y = 140
for button in buttons:
    get_lbl = lambda x=button: calculate(x)
    tk.Button(text=button, bg='red', font=('Roboto', 20), command=get_lbl).place(x=x, y=y, width=115, height=79)
    x += 117
    if x> 400:
        x = 18
        y += 81




















window.mainloop()