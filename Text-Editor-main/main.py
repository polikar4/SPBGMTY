from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def new():
    text_box.delete(1.0, END)


def savefile():
    name = filedialog.asksaveasfilename()
    try:
        file = open(name, 'w')
        file.write(text_box.get("1.0", END))
        file.close()
    except:
        print('Error save')


def openfile():
    name = filedialog.askopenfilename()
    try:
        file = open(name, 'r')
        text_box.delete(1.0, END)
        text_box.insert('1.0', file.read())
    except:
        print('Error open')


def about():
    messagebox.showinfo('About programm', 'Text Editor')


def helpwin():
    messagebox.showinfo('About programm', 'Call this number: 112')


ws = Tk()
ws.title('Текстовый редактор')
ws.geometry('640x480')
ws.iconphoto(False, PhotoImage(file='1.png'))

mainmenu = Menu()
filemenu = Menu(mainmenu, tearoff=1)
filemenu.add_command(label='Open', command=openfile)
filemenu.add_command(label='New', command=new)
filemenu.add_command(label='Save', command=savefile)
filemenu.add_command(label='Exit', command=ws.destroy)

helpmenu = Menu(mainmenu, tearoff=1)
helpmenu.add_command(label='Help', command=helpwin)
helpmenu.add_command(label='About', command=about)

mainmenu.add_cascade(label='File', menu=filemenu)
mainmenu.add_cascade(label='Help', menu=helpmenu)

ws.config(menu=mainmenu)

text_box = Text(ws)
text_box.pack(expand=True)
scrollbar = Scrollbar(text_box)
scrollbar['command'] = text_box.yview
text_box['yscrollcommand'] = scrollbar.set
text_box.pack(fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

