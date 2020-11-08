from tkinter import *
from tkinter import messagebox

w = Tk()


def my_func():
    messagebox.showinfo('강아지 버튼', '강아지가 귀엽죠?')


p = PhotoImage(file='car.gif')
b = Button(w, image=p, command=my_func)

b.pack()
w.mainloop()
