from tkinter import *
from tkinter import messagebox

w = Tk()


def my_f():
    if chk.get() == 0:
        messagebox.showinfo('', '체크버튼이 켜졌')
    else:
        messagebox.showinfo('', '꺼졌')


chk = IntVar()

cb = Checkbutton(w, text='you can click', variable=chk, command=my_f)

cb.pack()

w.mainloop()
