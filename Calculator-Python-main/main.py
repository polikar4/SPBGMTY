from tkinter import *

string = ''


def calc(s): #логика кода
    global string
    if s == '=':
        string = str(eval(string))
    elif s == 'C':
        string = ''
    else:
        if string == '0':
            string == ''
        string += s
    window.config(text=string)


buttons = ['1', '2', '3', '=',
           '4', '5', '6', '*',
           '7', '8', '9', '/',
           '+', '0', '-', 'C']


cl = Tk()
cl.title('Калькулятор')
cl.geometry('485x550')
cl.resizable(False, False)

window = Label(cl)
window.place(anchor='center', x=210, y=50, width=420, height=100)

xb = 10
yb = 140

for button in buttons:
    Button(cl, text=button, command=lambda b=button: calc(b)).place(x=xb, y=yb, width=115, height=79)
    xb += 117
    if xb > 400:
        xb = 10
        yb += 81

