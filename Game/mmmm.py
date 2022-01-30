from tkinter import *
from tkinter.ttk import Radiobutton

def clicked():
#    lbl.configure(text=selected.get())
    lbl.configure( rad3 = Radiobutton(window,text='lancer', value=3, variable=selected))
window = Tk()
window.title("rpg")
window.geometry('2000x1500')
lbl = Label(window, text="hello friend")
btn = Button(window, text="Play!", command=clicked)

selected = IntVar()
rad1 = Radiobutton(window,text='Первый', value=3, variable=selected)
rad2 = Radiobutton(window,text='Второй', value=6, variable=selected)

lbl = Label(window)

rad3.grid(column=0, row=30)
btn.grid(column=1, row=0)
lbl.grid(column=0, row=0)
window.mainloop()