from tkinter import *
from tkinter.ttk import Radiobutton

def clicked():
    lbl.configure(window,text='choose hero', value=1, variable=selected) (window,text='create hero', value=2, variable=selected)
#rad1 = Radiobutton(window,text='choose hero', value=1, variable=selected)
#rad1.grid(column=0, row=0)
#rad2.grid(column=1, row=0)

window = Tk()
window.title("rpg")
window.geometry('2000x1500')
lbl = Label(window, text="hello friend")
btn = Button(window, text="Play!", command=clicked)
btn.grid(column=0, row=0)
lbl.grid(column=0, row=0)
selected = IntVar()

rad3 = Radiobutton(window,text='lancer', value=3, variable=selected)
rad4 = Radiobutton(window,text='wizard', value=4, variable=selected)
rad5 = Radiobutton(window,text='archer', value=5, variable=selected)
rad6 = Radiobutton(window,text='summoner', value=6, variable=selected)


lbl = Label(window)

rad3.grid(column=0, row=30)
rad4.grid(column=1, row=30)
rad5.grid(column=2, row=30)
rad6.grid(column=3, row=30)
btn.grid(column=4, row=20)
lbl.grid(column=5, row=20)
window.mainloop()
